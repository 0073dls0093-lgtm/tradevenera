"""Separação explícita entre ajuste e validação fora da amostra."""
from dataclasses import dataclass
from collections.abc import Sequence

from .domain import OHLCVBar, ValidationError


@dataclass(frozen=True)
class OutOfSampleSplit:
    adjustment: tuple[OHLCVBar, ...]
    validation: tuple[OHLCVBar, ...]
    split_index: int


def split_out_of_sample(bars: Sequence[OHLCVBar], split_index: int) -> OutOfSampleSplit:
    """Separa uma série em dois períodos contíguos e sem sobreposição."""
    if split_index <= 0 or split_index >= len(bars):
        raise ValidationError("split_index deve deixar ajuste e validação não vazios")
    adjustment = tuple(bars[:split_index])
    validation = tuple(bars[split_index:])
    if adjustment[-1].timestamp >= validation[0].timestamp:
        raise ValidationError("ajuste deve terminar antes da validação")
    return OutOfSampleSplit(adjustment, validation, split_index)
