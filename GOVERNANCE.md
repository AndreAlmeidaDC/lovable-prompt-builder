# Governance

## Fonte canônica

O repositório canônico está em:

`https://github.com/AndreAlmeidaDC/lovable-prompt-builder`

O protocolo de atualização lê a origem de `metadata.json` e nunca atualiza a skill
silenciosamente.

## Escopo

A skill pode operar de duas formas:

- gerar prompts para ponte manual;
- conduzir uma ferramenta Lovable conectada quando o usuário pedir execução direta.

Em ambos os casos, publish/deploy, mudanças destrutivas, envio de dados reais, cobrança
e mutação de serviços externos exigem autorização explícita.

## Autoridade

Materiais do usuário e fontes canônicas do projeto prevalecem sobre suposições da skill.
A skill deve separar fato verificado, decisão do proprietário, alegação de terceiros e
inferência.

## Mudanças na skill

- processo compartilhado fica no CORE;
- comportamento específico da plataforma fica na referência Lovable;
- mudanças legais e de segurança exigem fonte primária;
- mudança significativa exige version bump e changelog;
- CORE alterado deve ser avaliado para backport consciente à família, sem atualização
  automática de outros repositórios.

## Release da skill

Antes de merge:

1. validator local;
2. revisão de origem e versão;
3. ausência de padrões proibidos;
4. documentação e exemplos coerentes;
5. CI verde.

## Autor

André Almeida — github.com/AndreAlmeidaDC
