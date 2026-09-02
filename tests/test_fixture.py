from datetime import date, time
from pathlib import Path

from backend.configuration import build_config
from backend.fixture import load_ohlcv_csv
from backend.backtest import run_backtest
from backend.strategies import moving_average_cross_signal


ROOT = Path(__file__).parents[1]


def test_sample_fixture_runs_through_the_full_local_flow():
    bars = load_ohlcv_csv(ROOT / "data" / "sample_ohlcv.csv")
    config = build_config({
        "asset":"WIN", "contract":"FIXTURE", "start":"2024-01-01", "end":"2024-01-02",
        "timeframe_minutes":"5", "session_start":"09:00", "session_end":"18:00",
        "order_type":"market", "execution_price":"next_open", "stop_loss_points":"2",
        "target_points":"3", "quantity":"1", "commission_per_contract":"0",
        "slippage_points":"0", "same_candle_policy":"stop_first", "rollover_rule":"manual",
        "data_source":"data/sample_ohlcv.csv",
    })
    result = run_backtest(bars, config, lambda index, history: moving_average_cross_signal(index, history, fast=2, slow=3))
    assert len(bars) == 6
    assert result.trades
    assert result.trades[0].entry_time == bars[5].timestamp
