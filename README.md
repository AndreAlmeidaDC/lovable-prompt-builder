# Lovable Prompt Builder Skill

*Autor: André Almeida*

Um repositório contendo a skill **Lovable Prompt Builder**, projetada para ser utilizada por agentes de IA (como o Manus) para gerar documentos de requisitos e prompts otimizados para a plataforma [Lovable.dev](https://lovable.dev/).

## O Problema

O Lovable é uma ferramenta incrível para desenvolvimento full-stack assistido por IA, mas ele sofre do problema clássico de "garbage in, garbage out". Se você pedir para ele "criar um app de gestão de estoque", ele fará suposições sobre a arquitetura de dados, muitas vezes resultando em bancos de dados frágeis (sem Row Level Security - RLS) e interfaces confusas.

O Lovable funciona melhor quando:
1. Recebe instruções atômicas (construir componente por componente).
2. Tem uma separação clara entre a complexidade da UI e a arquitetura de dados (exigindo schemas Supabase explícitos).
3. Recebe contexto de negócio e restrições claras (ex: "não use soluções enterprise caras").

## A Solução (Esta Skill)

A skill `lovable-prompt-builder` atua como um Arquiteto de Software e Engenheiro de Requisitos. Quando ativada, ela pega uma ideia simples do usuário e:

1. **Aplica Pensamento Lateral:** Adiciona conexões de negócio, como loops de Product-Led Growth (PLG) e melhorias de UX.
2. **Estrutura a Complexidade:** Divide a ideia em *Core Features* priorizadas e *Technical Requirements*.
3. **Protege a Arquitetura:** Define o schema de banco de dados mockado e regras de segurança (RLS) que o Lovable deve seguir rigorosamente.
4. **Gera o Prompt de Kickoff:** Entrega um documento Markdown padronizado, pronto para ser copiado e colado no Lovable.

## Conteúdo do Repositório

Este repositório é focado na aplicação prática e contém:

- `SKILL.md`: O arquivo principal da skill que deve ser lido pelo agente de IA. Contém as instruções de como o agente deve se comportar e a estrutura obrigatória do documento de saída.
- `framework_prompting.md`: Um documento consolidado com os princípios fundamentais, estrutura ideal de prompts e o workflow de produção (Lovable → GitHub → Cursor) descobertos na documentação oficial e na comunidade.
- `examples/exemplo_prompt_lovable.md`: Um exemplo prático e genérico (Sistema de Gestão de Inventário B2B) de como o output gerado pela skill se parece.

## Como Usar

Se você estiver usando o Manus ou outro agente compatível com skills:

1. Forneça o arquivo `SKILL.md` ao agente.
2. Dê o comando: *"Gere os requisitos para o Lovable de um aplicativo de [sua ideia]"*.
3. O agente analisará a ideia, expandirá com pensamento lateral e gerará o documento de kickoff estruturado.
4. Copie a seção indicada no documento gerado e cole no chat inicial do Lovable.dev.

## O Padrão Ouro de Prompts para Lovable

A skill força a geração de prompts na seguinte estrutura:

1. **Context:** O que é o produto e quem é o usuário final.
2. **Tech Stack:** Definição clara das tecnologias (React, Tailwind, Supabase, etc).
3. **Core Features (Priority Order):** Lista numerada dos recursos essenciais do MVP.
4. **Visual Style:** Diretrizes de design e componentes de UI preferidos.
5. **Technical Requirements & Database Architecture:** Especificação de tabelas, tipos e RLS policies.
6. **Implementation Strategy:** O passo a passo que a IA deve seguir.
7. **Safe-Guard Instructions:** O que a IA *não* deve fazer.

---
*Histórico de Alterações:*
- *[2026-04-30 14:40] - Criação do repositório inicial com README, framework de prompting e exemplo de output.*
- *[2026-05-04 15:20] - Atualização da skill e exemplos para incluir diretrizes estritas de segurança (OWASP BOLA, RLS, proteção de segredos), failover de LLMs e acessibilidade.*
