"""Executor determinístico inicial; não acessa rede nem envia ordens."""
from dataclasses import dataclass
from typing import Callable, Sequence

from .domain import BacktestConfig, OHLCVBar, SameCandlePolicy


@dataclass(frozen=True)
class Trade:
    entry_time: object
    entry_price: float
    exit_time: object
    exit_price: float
    points: float
    net_result: float
    reason: str


@dataclass(frozen=True)
class BacktestResult:
    trades: tuple[Trade, ...]
    gross_result: float
    total_costs: float
    net_result: float
    gains: int
    losses: int
    max_drawdown: float


def run_backtest(
    bars: Sequence[OHLCVBar],
    config: BacktestConfig,
    entry_signal: Callable[[int, Sequence[OHLCVBar]], bool],
) -> BacktestResult:
    """Executa uma estratégia long-only sem look-ahead.

    O sinal no índice i só pode gerar entrada no open do candle i+1.
    Stops/alvos usam o candle posterior à entrada. Caso ambos ocorram,
    a política configurada decide o desfecho de forma determinística.
    """
    config.ensure_valid()
    if not bars:
        return BacktestResult((), 0.0, 0.0, 0.0, 0, 0, 0.0)
    ordered = tuple(bars)
    trades: list[Trade] = []
    position: tuple[int, float] | None = None
    costs_per_trade = (config.commission_per_contract * config.quantity)
    i = 0
    while i < len(ordered):
        bar = ordered[i]
        if position is None and i < len(ordered) - 1 and entry_signal(i, ordered):
            entry_bar = ordered[i + 1]
            entry_price = entry_bar.open + config.slippage_points
            position = (i + 1, entry_price)
            i += 1
            continue
        if position is not None:
            entry_index, entry_price = position
            stop = entry_price - config.stop_loss_points if config.stop_loss_points else None
            target = entry_price + config.target_points if config.target_points else None
            stop_hit = stop is not None and bar.low <= stop
            target_hit = target is not None and bar.high >= target
            exit_price = None
            reason = ""
            if stop_hit and target_hit:
                if config.same_candle_policy is SameCandlePolicy.STOP_FIRST:
                    exit_price, reason = stop, "stop_first"
                elif config.same_candle_policy is SameCandlePolicy.TARGET_FIRST:
                    exit_price, reason = target, "target_first"
                else:
                    exit_price, reason = bar.close, "same_candle_invalidated"
            elif stop_hit:
                exit_price, reason = stop, "stop"
            elif target_hit:
                exit_price, reason = target, "target"
            elif i == len(ordered) - 1:
                exit_price, reason = bar.close - config.slippage_points, "end_of_data"
            if exit_price is not None:
                points = exit_price - entry_price
                net = points * config.quantity - costs_per_trade
                trades.append(Trade(ordered[entry_index].timestamp, entry_price, bar.timestamp, exit_price, points, net, reason))
                position = None
        i += 1
    gross = sum(t.points * config.quantity for t in trades)
    costs = sum(costs_per_trade for _ in trades)
    net = sum(t.net_result for t in trades)
    equity = 0.0
    peak = 0.0
    drawdown = 0.0
    for trade in trades:
        equity += trade.net_result
        peak = max(peak, equity)
        drawdown = max(drawdown, peak - equity)
    return BacktestResult(tuple(trades), gross, costs, net, sum(t.net_result > 0 for t in trades), sum(t.net_result <= 0 for t in trades), drawdown)
