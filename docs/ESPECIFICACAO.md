# Especificação — TradeVenera

## Objetivo

O TradeVenera é uma aplicação educativa de backtesting histórico de estratégias, com foco inicial em ativos da B3, especialmente o contrato futuro de índice WIN. O sistema deve permitir configurar um backtest, visualizar candles e marcações de operações e consultar métricas como gains, losses, resultado líquido e drawdown.

Backtest não é recomendação de investimento e resultados passados não garantem resultados futuros.

## Escopo da primeira versão

A primeira versão permanece separada de corretoras e de operações reais. O motor deve trabalhar com barras OHLCV normalizadas e configuração explícita de ativo, contrato e vencimento, período, timeframe, horário de pregão, tipo e preço de execução, stop, alvo, encerramento, quantidade, custos, slippage, política para candles ambíguos, rolagem de vencimento e qualidade dos dados.

A execução deve evitar look-ahead bias, sinalizar dados ausentes ou incompletos e informar o número de operações. Quando houver otimização, o período de ajuste deve ser separado do período de validação.

## Estado atual do escopo

A aplicação já possui uma fixture sintética local autorizada, um domínio Python validado, um executor determinístico long-only, uma estratégia causal de cruzamento de médias móveis, serialização JSON versionada, uma API HTTP local mínima e telas estáticas de apresentação e configuração. A API atual aceita somente a fixture `data/sample_ohlcv.csv`; ela não consulta dados reais nem corretoras.

## Fora do escopo atual

Não fazem parte da primeira versão, até decisão específica e documentação correspondente, a execução de ordens reais, a integração com corretoras, a recomendação de investimento, a escolha ou importação automática de dados reais, a rolagem real de contratos WIN e a publicação de dados cuja licença não esteja confirmada.

## Fonte oficial do documento

Este arquivo é o único local oficial da especificação do TradeVenera. Decisões técnicas são registradas exclusivamente em [`DECISOES.md`](DECISOES.md).
