"""Conversão segura dos campos da interface para o contrato de domínio."""
from datetime import date, time
from typing import Mapping

from .domain import BacktestConfig, OrderType, SameCandlePolicy, ValidationError


def _required(values: Mapping[str, str], key: str) -> str:
    value = values.get(key, "").strip()
    if not value:
        raise ValidationError(f"{key} é obrigatório")
    return value


def _optional_positive(values: Mapping[str, str], key: str) -> float | None:
    raw = values.get(key, "").strip()
    if not raw:
        return None
    try:
        value = float(raw)
    except ValueError as exc:
        raise ValidationError(f"{key} deve ser numérico") from exc
    if value <= 0:
        raise ValidationError(f"{key} deve ser positivo")
    return value


def build_config(values: Mapping[str, str]) -> BacktestConfig:
    """Converte um payload textual sem aceitar enums ou datas arbitrárias."""
    try:
        start = date.fromisoformat(_required(values, "start"))
        end = date.fromisoformat(_required(values, "end"))
        session_start = time.fromisoformat(_required(values, "session_start"))
        session_end = time.fromisoformat(_required(values, "session_end"))
        timeframe = int(_required(values, "timeframe_minutes"))
        quantity = int(_required(values, "quantity"))
        commission = float(values.get("commission_per_contract", "0"))
        slippage = float(values.get("slippage_points", "0"))
        order_type = OrderType(_required(values, "order_type"))
        policy = SameCandlePolicy(_required(values, "same_candle_policy"))
    except (ValueError, TypeError) as exc:
        raise ValidationError(f"configuração inválida: {exc}") from exc
    config = BacktestConfig(
        asset=_required(values, "asset"), contract=_required(values, "contract"), start=start, end=end,
        timeframe_minutes=timeframe, session_start=session_start, session_end=session_end,
        order_type=order_type, execution_price=_required(values, "execution_price"),
        stop_loss_points=_optional_positive(values, "stop_loss_points"), target_points=_optional_positive(values, "target_points"),
        quantity=quantity, commission_per_contract=commission, slippage_points=slippage,
        same_candle_policy=policy, rollover_rule=_required(values, "rollover_rule"), data_source=_required(values, "data_source"),
    )
    config.ensure_valid()
    return config
