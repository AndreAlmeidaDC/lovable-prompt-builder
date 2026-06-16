# Data Model

**Projeto:** [Nome]
**Plataforma:** [Lovable / bolt.new / Base44 / a0.dev]

## Entidades / Tabelas

### [Entidade 1]
| Campo | Tipo | Descrição |
|---|---|---|
| id | uuid | Identificador único |
| [campo] | [tipo] | [descrição] |
| created_at | timestamp | Data de criação |

### [Entidade 2]
| Campo | Tipo | Descrição |
|---|---|---|
| id | uuid | Identificador único |
| [entidade1]_id | uuid | FK para Entidade 1 |
| [campo] | [tipo] | [descrição] |

## Relações

- [Entidade 1] → [Entidade 2]: [1:N / N:N / 1:1]

## Papéis e Permissões

| Role | Entidade 1 | Entidade 2 |
|---|---|---|
| admin | CRUD | CRUD |
| user | R | CR |
| viewer | R | R |

## Notas de segurança

- [RLS ativado em todas as tabelas — Lovable/Bolt]
- [Permissões configuradas via plataforma — Base44]
- [Convex/Supabase policies — a0.dev]
