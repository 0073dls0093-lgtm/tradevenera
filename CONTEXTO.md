# Contexto do projeto — TradeVenera

## Última atualização

- Data: 02/09/2026
- Responsável: IA Manus
- Fase atual: fluxo demonstrativo com ajuste/validação integrado e API HTTP validada

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
- Adaptador sem dependências em `backend/settlements.py` para registros normalizados de preços de ajuste diários da B3; não converte esses registros em OHLCV.
- API devolve candles da fixture e aviso explícito de demonstração; `frontend/configurar.html` renderiza um gráfico SVG com candles e marcações de entrada/saída.
- Estratégia causal `previous_day_high_breakout_signal` adicionada: usa somente máximas de dias anteriores e rompe pelo fechamento atual.
- API e interface permitem selecionar explicitamente `moving_average` ou `previous_day_high` no modo demonstração.
- Utilitário `backend/validation.py` separa períodos de ajuste e validação fora da amostra sem sobreposição.
- API retorna resumos separados de ajuste e validação, e a interface os exibe junto do resultado total.

## Testado e funcionando

- Repositório oficial consultado e atualizado em commits incrementais.
- Preview React do WebDev executado sem erros de TypeScript ou LSP.
- Home visual validada por screenshot no preview.
- Fluxo home → `/configurar` validado no preview.
- Suíte local executada em ambiente virtual: 27 testes aprovados nesta versão.
- Arquivo estático principal validado localmente quanto à existência e conteúdo.
- Limpeza documental verificada com `git ls-files` e busca de referências.
- Suíte e smoke test HTTP executados após a inclusão do gráfico demonstrativo.
- Suíte local: 27 testes aprovados; smoke test HTTP confirmou o campo `evaluation`.

## Planejado, mas ainda não implementado

- Importar dados reais da B3 com granularidade adequada ao WIN.
- Definir tratamento de vencimentos e rolagem dos contratos WIN.
- Criar telas completas para comparação de estratégias.

## Dados e limitações

- Fonte dos dados reais: a B3 publica arquivos públicos de derivativos diários, mas os termos do portal restringem reprodução, distribuição e disponibilização sem autorização expressa. O Kaggle “Mini Index Futures (WIN) Dataset”, de Rafael G. Eder, declara CC BY-NC 4.0 e foi avaliado apenas como opção de protótipo não comercial; nenhum arquivo foi baixado ou versionado.
- Granularidade: ainda não definida.
- Não há dados de mercado versionados; nenhuma amostra real será adicionada sem licença compatível.
- A home usa somente estados vazios e uma linha visual ilustrativa; não apresenta resultado financeiro real.
- Contrato, vencimento, custos e política de rolagem ainda precisam ser definidos antes de resultados financeiros serem calculados.

## Problemas conhecidos

- O push via Git local não está autorizado pelo token de terminal; os commits desta etapa são publicados pela sessão autenticada do GitHub.
- A implementação React do preview e a página estática do repositório ainda não compartilham um pipeline de build.
- A conexão frontend → API depende de executar a API local em `127.0.0.1:8000`; não é uma API pública.

## Próxima tarefa sugerida

- Criar telas completas para comparação de estratégias.

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
| 02/09/2026 | IA Manus | Documentada a B3 como fonte candidata para derivativos diários, sem importação | Referências oficiais consultadas; implementação não alterada |
| 02/09/2026 | IA Manus | Fixada a restrição de custo zero e escolhida a fonte pública da B3 para a primeira integração | Documentação atualizada; sem importação |
| 02/09/2026 | IA Manus | Criado adaptador independente para liquidações diárias normalizadas da B3 | 18 testes aprovados; sem dados reais versionados |
| 02/09/2026 | IA Manus | Avaliados arquivos públicos e termos da B3; bloqueado o versionamento sem autorização específica | Pesquisa documental; nenhum download ou dado real incorporado |
| 02/09/2026 | IA Manus | Avaliado o dataset Kaggle WIN sob CC BY-NC 4.0, sem download ou cópia | Página do dataset e licença Creative Commons consultadas |
| 02/09/2026 | IA Manus | Adicionada estratégia causal de rompimento da máxima do dia anterior | 20 testes aprovados; somente fixture sintética |
| 02/09/2026 | IA Manus | Integrada seleção explícita de estratégia na API e interface | 22 testes aprovados; checkpoint publicado |
| 02/09/2026 | IA Manus | Criada separação contígua e sem sobreposição para validação fora da amostra | 27 testes aprovados; checkpoint publicado |
| 02/09/2026 | IA Manus | Integrados resultados de ajuste e validação na API e na interface | 27 testes aprovados + smoke HTTP; checkpoint pendente nesta linha |
