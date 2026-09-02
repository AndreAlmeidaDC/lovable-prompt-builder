# Data Model

> Use somente quando o projeto realmente tiver dados persistentes.

**Projeto:**
**Backend:** Lovable Cloud | Supabase | External
**Tenant boundary:** none | user | workspace | organization

## Classificação dos dados

| Dado | Pessoal? | Sensível? | Fonte | Base/propósito | Retenção |
|---|---|---|---|---|---|
| | | | | | |

## Entidades / tabelas

### [Entidade]

| Campo | Tipo | Nulo? | Regra/constraint | Índice | Descrição |
|---|---|---|---|---|---|
| id | uuid | não | primary key | sim | |
| created_at | timestamptz | não | default now() | | |

## Relações

-

## Regras de integridade

- constraints:
- unicidade:
- cascatas:
- idempotência:
- concorrência:

## Papéis e permissões

| Role | Recurso | SELECT | INSERT | UPDATE | DELETE |
|---|---|---|---|---|---|
| | | | | | |

## RLS / autorização

- Schemas expostos:
- Estratégia deny-by-default:
- Policies:
- Testes negativos entre usuários/tenants:
- Operações exclusivamente server-side:

## Retenção e exclusão

-
