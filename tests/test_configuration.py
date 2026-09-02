from backend.configuration import build_config
from backend.domain import OrderType, SameCandlePolicy, ValidationError


def payload():
    return {"asset":"WIN", "contract":"WINJ24", "start":"2024-01-01", "end":"2024-01-02", "timeframe_minutes":"5", "session_start":"09:00", "session_end":"18:00", "order_type":"market", "execution_price":"next_open", "stop_loss_points":"100", "target_points":"150", "quantity":"1", "commission_per_contract":"0.5", "slippage_points":"1", "same_candle_policy":"stop_first", "rollover_rule":"manual", "data_source":"fixture"}


def test_build_config_converts_form_strings():
    config = build_config(payload())
    assert config.order_type is OrderType.MARKET
    assert config.same_candle_policy is SameCandlePolicy.STOP_FIRST
    assert config.timeframe_minutes == 5


def test_build_config_rejects_unknown_enum():
    values = payload()
    values["order_type"] = "unknown"
    try:
        build_config(values)
    except ValidationError as exc:
        assert "configuração inválida" in str(exc)
    else:
        raise AssertionError("expected ValidationError")


def test_build_config_rejects_invalid_number():
    values = payload()
    values["quantity"] = "abc"
    try:
        build_config(values)
    except ValidationError as exc:
        assert "configuração inválida" in str(exc)
    else:
        raise AssertionError("expected ValidationError")
