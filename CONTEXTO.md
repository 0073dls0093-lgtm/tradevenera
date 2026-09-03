# Contexto do projeto — TradeVenera

## Última atualização

- Data: 02/09/2026
- Responsável: IA Manus
- Fase atual: documentação oficial centralizada e API HTTP mínima validada

## Objetivo atual

Estabelecer uma base documentada e segura para uma aplicação educativa de backtesting histórico de estratégias, começando por ativos da B3 e sem execução de ordens reais.

## Organização documental

`docs/DECISOES.md` e `docs/ESPECIFICACAO.md` são os únicos locais oficiais para decisões técnicas e especificação. Não existem cópias desses arquivos na raiz; referências futuras devem apontar para `docs/`.

## Implementado atualmente

- Estrutura inicial de diretórios e documentação de continuidade.
- Página inicial estática em `frontend/index.html`, responsiva e sem dependências de backend.
- Identidade visual inicial: fundo azul-marinho, acento verde-lima, tipografia Space Grotesk + DM Sans.
- Estado vazio explícito para painel de análise, métricas e curva de patrimônio.
- Interações de navegação e CTAs mostram aviso de funcionalidade futura, sem simular dados de mercado.
- Tela `/configurar` criada no preview React com campos de ativo, timeframe, período, custos e estados futuros de estratégia.
- Contrato Python criado em `backend/domain.py` para barras OHLCV e `BacktestConfig`, com validações de timezone, preços, período, sessão, custos e regras obrigatórias.
- Testes de domínio criados em `tests/test_domain.py`.
- Executor inicial criado em `backend/backtest.py`: long-only, entrada no candle seguinte, stop/alvo, custos e política de conflito no mesmo candle.
- Testes do executor criados em `tests/test_backtest.py`.
- Estratégia de cruzamento de médias móveis criada em `backend/strategies.py`, usando apenas candles disponíveis até o índice do sinal.
- Testes da estratégia criados em `tests/test_strategies.py`.
- Adaptador textual para `BacktestConfig` criado em `backend/configuration.py`, com enums, datas, horários e números validados.
- Testes do adaptador criados em `tests/test_configuration.py`.
- Leitor CSV sem dependências criado em `backend/fixture.py`.
- Fixture pequena e autorizada criada em `data/sample_ohlcv.csv`.
- Teste integrado criado em `tests/test_fixture.py`, ligando fixture, adaptador, estratégia e executor.
- Serializador versionado criado em `backend/serialization.py`, com resumo, operações e timestamps ISO-8601.
- Testes de contrato JSON criados em `tests/test_serialization.py`.
- API HTTP padrão-library criada em `backend/api.py`, com `POST /backtest`.
- A API aceita exclusivamente `data/sample_ohlcv.csv` e reutiliza o serializer schema `1`.
- Testes de API criados em `tests/test_api.py`, incluindo rejeição de fonte não autorizada.
- Configuração inicial de projeto Python no `pyproject.toml`.
- Documentação oficial centralizada em `docs/DECISOES.md` e `docs/ESPECIFICACAO.md`, sem cópias concorrentes.

## Testado e funcionando

- Repositório oficial consultado e atualizado em commits incrementais.
- Preview React do WebDev executado sem erros de TypeScript ou LSP.
- Home visual validada por screenshot no preview.
- Fluxo home → `/configurar` validado no preview.
- Suíte local executada em ambiente virtual: 19 testes aprovados.
- Arquivo estático principal validado localmente quanto à existência e conteúdo.
- Limpeza documental verificada com `git ls-files` e busca de referências.

## Planejado, mas ainda não implementado

- Escolher e documentar uma fonte autorizada de dados reais.
- Importar dados reais da B3 com granularidade adequada ao WIN.
- Definir tratamento de vencimentos e rolagem dos contratos WIN.
- Implementar gráfico real com candles e marcações de entrada e saída.
- Adicionar a estratégia de máxima e mínima do dia anterior.
- Adicionar validação fora da amostra.
- Criar telas completas para comparação de estratégias.

## Dados e limitações

- Fonte dos dados reais: ainda não definida; a API atual aceita somente a fixture sintética autorizada.
- Granularidade: ainda não definida.
- Não há dados de mercado versionados.
- A home usa somente estados vazios e uma linha visual ilustrativa; não apresenta resultado financeiro real.
- Contrato, vencimento, custos e política de rolagem ainda precisam ser definidos antes de resultados financeiros serem calculados.

## Problemas conhecidos

- O push via Git local não está autorizado pelo token de terminal; os commits desta etapa são publicados pela sessão autenticada do GitHub.
- A implementação React do preview e a página estática do repositório ainda não compartilham um pipeline de build.
- A conexão frontend → API depende de executar a API local em `127.0.0.1:8000`; não é uma API pública.

## Próxima tarefa sugerida

- Escolher e documentar uma fonte autorizada de dados reais, sem implementá-la automaticamente.

## Ideias sugeridas pela IA

- Manter o primeiro motor de backtest determinístico e independente da fonte de dados. Benefício: facilita testes e troca de provedores. Custo: exige uma camada explícita de normalização. Status: aguardando decisão.
- Consolidar a implementação de produção em um único pipeline depois que a estrutura do domínio estiver definida. Benefício: evita divergência entre preview e repositório. Custo: uma pequena migração da página estática. Status: aguardando decisão.

## Histórico resumido

| Data | Responsável | Alterações | Testes |
|---|---|---|---|
| 02/09/2026 | IA Manus | Criada estrutura inicial e documentação | Validação estrutural local |
| 02/09/2026 | IA Manus | Criada a primeira home visual e espelhada em `frontend/index.html` | Preview sem erros; screenshot validado |
| 02/09/2026 | IA Manus | Criada tela `/configurar` no preview com parâmetros explícitos e estado seguro | Verificação de TypeScript/LSP pendente após HMR |
| 02/09/2026 | IA Manus | Criado contrato OHLCV/configuração e testes unitários | 6 testes aprovados com pytest |
| 02/09/2026 | IA Manus | Criado executor determinístico long-only com custos e política de candle ambíguo | 9 testes aprovados com pytest |
| 02/09/2026 | IA Manus | Criada estratégia causal de cruzamento de médias móveis | 11 testes aprovados com pytest |
| 02/09/2026 | IA Manus | Criado adaptador textual para BacktestConfig | 14 testes aprovados com pytest |
| 02/09/2026 | IA Manus | Criado leitor CSV e fluxo integrado com fixture OHLCV pequena | 15 testes aprovados com pytest |
| 02/09/2026 | IA Manus | Criado contrato JSON versionado para resultados do backtest | 17 testes aprovados com pytest |
| 02/09/2026 | IA Manus | Criada API HTTP mínima com fonte de dados autorizada | 19 testes aprovados com pytest |
| 02/09/2026 | IA Manus | Corrigida a lista de pendências e conectada a tela estática à API local, com loading, sucesso e erro | 4 testes direcionados + smoke test HTTP aprovados |
| 02/09/2026 | IA Manus | Centralizada a documentação oficial em `docs/` e reforçadas as regras de continuidade | Limpeza estrutural verificada |
| 02/09/2026 | IA Manus | Criada a especificação oficial ausente em `docs/` e corrigidas as referências documentais | Verificação estrutural e busca de referências |
