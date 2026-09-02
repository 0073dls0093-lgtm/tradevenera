# Especificação inicial

## Visão do produto

O TradeVenera permitirá configurar um backtest histórico educativo, executar uma estratégia sobre dados OHLCV autorizados e visualizar operações e estatísticas. A primeira versão será exclusivamente histórica e não enviará ordens.

## Escopo inicial

A primeira entrega funcional deverá aceitar uma série OHLCV normalizada, uma configuração de backtest e regras de estratégia claramente documentadas. O resultado deverá incluir operações, gains, losses, resultado líquido, drawdown e alertas sobre limitações dos dados.

## Configuração obrigatória

- Ativo, contrato e vencimento;
- período e timeframe;
- horário do pregão;
- tipo de ordem e preço de execução;
- stop loss, alvo e regra de encerramento;
- corretagem, emolumentos e slippage;
- quantidade de contratos;
- regra para candle em que stop e alvo ocorrem no mesmo intervalo;
- regra de rolagem do vencimento;
- fonte, período e qualidade dos dados.

## Critérios de confiabilidade

O motor não pode usar informação futura para gerar sinais. Dados ausentes ou incompletos devem ser informados. O resultado deve exibir o número de operações e separar período de ajuste de período de validação quando houver otimização.

## Marco de interface atual

A tela inicial de configuração deverá apresentar o ativo, o timeframe, o período e a opção de considerar custos antes de permitir a execução. Regras de estratégia que ainda não possuem contrato de implementação devem aparecer como indisponíveis, e não como valores simulados. Até a definição da fonte e do modelo OHLCV, a tela não persiste configurações nem calcula métricas.

## Fora do escopo inicial

Execução real, conexão com corretoras, recomendações de investimento, otimização automática irrestrita, promessa de dados gratuitos e suporte a qualquer ativo sem validação de contrato e licença.
