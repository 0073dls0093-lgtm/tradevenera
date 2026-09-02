# TradeVenera

Aplicação educativa para análise histórica e backtesting de estratégias de mercado, com foco inicial em ativos da B3, especialmente o contrato futuro de índice WIN.

> **Aviso:** o TradeVenera não envia ordens reais, não é recomendação de investimento e resultados passados não garantem resultados futuros.

## Status

A fundação documental e a primeira home visual já foram criadas. A página estática em `frontend/index.html` apresenta a proposta do produto, o estado vazio do painel de análise e os limites da primeira versão. O motor de backtest, a fonte de dados e a interface de configuração ainda não foram implementados.

## Estrutura

- `CONTEXTO.md`: estado factual do projeto e próxima tarefa.
- `AI_INSTRUCTIONS.md`: regras para agentes e colaboradores.
- `docs/ESPECIFICACAO.md`: escopo e requisitos da primeira versão.
- `docs/DECISOES.md`: decisões técnicas registradas.
- `frontend/index.html`: primeira entrega visual estática, sem backend.
- `backend/`: futura API e domínio de backtesting.
- `data/`: somente amostras pequenas e autorizadas.
- `tests/`: testes automatizados.

## Como visualizar a home

A página pode ser aberta diretamente no navegador ou servida por qualquer servidor HTTP estático. Por exemplo:

```bash
python3 -m http.server 8080 --directory frontend
```

Depois, acesse `http://localhost:8080`.

## Próximos passos

1. Definir o modelo de dados OHLCV e o contrato de entrada da API.
2. Implementar um motor determinístico de backtest com custos, slippage e regras explícitas.
3. Adicionar dados de exemplo pequenos e testes de casos-limite.
4. Criar a tela de configuração e conectar a home ao fluxo real.

## Regras de segurança

Nunca versionar chaves, tokens, senhas, arquivos `.env` reais ou dados históricos cuja licença não esteja confirmada. A primeira versão não terá integração com corretora nem execução real.
