# Checklist de Segurança para Apps Lovable

*Autor: André Almeida*

O Lovable é uma ferramenta fantástica para prototipagem rápida, mas aplicativos gerados por IA (Vibe Coding) frequentemente apresentam vulnerabilidades críticas quando vão para produção. Baseado em análises de segurança reais e nas melhores práticas oficiais do Lovable, este documento lista as vulnerabilidades mais comuns e como a skill `lovable-prompt-builder` as mitiga.

Este documento foi desenhado para ser útil tanto para fundadores quanto para Analistas de Segurança da Informação (Júnior a Sênior).

## As 5 Vulnerabilidades Mais Comuns em Apps Lovable

Segundo análises independentes de dezenas de apps em produção, estas são as falhas mais frequentes:

### 1. Ausência de Row Level Security (RLS) - 89% dos apps
O Lovable cria tabelas no Supabase, mas frequentemente **não ativa o RLS**. Isso significa que a API do banco de dados fica essencialmente pública. Qualquer usuário autenticado pode ler, editar ou deletar os dados de **todos os outros usuários** simplesmente contornando o frontend e chamando a API do Supabase diretamente. Esta é uma vulnerabilidade clássica de **BOLA (Broken Object Level Authorization)**, presente no OWASP Top 10.

*   **Mitigação:** A skill `lovable-prompt-builder` **exige** que a cláusula `Technical Requirements` do prompt inclua instruções explícitas para ativar o RLS em todas as tabelas e criar políticas restritas (`auth.uid() = user_id`).

### 2. Uso da Service Role Key no Frontend - 34% dos apps
A `SERVICE_ROLE_KEY` do Supabase é a "chave mestra" que ignora todas as políticas de segurança (RLS). O Lovable às vezes inicializa o cliente Supabase no React usando essa chave. Como o código React roda no navegador, a chave mestra fica exposta para qualquer um que abrir o DevTools.

*   **Mitigação:** O prompt gerado pela skill instrui o Lovable a usar apenas a `anon key` no frontend e a manter a lógica sensível e chaves mestras em **Edge Functions** (backend isolado).

### 3. Consulta Direta à Tabela `auth.users` - 28% dos apps
Em vez de criar uma tabela pública `profiles` sincronizada via triggers, a IA tenta consultar diretamente a tabela interna `auth.users` do Supabase, que contém hashes de senha e tokens de confirmação.

*   **Mitigação:** A skill força a definição de uma arquitetura de banco de dados explícita no prompt, incluindo tabelas de perfis segregadas da tabela de autenticação interna.

### 4. Segredos em Variáveis `VITE_` ou `NEXT_PUBLIC_` - 22% dos apps
O Lovable coloca credenciais sensíveis (ex: chaves de API da Stripe, OpenAI) em variáveis com prefixos públicos. Isso faz com que essas chaves sejam embutidas no JavaScript enviado ao navegador do usuário.

*   **Mitigação:** A skill adiciona uma instrução de salvaguarda explícita: "Nunca armazene segredos no frontend. Use Edge Functions para qualquer integração com APIs de terceiros".

### 5. Falta de Validação de Input (Zero Input Validation) - 18% dos apps
Os dados dos formulários vão direto para o Supabase sem validação via Zod ou tipagem estrita no backend, abrindo margem para injeção de dados maliciosos.

*   **Mitigação:** A skill instrui o uso de validação estrita em Edge Functions, não confiando apenas na validação do frontend.

---

## Alinhamento com o OWASP Top 10 for Agentic Applications 2026

Ao desenvolver aplicações usando agentes e LLMs, novas categorias de risco emergem. O `lovable-prompt-builder` atua como uma barreira preventiva contra:

*   **Agentic BOLA (Broken Object Level Authorization):** Prevenido através da exigência estrita de RLS e arquitetura multi-tenant no prompt inicial.
*   **Prompt Injection / Leakage via Debugging:** O Lovable pode vazar dados se o desenvolvedor colar logs de erro contendo PII (Personally Identifiable Information) ou chaves de API no chat. A skill orienta a separação clara de responsabilidades, reduzindo a necessidade de debugar credenciais no chat.
*   **Insecure External Tool Usage:** Ao forçar o uso de Edge Functions, garantimos que a aplicação não faça chamadas a APIs de terceiros diretamente do cliente, escondendo a lógica e as credenciais.

## Requisitos Arquiteturais de Resiliência (Failover)

Para aplicações Lovable que integram com LLMs externos (ex: OpenAI, Anthropic):
A skill instrui que integrações com IA **devem** ser implementadas através de Edge Functions e, obrigatoriamente, devem utilizar um **Gateway de LLM** (como Portkey, Helicone ou similar) para gerenciar roteamento, caching e **failover**. A estratégia recomendada é iniciar com um gateway cloud-hosted e planejar a migração para self-hosted conforme a escala.

## Checklist de Liberação para Produção (Go-Live)

Antes de publicar qualquer app Lovable, a equipe de segurança (ou o fundador) deve verificar:

- [ ] O RLS está ativado em **todas** as tabelas sensíveis?
- [ ] O código fonte do frontend foi inspecionado em busca da string `SERVICE_ROLE`?
- [ ] Chaves de API de terceiros (Stripe, LLMs) estão restritas a Edge Functions?
- [ ] A tabela `auth.users` não está sendo exposta ou consultada diretamente pelo frontend?
- [ ] A aplicação atende aos padrões de acessibilidade visual (WCAG)?
- [ ] Os testes de penetração (ex: via Aikido Security, integrado ao Lovable) foram executados e as falhas críticas foram resolvidas?
