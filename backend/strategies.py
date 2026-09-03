"""Estratégias de exemplo, sem estado global e sem acesso a dados futuros."""
from collections.abc import Sequence

from .domain import OHLCVBar


def moving_average_cross_signal(index: int, bars: Sequence[OHLCVBar], fast: int = 3, slow: int = 5) -> bool:
    """Sinaliza compra quando a média rápida cruza acima da lenta.

    O cálculo usa somente candles até ``index``. O executor abre no candle
    seguinte, portanto a estratégia não observa o preço de entrada futuro.
    """
    if fast <= 0 or slow <= 0 or fast >= slow:
        raise ValueError("fast e slow devem ser positivos, com fast < slow")
    if index < slow - 1 or index >= len(bars):
        return False
    closes = [bar.close for bar in bars[: index + 1]]
    current_fast = sum(closes[-fast:]) / fast
    current_slow = sum(closes[-slow:]) / slow
    previous_fast = sum(closes[-fast - 1 : -1]) / fast
    previous_slow = sum(closes[-slow - 1 : -1]) / slow
    return previous_fast <= previous_slow and current_fast > current_slow


def previous_day_high_breakout_signal(index: int, bars: Sequence[OHLCVBar]) -> bool:
    """Sinaliza compra no primeiro rompimento da máxima do dia anterior.

    A máxima é calculada somente com barras cujo ``timestamp.date()`` é
    anterior ao dia do índice atual. A confirmação usa o fechamento atual e o
    fechamento da barra anterior, enquanto o executor entra no candle seguinte.
    """
    if index <= 0 or index >= len(bars):
        return False
    current_day = bars[index].timestamp.date()
    previous_day_bars = [bar for bar in bars[:index] if bar.timestamp.date() < current_day]
    if not previous_day_bars:
        return False
    previous_day_high = max(bar.high for bar in previous_day_bars)
    previous_close = bars[index - 1].close
    return previous_close <= previous_day_high < bars[index].close
