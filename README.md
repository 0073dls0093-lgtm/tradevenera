# TradeVenera

Aplicação educativa para análise histórica e backtesting de estratégias de mercado, com foco inicial em ativos da B3, especialmente o contrato futuro de índice WIN.

> **Aviso:** o TradeVenera não envia ordens reais, não é recomendação de investimento e resultados passados não garantem resultados futuros.

## Status

A fundação documental, a home visual, a tela de configuração, o domínio de backtest, o executor determinístico, a estratégia causal, a fixture OHLCV, a serialização JSON versionada e uma API HTTP local mínima já foram implementados e testados. A configuração estática em `frontend/configurar.html` agora envia parâmetros à API local e apresenta estados de carregamento, sucesso e erro.

## Estrutura

- `CONTEXTO.md`: estado factual do projeto e próxima tarefa.
- `AI_INSTRUCTIONS.md`: regras para agentes e colaboradores sequenciais.
- `docs/ESPECIFICACAO.md`: único local oficial do escopo e requisitos da primeira versão.
- `docs/DECISOES.md`: único local oficial das decisões técnicas registradas.
- `frontend/index.html`: primeira entrega visual estática.
- `frontend/configurar.html`: tela estática de configuração conectada à API local.
- `backend/`: domínio, executor, fixture, serializer e API HTTP.
- `data/`: somente amostras pequenas e autorizadas.
- `tests/`: testes automatizados.

## Como visualizar a home e executar a prévia local

Em um terminal, inicie a API a partir da raiz do projeto:

```bash
python3 -m backend.api
```

Em outro terminal, sirva o frontend estático:

```bash
python3 -m http.server 8080 --directory frontend
```

Depois, acesse `http://localhost:8080/configurar.html`. A API aceita somente `data/sample_ohlcv.csv`; não consulta dados reais nem corretoras.

## Regras de segurança

Nunca versionar chaves, tokens, senhas, arquivos `.env` reais ou dados históricos cuja licença não esteja confirmada. A primeira versão não terá integração com corretora nem execução real.
