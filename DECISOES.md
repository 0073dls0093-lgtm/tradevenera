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

## 02/09/2026 — Contrato de domínio sem dependências externas

**Decisão:** representar OHLCV e configuração de backtest com dataclasses Python e validação explícita, antes de escolher provedor de dados ou framework de execução.

**Motivo:** mantém o núcleo determinístico, testável e independente de rede. Também permite rejeitar dados incompatíveis e configurações incompletas antes de qualquer cálculo.

**Impacto:** `backend/domain.py` é a fonte inicial do contrato; os testes cobrem seis casos essenciais. Persistência, API, provedor e execução de estratégia permanecem como etapas seguintes.

## 02/09/2026 — Execução long-only determinística inicial

**Decisão:** o primeiro executor aceita barras OHLCV normalizadas e uma função de sinal, abre no candle seguinte ao sinal, aplica slippage e encerra por stop, alvo ou fim dos dados.

**Motivo:** a regra de entrada no candle seguinte reduz look-ahead bias e a função de sinal mantém a estratégia separada do executor. A política explícita de candle ambíguo evita resultados silenciosamente diferentes.

**Impacto:** `backend/backtest.py` calcula operações, resultado bruto, custos, líquido, gains, losses e drawdown. Não há fonte externa, persistência ou execução real.

## 02/09/2026 — Estratégia separada do executor

**Decisão:** estratégias recebem o índice atual e a sequência OHLCV, retornando apenas um sinal booleano; o executor continua responsável por entrada, saída, custos e métricas.

**Motivo:** reduz acoplamento e permite testar a causalidade da estratégia separadamente. O exemplo inicial usa cruzamento de médias móveis e não consulta candles posteriores ao índice.

**Impacto:** `backend/strategies.py` é demonstrativo, não uma recomendação de investimento. Parâmetros, persistência e seleção na interface serão integrados em etapa posterior.

## 02/09/2026 — Adaptador textual para configuração

**Decisão:** campos vindos da interface são convertidos em `BacktestConfig` por `backend/configuration.py`, com parsing explícito de ISO dates, horários, inteiros, floats e enums.

**Motivo:** a tela não deve duplicar regras de domínio nem aceitar valores inválidos silenciosamente. O adaptador falha com `ValidationError` antes de qualquer execução.

**Impacto:** o fluxo ainda não consulta dados externos e não persiste configurações. A próxima etapa pode usar uma fixture local pequena para ligar formulário, executor e métricas.

## 02/09/2026 — Fixture CSV pequena para integração local

**Decisão:** a primeira integração usa somente `data/sample_ohlcv.csv`, com seis barras sintéticas e timestamps UTC, lidas por `backend/fixture.py`.

**Motivo:** permite testar o fluxo completo sem depender de rede, credenciais, licença de dados ou disponibilidade de provedor. O arquivo é explicitamente uma fixture, não histórico de mercado para decisão.

**Impacto:** o leitor exige cabeçalho OHLCV, timezone e timestamps crescentes. Dados reais e integrações externas permanecem fora do escopo desta etapa.
