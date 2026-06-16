# Archetypes — Escolhendo a Plataforma Certa

Use este guia quando o usuário não souber qual ferramenta de vibe coding usar,
ou quando houver dúvida sobre qual arquétipo seu produto pertence.

---

## Os 4 Arquétipos

### Arquétipo 1 — Web Full-Stack
**Plataformas:** Lovable, bolt.new

Escolha quando o produto é um **app web completo**: SaaS, ferramenta interna,
dashboard, marketplace, portal de clientes. Precisa de backend, banco de dados,
autenticação e deploy web.

| Critério | Lovable | bolt.new |
|---|---|---|
| Fluxo de geração | 4 fases interativas guiadas | Brief único estruturado |
| Ambiente de execução | Cloud (servidores deles) | WebContainer (no browser) |
| Branding | Sessão de branding embutida | Figma import ou tokens manuais |
| Dependências nativas | Suportadas | Somente pure-JS |
| Melhor para | Usuário quer ser guiado passo a passo | Usuário quer controle do brief |

**Use Lovable se:** é seu primeiro app ou prefere um fluxo mais interativo e guiado.
**Use bolt.new se:** tem clareza do que quer construir e prefere especificar tudo num brief.

---

### Arquétipo 2 — UI-First / Componentes
**Plataforma:** v0 by Vercel

Escolha quando o objetivo é **gerar componentes React ou páginas de UI** de alta
qualidade para integrar num projeto existente — não construir um app do zero.

Sinais de que o v0 é a escolha certa:
- "Preciso de um componente de X para meu projeto Next.js"
- "Quero gerar uma tela/página de Y em React"
- "Tenho um design system e preciso de componentes consistentes"
- "Sou desenvolvedor e quero acelerar a parte de UI"

**Não escolha v0 se:** quer um app completo com backend. O v0 gera UI; você traz o resto.

---

### Arquétipo 3 — Mobile Nativo
**Plataforma:** a0.dev

Escolha quando o produto é um **app para iOS e/ou Android** que será publicado
na App Store e/ou Google Play.

Sinais de que a0.dev é a escolha certa:
- "Quero publicar na App Store"
- "Precisa de notificações push no celular"
- "O usuário vai usar câmera, GPS ou outros recursos do device"
- "Precisa funcionar offline no celular"

**Não escolha a0.dev se:** quer um site ou app web — a0.dev é mobile only.

---

### Arquétipo 4 — App Builder Integrado
**Plataforma:** Base44

Escolha quando quer construir **rápido, sem se preocupar com código** — especialmente
para ferramentas internas, dashboards e protótipos de validação.

Sinais de que Base44 é a escolha certa:
- "Preciso de uma ferramenta interna para minha equipe"
- "Quero validar a ideia antes de contratar um desenvolvedor"
- "Não preciso do código — só que funcione"
- "Quero integrar com Slack, Stripe ou Google Drive sem codar"

**Atenção antes de escolher Base44:** você não terá o código-fonte. Se o produto
precisar escalar ou migrar de plataforma no futuro, terá que reescrever do zero.
Leia o aviso de lock-in em `references/platform-base44.md` antes de começar.

---

## Árvore de Decisão Rápida

```
O que você quer construir?

├── App mobile (iOS/Android, App Store/Play)
│   └── → a0.dev

├── Componente ou página React para projeto existente
│   └── → v0 (Vercel)

├── App web completo (SaaS, dashboard, ferramenta)
│   ├── Prefere fluxo guiado + não precisa de código exportável imediato
│   │   └── → Base44 (se for protótipo/ferramenta interna)
│   │       → Lovable (se quiser ser guiado passo a passo)
│   └── Prefere escrever o brief você mesmo + quer controle total do código
│       └── → bolt.new
```

---

## Combinações Comuns

**SaaS web + landing page:** Lovable ou bolt.new para o app; v0 para componentes
específicos de UI que precisam ser perfeitos.

**Protótipo para validar → produto real:** Base44 para o protótipo rápido;
Lovable ou bolt.new para o produto final (quando a ideia foi validada).

**App mobile + web admin:** a0.dev para o app mobile; Lovable ou bolt.new para
o painel administrativo web.
