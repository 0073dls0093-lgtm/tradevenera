# TradeVenera



Aplicação educativa para análise histórica e backtesting de estratégias de mercado, com foco inicial em ativos da B3, especialmente o contrato futuro de índice WIN.



> **Aviso:** o TradeVenera não envia ordens reais, não é recomendação de investimento e resultados passados não garantem resultados futuros.
> 


## Status



O projeto está na fase de fundação: documentação, regras iniciais e estrutura de trabalho foram criadas. O motor de backtest e a interface ainda não foram implementados.



## Estrutura



- `CONTEXTO.md`: estado factual do projeto e próxima tarefa.
- 
- `AI_INSTRUCTIONS.md`: regras para agentes e colaboradores.
- 
- `docs/ESPECIFICACAO.md`: escopo e requisitos da primeira versão.
- 
- `docs/DECISOES.md`: decisões técnicas registradas.
- 
- `backend/`: futura API e domínio de backtesting.
- 
- `frontend/`: futura interface web.
- 
- `data/`: somente amostras pequenas e autorizadas.
- 
- `tests/`: testes automatizados.
- 


## Próximos passos



1. Definir o modelo de dados OHLCV e o contrato de entrada da API.
2. 
2. Implementar um motor determinístico de backtest com custos, slippage e regras explícitas.
3. 
3. Adicionar dados de exemplo pequenos e testes de casos-limite.
4. 
4. Criar a primeira tela de configuração e resultados.
5. 


## Regras de segurança



Nunca versionar chaves, tokens, senhas, arquivos `.env` reais ou dados históricos cuja licença não esteja confirmada. A primeira versão não terá integração com corretora nem execução real.














