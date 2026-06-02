# Lovable Prompt Builder

> Skill para guiar o desenvolvimento de produtos no Lovable.dev do zero ao deploy — prompt por prompt, com feedback em tempo real.

*Autor: André Almeida — [Comunidade AI Brasil](https://linkedin.com/in/andrealmeidadc)*

---

## O Problema que Esta Skill Resolve

O Lovable.dev é uma plataforma poderosa de desenvolvimento full-stack com IA. Mas ele sofre de um problema clássico: **garbage in, garbage out**.

Peça para ele "criar um app de gestão de estoque" e ele vai:
- Fazer suposições erradas sobre a arquitetura de dados
- Criar tabelas sem Row Level Security (RLS) — uma vulnerabilidade crítica
- Ignorar onboarding, estados vazios e tratamento de erro
- Esquecer SEO, analytics e compliance desde o início
- Construir tudo de uma vez e quebrar no meio do caminho

Esta skill resolve isso atuando como um **Arquiteto de Software Sênior** que guia o usuário em todo o processo.

---

## Como Funciona

```
Ideia do usuário
      |
      v
Fase 1: Perguntas de escopo + pesquisa de concorrentes
      |
      v
Fase 2: Validação do entendimento (aguarda confirmação)
      |
      v
Fase 3: Prompt 1 entregue ao usuário
      |
      v
Usuário cola no Lovable e retorna o resultado
      |
   Sucesso ──────> Próximo prompt
      |
   Erro ─────────> Prompt de correção ──> Retoma fila
      |
   Parcial ──────> Anota ou corrige agora
      |
      v
Repete até produto completo
```

---

## O que a Skill Cobre

### Processo
- Coleta de requisitos com perguntas de escopo antes de gerar qualquer coisa
- Pesquisa de concorrentes e análise de diferenciação
- Validação do entendimento antes de gerar o kickoff
- Entrega atômica: um prompt por vez, nunca dois ao mesmo tempo
- Loop de feedback: sucesso, erro técnico ou sucesso parcial — cada um tratado diferente

### Produto Gerado
- Stack definida: React + TypeScript + Tailwind + shadcn/ui + Supabase
- Segurança by design: RLS em todas as tabelas, proteção OWASP BOLA, Edge Functions para secrets
- SEO clássico: metadata dinâmica, Open Graph, JSON-LD/Schema.org, sitemap.xml, robots.txt
- GEO (Generative Engine Optimization): HTML semântico, llms.txt, Core Web Vitals < threshold
- Analytics desde o dia 1: PostHog para product intelligence, Sentry para erros
- LGPD: cookie consent, exportação de dados, exclusão de conta, audit log
- Onboarding e empty states explícitos — o Lovable nunca gera isso sozinho
- Admin panel com roles separados desde o schema
- Monetização via Stripe com webhooks em Edge Functions
- Email transacional via Resend
- Dynamic OG images por rota
- Content architecture: /blog, /changelog, /docs para SEO e GEO de longo prazo

---

## Conteúdo do Repositório

```
lovable-prompt-builder/
├── SKILL.md                    # Arquivo principal — lido pelo agente de IA
├── README.md                   # Este arquivo
├── framework_prompting.md      # Princípios e workflow Lovable → GitHub → Cursor
├── security-checklist.md       # Checklist de segurança para revisão pós-build
└── examples/
    └── exemplo_prompt_lovable.md  # Exemplo de output gerado pela skill
```

---

## Como Usar

### Com qualquer agente de IA (Manus, Claude, GPT, Gemini)

1. Forneça o conteúdo do `SKILL.md` ao agente no início da conversa
2. Diga: *"Quero criar um aplicativo de [sua ideia]. Siga a skill."*
3. O agente vai fazer perguntas de escopo, pesquisar concorrentes e validar o entendimento antes de gerar qualquer coisa
4. Após a validação, ele entrega os prompts um por um
5. Você cola cada prompt no Lovable e retorna o resultado para o agente
6. O agente processa o feedback e avança ou corrige

### Com Claude (recomendado)

Adicione o `SKILL.md` como contexto num Project do Claude para que ele esteja sempre disponível sem precisar reenviar.

---

## Princípios Fundamentais

**Atomicidade** — Um prompt, uma responsabilidade. O Lovable constrói melhor peça por peça.

**Dados antes de UI** — O schema do banco e as regras de RLS são definidos no kickoff e não mudam sem revisão explícita.

**Security by Design** — Segurança não é um passo final. É requisito de cada componente.

**Feedback Loop** — Nenhum prompt novo sem confirmação do anterior. Sem exceção.

**Discoverabilidade** — Todo produto gerado deve ser encontrável por humanos (SEO) e por AI crawlers (GEO) desde o primeiro deploy.

---

## Verificação de versão com consentimento

Esta skill foi padronizada para operar como uma skill atualizável com consentimento humano. No início de um uso relevante, quando houver internet e ferramentas Git ou HTTP disponíveis, o agente deve consultar o repositório de origem, ler o `README.md` e o `CHANGELOG.md` quando existirem, comparar a cópia local com a versão upstream e resumir as novidades encontradas.

Essa checagem não autoriza autoatualização silenciosa. A regra é: **verificar, explicar e perguntar**. O agente deve informar o que mudou, dizer se a mudança impacta a tarefa atual e pedir autorização explícita antes de atualizar qualquer arquivo local da skill. O protocolo completo está em [`references/version-check.md`](references/version-check.md).

## Histórico de Alterações

- **2026-04-30** — Criação do repositório inicial com README, framework de prompting e exemplo de output
- **2026-05-04** — Segurança OWASP BOLA, RLS obrigatório, proteção de segredos, failover de LLMs e acessibilidade
- **2026-05-15** — Refatoração completa: fluxo interativo guiado, loop de feedback do Lovable, GEO/SEO, llms.txt, Core Web Vitals, PostHog, Sentry, LGPD, onboarding, monetização Stripe, admin panel, notificações, content architecture, competitive research, audit log, export de dados, dynamic OG images, rate limiting e Resend

---

## Licença

MIT — use, modifique e distribua livremente com atribuição.
