# Platform Reference — Lovable

Referência específica da plataforma Lovable. Leia depois de classificar o modo do
projeto no CORE.

> **Snapshot de capacidades:** 2026-09-01. O Lovable muda rápido. Em projeto existente,
> inspecione a stack e as configurações atuais; em projeto novo, consulte a documentação
> oficial quando a escolha técnica for material.

Fontes oficiais principais:

- https://docs.lovable.dev/features/plan-mode
- https://docs.lovable.dev/features/agent-mode
- https://docs.lovable.dev/features/knowledge
- https://docs.lovable.dev/features/skills
- https://docs.lovable.dev/features/design-guidance
- https://docs.lovable.dev/features/browser-testing
- https://docs.lovable.dev/features/testing
- https://docs.lovable.dev/tips-tricks/security-best-practices
- https://docs.lovable.dev/integrations/github

---

## 1. Não presuma a stack

Segundo a documentação do Lovable em 2026, projetos novos podem usar a stack padrão
atual da plataforma, enquanto projetos antigos podem continuar em React + Vite. O
procedimento correto é:

1. **Projeto existente:** leia `package.json`, estrutura de rotas, backend e arquivos de
   estilo antes de propor mudanças.
2. **Projeto novo:** use o padrão atual do Lovable, salvo requisito concreto que peça
   outra arquitetura.
3. Não mencione `tailwind.config.ts`, Vite, TanStack Start, shadcn ou Supabase como
   obrigatórios sem verificar o projeto.
4. Não migre stack durante uma mudança visual ou funcional sem escopo próprio.

O Lovable é voltado a web. Ele pode produzir experiências responsivas/PWA, mas não é
builder de aplicativo mobile nativo.

---

## 2. Modos de execução

### Ponte manual

Use quando a skill está em ChatGPT, Claude ou outro host sem ferramenta Lovable
conectada. Entregue Project Knowledge, prompt de Plan mode, prompt atômico de Agent mode
e prompt de verificação, um por vez.

### Execução conectada

Use quando há conector, MCP ou a skill está importada no próprio Lovable. O agente pode
criar, inspecionar e alterar projetos diretamente, desde que preserve:

- plano aprovado antes de mudanças amplas;
- uma unidade verificável por vez;
- inspeção do retorno;
- autorização explícita para publish, dados reais e ações externas.

Não prometa conexão inexistente. Não force ponte manual quando uma ferramenta Lovable
compatível está disponível.

---

## 3. Onde cada tipo de contexto vive

### Workspace Knowledge

Regras que valem para todos os projetos: padrões de código, bibliotecas preferidas,
qualidade, nomenclatura e políticas compartilhadas.

### Project Knowledge

Contexto durável de um projeto: propósito, usuários, termos, arquitetura, marca, claims,
segurança, acessibilidade e restrições. Use `templates/PROJECT_KNOWLEDGE.md`.

A documentação informa limite de 10.000 caracteres para cada campo de knowledge. Seja
direto. Não cole histórico de chat nem plano transitório.

### Instruction files

Quando o projeto está sincronizado com Git, use `AGENTS.md` na raiz para regras técnicas
duráveis. O Lovable também pode considerar outros arquivos de instrução, mas evite
duplicar regras contraditórias em vários lugares.

### Skills

Skills do workspace são playbooks sob demanda. Este repositório pode ser importado em
Settings → Skills por URL pública, pois contém `SKILL.md` na raiz. A descrição deve
começar pelo gatilho e a skill deve manter um trabalho principal bem definido.

### Plano

Plan mode pensa sem alterar código. Quando aprovado, o plano mais recente fica em
`.lovable/plan.md`. O plano não substitui Project Knowledge.

---

## 4. Sequência recomendada

1. Classificar o modo e reunir fontes.
2. Criar/atualizar Project Knowledge.
3. Usar Plan mode para arquitetura, mudança ampla ou Experience Spec.
4. Revisar o plano e definir o limite do primeiro build.
5. Usar Design Guidance quando a direção visual estiver aberta.
6. Submeter uma direção somente após escolha humana; a submissão inicia o build, então
   o prompt já deve limitar essa etapa.
7. Inspecionar diff/preview.
8. Retornar a Plan mode quando a próxima unidade exigir decisão.
9. Usar Agent mode para uma unidade de implementação.
10. Verificar em prompt separado e repetir.
11. Publicar somente após gate humano e técnico.

---

## 5. Design Guidance e design system

### Design Guidance

Para landing pages, portfólios e sites visuais, peça três direções quando ainda houver
espaço de decisão. Os previews são leves e usam placeholders; servem para escolher
linguagem, não para aprovar copy ou implementação final. **Design Guidance não é um
modo de planejamento separado:** quando a direção é submetida, o Lovable inicia o build.
Por isso, antes de dispará-la, defina no prompt o escopo do primeiro build. Em site
experiencial, prefira shell semântico e hero estático; deixe Canvas/WebGL, som, backend
e tracking para unidades posteriores.

Se marca, tokens e composição já estiverem definidos, forneça um brief detalhado e pule
variações genéricas.

### Tokens

Use o sistema de tokens já presente no projeto. Em muitos projetos Lovable, cores,
tipografia e radius vivem como variáveis CSS. Não presuma que `tailwind.config.ts`
existe.

Formato recomendado:

```text
DESIGN TOKENS — [projeto]

Color roles
- --background:
- --foreground:
- --surface:
- --surface-elevated:
- --muted:
- --muted-foreground:
- --primary:
- --primary-foreground:
- --accent:
- --border:
- --focus-ring:
- --destructive:
- --success:
- --warning:

Typography
- body:
- display:
- mono:
- scale:
- line-height:

Geometry
- radius:
- spacing rhythm:
- content width:
- grid:

Interaction
- focus:
- hover:
- motion:
- reduced motion:

Rules
- Use semantic tokens, not raw color utilities in components.
- Preserve contrast in every state.
- Do not replace official brand assets with generated approximations.
```

Para times com biblioteca aprovada, avalie Design Systems e templates do Lovable em vez
de pedir que cada projeto regenere componentes.

---

## 6. Decisão de backend

| Necessidade | Decisão inicial |
|---|---|
| Site estático, portfólio, campanha ou protótipo visual | frontend-only |
| Formulário ainda sem destino aprovado | UI simulada; não enviar dados |
| Persistência simples, auth, storage, realtime | Lovable Cloud ou Supabase, conforme governança |
| Banco/infra já existentes | integrar somente após contrato e segurança definidos |
| Requisito de residência, controle ou migração | avaliar backend externo/híbrido |
| Pagamento, email ou API com segredo | fronteira server-side; segredo nunca no cliente |

A documentação oficial recomenda frontend-first com dados mockados como caminho válido.
Não conecte banco no primeiro prompt apenas porque a plataforma consegue.

PostHog, Sentry, Resend, Stripe, gateways de LLM e outros serviços são opcionais. Cada um
precisa de caso de uso, responsável, base legal/consentimento quando aplicável, custo,
ambiente e critério de sucesso.

---

## 7. Arquitetura dos prompts

### A. Project Knowledge

Persistente, sem task atual. Use o template do repositório.

### B. Prompt de Plan mode

```text
MODO: Plan. Não altere código.

OBJETIVO
[resultado desejado]

CONTEXTO RELEVANTE
[fontes, estado atual e decisões]

RESTRIÇÕES
[o que preservar, o que não criar, limites de stack e publicação]

PEDIDO
Investigue o projeto e produza um plano editável com:
- arquivos/áreas afetados;
- decisões e trade-offs;
- sequência atômica;
- riscos e rollback;
- testes;
- dúvidas realmente bloqueantes.

Não implemente. Não publique.
```

### C. Prompt atômico de Agent mode

Use `templates/ATOMIC_PROMPT.md`. Uma mudança, critérios observáveis, sem deploy.

### D. Prompt de verificação

```text
Verifique somente a mudança recém-implementada.

Use o método adequado:
- build/typecheck/lint para integridade;
- frontend test para regra isolada;
- browser testing para fluxo visível;
- chamada/teste de backend para lógica servidor.

Cheque também console e requests quando usar browser testing.
Não corrija silenciosamente problemas fora do escopo; liste-os.
Não publique e não envie dados reais.
```

Separar mudança e browser testing é especialmente importante: a documentação do Lovable
recomenda construir primeiro e testar em uma mensagem posterior.

---

## 8. Browser testing

É útil para:

- screenshots;
- navegação, cliques e formulários;
- console e rede;
- erros de runtime;
- mobile, tablet e desktop.

Limites documentados:

- não opera bem Canvas/desenho;
- upload/download e right-click não são suportados;
- drag-and-drop e clipboard podem ser instáveis;
- não é confiável para sutilezas de design ou cor;
- ícones sem texto podem ser difíceis de acionar.

Para sites experienciais, teste o fallback DOM e faça revisão humana separada da camada
Canvas/WebGL.

---

## 9. Segurança

Use `security-checklist.md`.

Princípios específicos:

- frontend é público e não toma decisão de segurança;
- secrets ficam em fronteira server-side/secret manager;
- tabelas em schemas expostos usam RLS deny-by-default e policies explícitas;
- validação existe no cliente para UX e no servidor/banco para confiança;
- execute o Security view/scan e atualize resultados antes do release;
- não use service role no cliente;
- não copie dados pessoais para chat, logs ou screenshots.

---

## 10. SEO, descoberta e GEO

A stack atual do Lovable oferece renderização voltada a crawlers, mas a implementação
deve ser verificada no projeto.

Para página pública indexável:

- title e description próprios;
- canonical consistente;
- headings e HTML semântico;
- conteúdo principal presente em texto renderizado;
- Open Graph quando compartilhamento importa;
- sitemap e robots coerentes;
- JSON-LD somente para tipos realmente representados;
- performance, mobile e acessibilidade;
- páginas de prova, documentação ou FAQ com fontes e limites claros.

`llms.txt` pode ser experimento complementar. `ai-summary.md` não é requisito universal.
Não declare arquivos opcionais como garantia de ranking em mecanismos generativos.

Google Search Console é configuração externa e só se aplica a domínio publicado que deve
ser indexado. Gerar a meta tag é diferente de configurar a conta e submeter sitemap.

---

## 11. Git, preview e publicação

- Conecte GitHub quando ownership, revisão, branch, CI ou portabilidade justificarem.
- Confirme como o projeto lida com branch/default branch antes de editar fora do Lovable.
- Use preview para aprovação; URL acessível não significa direção aprovada.
- Confirme rollback antes do deploy.
- Publish é ação separada e explícita.

### Badge

A documentação oficial informa que usuários pagantes podem ocultar o badge em Project
Settings. Em plano gratuito, não proponha CSS para esconder `#lovable-badge`; é um
workaround frágil e pode contornar a regra comercial da plataforma.

---

## 12. Reancoragem no Lovable

Quando houver drift:

1. atualize Project Knowledge;
2. confira `.lovable/plan.md`;
3. referencie arquivos relevantes com `@`;
4. informe o último estado verificado;
5. peça uma correção atômica.

Cross-project referencing pode reutilizar código, assets e padrões de outro projeto do
mesmo workspace em modo somente leitura. Use apenas quando o usuário autorizar e a
referência for realmente canônica.
