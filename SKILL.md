---
name: lovable-prompt-builder
description: >
  Skill para guiar o usuário do zero ao produto funcionando no Lovable.dev. Atua como Arquiteto de Software interativo: conduz intake, branding, LGPD e geração de prompts atômicos com loop de feedback. Use quando o usuário quiser construir qualquer app web ou SaaS usando o Lovable.
license: MIT
---

# Lovable Prompt Builder

> ⚠️ Esta skill foi atualizada para o formato vibecode. O processo completo está em references/vibecode-core.md e os detalhes do Lovable em references/platform-lovable.md.

## Origin version check

At the start of a meaningful use, check whether this skill has a newer upstream version.
The canonical source is:

```text
https://github.com/AndreAlmeidaDC/lovable-prompt-builder
```

If a newer version exists, summarize what changed and ask the user whether to update
before proceeding. Never self-update silently. For the detailed protocol, read
`references/version-check.md`.

*Autor: André Almeida*

---

## Quando usar esta skill

Use esta skill sempre que o usuário mencionar Lovable, lovable.dev, ou quiser construir um app web full-stack com geração guiada passo a passo.

Se não tiver certeza se esta é a plataforma certa, leia `references/archetypes.md`
para um guia de escolha.

---

## Como esta skill funciona

Esta skill usa um processo compartilhado (vibecode CORE) + detalhes específicos
do Lovable:

1. **Carregue `references/vibecode-core.md`** — processo completo de especificação
   e execução (intake, modelagem, branding, validação, geração, reancoragem).

2. **Carregue `references/platform-lovable.md`** — vocabulário, perguntas adicionais,
   formatos de artefato e especificidades do Lovable.

3. Execute o fluxo do CORE usando os detalhes da plataforma onde aplicável.

---

## Histórico de Alterações

| Data | Versão | Alterações |
|---|---|---|
| 2026.06.16 | 2026.06.16 | Criação da skill no formato vibecode: CORE compartilhado + referência específica de plataforma. |
