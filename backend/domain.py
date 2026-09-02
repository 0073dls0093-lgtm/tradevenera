"""Contratos puros do domínio TradeVenera.



Sem dependências externas e sem acesso a mercado: esta etapa valida apenas

premissas necessárias antes de qualquer execução de backtest.

"""

from dataclasses import dataclass

from datetime import date, datetime, time

from enum import Enum



class ValidationError(ValueError):
  
    """Erro de entrada inválida no contrato do domínio."""
  


class OrderType(str, Enum):
  
    MARKET = "market"
  
    LIMIT = "limit"
  


class SameCandlePolicy(str, Enum):
  
    STOP_FIRST = "stop_first"
  
    TARGET_FIRST = "target_first"
  
    INVALIDATE = "invalidate"
  


@dataclass(frozen=True)

class OHLCVBar:
  
    timestamp: datetime
  
    open: float
  
    high: float
  
    low: float
  
    close: float
  
    volume: float
  


    def __post_init__(self) -> None:
      
        if self.timestamp.tzinfo is None:
          
            raise ValidationError("timestamp deve incluir timezone")
          
        values = (self.open, self.high, self.low, self.close, self.volume)
      
        if any(value != value for value in values):
          
            raise ValidationError("OHLCV não pode conter NaN")
          
        if min(self.open, self.high, self.low, self.close) < 0:
          
            raise ValidationError("preços não podem ser negativos")
          
        if self.high < max(self.open, self.close) or self.low > min(self.open, self.close):
          
            raise ValidationError("high/low são incompatíveis com open/close")
          
        if self.high < self.low:
          
            raise ValidationError("high deve ser maior ou igual a low")
          
        if self.volume < 0:
          
            raise ValidationError("volume não pode ser negativo")
          


@dataclass(frozen=True)

class BacktestConfig:
  
    asset: str
  
    contract: str
  
    start: date
  
    end: date
  
    timeframe_minutes: int
  
    session_start: time
  
    session_end: time
  
    order_type: OrderType
  
    execution_price: str
  
    stop_loss_points: float | None
  
    target_points: float | None
  
    quantity: int
  
    commission_per_contract: float
  
    slippage_points: float
  
    same_candle_policy: SameCandlePolicy
  
    rollover_rule: str
  
    data_source: str
  


    def validate(self) -> list[str]:
      
        errors: list[str] = []
      
        if not self.asset.strip(): errors.append("asset é obrigatório")
          
        if not self.contract.strip(): errors.append("contract é obrigatório")
          
        if self.start > self.end: errors.append("start deve ser anterior ou igual a end")
          
        if self.timeframe_minutes <= 0: errors.append("timeframe_minutes deve ser positivo")
          
        if self.session_start >= self.session_end: errors.append("sessão deve ter início antes do fim")
          
        if not self.execution_price.strip(): errors.append("execution_price é obrigatório")
          
        if self.stop_loss_points is not None and self.stop_loss_points <= 0: errors.append("stop_loss_points deve ser positivo")
          
        if self.target_points is not None and self.target_points <= 0: errors.append("target_points deve ser positivo")
          
        if self.quantity <= 0: errors.append("quantity deve ser positivo")
          
        if self.commission_per_contract < 0: errors.append("commission_per_contract não pode ser negativa")
          
        if self.slippage_points < 0: errors.append("slippage_points não pode ser negativo")
          
        if not self.rollover_rule.strip(): errors.append("rollover_rule é obrigatório")
          
        if not self.data_source.strip(): errors.append("data_source é obrigatório")
          
        if self.stop_loss_points is None and self.target_points is None: errors.append("stop ou alvo deve ser informado")
          
        return errors
      


    def ensure_valid(self) -> None:
      
        errors = self.validate()
      
        if errors:
          
            raise ValidationError("; ".join(errors))



































































