from datetime import date, datetime, time, timedelta, timezone

from backend.backtest import run_backtest
from backend.domain import BacktestConfig, OHLCVBar, OrderType, SameCandlePolicy


def cfg(**changes):
    values = dict(asset="WIN", contract="WINJ24", start=date(2024, 1, 1), end=date(2024, 1, 2), timeframe_minutes=5, session_start=time(9), session_end=time(18), order_type=OrderType.MARKET, execution_price="next_open", stop_loss_points=2, target_points=3, quantity=1, commission_per_contract=1, slippage_points=0, same_candle_policy=SameCandlePolicy.STOP_FIRST, rollover_rule="manual", data_source="fixture")
    values.update(changes)
    return BacktestConfig(**values)


def bars(*ohlc):
    start = datetime(2024, 1, 2, 12, tzinfo=timezone.utc)
    return tuple(OHLCVBar(start + timedelta(minutes=i), *row, 100) for i, row in enumerate(ohlc))


def test_entry_uses_next_candle_and_target_includes_cost():
    result = run_backtest(bars((100, 101, 99, 100), (105, 106, 104, 105), (105, 109, 104, 108)), cfg(), lambda i, _: i == 0)
    assert len(result.trades) == 1
    assert result.trades[0].entry_price == 105
    assert result.trades[0].reason == "target"
    assert result.net_result == 2


def test_same_candle_stop_first_is_deterministic():
    result = run_backtest(bars((100, 101, 99, 100), (100, 104, 96, 101)), cfg(), lambda i, _: i == 0)
    assert result.trades[0].reason == "stop_first"
    assert result.trades[0].exit_price == 98


def test_no_signal_produces_empty_result():
    result = run_backtest(bars((100, 101, 99, 100), (100, 101, 99, 100)), cfg(), lambda i, _: False)
    assert result.trades == ()
    assert result.net_result == 0
