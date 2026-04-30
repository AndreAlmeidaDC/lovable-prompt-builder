---
name: lovable-prompt-builder
description: Gera documentos de requisitos completos e prompts otimizados para o Lovable.dev. Use esta skill quando o usuário pedir para criar requisitos, documentação ou prompts iniciais para construir um aplicativo web ou SaaS usando o Lovable.
---

# Lovable Prompt Builder

Esta skill orienta a criação de documentos de requisitos (prompts de kickoff) otimizados para a plataforma Lovable.dev. O Lovable é uma ferramenta de desenvolvimento full-stack baseada em IA que funciona melhor com instruções atômicas, estruturadas e com separação clara entre UI e arquitetura de dados.

## Quando Usar

Sempre que o usuário solicitar a criação de requisitos, documentação inicial, ou um prompt para começar um projeto no Lovable.dev.

## O Papel do Agente

Ao usar esta skill, você atua como um Arquiteto de Software e Engenheiro de Requisitos experiente. Seu trabalho NÃO é apenas formatar a ideia do usuário, mas sim:
1.  **Pensar fora da caixa e fazer conexões:** Analise a ideia inicial do usuário, identifique lacunas e sugira recursos de crescimento (ex: Product-Led Growth, loops de convite) e melhorias de UX que o usuário não pensou. Mostre explicitamente como essas conexões foram feitas.
2.  **Estruturar a Complexidade:** Divida o problema em componentes atômicos. O Lovable constrói melhor peça por peça.
3.  **Proteger o Usuário:** O Lovable pode criar arquiteturas de dados frágeis se não for guiado. Você deve sempre especificar a estrutura de dados e as políticas de segurança (RLS).

## Estrutura Obrigatória do Documento de Saída

Você deve gerar um documento Markdown exaustivo e detalhado, sem resumos, com a autoria de **André Almeida**. O documento deve seguir rigorosamente esta estrutura:

```markdown
# [Nome do Projeto] - Lovable Kickoff Prompt

*Autor: André Almeida*

## 1. Visão Geral e Conexões Estratégicas
[Explique como você analisou a ideia do usuário, quais conexões de negócio/UX você fez e quais recursos adicionais (PLG, retenção, etc.) você incluiu no prompt para tornar o produto melhor.]

---
*(O conteúdo abaixo deve ser copiado e colado no Lovable)*

# Context
[O que é o produto, qual problema resolve, quem é o usuário final. Exemplo: "Um SaaS B2B leve para gerenciamento de inventário de pequenas lojas..."]

## Tech Stack
- React + TypeScript + Tailwind CSS + shadcn/ui
- Supabase (Autenticação, Banco de Dados, Storage)
- [Outras tecnologias específicas necessárias]

## Core Features (Priority Order)
[Lista numerada exaustiva dos recursos essenciais do MVP. A ordem de prioridade é crítica para o Lovable focar no que importa primeiro.]
1. **[Recurso 1]:** [Descrição detalhada do recurso e como deve funcionar].
2. **[Recurso 2]:** [Descrição detalhada do recurso e como deve funcionar].
...

## Visual Style
[Diretrizes de design, paleta de cores (ex: "Dark mode support via Tailwind's dark: prefix"), tipografia, e componentes específicos do Shadcn que devem ser usados (Card, Button, Avatar, etc).]

## Technical Requirements & Database Architecture
[Requisitos de performance, responsividade (mobile-first). **CRÍTICO:** Especifique as tabelas do banco de dados necessárias, campos principais, tipos de dados e a necessidade de Row Level Security (RLS) policies.]

## Implementation Strategy
[O passo a passo que o Lovable deve seguir. Exemplo: "1. Comece com o fluxo de autenticação. 2. Construa a UI estática dos dashboards. 3. Conecte ao Supabase e implemente as regras de RLS."]

## Safe-Guard Instructions
[O que o Lovable NÃO deve fazer. Exemplo: "Não construa o aplicativo inteiro de uma vez. Aja como um desenvolvedor sênior: se uma solução for complexa, explique os trade-offs antes de codar. Não use jargões de marketing no código."]
```

## Princípios de Prompting do Lovable para Lembrar

*   **Atomicidade:** Instrua o Lovable a construir componente por componente, não a página inteira de uma vez.
*   **Dados vs UI:** Peça para o Lovable fazer o mock da UI enquanto projeta a arquitetura de dados (Supabase SQL) corretamente desde o início.
*   **Restrições:** Defina o papel do Lovable (ex: "Aja como um fundador solo com orçamento zero. Não use soluções enterprise complexas").

## Fluxo de Execução

1.  Receba a ideia do usuário.
2.  Expanda a ideia aplicando pensamento lateral.
3.  Gere o documento Markdown seguindo a estrutura exata fornecida acima.
4.  Entregue o documento final ao usuário, garantindo que seja exaustivo e pronto para uso no Lovable.
