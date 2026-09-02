---
name: lovable-prompt-builder
description: >
  Use when the user wants an end-to-end, gated Lovable workflow for planning,
  building, redesigning, repairing, testing, or releasing a website or web app,
  including landing pages, portfolios, experiential sites, dashboards, internal
  tools, and SaaS; classify the project mode, turn source material into persistent
  knowledge, sequence Plan and Agent work, and avoid forcing unnecessary stack,
  while excluding one-off Lovable questions that do not involve project work.
license: MIT
---

# Lovable Prompt Builder

Skill para conduzir projetos no Lovable da intenção ao release, com processo
proporcional ao tipo de produto. O fluxo completo está em
`references/vibecode-core.md`; as capacidades atuais do Lovable e o formato dos
prompts estão em `references/platform-lovable.md`.

## Origin version check

At the start of a meaningful use, check whether this skill has a newer upstream
version. The canonical source is:

```text
https://github.com/AndreAlmeidaDC/lovable-prompt-builder
```

Read `references/version-check.md` for the protocol. Never self-update silently,
never execute downloaded scripts as part of an update check, and never modify the
user's target project while updating the skill.

## Quando usar

Use esta skill quando o trabalho envolver Lovable para:

- criar ou redesenhar landing pages, sites institucionais, portfólios e experiências
  interativas;
- construir aplicações web, SaaS, dashboards e ferramentas internas;
- estruturar um projeto novo ou recuperar um projeto que perdeu direção;
- transformar briefing, arquivos, URLs, screenshots e decisões existentes em
  especificação executável;
- revisar segurança, acessibilidade, qualidade, performance e preparação para
  publicação.

Não presuma que todo projeto precisa de autenticação, banco, Supabase, analytics,
email ou pagamento. Classifique o projeto primeiro.

## Arquivos que devem ser carregados

1. Sempre carregue `references/vibecode-core.md`.
2. Sempre carregue `references/platform-lovable.md`.
3. Para landing pages, portfólios, campanhas ou sites com ambição visual, carregue
   `references/experience-sites.md`.
4. Para qualquer interface pública ou usada por terceiros, carregue
   `references/accessibility-web.md`.
5. Quando houver dados, autenticação, integrações, pagamentos ou publicação,
   carregue `security-checklist.md`.
6. Quando houver dúvida sobre o tipo de projeto, carregue
   `references/archetypes.md`.

## Contrato de execução

- Use primeiro o contexto que o usuário já forneceu. Não repita perguntas respondidas.
- Diferencie fatos verificados, decisão do usuário, alegação de terceiros e inferência.
- Separe conhecimento persistente, plano, ação atual e verificação.
- Em integração direta com o Lovable, use as ferramentas disponíveis; sem integração,
  entregue prompts para a ponte manual.
- Implemente uma unidade verificável por vez. Não acumule mudanças não testadas.
- Não publique, envie dados reais, acione checkout ou altere serviços externos sem
  autorização explícita.
- Gate técnico não substitui aprovação humana de marca, conteúdo ou experiência.

## Histórico de alterações

| Data | Versão | Alterações |
|---|---|---|
| 2026.09.01 | 2026.09.01 | Processo proporcional por modo; suporte a sites experienciais; Plan/Agent mode, Knowledge, Skills e browser testing; backend opcional; acessibilidade pública por padrão; segurança/LGPD corrigidas; version check e validação endurecidos. |
| 2026.06.23 | 2026.06.23 | Referência de acessibilidade web adicionada. |
| 2026.06.16 | 2026.06.16 | Criação no formato vibecode: CORE compartilhado + referência específica do Lovable. |
