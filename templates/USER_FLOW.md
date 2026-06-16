# User Flow

**Projeto:** [Nome]
**Plataforma:** [Lovable / bolt.new / Base44 / a0.dev]

## Fluxo principal (happy path)

```
[Ponto de entrada]
      |
      v
[Passo 1]
      |
      v
[Passo 2]
      |
      v
[Valor entregue ao usuário]
```

## Telas / Páginas principais

| Tela / Página | Propósito | Ações disponíveis |
|---|---|---|
| [Nome] | [O que o usuário faz aqui] | [Ações] |

## Estrutura de navegação (mobile — a0.dev)

```
Bottom Tab Navigator:
  - [Tab 1] (Stack)
    - [Screen 1a]
    - [Screen 1b]
  - [Tab 2] (Stack)
    - [Screen 2a]

Auth Stack (fora do tab):
  - LoginScreen
  - SignupScreen
```

## Estados de exceção

| Situação | O que acontece |
|---|---|
| Usuário não autenticado | Redireciona para Login |
| Dados não encontrados | Empty state com CTA |
| Erro de rede | Mensagem de erro + retry |
| Carregando | Skeleton / spinner |
