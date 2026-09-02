# Decisões técnicas

## 02/09/2026 — Fundação documental e Python como base do domínio

**Decisão:** iniciar com uma estrutura orientada a Python, mantendo `backend/`, `frontend/`, `data/` e `tests/` separados.

**Motivo:** o domínio de séries temporais e backtesting tem boa compatibilidade com Python e permite começar pelo motor determinístico antes da interface. A separação reduz acoplamento entre cálculo, API e apresentação.

**Alternativas consideradas:** começar diretamente com uma aplicação full-stack React/Next.js ou adotar um framework de backtest pronto. Essas opções permanecem possíveis, mas dependem da definição do contrato de dados, das licenças e das regras financeiras.

**Impacto:** a primeira etapa não promete uma fonte de dados nem uma biblioteca de backtest específica.

## 02/09/2026 — Nenhum dado de mercado no primeiro commit

**Decisão:** não versionar dados históricos neste momento.

**Motivo:** fonte, licença, granularidade, contrato WIN e política de rolagem ainda não foram definidos. Amostras só serão adicionadas quando autorizadas e pequenas.

**Risco:** o projeto ainda não produz resultados de backtest; isso é intencional e está registrado em `CONTEXTO.md`.

## 02/09/2026 — Configuração explícita antes do motor

**Decisão:** a primeira tela funcional será uma configuração declarativa, com ativo, timeframe, período e custos visíveis, sem calcular resultados antes de existir um contrato de dados validado.

**Motivo:** evita que a interface crie a impressão de que dados ou resultados financeiros já estão disponíveis. Também transforma os requisitos obrigatórios da especificação em um contrato verificável para a próxima etapa.

**Impacto:** a tela `/configurar` usa apenas estado local no preview; a validação real e a persistência ficam bloqueadas até o modelo OHLCV e o motor determinístico serem definidos.
