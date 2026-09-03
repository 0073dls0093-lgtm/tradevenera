from pathlib import Path

import pytest

from backend.domain import ValidationError
from backend.settlements import load_futures_settlements_csv


ROOT = Path(__file__).parents[1]


HEADER = "refdate,symbol,commodity,maturity_code,previous_price,price,price_change,settlement_value\n"


def test_loads_normalized_daily_settlement_csv(tmp_path):
    path = tmp_path / "settlements.csv"
    path.write_text(
        HEADER
        + "2024-01-02,WINF24,WIN,F24,130000,130500,500,130450\n"
        + "2024-01-03,WINF24,WIN,F24,130500,131000,500,130950\n",
        encoding="utf-8",
    )

    records = load_futures_settlements_csv(path)

    assert len(records) == 2
    assert records[0].symbol == "WINF24"
    assert records[0].settlement_value == 130450
    assert records[1].refdate.isoformat() == "2024-01-03"


def test_rejects_missing_columns(tmp_path):
    path = tmp_path / "invalid.csv"
    path.write_text("refdate,symbol\n2024-01-02,WINF24\n", encoding="utf-8")

    with pytest.raises(ValidationError, match="colunas normalizadas"):
        load_futures_settlements_csv(path)


def test_rejects_invalid_number_and_reports_line(tmp_path):
    path = tmp_path / "invalid.csv"
    path.write_text(
        HEADER + "2024-01-02,WINF24,WIN,F24,130000,not-a-number,500,130450\n",
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="linha 2"):
        load_futures_settlements_csv(path)


def test_rejects_dates_out_of_order(tmp_path):
    path = tmp_path / "invalid.csv"
    path.write_text(
        HEADER
        + "2024-01-03,WINF24,WIN,F24,130500,131000,500,130950\n"
        + "2024-01-02,WINF24,WIN,F24,130000,130500,500,130450\n",
        encoding="utf-8",
    )

    with pytest.raises(ValidationError, match="ordem crescente"):
        load_futures_settlements_csv(path)


def test_settlement_source_is_not_the_ohlcv_fixture():
    assert not (ROOT / "data" / "settlements.csv").exists()
