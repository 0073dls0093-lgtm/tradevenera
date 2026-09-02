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


def test_api_rejects_any_data_source_outside_authorized_fixture():
    payload = {**PAYLOAD, "data_source": "data/other.csv"}
    with pytest.raises(ValueError, match="somente"):
        execute_backtest(payload)
