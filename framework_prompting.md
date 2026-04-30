# Framework de Prompting para Lovable.dev

Este documento consolida as melhores práticas, estruturas de prompts e padrões descobertos na documentação oficial do Lovable, no Lovable Prompting Bible e em exemplos validados pela comunidade. O objetivo é servir como base para a criação de uma skill reutilizável.

## 1. Princípios Fundamentais do Lovable

O Lovable é uma plataforma de desenvolvimento assistido por IA (AI-assisted development platform) focada em construir aplicações web completas (full-stack). Para extrair o máximo valor da ferramenta, alguns princípios são essenciais:

*   **Atomicidade (Build by component):** Não peça para construir a aplicação inteira de uma vez. Comece pelo layout principal, depois adicione componentes individuais (ex: "Agora construa apenas o modal de upload de imagem").
*   **Separação de Preocupações (UI vs Data):** O Lovable é excelente em UI, mas pode ser ingênuo em arquitetura de dados. Defina explicitamente a estrutura do banco de dados (ex: esquemas Supabase, RLS, foreign keys) antes de pedir para a IA conectar a UI aos dados.
*   **Contexto é Rei:** A IA precisa entender *o que* está construindo, *para quem* e *por quê*. Forneça contexto de negócio, não apenas instruções técnicas.
*   **Uso de Knowledge Files (.lovable):** Para projetos complexos, é fundamental fornecer documentação de design system, esquemas de banco de dados ou regras de negócio através do upload de arquivos `.lovable` ou PDFs/Markdown.
*   **Diretividade (No Autopilot):** Evite jargões corporativos ("robusto", "inovador", "perfeito"). Seja direto sobre o que deseja. Se algo for complexo, peça para a IA explicar as compensações (trade-offs).

## 2. Estrutura Ideal de um Prompt (O Padrão Ouro)

Analisando mais de 100 templates da comunidade e a documentação oficial, o padrão ouro para um prompt inicial (Project Kickoff) no Lovable segue uma estrutura rigorosa baseada em Markdown:

### Seções Recomendadas:

1.  **# Context (Contexto):** O que é o produto, qual o problema que resolve e quem é o usuário final.
2.  **## Tech Stack (Stack Tecnológico):** Definição clara das tecnologias (ex: React, TypeScript, Tailwind CSS, shadcn/ui, Supabase).
3.  **## Core Features (Recursos Principais - Ordem de Prioridade):** Lista numerada dos recursos essenciais (MVP). A priorização é crucial para a IA entender o que focar primeiro.
4.  **## Visual Style (Estilo Visual):** Diretrizes de design, paleta de cores, tipografia, referências visuais e componentes de UI preferidos.
5.  **## Technical Requirements (Requisitos Técnicos):** Regras de arquitetura, responsividade, acessibilidade, tratamento de erros, performance e limites.
6.  **## Implementation Strategy (Estratégia de Implementação):** O passo a passo que a IA deve seguir. (ex: "1. Construa a UI estática primeiro. 2. Adicione os estados locais. 3. Conecte ao banco de dados").
7.  **## Safe-Guard Instructions (Instruções de Segurança/Limites):** O que a IA *não* deve fazer, como tratar falhas, validações de segurança e restrições de escopo.

## 3. Comandos Essenciais (Workflow)

Para interagir com o Lovable de forma iterativa, os seguintes comandos provaram ser altamente eficazes:

*   **O Comando de Clarificação:**
    `"Antes de escrever qualquer código, faça-me 3 perguntas esclarecedoras sobre [feature]. Foque em: estrutura de dados, fluxo do usuário e edge cases."`
    *Por que funciona:* Impede a IA de fazer suposições erradas e forçar retrabalhos massivos.

*   **O Comando de Mock de Banco de Dados:**
    `"Crie a UI para isso usando dados mockados por enquanto. Ao mesmo tempo, escreva o SQL exato do Supabase para a tabela que lidará com isso, incluindo tipos corretos, RLS policies e relacionamentos de foreign keys."`
    *Por que funciona:* Separa a complexidade visual da complexidade de dados.

*   **O Comando de Atuação (Roleplay com Restrições):**
    `"Aja como um fundador solo técnico com orçamento zero para serviços enterprise. Não sugira integrações caras ou arquiteturas excessivamente complexas."`
    *Por que funciona:* Calibra o nível de sofisticação das soluções propostas.

*   **O Teste ELI5 (Explain Like I'm 5):**
    `"Explique esse fluxo de usuário para mim como se eu fosse um adolescente que nunca usou um SaaS antes. Se for difícil de explicar, simplifique o fluxo antes de codar."`
    *Por que funciona:* Valida a UX antes de investir tempo em código.

## 4. O Workflow de Produção (A Realidade)

Segundo a comunidade (ex: Reddit), o Lovable é um "laboratório de UI" incrível, mas não necessariamente a plataforma final para produção em escala sem intervenção. O workflow recomendado para fundadores é:

1.  **Lovable:** Prototipagem rápida de UI, validação da ideia, construção do frontend estático e lógica básica (70% do trabalho em 10% do tempo).
2.  **GitHub:** Exportação do código e controle de versão (proteção da branch principal).
3.  **Cursor + MCP:** Clonar o repositório localmente e usar o Cursor IDE (com Model Context Protocol) para refinar o código, adicionar tratamento de erros robusto, otimizar integrações (Stripe, Supabase) e preparar para produção (os 30% finais).

## 5. Diretrizes para a Skill (lovable-prompt-builder)

A skill a ser criada deve atuar como um engenheiro de requisitos experiente. Quando o usuário pedir "Gere os requisitos para um app de X", a skill deve:

1.  **Pensar fora da caixa:** Não aceitar a ideia básica do usuário passivamente. Fazer conexões, sugerir recursos de crescimento (PLG - Product-Led Growth) e melhorias de UX.
2.  **Gerar o Documento Completo:** Produzir um arquivo Markdown completo seguindo a estrutura de 7 seções (Context, Tech Stack, Core Features, Visual Style, Technical Requirements, Implementation Strategy, Safe-Guard Instructions).
3.  **Injetar as Melhores Práticas:** Garantir que o documento instrua o Lovable a construir componentes de forma atômica e priorize a UI antes do backend.
4.  **Autoria:** O documento gerado deve ter a autoria atribuída a André Almeida.
5.  **Exaustividade:** O documento deve ser exaustivo, detalhado e pronto para ser copiado e colado no Lovable.
