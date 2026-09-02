# Contexto do projeto — TradeVenera

## Última atualização

- Data: 02/09/2026
- Responsável: IA Manus
- Fase atual: fundação do projeto

## Objetivo atual

Estabelecer uma base documentada e segura para uma aplicação educativa de backtesting histórico de estratégias, começando por ativos da B3 e sem execução de ordens reais.

## Implementado atualmente

- Estrutura inicial de diretórios.
- Documentação de visão, escopo, regras mínimas e fluxo de trabalho entre IAs.
- Política inicial de segurança e proteção de dados sensíveis.
- Configuração inicial de projeto Python no `pyproject.toml`.

## Testado e funcionando

- Repositório clonado com sucesso.
- Arquivos iniciais validados localmente antes do primeiro commit.

## Planejado, mas ainda não implementado

- Motor de backtest.
- API HTTP.
- Interface web e gráfico de candles.
- Importação/validação de dados OHLCV.
- Cálculo de gains, losses, resultado líquido e drawdown.
- Testes automatizados do domínio.

## Dados e limitações

- Fonte dos dados: ainda não definida.
- Granularidade: ainda não definida.
- Não há dados de mercado versionados neste commit.
- Contrato, vencimento, custos e política de rolagem ainda precisam ser definidos antes de resultados financeiros serem calculados.

## Problemas conhecidos

- Nenhum problema conhecido na estrutura inicial.

## Próxima tarefa sugerida

- Definir o modelo de dados OHLCV e implementar a validação de configuração do backtest, acompanhada de testes unitários.

## Ideias sugeridas pela IA

- Manter o primeiro motor de backtest determinístico e independente da fonte de dados. Benefício: facilita testes e troca de provedores. Custo: exige uma camada explícita de normalização. Status: aguardando decisão.

## Histórico resumido

| Data | Responsável | Alterações | Testes |
|---|---|---|---|
| 02/09/2026 | IA Manus | Criada a estrutura inicial e documentação do projeto | Validação estrutural local |
