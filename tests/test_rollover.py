import pytest

from backend.domain import ValidationError
from backend.rollover import RolloverRule, describe_rollover, validate_rollover_rule


def test_manual_rollover_is_explicit():
    assert validate_rollover_rule("manual") is RolloverRule.MANUAL
    assert "manualmente" in describe_rollover("manual")


def test_continuous_adjusted_is_documented_as_synthetic_only():
    assert validate_rollover_rule("continuous_adjusted") is RolloverRule.CONTINUOUS_ADJUSTED
    assert "sintética" in describe_rollover("continuous_adjusted")


def test_unknown_rollover_rule_is_rejected():
    with pytest.raises(ValidationError, match="manual ou continuous_adjusted"):
        validate_rollover_rule("auto_guess")
