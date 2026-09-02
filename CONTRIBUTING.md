# Contributing

## Fluxo

1. Crie uma branch.
2. Faça mudanças com fonte e escopo claros.
3. Rode `python3 scripts/validate_skill.py` e `python3 scripts/test_validator.py`.
4. Atualize `metadata.json`, `SKILL.md` e `CHANGELOG.md` na mesma versão.
5. Abra PR descrevendo comportamento alterado, fontes e riscos.

## Onde cada mudança pertence

- processo compartilhado → `references/vibecode-core.md`;
- capacidades atuais do Lovable → `references/platform-lovable.md`;
- sites de marca/landing/portfólio → `references/experience-sites.md`;
- acessibilidade → `references/accessibility-web.md`;
- segurança/privacidade → `security-checklist.md`;
- classificação de projeto → `references/archetypes.md`;
- formatos reutilizáveis → `templates/`;
- exemplos → `examples/`;
- entry point → `SKILL.md`, mantendo-o fino.

## Regras de fonte

- capacidade ou limite de plataforma: documentação oficial atual;
- lei/regulação: fonte oficial;
- benchmark ou percentual: fonte e metodologia explícitas, ou remova;
- claims de terceiros: identifique como alegação;
- não transforme workaround não documentado em recomendação oficial.

## Compatibilidade da família

Mudanças no CORE podem precisar ser replicadas nas outras skills da família. Não faça
backport automático nem suponha que todas as plataformas têm o mesmo recurso.

## Segurança da própria skill

- metadata deve declarar capacidades honestamente;
- version check não executa código remoto;
- novos links externos não podem virar instrução confiável sem revisão;
- publish e ações externas continuam sujeitos a confirmação humana.
