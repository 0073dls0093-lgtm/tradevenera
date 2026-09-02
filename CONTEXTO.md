# Contexto do projeto — TradeVenera

## Última atualização

- Data: 02/09/2026
- Responsável: IA Manus
- Fase atual: home visual + tela de configuração inicial

## Objetivo atual

Estabelecer uma base documentada e segura para uma aplicação educativa de backtesting histórico de estratégias, começando por ativos da B3 e sem execução de ordens reais.

## Implementado atualmente

- Estrutura inicial de diretórios e documentação de continuidade.
- Página inicial estática em `frontend/index.html`, responsiva e sem dependências de backend.
- Identidade visual inicial: fundo azul-marinho, acento verde-lima, tipografia Space Grotesk + DM Sans.
- Estado vazio explícito para painel de análise, métricas e curva de patrimônio.
- Interações de navegação e CTAs mostram aviso de funcionalidade futura, sem simular dados de mercado.
- Tela `/configurar` criada no preview React com campos de ativo, timeframe, período, custos e estados futuros de estratégia.
- Configuração inicial de projeto Python no `pyproject.toml`.

## Testado e funcionando

- Repositório oficial consultado e atualizado em commits incrementais.
- Preview React do WebDev executado sem erros de TypeScript ou LSP.
- Home visual validada por screenshot no preview.
- Fluxo home → `/configurar` validado no preview.
- Arquivo estático principal validado localmente quanto à existência e conteúdo.

## Planejado, mas ainda não implementado

- Publicar e organizar todos os documentos em `docs/` no GitHub.
- Motor de backtest.
- API HTTP.
- Importação/validação de dados OHLCV.
- Cálculo de gains, losses, resultado líquido e drawdown.
- Configuração real de estratégia e seletor de ativo.
- Testes automatizados do domínio.

## Dados e limitações

- Fonte dos dados: ainda não definida.
- Granularidade: ainda não definida.
- Não há dados de mercado versionados.
- A home usa somente estados vazios e uma linha visual ilustrativa; não apresenta resultado financeiro real.
- Contrato, vencimento, custos e política de rolagem ainda precisam ser definidos antes de resultados financeiros serem calculados.

## Problemas conhecidos

- O push via Git local não está autorizado pelo token de terminal; os commits desta etapa são publicados pela sessão autenticada do GitHub.
- A implementação React do preview e a página estática do repositório são equivalentes na intenção, mas ainda não compartilham um pipeline de build.

## Próxima tarefa sugerida

- Definir o modelo de dados OHLCV e implementar a validação de configuração do backtest, acompanhada de testes unitários. Em paralelo, espelhar a tela de configuração no frontend estático publicado.

## Ideias sugeridas pela IA

- Manter o primeiro motor de backtest determinístico e independente da fonte de dados. Benefício: facilita testes e troca de provedores. Custo: exige uma camada explícita de normalização. Status: aguardando decisão.
- Consolidar a implementação de produção em um único pipeline depois que a estrutura do domínio estiver definida. Benefício: evita divergência entre preview e repositório. Custo: uma pequena migração da página estática. Status: aguardando decisão.

## Histórico resumido

| Data | Responsável | Alterações | Testes |
|---|---|---|---|
| 02/09/2026 | IA Manus | Criada estrutura inicial e documentação | Validação estrutural local |
| 02/09/2026 | IA Manus | Criada a primeira home visual e espelhada em `frontend/index.html` | Preview sem erros; screenshot validado |
| 02/09/2026 | IA Manus | Criada tela `/configurar` no preview com parâmetros explícitos e estado seguro | Verificação de TypeScript/LSP pendente após HMR |
