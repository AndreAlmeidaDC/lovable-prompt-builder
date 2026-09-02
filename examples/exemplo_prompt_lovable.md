# Exemplo — Aplicação de Inventário no fluxo atual

Este exemplo mostra a separação entre conhecimento, plano, implementação e verificação.
Não cole tudo como um único prompt.

---

## 1. Project Knowledge

```text
Projeto
Aplicação B2B leve para pequenas lojas controlarem produtos e movimentações.

Modo
Product/App.

Público
Dono da loja e funcionários autorizados.

Valor principal
Ver estoque atual, registrar entradas/saídas e identificar ruptura.

Escopo inicial
- dashboard resumido;
- produtos;
- movimentações;
- alerta de estoque mínimo.

Fora do escopo
ERP, nota fiscal, compras automáticas e integração contábil.

Arquitetura
Começar frontend-first com dados mockados.
Backend só entra após validação do fluxo.
Quando entrar: isolamento por store/workspace, autenticação e RLS testada.

Design
Utilitário, alta legibilidade, desktop/tablet prioritários e mobile funcional.
Usar tokens semânticos do projeto; não hardcode de cores em componentes.

Acessibilidade
Interface usada por terceiros: WCAG 2.2 AA ativa.

Release
Não publicar nem conectar dados reais sem aprovação.
```

---

## 2. Prompt de Plan mode

```text
MODO: Plan. Não altere código.

Crie um plano para o primeiro protótipo frontend-only da aplicação de inventário
descrita no Project Knowledge.

Inclua:
- rotas e componentes;
- modelo de dados mockado em TypeScript;
- estados loading/empty/error;
- fluxo produto → movimentação → atualização de estoque;
- responsividade e acessibilidade;
- sequência atômica;
- testes de componente e browser;
- ponto futuro de conexão com backend, sem implementar agora.

Não adicione autenticação, Supabase, analytics, email, Stripe ou painel admin.
Não implemente e não publique.
```

---

## 3. Primeiro prompt de Agent mode

```text
MODO: Agent. Não publique.

ESTADO
Projeto novo, sem backend. Use a stack atual criada pelo Lovable.

TASK ÚNICA
Construa o shell responsivo da aplicação e a página de produtos com dados mockados
tipados.

PRESERVE
- frontend-only;
- nenhuma autenticação ou integração;
- tokens semânticos;
- navegação futura prevista pelo plano, sem construir outras features.

ESTADOS
- lista com produtos;
- vazio com CTA “Adicionar produto”;
- loading com skeleton;
- erro simulado com retry.

ACESSIBILIDADE
- tabela ou lista semântica;
- foco visível;
- ações operáveis por teclado;
- labels e nomes acessíveis;
- mobile sem scroll horizontal obrigatório.

CRITÉRIOS
- a página carrega sem erro;
- trocar o estado mock exibe cada variação;
- TypeScript sem `any`;
- nenhum request externo;
- nenhuma publicação.

Ao concluir, liste arquivos alterados e como verificar.
```

---

## 4. Prompt de verificação

```text
Verifique somente o shell e a página de produtos.

1. Rode build/typecheck/lint disponíveis.
2. Adicione ou rode testes de componente para os quatro estados.
3. Use browser testing em desktop e mobile para:
   - abrir a página;
   - navegar por teclado;
   - verificar lista e empty state;
   - observar console e requests.

Não conecte backend e não publique.
Retorne evidências, falhas e screenshots relevantes.
```

---

## 5. Backend posterior

A modelagem e conexão de backend só começam depois que o fluxo visual estiver aprovado.
Nesse momento, produza `DATA_MODEL.md`, threat model, policies RLS e testes negativos
entre dois stores antes de migrar os mocks.
