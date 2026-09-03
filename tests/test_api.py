import pytest

from backend.api import execute_backtest


PAYLOAD = {
    "asset":"WIN", "contract":"FIXTURE", "start":"2024-01-01", "end":"2024-01-02",
    "timeframe_minutes":"5", "session_start":"09:00", "session_end":"18:00",
    "order_type":"market", "execution_price":"next_open", "stop_loss_points":"2",
    "target_points":"3", "quantity":"1", "commission_per_contract":"0",
    "slippage_points":"0", "same_candle_policy":"stop_first", "rollover_rule":"manual",
    "data_source":"data/sample_ohlcv.csv",
}


def test_api_executes_authorized_fixture_and_returns_schema_one():
    response = execute_backtest(PAYLOAD)
    assert response["schema_version"] == "1"
    assert response["summary"]["net_result"] == 3.0
    assert len(response["trades"]) == 1
    assert response["demo"]["source"] == "data/sample_ohlcv.csv"
    assert len(response["demo"]["bars"]) == 6
    assert "sintéticos" in response["demo"]["notice"]
    assert response["evaluation"]["split_index"] == 3
    assert "net_result" in response["evaluation"]["adjustment"]
    assert "net_result" in response["evaluation"]["validation"]
    assert set(response["comparison"]) == {"moving_average", "previous_day_high"}
    assert response["comparison"]["moving_average"]["trades"] == 1


def test_api_rejects_any_data_source_outside_authorized_fixture():
    payload = {**PAYLOAD, "data_source": "data/other.csv"}
    with pytest.raises(ValueError, match="somente"):
        execute_backtest(payload)


def test_api_accepts_previous_day_high_strategy():
    response = execute_backtest({**PAYLOAD, "strategy": "previous_day_high"})
    assert response["strategy"] == "previous_day_high"
    assert response["summary"]["trades"] == 0


def test_api_rejects_unknown_strategy():
    with pytest.raises(ValueError, match="não suportada"):
        execute_backtest({**PAYLOAD, "strategy": "future_prediction"})
