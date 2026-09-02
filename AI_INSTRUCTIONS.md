# Instruções para IAs — TradeVenera

Antes de trabalhar, leia `CONTEXTO.md`, `README.md` e os arquivos diretamente relacionados à tarefa. Continue a partir da próxima tarefa registrada, preservando o que já funciona.

## Regras de trabalho

1. Analise somente os arquivos necessários para a tarefa.
2. Não registre como concluído algo que não esteja implementado e verificado.
3. Execute testes proporcionais às alterações e registre os testes realmente executados em `CONTEXTO.md`.
4. Atualize `CONTEXTO.md` ao concluir uma etapa.
5. Registre decisões técnicas relevantes em `docs/DECISOES.md`.
6. Faça commits pequenos e descritivos quando tiver acesso ao GitHub.
7. Não inclua segredos, credenciais, arquivos `.env` reais ou dados restritos.
8. Não introduza execução de ordens reais, integração com corretora ou mudança de escopo sem decisão explícita.
9. Ao sugerir melhorias relevantes, explique benefício, complexidade, custo, riscos e alternativas antes de implementá-las.
10. Diferencie fatos implementados, itens planejados e hipóteses.

## Regras do backtest

Toda implementação deve tornar explícitos: ativo e vencimento, período e timeframe, horário do pregão, tipo e preço de execução, stop, alvo, encerramento, custos, slippage, quantidade, candles com stop e alvo simultâneos, rolagem de vencimento e qualidade dos dados. O sistema deve evitar look-ahead bias, sinalizar dados incompletos e informar o número de operações.
