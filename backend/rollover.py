"""Políticas de vencimento e rolagem, sem dados reais ou execução externa."""
from enum import Enum

from .domain import ValidationError


class RolloverRule(str, Enum):
    MANUAL = "manual"
    CONTINUOUS_ADJUSTED = "continuous_adjusted"


def validate_rollover_rule(rule: str) -> RolloverRule:
    """Aceita somente políticas declaradas; não infere vencimentos."""
    try:
        return RolloverRule(rule.strip())
    except (AttributeError, ValueError) as exc:
        raise ValidationError(
            "rollover_rule deve ser manual ou continuous_adjusted"
        ) from exc


def describe_rollover(rule: str) -> str:
    """Explica a política aplicada ao usuário do backtest."""
    selected = validate_rollover_rule(rule)
    if selected is RolloverRule.MANUAL:
        return "Contrato único; a troca de vencimento deve ser informada manualmente."
    return "Série contínua sintética; ajuste entre contratos não é calculado nesta versão."
