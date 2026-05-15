# Checklist de Segurança para Apps Lovable — v2.0

*Autor: André Almeida*

O Lovable é fantástico para prototipagem, mas aplicativos gerados por IA frequentemente apresentam vulnerabilidades críticas em produção. Baseado em análises reais e best practices oficiais, este checklist lista as vulnerabilidades mais comuns e como mitigá-las.

---

## As 5 Vulnerabilidades Mais Comuns em Apps Lovable

### 1. Ausência de Row Level Security (RLS) — 89% dos apps

**O problema:** Tabelas no Supabase sem RLS ativado. Qualquer usuário autenticado pode ler, editar ou deletar dados de todos os outros. Vulnerabilidade clássica de BOLA (Broken Object Level Authorization) — OWASP Top 10.

**Mitigação:** RLS ativado em TODAS as tabelas. Políticas explícitas: `auth.uid() = user_id`.

---

### 2. Uso da Service Role Key no Frontend — 34% dos apps

**O problema:** A `SERVICE_ROLE_KEY` é a "chave mestra" que ignora RLS. Se inicializada no React, fica exposta no DevTools.

**Mitigação:** NUNCA service_role_key no cliente. Use `anon key` apenas. Lógica sensível e secrets em Edge Functions (backend isolado).

---

### 3. Consulta Direta à Tabela `auth.users` — 28% dos apps

**O problema:** IA tenta consultar `auth.users` diretamente, expondo hashes de senha e tokens de confirmação.

**Mitigação:** Crie tabela `profiles` pública sincronizada via triggers. Nunca consulte `auth.users` do frontend.

---

### 4. Segredos em Variáveis `VITE_` ou `NEXT_PUBLIC_` — 22% dos apps

**O problema:** Chaves de API (Stripe, OpenAI) em prefixos públicos. Ficam embutidas no JavaScript enviado ao navegador.

**Mitigação:** NUNCA armazene secrets no frontend. Use Edge Functions para qualquer integração com APIs de terceiros.

---

### 5. Falta de Validação de Input — 18% dos apps

**O problema:** Dados de formulários vão direto para o Supabase sem validação, abrindo margem para injeção.

**Mitigação:** Validação estrita em Edge Functions. Nunca confie apenas em validação do frontend.

---

## Vulnerabilidades Emergentes em Agentic Applications — OWASP 2026

**Agentic BOLA:** Prevenido com RLS obrigatório e arquitetura multi-tenant.

**Prompt Injection / Leakage via Debugging:** Separação clara de responsabilidades reduz necessidade de debugar credenciais.

**Insecure External Tool Usage:** Edge Functions garantem que APIs de terceiros não sejam chamadas diretamente do cliente.

---

## Rate Limiting e Proteção de APIs

**O problema:** Edge Functions sem rate limiting podem ser abusadas. LLM APIs são caras.

**Mitigação:**
- Rate limiting por usuário/IP em Edge Functions críticas
- Cache agressivo para reduzir chamadas a APIs externas
- Gateway de LLM (Portkey, Helicone) com roteamento e failover
- Validação de input antes de qualquer chamada externa

---

## Badge do Lovable e Branding

**O problema:** Badge "Edit with Lovable" pode parecer não-profissional em produção.

**Mitigação:**
- Se em plano pago: remover via Project Settings do Lovable
- Se em plano gratuito: CSS workaround — adicione ao `src/index.css`:
  ```css
  @layer base {
    #lovable-badge { display: none !important; }
  }
  ```

---

## Compliance e Discoverabilidade

### Google Search Console (GSC)

**O problema:** Sem GSC configurado, Google não consegue indexar corretamente.

**Mitigação:**
1. Acesse search.google.com/search-console
2. Adicione domínio e verifique via meta tag no `<head>`
3. Submeta sitemap: Settings > Sitemaps > `[domínio]/sitemap.xml`
4. Confirme indexabilidade via URL Inspection

---

### LGPD — Checklist por Nível

**Nível Básico** (todos os projetos):
- [ ] Cookie consent na primeira visita
- [ ] Política de privacidade acessível
- [ ] Termos de uso acessíveis
- [ ] Exportação de dados do usuário (JSON/CSV)
- [ ] Exclusão de conta com deleção de dados
- [ ] Audit log de ações críticas

**Nível Intermediário** (dados financeiros ou menores):
- [ ] Tudo do básico
- [ ] Cookie consent granular: necessários / analytics / marketing
- [ ] Página `/minha-conta/privacidade` com direitos do titular
- [ ] Canal de contato para solicitações de dados (email/formulário)
- [ ] Prazo de resposta: 15 dias (exigência ANPD)
- [ ] Base legal explícita por tipo de dado na política
- [ ] Transferência internacional declarada (Supabase, Stripe, PostHog)
- [ ] Política de retenção de dados
- [ ] Gate de verificação de idade

**Nível Avançado** (dados sensíveis: saúde, biometria):
- [ ] Tudo do intermediário
- [ ] Consentimento explícito por tipo de dado sensível
- [ ] RIPD documentado
- [ ] DPO formalmente designado
- [ ] Notificação de incidentes em 72h à ANPD

---

## Checklist Completo de Go-Live para Produção

**Segurança:**
- [ ] RLS ativado em TODAS as tabelas sensíveis?
- [ ] Código frontend inspecionado: sem `SERVICE_ROLE`, sem secrets `VITE_`?
- [ ] APIs de terceiros (Stripe, LLM) restritas a Edge Functions?
- [ ] Tabela `auth.users` não exposta ou consultada do frontend?
- [ ] Rate limiting ativado nas Edge Functions críticas?
- [ ] Validação de input em Edge Functions?

**Branding & Produto:**
- [ ] Badge do Lovable removido (se acordado)?
- [ ] Tema de branding aplicado globalmente (sem cores hardcoded)?
- [ ] Onboarding e empty states implementados?
- [ ] Tratamento de erro com mensagens úteis?

**Acessibilidade:**
- [ ] Contraste mínimo WCAG AA?
- [ ] Todos os elementos interativos com aria-label?
- [ ] Navegação por teclado funcional?

**SEO/GEO:**
- [ ] Google Search Console configurado?
- [ ] Sitemap submetido ao GSC?
- [ ] Metadata dinâmica por rota?
- [ ] JSON-LD configurado?
- [ ] /llms.txt e /ai-summary.md presentes?
- [ ] Checklist SEO/GEO do Lovable passando em todos os itens?
- [ ] Core Web Vitals dentro dos thresholds?

**Compliance:**
- [ ] LGPD checklist concluído (nível apropriado)?
- [ ] Cookie consent granular (se nível intermediário+)?
- [ ] Política de privacidade e termos acessíveis?
- [ ] Canal DPO para solicitações de dados?
- [ ] Exportação de dados funcional?
- [ ] Exclusão de conta funcional?
- [ ] Audit log registrando ações críticas?

**Testes & Monitoramento:**
- [ ] Testes de penetração executados (ex: Aikido Security)?
- [ ] Falhas críticas resolvidas?
- [ ] PostHog (analytics) configurado?
- [ ] Sentry (error monitoring) configurado?
- [ ] Notificações de erro habilitadas?

---

## Alinhamento com Frameworks de Segurança

**OWASP Top 10:**
- A01 - Broken Access Control: Mitigado com RLS + BOLA protection
- A02 - Cryptographic Failures: Secrets em Edge Functions, não frontend
- A03 - Injection: Validação estrita em Edge Functions
- A04 - Insecure Design: Security by design no kickoff
- A07 - Identification & Authentication: Supabase Auth + session management
- A08 - Data Integrity: RLS policies + audit log

**LGPD (Lei Geral de Proteção de Dados):**
- Art. 5 — Princípios: Transparência via políticas
- Art. 6 — Bases Legais: Explícitas no kickoff
- Art. 9 — Direitos do Titular: Página dedicada
- Art. 18 — Notificação: 72 horas à ANPD

---

*Histórico:*
- *v1.0 — 5 vulnerabilidades + OWASP + failover*
- *v2.0 (2026-05-15) — Adiciona LGPD 3 níveis, GSC, rate limiting, badge do Lovable, checklist completo de go-live*

