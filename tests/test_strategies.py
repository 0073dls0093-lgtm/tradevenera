from datetime import datetime, timedelta, timezone

import pytest

from backend.domain import OHLCVBar
from backend.strategies import moving_average_cross_signal


def make_bars(closes):
    start = datetime(2024, 1, 1, 12, tzinfo=timezone.utc)
    return tuple(OHLCVBar(start + timedelta(minutes=i), close - 1, close + 1, close - 2, close, 10) for i, close in enumerate(closes))


def test_moving_average_cross_uses_only_history_available_at_index():
    bars = make_bars([10, 9, 8, 7, 8, 12, 14])
    assert moving_average_cross_signal(3, bars) is False
    assert moving_average_cross_signal(5, bars, fast=2, slow=4) is True


def test_moving_average_cross_rejects_invalid_windows():
    with pytest.raises(ValueError):
        moving_average_cross_signal(3, make_bars([1, 2, 3, 4]), fast=3, slow=3)
