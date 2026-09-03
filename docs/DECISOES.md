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

## 02/09/2026 — Fonte oficial inicial limitada a dados diários de derivativos

**Decisão:** adotar os dados históricos publicados pela B3 como fonte autorizada candidata para uma futura integração de dados diários de derivativos, especialmente preços de ajuste e resumo estatístico. Não considerar essa fonte, neste momento, suficiente para histórico intradiário OHLCV do WIN.

**Motivo:** a página oficial de dados históricos da B3 disponibiliza uma seção de derivativos com preços de ajuste e resumo estatístico, enquanto a plataforma de market data informa que cotações de mercado são distribuídas por distribuidores autorizados. A documentação do pacote `rb3` confirma que seu template de futuros trata preços de ajuste, não candles intradiários. Portanto, usar esses dados como se fossem candles intradiários produziria uma representação inadequada do produto.

**Alternativas consideradas:** contratar ou integrar um distribuidor autorizado que forneça histórico intradiário do WIN; aceitar um arquivo fornecido pelo usuário com licença e contrato comprovados; ou começar somente com dados diários de ajuste. A escolha entre essas alternativas depende de granularidade necessária, licença, custo e política de vencimento/rolagem.

**Impacto:** nenhuma importação foi implementada. A fixture sintética continua sendo a única fonte aceita pela API. Antes de aceitar dados reais, será necessário confirmar contrato e vencimento, período, timeframe, horário, formato OHLCV, completude, licença, custos, slippage e política de rolagem. Referências consultadas: [dados históricos da B3](https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/), [plataforma de market data da B3](https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/market-data-platform/) e [documentação do rb3](https://docs.ropensci.org/rb3/).

## 02/09/2026 — Restrição de custo zero e primeira fonte pública

**Decisão:** o TradeVenera não terá dependências pagas, assinaturas, APIs premium ou contratação de distribuidores. A primeira integração real, quando iniciada, deverá usar exclusivamente os dados históricos publicamente disponibilizados pela B3 para derivativos diários, começando por preços de ajuste e resumo estatístico.

**Motivo:** a restrição de custo zero foi definida pelo usuário. A B3 mantém uma página pública de dados históricos com seção de derivativos; essa opção permite validar o pipeline sem cobrança. Ela não deve ser tratada como fonte de candles intradiários do WIN, e a disponibilidade pública não elimina a necessidade de confirmar os termos de uso antes de redistribuir ou versionar dados.

**Impacto:** ficam fora do escopo as fontes comerciais e qualquer integração que exija pagamento. Nenhum dado real foi importado nesta etapa; a API continua aceitando somente a fixture sintética autorizada. A próxima implementação deverá começar por um adaptador reprodutível para dados diários da B3, com validação de formato, contrato, vencimento, datas, completude e licença.

## 02/09/2026 — Bloqueio de versionamento e redistribuição de dados da B3

**Decisão:** não baixar, versionar, redistribuir ou disponibilizar no TradeVenera uma amostra real extraída do portal da B3 sem confirmação específica de autorização. O adaptador de liquidações permanece somente como leitor de um formato normalizado fornecido de forma autorizada.

**Motivo:** a página pública de pesquisa por pregão confirma a existência de arquivos diários de derivativos, incluindo o boletim simplificado de preços de derivativos (`BVBG.187.01`). Porém, os termos de uso do portal informam que os dados são para uso pessoal e restringem reprodução, publicação, distribuição e disponibilização de acesso sem autorização prévia e expressa. A página consultada também não expõe, no conteúdo acessível automaticamente, um layout estável suficiente para confirmar o mapeamento completo do arquivo ao WIN.

**Impacto:** a fonte B3 continua documentada como referência gratuita para pesquisa e futura ingestão autorizada, mas não é usada como fonte operacional do site nesta etapa. O TradeVenera continua sem dados reais versionados e sem candles OHLCV reais. Para avançar, será necessário obter autorização compatível ou receber do usuário um arquivo cuja licença permita o uso pretendido; não será adotada fonte paga.

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

## 02/09/2026 — Payload de resultado versionado

**Decisão:** resultados serão expostos por `backend/serialization.py` no schema `1`, com os campos `summary` e `trades`. Timestamps usam ISO-8601 e a serialização JSON é ordenada e compacta para facilitar testes e logs.

**Motivo:** separa o domínio interno da futura API HTTP e evita que a interface dependa diretamente de dataclasses Python. O serializer não arredonda valores; apresentação e formatação monetária pertencem à camada de interface.

**Impacto:** qualquer alteração incompatível deve criar uma nova versão de schema e manter o contrato anterior durante uma transição documentada.

## 02/09/2026 — API HTTP mínima sobre fixture autorizada

**Decisão:** `backend/api.py` expõe `POST /backtest` usando apenas a biblioteca padrão. A requisição é convertida pelo adaptador existente, executa a estratégia causal sobre `data/sample_ohlcv.csv` e devolve o schema JSON `1`.

**Motivo:** cria um limite HTTP testável sem introduzir framework, rede externa, autenticação ou risco de consulta arbitrária ao filesystem. A fonte é comparada após resolução de caminho e qualquer outra é rejeitada.

**Impacto:** a API é deliberadamente local e demonstrativa. Antes de aceitar dados reais, será necessário definir autenticação, limites de payload, observabilidade, licenciamento da fonte e uma política de execução.

## 02/09/2026 — Tela estática conectada à API local

**Decisão:** `frontend/configurar.html` envia a configuração para `http://127.0.0.1:8000/backtest` e apresenta estados explícitos de execução, sucesso e erro. A API recebeu CORS mínimo e preflight para permitir a execução a partir de um servidor estático local.

**Limite:** a tela não simula resultado quando a API está indisponível; informa como iniciar o processo local. A conexão continua sendo demonstrativa e não consulta dados reais.
