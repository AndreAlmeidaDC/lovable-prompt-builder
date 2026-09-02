# Exemplo — Site experiencial no Lovable

## Tese

“Transforme um briefing em uma execução verificável.”

A experiência deve fazer o visitante ver o mecanismo, não apenas ler uma promessa.

## Project Knowledge resumido

```text
Modo
Experience/Marketing Site.

Público
Profissionais que já usam ferramentas de IA, mas sofrem para coordenar execução e
qualidade.

Valor
Demonstrar um fluxo: briefing → roteamento → execução → evidência → gate.

Arquitetura
Primeiro protótipo frontend-only e determinístico. Sem auth, banco, analytics ou envio
real de lead.

Interação assinatura
O visitante escolhe um briefing e observa o fluxo mudar de estado. Cada etapa pode ser
explorada. Conteúdo e CTA continuam disponíveis em DOM sem Canvas.

Movimento e som
Movimento comunica estado. Reduced motion mantém a sequência em passos estáticos.
Som começa desligado e só confirma eventos semânticos.

Release
Preview humano obrigatório. Não publicar sem aprovação explícita.
```

## Primeiro prompt de Plan mode

```text
MODO: Plan. Não altere código.

Produza uma Experience Spec e um plano para a landing descrita no Project Knowledge.

Defina:
1. tese, prova e arco narrativo;
2. arquitetura semântica da página;
3. três direções visuais que mudem a lógica da experiência;
4. primeiro build limitado a shell e hero estáticos;
5. interação assinatura como etapa posterior isolada;
6. conteúdo de prova, FAQ e CTA;
7. reduced motion, fallback, mobile e orçamento de performance;
8. sequência de verificação.

Não adicione backend, formulário real ou analytics. Não implemente nem publique.
```

## Prompt que aciona Design Guidance e o primeiro build

```text
MODO: Agent. Não publique.

Use a Experience Spec aprovada. Mostre três direções visuais realmente distintas antes
do build. Para cada uma, diferencie composição, tipografia, hierarquia, linguagem de
movimento e representação do mecanismo; não mude apenas paleta.

Quando eu submeter uma direção, construa SOMENTE:
- o shell semântico da página;
- o hero estático da direção escolhida;
- CTA visível;
- composição própria para desktop e mobile.

Não implemente interação avançada, Canvas, WebGL, som, backend, formulário real,
analytics ou outras seções. Preserve marca oficial, foco visível e reduced motion.
```

> No Lovable, os previews de Design Guidance vêm antes do build, mas submeter a direção
> inicia a construção. Por isso o limite acima faz parte do mesmo pedido.

## Prompt de verificação do primeiro build

```text
Verifique somente o shell e o hero estático.

1. Rode build/typecheck/lint disponíveis.
2. Use browser testing em desktop e mobile para composição, CTA, teclado, console e
   requests.
3. Liste sutilezas visuais que exigem revisão humana.

Não implemente a interação, não corrija outro escopo e não publique.
```

## Próxima unidade

Depois do aceite visual, volte a Plan mode para detalhar estados, tecnologia, fallback e
testes da interação assinatura. Só então gere o próximo prompt atômico de Agent mode.
