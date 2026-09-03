# Instruções para IAs — TradeVenera

Antes de trabalhar, leia `CONTEXTO.md`, `README.md` e os arquivos diretamente relacionados à tarefa. Continue a partir da próxima tarefa registrada, preservando o que já funciona.

## Continuidade entre IAs

O TradeVenera é um projeto compartilhado do usuário. As IAs trabalham **sequencialmente**: somente uma IA deve editar o repositório por vez. Ao terminar uma etapa, registre no GitHub o que foi feito, os testes executados, problemas conhecidos, a próxima tarefa e ideias aguardando decisão. A IA seguinte deve consultar esses arquivos e continuar sem depender desta conversa.

`docs/DECISOES.md` e `docs/ESPECIFICACAO.md` são os únicos locais oficiais desses documentos. Não criar cópias na raiz nem manter referências ambíguas.

## Regras de trabalho

1. Analise somente os arquivos necessários para a tarefa.
2. Não registre como concluído algo que não esteja implementado e verificado.
3. Execute apenas os testes proporcionais às alterações e registre os testes realmente executados em `CONTEXTO.md`.
4. Atualize `CONTEXTO.md` ao concluir uma etapa.
5. Registre decisões técnicas relevantes em `docs/DECISOES.md`.
6. Faça commits pequenos e descritivos quando tiver acesso ao GitHub.
7. Não inclua segredos, credenciais, arquivos `.env` reais ou dados restritos.
8. Não introduza execução de ordens reais, integração com corretora ou mudança de escopo sem decisão explícita.
9. Ao sugerir melhorias relevantes, explique benefício, complexidade, custo, riscos e alternativas antes de implementá-las.
10. Diferencie fatos implementados, itens planejados e hipóteses.
11. Trabalhe por partes relacionadas: implemente, verifique e documente cada avanço relevante antes de continuar.
12. Quando a tarefa registrada estiver concluída, pare; não inicie automaticamente outra funcionalidade.
13. Não revise repetidamente o que já foi concluído, não fique rodando em círculos e não repita explicações ou testes sem motivo objetivo.
14. Não envie relatórios longos a cada ação nem gere PDFs, imagens ou outros materiais extras que não foram solicitados. Prefira atualizações curtas e objetivas.
15. Trabalhe em partes relacionadas, salve checkpoints no GitHub, atualize o contexto e pare assim que a tarefa atual estiver concluída e verificada.

## Regras do backtest

Toda implementação deve tornar explícitos: ativo e vencimento, período e timeframe, horário do pregão, tipo e preço de execução, stop, alvo, encerramento, custos, slippage, quantidade, candles com stop e alvo simultâneos, rolagem de vencimento e qualidade dos dados. O sistema deve evitar look-ahead bias, sinalizar dados incompletos e informar o número de operações.
