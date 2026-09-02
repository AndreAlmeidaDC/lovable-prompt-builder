# Segurança e Privacidade para Projetos Lovable — v3.0

Este checklist é proporcional ao risco. Ele não é parecer jurídico, certificação de
conformidade nem substituto para threat modeling, revisão técnica ou assessoria legal.

Fontes de referência:

- Lovable security best practices:
  https://docs.lovable.dev/tips-tricks/security-best-practices
- Lovable Security view:
  https://docs.lovable.dev/features/security-view
- Supabase Row Level Security:
  https://supabase.com/docs/guides/database/postgres/row-level-security
- OWASP Top 10:2025:
  https://owasp.org/Top10/2025/
- LGPD:
  https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- ANPD Resolução 15/2024 e canal oficial de comunicação:
  https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis
- ANPD Resolução 2/2022:
  https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022

---

## 1. Perfil interno de risco

Use estes perfis apenas para dimensionar engenharia. Eles não são “níveis LGPD”.

### S0 — Frontend sem coleta

Conteúdo público, sem login, banco, formulário ou tracking não essencial.

### S1 — Coleta limitada

Formulário, analytics, preferências ou dados pessoais comuns em baixo volume.

### S2 — Conta, multi-tenant ou transação

Auth, dados persistentes por usuário/organização, integrações, pagamento ou operações
que alteram estado relevante.

### S3 — Alto impacto

Dados sensíveis, crianças/adolescentes, saúde, biometria, finanças detalhadas, larga
escala, decisão automatizada relevante ou operação crítica.

Quanto maior o perfil, mais necessária é revisão especializada, teste negativo,
observabilidade e governança.

---

## 2. Threat model mínimo

Antes do backend:

- ativos e dados que precisam de proteção;
- atores e papéis;
- fronteiras de confiança;
- tenants e isolamento;
- operações destrutivas ou financeiras;
- integrações e secrets;
- abuso previsível, automação e custo;
- logging, retenção e resposta a incidente;
- rollback e recuperação.

---

## 3. Frontend é público

- Todo código e variável entregue ao navegador pode ser inspecionado.
- Frontend nunca decide autorização.
- `VITE_*`, `NEXT_PUBLIC_*` ou equivalentes são públicos por definição.
- Publishable/anon key de backend pode existir no cliente quando o modelo da plataforma
  prevê isso, mas depende de RLS/policies corretas. Não é secret.
- Service role, chaves privadas, webhooks secretos e credenciais de terceiros nunca vão
  para o cliente.
- Não registre token, email, lead ID, conteúdo sensível ou secret em console/analytics.

---

## 4. Fronteira server-side

Use server function, Edge Function ou backend equivalente para:

- secrets;
- integrações externas autenticadas;
- pagamentos e webhooks;
- operações administrativas;
- autorização e regras sensíveis;
- rate limiting e cost controls;
- validação confiável;
- chamadas de IA com credenciais.

“Edge Function para tudo” não é requisito. O requisito é uma fronteira server-side
adequada à stack atual.

---

## 5. Banco e RLS

Quando usar Supabase/Postgres exposto por API:

- [ ] RLS ativo em toda tabela de schema exposto;
- [ ] deny-by-default;
- [ ] policies explícitas por operação;
- [ ] policies consideram tenant/workspace, não apenas usuário quando necessário;
- [ ] testes negativos entre dois usuários e dois tenants;
- [ ] views/functions revisadas quanto a `security definer`;
- [ ] buckets/storage com policies;
- [ ] operações administrativas ficam server-side;
- [ ] índices suportam colunas usadas nas policies.

Não consulte `auth.users` diretamente do frontend. Use APIs de autenticação apropriadas
e, quando o produto precisar de dados públicos de perfil, uma tabela de domínio própria
com exposição mínima. Não afirme que uma consulta comum ao schema `auth` automaticamente
expõe hashes; o risco real é quebrar a fronteira privilegiada e o modelo de acesso.

---

## 6. Validação e integridade

- Validação no cliente para UX.
- Validação no servidor para confiança.
- Constraints no banco para invariantes.
- Schemas explícitos para requests e responses.
- Limites de tamanho, tipo e frequência.
- Uploads validados por tipo, tamanho, nome e autorização.
- Queries parametrizadas e APIs que não concatenam input em comandos.
- Idempotência em webhooks e operações repetíveis.
- Tratamento seguro de exceções sem vazar stack, secret ou PII.

---

## 7. Auth, sessão e papéis

- [ ] método de login compatível com risco;
- [ ] reset e recuperação seguros;
- [ ] sessão, expiração e logout testados;
- [ ] roles não vêm de campo editável pelo próprio usuário;
- [ ] rota escondida não conta como autorização;
- [ ] admin separado e auditável;
- [ ] ações críticas pedem reautenticação quando necessário;
- [ ] MFA considerado para contas privilegiadas;
- [ ] OAuth redirect URLs restritas aos ambientes corretos.

---

## 8. Integrações, rate limit e supply chain

- menor escopo de permissão possível;
- chaves separadas por ambiente;
- timeout, retry e circuit breaker proporcionais;
- rate limit por usuário/tenant/IP quando útil;
- quotas e alertas para APIs cobradas;
- webhooks autenticados e idempotentes;
- dependências pinadas por lockfile;
- Security view atualizado;
- CVEs críticas resolvidas ou justificadas;
- conectores removidos quando não usados.

---

## 9. Recursos de IA e agentes

Quando houver LLM, tools ou ações:

- trate prompt, página, arquivo e output do modelo como input não confiável;
- limite ferramentas, escopo e autonomia;
- valide output antes de executar ou persistir;
- exija confirmação para ação externa, financeira, destrutiva ou irreversível;
- proteja contra exfiltração de contexto, secrets e dados de outros tenants;
- aplique orçamento, rate limit e tamanho máximo;
- registre decisões sem armazenar conteúdo sensível desnecessário;
- tenha fallback quando provedor/modelo falhar.

Gateway de LLM é opção arquitetural, não obrigação automática.

---

## 10. Privacidade e LGPD

### Inventário

- finalidade e necessidade de cada dado;
- papel de controlador/operador;
- base legal validada;
- retenção e exclusão;
- compartilhamento e transferência internacional;
- canal do titular;
- consentimento separado de termos quando essa for a base;
- cookies/analytics carregados somente conforme a decisão de consentimento aplicável.

### Direitos do titular

O prazo de até 15 dias do art. 19 refere-se à declaração clara e completa de confirmação
de existência/acesso. Não generalize esse prazo para todos os direitos do art. 18.

### Incidentes

Pelo art. 48 da LGPD e pela Resolução CD/ANPD nº 15/2024, o controlador comunica ANPD e
titulares em até **3 dias úteis** quando o incidente confirmado com dados pessoais puder
acarretar risco ou dano relevante. Nem toda vulnerabilidade ou incidente técnico exige
comunicação. O registro de incidentes com dados pessoais deve ser mantido por pelo menos
cinco anos, conforme o regulamento.

### Encarregado

Não presuma “DPO formal obrigatório” para todo projeto. A indicação depende do papel e
do enquadramento do agente. A Resolução CD/ANPD nº 2/2022 dispensa certos agentes de
pequeno porte, mas exige canal de comunicação com titulares e não elimina as demais
obrigações.

Para S3, obtenha revisão jurídica/privacidade especializada e avalie RIPD.

---

## 11. Testes e observabilidade

- [ ] unit/component tests para regras;
- [ ] teste de integração para backend;
- [ ] browser testing para fluxo visível;
- [ ] testes de autorização negativos;
- [ ] teste de webhook/idempotência;
- [ ] scan de dependência e secret;
- [ ] logs sem PII/secrets;
- [ ] alertas para falhas críticas e abuso;
- [ ] backup/restore quando houver dados;
- [ ] plano de incidente e responsável;
- [ ] resultados do Security view estão atuais, não stale.

Ferramenta comercial de pentest é opcional. Para S2/S3 ou exposição relevante, considere
revisão independente proporcional ao risco.

---

## 12. Go-live

### Todos os projetos

- [ ] nenhum secret no cliente/repositório;
- [ ] dependências e build verificados;
- [ ] domínio, ambiente e rollback confirmados;
- [ ] conteúdo jurídico corresponde ao tratamento real;
- [ ] dados de teste removidos ou isolados;
- [ ] publish explicitamente aprovado.

### Com backend/dados

- [ ] RLS/autorização testadas;
- [ ] migrations revisadas;
- [ ] backup/restore;
- [ ] rate limits;
- [ ] retenção/exclusão;
- [ ] canais de suporte e incidente.

### Com pagamento ou ação externa

- [ ] ambiente test/live conferido;
- [ ] webhook e idempotência;
- [ ] nenhum teste aciona cobrança real sem autorização;
- [ ] reconciliação e logs.

### Com IA

- [ ] tools mínimas;
- [ ] output validation;
- [ ] confirmação humana para alto impacto;
- [ ] custo e abuso controlados;
- [ ] fallback.

---

## Mapeamento orientativo

Use OWASP Top 10:2025 como documento de conscientização, não como selo. Os temas mais
relevantes incluem controle de acesso, configuração insegura, supply chain, criptografia,
injeção, design inseguro, autenticação, integridade, logging/alertas e tratamento de
condições excepcionais.
