# Framework de Prompting para Lovable.dev — v2.0

*Autor: André Almeida*

Este documento consolida as melhores práticas e padrões de prompting para o Lovable.dev, baseado na documentação oficial, comunidade e descobertas da skill `lovable-prompt-builder`. Ele descreve como estruturar requisitos, fazer iterações com feedback do Lovable e entregar produtos em produção.

---

## 1. Princípios Fundamentais

**Atomicidade (Build by component):** Nunca peça para construir tudo de uma vez. Comece pelo layout, depois componentes individuais. O Lovable quebra com escopo demais.

**Separação de preocupações (UI vs Data):** UI é forte. Dados e segurança precisam de direção explícita. Defina schema, RLS e integrações externas no kickoff.

**Contexto é rei:** A IA precisa saber O QUE está construindo, PARA QUEM e POR QUÊ. Contexto de negócio e restrições são fundamentais.

**Branding desde o início:** Cores, fontes e tom visual devem ser tokens Tailwind definidos globalmente no primeiro prompt. Nunca hardcoded.

**Security by design:** RLS, Edge Functions, sem secrets no frontend — não são passos finais, são requisitos de cada componente.

**Feedback loop obrigatório:** Cada prompt entregue depende do sucesso do anterior. Sem exceções.

---

## 2. O Fluxo em 4 Fases

### FASE 1 — Escopo, Badge, LGPD e Concorrentes

Pergunte:
1. Público-alvo? (consumidor / B2B / interno)
2. Monetização?
3. Offline ou PWA?
4. Múltiplos idiomas?
5. Multi-tenant (B2B)?
6. Badge do Lovable — remover?
7. Usuários menores de 18?
8. Dados sensíveis?
9. Serviços de terceiros fora do Brasil?

Output: Nível de compliance LGPD definido (Básico / Intermediário / Avançado).

### FASE 2 — Branding

Pergunte:
- Tem identidade visual existente?
- URLs de inspiração (até 3)?
- Tom visual (minimalista / bold / corporativo / lúdico)?
- Dark mode?
- Referências negativas?

Output: Bloco completo de tokens Tailwind, tipografia, radius, dark mode, componentes shadcn.

```
CONFIGURAÇÃO DE TEMA — [Projeto]

Cores (tokens Tailwind):
  primary:     #[hex]
  secondary:   #[hex]
  accent:      #[hex]
  background:  #[hex]
  foreground:  #[hex]
  muted:       #[hex]
  border:      #[hex]
  destructive: #[hex]

Tipografia:
  font-sans:    [família]
  font-display: [família]

Border radius:
  --radius: [valor]rem

Dark mode: [sim / não / toggle]

Componentes shadcn: [lista]

Tom visual: [descrição]
```

### FASE 3 — Validação

Apresente resumo:
- O que faz, quem usa
- Top 5 features do MVP
- Pensamento lateral (PLG, retenção)
- Backlog imediato
- Diferenciais competitivos
- Nível LGPD
- Branding resumido

Aguarde confirmação EXPLÍCITA.

### FASE 4 — Execução Iterativa

Entregue prompts UM POR UM. Para cada um:

```
Próximo passo: Cole este prompt no Lovable e retorne o resultado.
- "OK / funcionou" — avanço
- Texto do erro — analiso e corrijo
- "Funcionou mas errado" — ajusto
```

Após cada retorno:
- **Sucesso:** Próximo prompt
- **Erro:** Prompt de correção com diagnóstico
- **Parcial:** Anota ou corrige agora?

Último prompt: Google Search Console setup.

---

## 3. Estrutura Ideal do Kickoff

```
# [Nome] — Lovable Kickoff Prompt

*Autor: André Almeida*

## Context
[Produto, problema, usuário, conexões de negócio]

## Competitive Edge
[2-3 diferenciais concretos]

## Tech Stack
React + TypeScript + Tailwind + shadcn/ui
Supabase (Auth, Database, Storage, Edge Functions)
PostHog (Analytics)
Sentry (Error Monitoring)
Resend (Email)
[Stripe — se monetização]

## Branding & Visual Identity
[Bloco completo de tokens Tailwind gerado na Fase 2]

## Core Features — Priority Order
1. **[Feature 1]:** [comportamento esperado]
2. **[Feature 2]:** [comportamento esperado]
...

## Onboarding & Empty States
[Fluxo de primeiro acesso, ações sugeridas]

## SEO, GEO & Discoverabilidade

### SEO
- HTML semântico (h1 único, landmark roles)
- Metadata dinâmica por rota
- Open Graph + Twitter Cards
- Sitemap.xml automático
- robots.txt com regras explícitas
- Imagens com lazy loading e alt text
- Core Web Vitals: LCP < 2.5s / CLS < 0.1 / INP < 200ms
- Dynamic OG images por rota

### GEO — Generative Engine Optimization
- /public/llms.txt (descrição para AI crawlers)
- /public/ai-summary.md (resumo estruturado do produto)
- Meta description 150-300 chars, otimizada para AI
- JSON-LD / Schema.org: WebSite + WebPage + específico por tipo
- HTML que converte bem para markdown
- /blog, /changelog, /docs indexáveis

### Checklist Auditoria SEO/GEO (Lovable nativo)
Todos devem passar antes de encerrar:
- [ ] Homepage heading and structure
- [ ] Google Search Console configurado
- [ ] Crawler rules (robots.txt)
- [ ] Sitemap submetido ao GSC
- [ ] AI summary (/ai-summary.md + meta description)
- [ ] Core Web Vitals OK
- [ ] Schema para rich results
- [ ] Page metadata por rota
- [ ] Social previews (Open Graph)
- [ ] Acessibilidade (WCAG AA)
- [ ] Mobile-friendly
- [ ] Indexabilidade confirmada

## Technical Requirements & Database Architecture

### Banco de Dados
[Tabelas com campos, tipos e relações]

### Segurança (sem exceção)
- RLS em TODAS as tabelas
- Políticas RLS explícitas: SELECT, INSERT, UPDATE, DELETE
- Proteção contra BOLA — OWASP
- NUNCA service_role_key no cliente
- NUNCA secrets em variáveis VITE_
- SEMPRE Edge Functions para integrações externas
- Rate limiting nas Edge Functions críticas
- Gateway de LLM (ex: Portkey) para failover

### Compliance LGPD — Nível [Básico / Intermediário / Avançado]

**Básico:**
Cookie consent, política, termos, exportação de dados, exclusão de conta, audit log

**Intermediário:**
Tudo + cookie consent granular, página de direitos do titular, canal DPO com prazo 15 dias, base legal por tipo de dado, transferência internacional, retenção de dados, gate de idade

**Avançado:**
Tudo + RIPD, consentimento específico por dado sensível, notificação de incidentes 72h, DPO designado

## Monetização [se aplicável]
- Stripe com webhooks via Edge Function
- Página de pricing com planos diferenciados
- Upgrade wall nos recursos premium
- Portal do cliente para gerenciar assinatura

## Notificações & Comunicação
- In-app com preferências por usuário
- Email transacional via Resend
- [Push via PWA — se definido]

## Admin Panel
- Rota /admin protegida por role admin no RLS
- Visão de usuários, métricas, gestão de conteúdo

## Implementation Strategy
1. Fluxo de autenticação completo
2. Layout base com branding aplicado globalmente
3. [Feature 1 do core]
...
N-2. LGPD: cookie consent, políticas, página de direitos
N-1. SEO/GEO: metadata, JSON-LD, sitemap, llms.txt, ai-summary.md
N.   Analytics (PostHog) + Error Monitoring (Sentry)
[Se badge]: CSS para ocultar #lovable-badge

## Safe-Guard Instructions
- NÃO construa tudo de uma vez
- NÃO use service_role_key no cliente
- NÃO use secrets em variáveis VITE_
- NÃO crie tabelas sem RLS ativado
- NÃO ignore empty states e error states
- NÃO avance sem o passo anterior funcionando
- NÃO use cores hardcoded — sempre tokens Tailwind
- NÃO aplique branding de forma parcial
```

---

## 4. Workflow de Produção

Lovable é excelente para prototipagem (70% do trabalho em 10% do tempo). Para produção:

1. **Lovable:** Construir UI, lógica básica, validar ideia
2. **GitHub:** Exportar código, controle de versão
3. **Cursor + MCP:** Refinar código, robustez, otimizar integrações (30% final)
4. **Google Search Console:** Configurar após deploy em produção

---

## 5. Comandos Essenciais

**Clarificação:** "Antes de codar, faça 3 perguntas sobre [feature]: estrutura de dados, fluxo do usuário, edge cases."

**Mock vs Schema:** "Crie a UI com dados mockados. Simultaneamente, defina o SQL exato do Supabase com tipos, RLS policies e foreign keys."

**Restrição de Escopo:** "Aja como fundador solo com orçamento zero. Sem soluções enterprise complexas."

**Teste ELI5:** "Explique esse fluxo como para um adolescente novo em SaaS. Se for difícil, simplifique antes de codar."

---

## 6. Checklist Pré-Deploy

- [ ] RLS ativado em todas as tabelas sensíveis
- [ ] Frontend inspecionado: sem SERVICE_ROLE, sem secrets VITE_
- [ ] APIs de terceiros só via Edge Functions
- [ ] Tabela auth.users não exposta no frontend
- [ ] Acessibilidade WCAG AA
- [ ] Testes de penetração executados (ex: Aikido Security)
- [ ] LGPD checklist concluído (nível apropriado)
- [ ] Badge do Lovable removido (se acordado)
- [ ] Google Search Console configurado
- [ ] Checklist SEO/GEO do Lovable passando em todos os itens
- [ ] Rate limiting nas Edge Functions críticas

---

*Histórico:*
- *v1.0 — Princípios e estrutura de prompt*
- *v2.0 (2026-05-15) — 4 fases, branding, GEO, LGPD, feedback loop, checklist SEO/GEO do Lovable*

