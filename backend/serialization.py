"""Serialização estável do resultado do backtest para a futura API."""
import json
from datetime import date, datetime, time
from typing import Any

from .backtest import BacktestResult


def _iso(value: Any) -> Any:
    if isinstance(value, (datetime, date, time)):
        return value.isoformat()
    return value


def result_payload(result: BacktestResult) -> dict[str, Any]:
    """Converte um resultado em um payload versionado, sem arredondar dados."""
    return {
        "schema_version": "1",
        "summary": {
            "trades": len(result.trades),
            "gross_result": result.gross_result,
            "total_costs": result.total_costs,
            "net_result": result.net_result,
            "gains": result.gains,
            "losses": result.losses,
            "max_drawdown": result.max_drawdown,
        },
        "trades": [
            {
                "entry_time": _iso(trade.entry_time),
                "entry_price": trade.entry_price,
                "exit_time": _iso(trade.exit_time),
                "exit_price": trade.exit_price,
                "points": trade.points,
                "net_result": trade.net_result,
                "reason": trade.reason,
            }
            for trade in result.trades
        ],
    }


def result_json(result: BacktestResult) -> str:
    """Retorna JSON determinístico para logs, fixtures e resposta HTTP futura."""
    return json.dumps(result_payload(result), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
