# Platform Reference — Lovable

Lovable (lovable.dev) é um AI app builder web full-stack. Gera apps React com Supabase,
faz deploy automático e tem um loop de feedback nativo entre o usuário e a IA.

> **Pré-requisito:** complete as Fases 1 a 4 do CORE antes de usar esta referência.
> Esta referência contém o vocabulário, as perguntas adicionais e os formatos de
> artefato específicos do Lovable.

---

## Perguntas adicionais de intake (Fase 1 do CORE)

Após as perguntas genéricas do CORE, adicione:

**Badge do Lovable:**
> "O Lovable adiciona um badge 'Edit with Lovable' no app publicado. Quer remover?
> Em planos pagos remove via Project Settings. Em planos gratuitos esconde via CSS.
> Incluo na fila?"

Se sim, adicione ao final da fila de prompts:
```
Adicione ao src/index.css dentro do @layer base:
#lovable-badge { display: none !important; }
```

**Compliance LGPD:** (relevante para produtos com usuários no Brasil)

9. O produto pode ter **usuários menores de 18 anos**?
10. Vai coletar **dados sensíveis**? (saúde / finanças / biometria / localização
    precisa / dados de crianças)
11. Haverá **serviços de terceiros que processam dados fora do Brasil**?
    (Supabase — EUA, Stripe — EUA, PostHog — EUA/EU)

Com base nas respostas, defina o nível de compliance LGPD:

**Nível Básico** — app simples, sem dados sensíveis, sem menores:
cookie consent, política de privacidade, termos de uso, exportação de dados,
exclusão de conta, audit log.

**Nível Intermediário** — dados financeiros ou menores possíveis:
tudo do básico + cookie consent granular, página de direitos do titular, canal DPO,
base legal explícita por tipo de dado, política de retenção, gate de verificação de idade.

**Nível Avançado** — dados sensíveis (saúde, biometria):
tudo do intermediário + RIPD, consentimento específico por dado sensível, notificação
de incidentes em 72h à ANPD, DPO formalmente designado.

---

## Output de Branding (Fase 3 do CORE — formato Lovable)

O bloco de branding gerado na Fase 3 deve seguir este formato para o Lovable:

```
CONFIGURAÇÃO DE TEMA — [Nome do Projeto]

Cores (tokens Tailwind em tailwind.config.ts):
  primary:     #[hex]  — CTAs, links ativos, destaques
  secondary:   #[hex]  — elementos secundários, hover states
  accent:      #[hex]  — badges, highlights, notificações
  background:  #[hex]  — fundo principal
  foreground:  #[hex]  — texto principal
  muted:       #[hex]  — texto secundário, placeholders
  border:      #[hex]  — bordas, divisores
  destructive: #[hex]  — erros, alertas críticos

Tipografia:
  font-sans:    [família] — corpo de texto e UI
  font-display: [família] — títulos e headings

Border radius: --radius: [valor]rem
Dark mode: [sim / não / toggle]

Componentes shadcn prioritários: [lista]
Tom visual: [1 linha]
Inspirações: [URLs]
Evitar: [referências negativas]

INSTRUÇÃO PARA O LOVABLE:
Configure o tema globalmente no tailwind.config.ts desde o primeiro prompt.
Nunca use cores hardcoded — sempre os tokens definidos acima.
Aplique dark mode via Tailwind dark: prefix em todos os componentes.
```

---

## Estrutura do Prompt Inicial (Kickoff Prompt)

```
# [Nome do Projeto] — Lovable Kickoff Prompt

## Context
[Produto, problema resolvido, usuário final, conexões de negócio.]

## Competitive Edge
[2 a 3 diferenciais concretos baseados na pesquisa de concorrentes.]

## Tech Stack
- React + TypeScript + Tailwind CSS + shadcn/ui
- Supabase (Auth, Database, Storage, Edge Functions)
- PostHog (Analytics)
- Sentry (Error Monitoring)
- Resend (Email Transacional)
- [Stripe — se monetização]

## Branding & Visual Identity
[Bloco completo da Fase 3.]

## Core Features — Priority Order
1. [Feature 1]: [comportamento esperado detalhado]
2. [Feature 2]: [comportamento esperado detalhado]
...

## Onboarding & Empty States
[Fluxo de primeiro acesso. O que o usuário vê sem dados? Ações sugeridas.]

## SEO, GEO & Discoverabilidade

### SEO
- HTML semântico (h1 único por página, landmark roles ARIA)
- Metadata dinâmica por rota (title, description, canonical)
- Open Graph e Twitter Cards por página
- Sitemap.xml gerado automaticamente
- robots.txt com regras explícitas
- Core Web Vitals: LCP < 2.5s / CLS < 0.1 / INP < 200ms

### GEO — Generative Engine Optimization
- /public/llms.txt descrevendo o produto para AI crawlers
- /public/ai-summary.md com resumo completo em linguagem natural para LLMs
- Meta description 150-300 chars com proposta de valor clara
- JSON-LD / Schema.org em todas as páginas

## Database Architecture
[Tabelas com campos, tipos e relações — baseado no modelo da Fase 2.]

## Segurança (sem exceção)
- RLS ativado em TODAS as tabelas
- Políticas RLS explícitas: SELECT, INSERT, UPDATE, DELETE
- NUNCA service_role_key no cliente
- NUNCA secrets em variáveis VITE_
- SEMPRE Edge Functions para integrações externas

## Compliance LGPD — Nível [Básico / Intermediário / Avançado]
[Items do nível definido no intake.]

## Implementation Strategy
1. Fluxo de autenticação completo
2. Layout base com branding aplicado globalmente
3. [Feature 1]
4. [Feature 2]
...
N-1. SEO/GEO + llms.txt + ai-summary.md
N.   Analytics (PostHog) + Error Monitoring (Sentry)

## Safe-Guard Instructions
- NÃO construa tudo de uma vez
- NÃO use service_role_key no cliente
- NÃO crie tabelas sem RLS ativado
- NÃO avance sem o passo anterior funcionando
- NÃO use cores hardcoded — sempre tokens Tailwind
```

---

## Prompt de Pós-Deploy — Google Search Console

Sempre o último prompt, após o produto em produção:

```
Com o app em produção, configure o Google Search Console:
1. Acesse search.google.com/search-console
2. Adicione o domínio e verifique via meta tag no <head>
3. Settings > Sitemaps > adicione [domínio]/sitemap.xml
4. Confirme indexabilidade via URL Inspection
```

---

## Artefatos de Reancoragem (Fase 5.5 do CORE)

Quando a IA do Lovable divergir, recole estes artefatos na sessão:
- O schema de banco (tabelas + RLS)
- A sequência de Implementation Strategy
- O bloco de Safe-Guard Instructions
- O estado atual (o que já está funcionando)

---

## Limitações e Gotchas do Lovable

- Limite de contexto de chat: para projetos longos, abra uma nova conversa com o
  contexto atualizado em vez de acumular erros na mesma sessão.
- O Lovable é cloud-based: o código roda nos servidores deles, não em WebContainer.
  Dependências são mais flexíveis que no bolt.new.
- Badge gratuito: a ocultação via CSS funciona, mas pode quebrar se o Lovable atualizar
  o ID. Verificar periodicamente.
