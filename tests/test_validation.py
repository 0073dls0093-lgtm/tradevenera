from datetime import datetime, timedelta, timezone

import pytest

from backend.domain import OHLCVBar, ValidationError
from backend.validation import split_out_of_sample


def make_bars(count=6):
    start = datetime(2024, 1, 1, 12, tzinfo=timezone.utc)
    return tuple(OHLCVBar(start + timedelta(minutes=i), 100, 101, 99, 100, 10) for i in range(count))


def test_split_has_contiguous_non_overlapping_periods():
    split = split_out_of_sample(make_bars(), 4)
    assert len(split.adjustment) == 4
    assert len(split.validation) == 2
    assert split.adjustment[-1].timestamp < split.validation[0].timestamp
    assert split.adjustment + split.validation == make_bars()


@pytest.mark.parametrize("split_index", [0, 6, -1, 7])
def test_split_rejects_empty_period(split_index):
    with pytest.raises(ValidationError, match="não vazios"):
        split_out_of_sample(make_bars(), split_index)
