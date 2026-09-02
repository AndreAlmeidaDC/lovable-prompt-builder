# lovable-prompt-builder

Skill para planejar e conduzir projetos no **Lovable** sem transformar todo pedido em
um promptão, um SaaS desnecessário ou uma colagem de efeitos.

Ela atende:

- landing pages, sites institucionais, portfólios e experiências interativas;
- SaaS, dashboards, portais e ferramentas internas;
- projetos novos e projetos existentes que precisam de auditoria ou recuperação;
- uso manual, por prompts, e uso conectado por ferramenta/MCP/skill do Lovable.

## O problema

Quando o Lovable recebe um pedido amplo, precisa adivinhar produto, stack, dados,
permissões, marca, conteúdo, interação e release. O retrabalho não vem apenas de prompt
ruim. Vem de misturar decisões permanentes, plano, implementação e teste numa mesma
mensagem.

A skill separa essas camadas e escolhe um processo proporcional ao projeto.

## O que mudou na versão 2026.09.01

- backend, Supabase, auth e integrações deixaram de ser padrão obrigatório;
- foi adicionado o modo **Experience/Marketing Site**;
- sites públicos usam acessibilidade por padrão;
- Project Knowledge, Plan mode, Agent mode, Design Guidance, Skills e browser testing
  entraram no fluxo;
- o kickoff monolítico foi substituído por knowledge → plano → prompt atômico →
  verificação;
- segurança e LGPD foram corrigidas e passaram a usar perfis internos de risco, não
  “níveis de conformidade”;
- o protocolo de versão deixou de apontar para outro repositório;
- badge por CSS, estatísticas sem fonte e arquivos GEO tratados como obrigatórios foram
  removidos;
- o validador agora checa drift, origem, versão e padrões proibidos.

## Modos de projeto

### Product/App

SaaS, dashboard, portal ou ferramenta com lógica persistente. Dados, auth e backend só
entram quando justificados.

### Experience/Marketing Site

Landing, portfólio, campanha ou experiência de marca. O fluxo exige tese, narrativa,
prova, interaction signature, mobile, reduced motion, fallback e performance antes do
código pesado.

### Existing Project/Repair

Auditoria, preservação do que funciona, mudança mínima, teste de regressão e rollback.

### Component/UI

Componente ou página isolada dentro de projeto existente.

## Como funciona

1. Lê as fontes e identifica autoridade e limites.
2. Classifica o modo.
3. Faz apenas as perguntas que mudam decisões.
4. Produz os artefatos necessários — não todos por ritual.
5. Cria Project Knowledge.
6. Usa Design Guidance e Plan mode quando cabem.
7. Implementa uma unidade por vez em Agent mode.
8. Verifica em mensagem separada.
9. Exige gate humano antes de publicar.

## Duas formas de usar

### Dentro do Lovable

O Lovable permite importar skills públicas por URL do GitHub em Settings → Skills.
Depois de importada, esta skill funciona como playbook do workspace.

### Em outro agente

ChatGPT, Claude ou outro agente pode usar a skill para produzir prompts. Quando houver
conector/MCP do Lovable, pode executar diretamente; sem conexão, o usuário faz a ponte
de copiar e colar.

A skill nunca deve fingir que tem acesso a uma plataforma desconectada.

## Backend não é ritual

Frontend-first com mocks é um caminho válido. Uma landing page pode terminar sem banco.
Uma aplicação pode começar visualmente e conectar backend depois. Quando houver dados,
a skill passa a exigir modelagem, autorização, RLS/policies, validação e testes
proporcionais.

## Acessibilidade

Sites e apps públicos ou usados por terceiros ativam WCAG 2.2 AA por padrão. Protótipos
internos isolados podem optar por não ativar, com motivo explícito.

Experiências com som, Canvas, WebGL ou movimento precisam de controle, teclado, reduced
motion e fallback DOM.

## Estrutura

```text
SKILL.md
metadata.json
references/
  vibecode-core.md
  platform-lovable.md
  experience-sites.md
  accessibility-web.md
  archetypes.md
  version-check.md
templates/
  PROJECT_KNOWLEDGE.md
  EXPERIENCE_SPEC.md
  ATOMIC_PROMPT.md
  PRD.md
  DATA_MODEL.md
  USER_FLOW.md
examples/
  exemplo_prompt_lovable.md
  exemplo_site_experiencial.md
security-checklist.md
framework_prompting.md
scripts/
  validate_skill.py
  test_validator.py
.github/workflows/
  validate-skill.yml
```

## Validação

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validator.py
```

O validador verifica arquivos, frontmatter, metadata, origem, versão, limites de pacote
e regressões conhecidas.

## Fontes oficiais do Lovable

- Plan mode: https://docs.lovable.dev/features/plan-mode
- Agent mode: https://docs.lovable.dev/features/agent-mode
- Knowledge: https://docs.lovable.dev/features/knowledge
- Skills: https://docs.lovable.dev/features/skills
- Design Guidance: https://docs.lovable.dev/features/design-guidance
- Browser testing: https://docs.lovable.dev/features/browser-testing
- Testing: https://docs.lovable.dev/features/testing
- Security: https://docs.lovable.dev/tips-tricks/security-best-practices

## Licença

MIT — André Almeida
