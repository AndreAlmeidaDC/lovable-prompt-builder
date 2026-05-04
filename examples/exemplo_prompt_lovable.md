# Sistema de Gestão de Inventário B2B - Lovable Kickoff Prompt

*Autor: André Almeida*

## 1. Visão Geral e Conexões Estratégicas
Para o projeto "Sistema de Gestão de Inventário B2B", a ideia inicial é um SaaS para pequenas lojas controlarem estoque. Pensando fora da caixa, adicionei um "Alerta de Ruptura Inteligente" e um "Loop de Fornecedores" (Product-Led Growth). Se a loja atingir estoque mínimo, o sistema não apenas avisa, mas já sugere o e-mail pré-formatado para o fornecedor. A arquitetura foi desenhada para focar na interface de gestão (CRUD rápido) e relatórios visuais, deixando o Lovable focar na experiência do usuário sem se perder em lógicas de ERP complexas.

---
*(O conteúdo abaixo deve ser copiado e colado no Lovable)*

# Context
Um SaaS B2B leve para pequenas lojas físicas e e-commerces gerenciarem seu inventário de forma simples. O usuário cadastra produtos, registra entradas/saídas e o sistema fornece alertas de estoque baixo e um dashboard de movimentação.

## Tech Stack
- React + TypeScript + Tailwind CSS + shadcn/ui
- Supabase (Autenticação, Banco de Dados, Storage para fotos de produtos)

## Core Features (Priority Order)
1. **Autenticação e Multi-tenant:** Login via email/senha. O usuário pertence a uma "Loja" (Workspace), permitindo que funcionários da mesma loja acessem os mesmos dados.
2. **Dashboard de Visão Geral:** Exibição do total de itens em estoque, produtos com estoque crítico (abaixo do mínimo) e gráfico de movimentação (entradas vs saídas nos últimos 7 dias).
3. **Gestão de Produtos (CRUD):** Tela para adicionar produtos (Nome, SKU, Categoria, Preço de Custo, Preço de Venda, Estoque Atual, Estoque Mínimo, Foto).
4. **Registro de Movimentação:** Modal rápido para registrar entrada (compra) ou saída (venda/perda) de um produto específico.
5. **Alertas Inteligentes:** Notificação na UI e listagem de produtos que atingiram o "Estoque Mínimo", com botão para "Gerar Pedido de Reposição".

## Visual Style
- Estilo: Limpo, utilitário, focado em dados (semelhante ao Shopify admin ou Stripe).
- Cores: Fundo cinza claro (`bg-slate-50`), azul primário para ações, vermelho para alertas de estoque crítico, verde para entradas.
- Dark mode support via Tailwind's dark: prefix.
- Componentes Shadcn obrigatórios: Table (para listagem), Dialog (para modais de movimentação), Card (para dashboard), Badge (para status).

## Technical Requirements & Database Architecture
A aplicação deve ser responsiva, mas focada na experiência desktop/tablet para uso no balcão da loja.

**Supabase Schema Necessário (Mock):**
- `stores`: `id` (uuid), `name` (text).
- `users`: (gerenciado pelo Supabase Auth) + tabela auxiliar vinculando `user_id` a `store_id`.
- `products`: `id` (uuid), `store_id` (uuid, FK), `name` (text), `sku` (text), `current_stock` (integer), `min_stock` (integer), `price` (numeric).
- `movements`: `id` (uuid), `product_id` (uuid, FK), `type` (text: 'in', 'out'), `quantity` (integer), `date` (timestamp).

**Segurança:** Implementar Row Level Security (RLS) estrito para garantir que um usuário só possa ler/editar dados onde `store_id` corresponda à sua loja.

## Implementation Strategy
1. Comece construindo o fluxo de autenticação e a criação da Loja (Workspace).
2. Construa a UI estática do Dashboard e a Tabela de Produtos.
3. Implemente os modais de Registro de Movimentação.
4. Conecte ao Supabase e implemente as regras de RLS (crucial para o multi-tenant).
5. Adicione a lógica de cálculo do Dashboard baseada na tabela de `movements`.

## Safe-Guard Instructions & Security
- Aja como um desenvolvedor sênior pragmático e focado em segurança (Security by Design). Não construa o aplicativo inteiro de uma vez. Comece APENAS pelo layout base e a Tabela de Produtos.
- Não tente implementar integrações complexas de ERP ou emissão de nota fiscal. O foco é apenas controle de quantidade.
- **Segurança de Dados:** O RLS (Row Level Security) DEVE estar ativado em todas as tabelas para evitar ataques de BOLA (Broken Object Level Authorization). NUNCA consulte a tabela `auth.users` diretamente no frontend.
- **Segredos e APIs:** NUNCA armazene chaves de API (como chaves de LLM ou Stripe) no frontend (ex: `VITE_API_KEY`). Use EXCLUSIVAMENTE Edge Functions para lidar com credenciais. NUNCA inicialize o cliente Supabase no React usando a `service_role_key`.
- **Acessibilidade:** A UI deve seguir práticas de acessibilidade (WCAG), incluindo contraste adequado e suporte a leitores de tela para deficiência visual.
- **Resiliência (Failover):** Se houver qualquer integração com LLMs, a Edge Function DEVE utilizar um gateway de LLM (como Portkey ou Helicone) para garantir failover e roteamento dinâmico.

---
*Histórico de Alterações:*
- *[2026-04-30 14:35] - Substituição do exemplo específico do RevisaConta por um exemplo genérico de Sistema de Gestão de Inventário, garantindo neutralidade e aplicabilidade geral da skill.*
