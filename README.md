# lovable-prompt-builder

Skill de IA que transforma o jeito como você constrói no **Lovable**: em vez de digitar
um pedido solto e torcer, você chega no Lovable com uma especificação de engenharia
completa — e gasta menos crédito, evita retrabalho e termina com um app que aguenta
usuário real.

---

## O problema que esta skill resolve

O Lovable é excelente em transformar instruções claras em apps funcionais. O ponto fraco
não é o Lovable — é o que a maioria das pessoas entrega para ele. Um prompt como
"cria um app de gestão de clientes" deixa o Lovable adivinhar dezenas de decisões:
modelo de dados, permissões, segurança, branding, fluxo. Cada decisão adivinhada errada
vira um prompt corretivo. Cada prompt corretivo queima crédito e tempo.

E há um custo que só aparece depois: apps gerados sem especificação costumam nascer com
tabelas sem RLS (Row Level Security), o que significa que, num app Supabase, os dados de
um usuário podem ficar acessíveis a qualquer outro. Você só descobre quando já está em
produção.

## Como a skill foi pensada

A skill foi desenhada em torno de uma ideia central: **fazer todo o trabalho de
especificação ANTES de tocar no Lovable**, porque é mais barato pensar no chat de IA
(ilimitado) do que pensar dentro do Lovable (limitado por créditos).

### Explorando as forças do Lovable

- **O Lovable é forte em executar planos estruturados.** Por isso a skill produz um
  "kickoff prompt" completo — contexto, stack, features priorizadas, modelo de dados,
  estratégia de implementação — em vez de pedidos fragmentados. Você dá ao Lovable
  exatamente o tipo de entrada em que ele rende melhor.
- **O Lovable aplica temas globalmente bem.** A skill conduz uma sessão de branding que
  termina em tokens Tailwind concretos para o `tailwind.config.ts`, aplicados desde o
  primeiro componente. Nada de cores hardcoded que depois precisam ser caçadas.
- **O Lovable tem ecossistema Supabase nativo.** A skill aproveita isso modelando o banco
  já no vocabulário do Supabase (tabelas, RLS, policies, Edge Functions).

### Mitigando as fraquezas do Lovable

- **Consumo de crédito em idas e vindas.** Mitigado movendo intake, modelagem e branding
  para fora do Lovable. Quando você chega no Lovable, já sabe o que vai ser construído.
- **Segurança negligenciada por padrão.** Mitigado com regras de segurança não-negociáveis
  embutidas no kickoff: RLS em todas as tabelas, policies explícitas, nunca
  service_role_key no cliente, integrações externas só via Edge Functions.
- **Perda de contexto em sessões longas.** Mitigado com o protocolo de reancoragem:
  quando o Lovable começa a divergir do plano, a skill te diz exatamente o que recolar
  para recuperar o rumo sem recomeçar.
- **Conformidade legal ignorada.** Mitigado com LGPD em três níveis proporcionais ao
  risco — um app de notas não carrega o mesmo peso de um app de saúde.

## O que a skill faz, passo a passo

**Fase 1 — Intake.** Escopo, público-alvo, modelo de negócio, pesquisa de 2-3
concorrentes, funcionalidades do MVP priorizadas, e perguntas específicas do Lovable
(badge, nível de LGPD).

**Fase 2 — Modelagem.** Schema de banco (entidades, campos, relações), fluxo de usuário
(telas e rotas) e papéis/permissões.

**Fase 3 — Branding.** Identidade visual existente ou criação do zero, com output em
bloco de tokens Tailwind prontos para colar.

**Fase 4 — Validação.** Um resumo estruturado de tudo, que você confirma antes de
qualquer geração.

**Fase 5 — Geração e loop.** Prompts entregues um de cada vez. A skill trata cada
retorno (funcionou / erro / funcionou mas ficou errado), mantém pendências visíveis e
reancora quando necessário.

**Fase 6 — Critério de pronto.** Checklist de verificação antes de considerar o produto
no ar, incluindo o prompt de configuração do Google Search Console pós-deploy.

## Como usar

1. Carregue esta skill no seu chat de IA (Claude, ChatGPT, etc.)
2. Responda as perguntas das fases de intake, modelagem e branding
3. Confirme o resumo de validação
4. Cole cada prompt gerado no Lovable e devolva o resultado para a skill
5. A skill trata erros e avança até o produto estar pronto

A skill gera os prompts; você faz a ponte de copiar e colar para o Lovable. Ela não se
conecta ao Lovable nem executa nada por você — é uma ferramenta de raciocínio e
especificação, não de automação.

## FAQ

**Preciso saber programar para usar?**
Não. A skill foi feita para guiar tanto quem nunca programou quanto quem é desenvolvedor.
Ela faz as perguntas certas e traduz suas respostas em especificação técnica.

**Funciona com o plano gratuito do Lovable?**
Sim. Aliás, é onde ela mais ajuda: como o plano gratuito tem créditos limitados, evitar
prompts corretivos faz diferença direta no quanto você consegue construir.

**A skill se conecta ao Lovable automaticamente?**
Não. Ela gera os prompts e você cola no Lovable. Isso é proposital: mantém a skill
funcionando em qualquer chat de IA, sem depender de integração.

**Por que tanta insistência em segurança e RLS?**
Porque é o erro mais comum e mais grave em apps gerados por IA. Um app que vaza dados de
usuários é pior do que um app que não existe. A skill trata segurança como requisito de
cada feature, não como passo final.

**O Lovable mudou e a skill ficou desatualizada. E agora?**
A skill verifica a versão do repositório no início de cada uso e te avisa se há
atualização disponível, explicando o que mudou antes de aplicar. Veja
`references/version-check.md`.

**Posso usar para um app que já comecei no Lovable?**
Pode, mas ela rende mais começando do zero. Para um app em andamento, use as fases de
modelagem e o protocolo de reancoragem para colocar o projeto de volta nos trilhos.

**Preciso ativar acessibilidade?**
Não. Acessibilidade é opcional e fica desligada por padrão. Logo no início do fluxo a
skill pergunta se o app terá interface web usada por terceiros ou se precisa atender a
requisito de acessibilidade. Se for uso interno, protótipo ou app da própria equipe,
responda que não e siga sem nenhum peso extra. Se responder que sim, a skill passa a
tratar acessibilidade como requisito de toda a UI, com base em
`references/accessibility-web.md`.

## Estrutura do repositório

```
SKILL.md                          # Ponto de entrada: papel e como usar
references/
  vibecode-core.md                # Processo de engenharia (compartilhado na família)
  platform-lovable.md             # Tudo específico do Lovable
  archetypes.md                   # Guia de escolha de plataforma
  version-check.md                # Protocolo de auto-atualização
  accessibility-web.md            # Acessibilidade web (opcional, ver gate na Fase 1)
templates/
  PRD.md                          # Template de requisitos de produto
  DATA_MODEL.md                   # Template de modelo de dados
  USER_FLOW.md                    # Template de fluxo de usuário
scripts/
  validate_skill.py               # Validação local da skill
```

## Por que existem 6 skills e não uma só

Essa pergunta é legítima — o processo de fundo (especificar antes de gerar, modelar
dados, iterar de forma atômica, reancorar quando a IA perde o contexto) é o mesmo em
todas as plataformas. Seria tentador fazer uma skill única que cobre tudo.

Não fizemos, por três razões:

**1. Contexto desperdiçado.** Uma skill única carregaria as particularidades de seis
plataformas em toda sessão, sendo que você só usa uma. A maior parte do que entrasse no
contexto seria ruído para a sua tarefa. Skills separadas carregam só o que importa para
a plataforma que você escolheu.

**2. As plataformas divergem mais do que parecem.** O v0 gera componentes, não apps.
O a0.dev fala de telas e navegação, não de páginas e rotas. O Base44 não te dá o código.
O emergent usa MongoDB e um time de agentes; os outros não. Espremer tudo num fluxo único
exigiria tantos "se for plataforma X, faça Y" que o resultado seria confuso e frágil.

**3. Evolução independente.** Cada plataforma muda no seu ritmo. Quando uma lança um
recurso novo, a skill dela é atualizada sem tocar nas outras cinco.

O que é genuinamente compartilhado (o processo de engenharia) vive em um único arquivo,
`references/vibecode-core.md`, idêntico em todas as skills. Assim evitamos duplicação no
que importa e mantemos independência onde importa.

## Família vibecode

| Skill | Plataforma | Melhor para |
|---|---|---|
| **lovable-prompt-builder** (esta skill) | Lovable | App web full-stack com fluxo guiado passo a passo |
| [bolt-prompt-builder](https://github.com/AndreAlmeidaDC/bolt-prompt-builder) | bolt.new | App web full-stack com brief único e controle total |
| [v0-prompt-builder](https://github.com/AndreAlmeidaDC/v0-prompt-builder) | v0 (Vercel) | Componentes React/shadcn de alta qualidade |
| [a0-prompt-builder](https://github.com/AndreAlmeidaDC/a0-prompt-builder) | a0.dev | App mobile nativo iOS/Android |
| [base44-prompt-builder](https://github.com/AndreAlmeidaDC/base44-prompt-builder) | Base44 | Ferramenta interna / protótipo com backend incluído |
| [emergent-prompt-builder](https://github.com/AndreAlmeidaDC/emergent-prompt-builder) | emergent.sh | Full-stack multi-agente (web + mobile), código seu |

## Licença

MIT — André Almeida
