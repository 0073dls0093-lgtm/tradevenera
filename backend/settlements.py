"""Leitura segura de preços de ajuste diários de futuros da B3.

Este formato não é OHLCV e não é aceito diretamente pelo motor de backtest.
Ele representa somente o primeiro limite de ingestão para uma fonte pública.
"""
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .domain import ValidationError


_REQUIRED = (
    "refdate",
    "symbol",
    "commodity",
    "maturity_code",
    "previous_price",
    "price",
    "price_change",
    "settlement_value",
)


@dataclass(frozen=True)
class FuturesSettlement:
    refdate: date
    symbol: str
    commodity: str
    maturity_code: str
    previous_price: float
    price: float
    price_change: float
    settlement_value: float

    def __post_init__(self) -> None:
        if not self.symbol.strip() or not self.commodity.strip() or not self.maturity_code.strip():
            raise ValidationError("identificação do contrato é obrigatória")
        values = (self.previous_price, self.price, self.price_change, self.settlement_value)
        if any(value != value for value in values):
            raise ValidationError("preços de ajuste não podem conter NaN")
        if self.previous_price < 0 or self.price < 0 or self.settlement_value < 0:
            raise ValidationError("preços de ajuste não podem ser negativos")


def load_futures_settlements_csv(path: str | Path) -> tuple[FuturesSettlement, ...]:
    """Carrega CSV normalizado de liquidações diárias, sem convertê-lo em OHLCV."""
    file_path = Path(path)
    with file_path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None or any(field not in reader.fieldnames for field in _REQUIRED):
            raise ValidationError("arquivo deve conter as colunas normalizadas de liquidação da B3")
        records: list[FuturesSettlement] = []
        for line_number, row in enumerate(reader, start=2):
            try:
                records.append(FuturesSettlement(
                    refdate=date.fromisoformat(row["refdate"]),
                    symbol=row["symbol"],
                    commodity=row["commodity"],
                    maturity_code=row["maturity_code"],
                    previous_price=float(row["previous_price"]),
                    price=float(row["price"]),
                    price_change=float(row["price_change"]),
                    settlement_value=float(row["settlement_value"]),
                ))
            except (KeyError, TypeError, ValueError, ValidationError) as exc:
                raise ValidationError(f"liquidação inválida na linha {line_number}: {exc}") from exc
    if any(current.refdate > following.refdate for current, following in zip(records, records[1:])):
        raise ValidationError("datas de referência devem estar em ordem crescente")
    return tuple(records)
