# Archetypes — Escolhendo a Plataforma Certa

Use este guia quando o usuário não souber qual ferramenta de vibe coding usar,
ou quando houver dúvida sobre qual arquétipo seu produto pertence.

---

## Os 4 Arquétipos

### Arquétipo 1 — Web Full-Stack
**Plataformas:** Lovable, bolt.new, emergent.sh

Escolha quando o produto é um **app web completo**: SaaS, ferramenta interna,
dashboard, marketplace, portal de clientes. Precisa de backend, banco de dados,
autenticação e deploy. (O emergent.sh também faz mobile no mesmo projeto — ver abaixo.)

| Critério | Lovable | bolt.new | emergent.sh |
|---|---|---|---|
| Fluxo de geração | 4 fases interativas guiadas | Brief único estruturado | Multi-agente autônomo por fases |
| Ambiente | Cloud (servidores deles) | WebContainer (no browser) | Cloud multi-agente |
| Banco padrão | Supabase | Supabase | MongoDB |
| Branding | Sessão de branding embutida | Figma import ou tokens | Especificação explícita (visual é fraco) |
| Código exportável | Sim | Sim | Sim (GitHub, VS Code) |
| Mobile | Não | Não | Sim (Expo/React Native) |
| Melhor para | Ser guiado passo a passo | Controle do brief | Full-stack + mobile, time de agentes |

**Use Lovable se:** é seu primeiro app ou prefere um fluxo mais interativo e guiado.
**Use bolt.new se:** tem clareza do que quer construir e prefere especificar tudo num brief.
**Use emergent.sh se:** quer full-stack com backend robusto, ou web + mobile no mesmo
projeto, e prefere delegar a um time de agentes autônomos. Atenção ao consumo de créditos.

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
**Plataformas:** a0.dev (mobile puro), emergent.sh (mobile + full-stack)

Escolha quando o produto é um **app para iOS e/ou Android** que será publicado
na App Store e/ou Google Play.

Sinais de que a0.dev é a escolha certa:
- "Quero publicar na App Store"
- "Precisa de notificações push no celular"
- "O usuário vai usar câmera, GPS ou outros recursos do device"
- "Precisa funcionar offline no celular"
- "Quero só o app mobile, indie, rápido, sem camada web"

**a0.dev vs emergent.sh para mobile:**
- **a0.dev:** mobile puro, indie, rápido, focado em store. Sem camada full-stack pesada.
- **emergent.sh:** quando o app mobile precisa de backend robusto, ou quando você quer
  web + mobile no mesmo produto. Os dois usam Expo/React Native.

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

**Base44 vs emergent.sh:** os dois constroem apps full-stack rápido. A diferença
decisiva é o código: o Base44 retém o código (lock-in), o emergent dá o código via
GitHub. Se portabilidade importa, emergent; se só quer que funcione rápido e não liga
para o código, Base44.

---

## Árvore de Decisão Rápida

```
O que você quer construir?

├── Componente ou página React para projeto existente
│   └── → v0 (Vercel)

├── App mobile (iOS/Android, App Store/Play)
│   ├── Só mobile, indie, rápido
│   │   └── → a0.dev
│   └── Mobile + backend robusto, ou web + mobile juntos
│       └── → emergent.sh

├── App web completo (SaaS, dashboard, ferramenta)
│   ├── Não preciso do código, só que funcione rápido
│   │   └── → Base44 (protótipo / ferramenta interna)
│   ├── Quero ser guiado passo a passo
│   │   └── → Lovable
│   ├── Quero escrever o brief eu mesmo, controle total
│   │   └── → bolt.new
│   └── Quero backend robusto / time de agentes / web + mobile
│       └── → emergent.sh
```

---

## Combinações Comuns

**SaaS web + landing page:** Lovable ou bolt.new para o app; v0 para componentes
específicos de UI que precisam ser perfeitos.

**Protótipo para validar → produto real:** Base44 para o protótipo rápido;
Lovable, bolt.new ou emergent.sh para o produto final (quando a ideia foi validada).

**App mobile + web admin:** a0.dev para o app mobile + Lovable/bolt.new para o painel;
ou emergent.sh sozinho, cobrindo web + mobile no mesmo projeto.

**Produto full-stack com backend complexo:** emergent.sh, pelo time multi-agente e
backend MongoDB integrado, com código portável via GitHub.
