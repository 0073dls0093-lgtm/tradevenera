"""API HTTP mínima para executar somente a fixture local autorizada."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from typing import Any

from .backtest import run_backtest
from .configuration import build_config
from .fixture import load_ohlcv_csv
from .serialization import result_payload
from .strategies import moving_average_cross_signal, previous_day_high_breakout_signal
from .validation import split_out_of_sample
from .rollover import describe_rollover

ROOT = Path(__file__).parents[1]
ALLOWED_FIXTURE = (ROOT / "data" / "sample_ohlcv.csv").resolve()


def execute_backtest(payload: dict[str, Any]) -> dict[str, Any]:
    """Executa uma requisição validada e devolve um payload JSON serializável."""
    source = (payload.get("data_source") or "").strip()
    requested = (ROOT / source).resolve()
    if requested != ALLOWED_FIXTURE:
        raise ValueError("esta API inicial aceita somente data/sample_ohlcv.csv")
    config = build_config(payload)
    bars = load_ohlcv_csv(requested)
    strategy_name = (payload.get("strategy") or "moving_average").strip()
    if strategy_name == "moving_average":
        signal = lambda index, history: moving_average_cross_signal(index, history, fast=2, slow=3)
    elif strategy_name == "previous_day_high":
        signal = previous_day_high_breakout_signal
    else:
        raise ValueError("estratégia não suportada; use moving_average ou previous_day_high")
    result = run_backtest(bars, config, signal)
    split = split_out_of_sample(bars, max(1, len(bars) // 2))
    adjustment_result = run_backtest(split.adjustment, config, signal)
    validation_result = run_backtest(split.validation, config, signal)
    comparison = {}
    for name, candidate in (("moving_average", lambda i, h: moving_average_cross_signal(i, h, fast=2, slow=3)), ("previous_day_high", previous_day_high_breakout_signal)):
        comparison[name] = result_payload(run_backtest(bars, config, candidate))["summary"]
    response = result_payload(result)
    response["strategy"] = strategy_name
    response["rollover"] = describe_rollover(config.rollover_rule)
    response["evaluation"] = {
        "split_index": split.split_index,
        "adjustment": result_payload(adjustment_result)["summary"],
        "validation": result_payload(validation_result)["summary"],
    }
    response["comparison"] = comparison
    response["demo"] = {
        "source": "data/sample_ohlcv.csv",
        "notice": "Dados sintéticos autorizados apenas para demonstração; não representam histórico real.",
        "bars": [
            {
                "timestamp": bar.timestamp.isoformat(),
                "open": bar.open,
                "high": bar.high,
                "low": bar.low,
                "close": bar.close,
            }
            for bar in bars
        ],
    }
    return response


class BacktestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self) -> None:  # noqa: N802
        self._send(204, {})

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/backtest":
            self._send(404, {"error": "rota não encontrada"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            response = execute_backtest(payload)
        except (ValueError, TypeError, json.JSONDecodeError) as exc:
            self._send(400, {"error": str(exc)})
            return
        self._send(200, response)

    def _send(self, status: int, payload: dict[str, Any]) -> None:
        body = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if status != 204:
            self.wfile.write(body)

    def log_message(self, *_args: object) -> None:
        return


def serve(host: str = "127.0.0.1", port: int = 8000) -> None:
    HTTPServer((host, port), BacktestHandler).serve_forever()


if __name__ == "__main__":
    serve()
