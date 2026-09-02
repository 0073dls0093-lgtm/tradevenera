import json
from datetime import date, time
from pathlib import Path

from backend.backtest import run_backtest
from backend.configuration import build_config
from backend.fixture import load_ohlcv_csv
from backend.serialization import result_json, result_payload
from backend.strategies import moving_average_cross_signal


ROOT = Path(__file__).parents[1]


def _result():
    bars = load_ohlcv_csv(ROOT / "data" / "sample_ohlcv.csv")
    config = build_config({
        "asset":"WIN", "contract":"FIXTURE", "start":"2024-01-01", "end":"2024-01-02",
        "timeframe_minutes":"5", "session_start":"09:00", "session_end":"18:00",
        "order_type":"market", "execution_price":"next_open", "stop_loss_points":"2",
        "target_points":"3", "quantity":"1", "commission_per_contract":"0",
        "slippage_points":"0", "same_candle_policy":"stop_first", "rollover_rule":"manual",
        "data_source":"data/sample_ohlcv.csv",
    })
    return run_backtest(bars, config, lambda index, history: moving_average_cross_signal(index, history, fast=2, slow=3))


def test_payload_is_versioned_and_contains_summary_and_trade_times():
    payload = result_payload(_result())
    assert payload["schema_version"] == "1"
    assert payload["summary"] == {"trades": 1, "gross_result": 3.0, "total_costs": 0.0, "net_result": 3.0, "gains": 1, "losses": 0, "max_drawdown": 0.0}
    assert payload["trades"][0]["entry_time"] == "2024-01-02T12:25:00+00:00"


def test_json_is_parseable_and_byte_stable():
    result = _result()
    serialized = result_json(result)
    assert json.loads(serialized)["summary"]["net_result"] == 3.0
    assert serialized == result_json(result)
    assert " " not in serialized
