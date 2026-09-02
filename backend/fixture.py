"""Leitura de fixtures OHLCV pequenas e versionáveis para testes locais."""
import csv
from datetime import datetime
from pathlib import Path

from .domain import OHLCVBar, ValidationError


_REQUIRED = ("timestamp", "open", "high", "low", "close", "volume")


def load_ohlcv_csv(path: str | Path) -> tuple[OHLCVBar, ...]:
    file_path = Path(path)
    with file_path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None or any(field not in reader.fieldnames for field in _REQUIRED):
            raise ValidationError("fixture deve conter colunas timestamp, open, high, low, close e volume")
        bars: list[OHLCVBar] = []
        for line_number, row in enumerate(reader, start=2):
            try:
                bars.append(OHLCVBar(
                    timestamp=datetime.fromisoformat(row["timestamp"]),
                    open=float(row["open"]), high=float(row["high"]),
                    low=float(row["low"]), close=float(row["close"]), volume=float(row["volume"]),
                ))
            except (KeyError, TypeError, ValueError, ValidationError) as exc:
                raise ValidationError(f"fixture inválida na linha {line_number}: {exc}") from exc
    if any(current.timestamp >= following.timestamp for current, following in zip(bars, bars[1:])):
        raise ValidationError("timestamps da fixture devem estar em ordem crescente")
    return tuple(bars)
