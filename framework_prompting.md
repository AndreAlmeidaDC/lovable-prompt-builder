# Framework Operacional de Prompting para Lovable — v3.0

Este é um guia rápido. O comportamento canônico está em:

- `references/vibecode-core.md`
- `references/platform-lovable.md`
- `references/experience-sites.md`
- `security-checklist.md`

Não duplique decisões permanentes em todos os prompts.

---

## 1. Os quatro artefatos

### Project Knowledge

Guarda propósito, termos, stack, regras de marca, segurança, acessibilidade e release.
É persistente.

### Plano

Produzido em Plan mode. Investiga e organiza a sequência sem alterar código.

### Prompt atômico

Executado em Agent mode. Muda uma responsabilidade e declara o que preservar.

### Verificação

Mensagem posterior que escolhe build/test/browser/backend conforme o comportamento.

Misturar os quatro em um “kickoff prompt” gigante aumenta drift e mudanças parciais.

---

## 2. Ordem

```text
fontes → modo → especificação → Project Knowledge → Plan mode
→ revisão do plano → Design Guidance quando aplicável → Agent mode atômico
→ verificação → próximo passo → release
```

Para site experiencial:

```text
tese → Experience Spec → limite do primeiro build → três direções
→ escolha humana → protótipo estático → interação assinatura isolada
→ integração → conteúdo de decisão → QA → release
```


### Atenção ao Design Guidance

Os três previews aparecem antes do build, mas submeter uma direção inicia a construção.
Defina antes o limite do primeiro build. Para experiência ambiciosa, comece pelo shell e
hero estáticos; não autorize Canvas/WebGL, som, backend e tracking nessa mesma rodada.

---

## 3. Anatomia do prompt atômico

Use `templates/ATOMIC_PROMPT.md`.

Um bom prompt responde:

- qual é o último estado verificado;
- qual única mudança deve acontecer;
- o que deve permanecer igual;
- quais estados/edge cases importam;
- como saber que terminou;
- o que não pode ser publicado ou acionado.

Evite adjetivos vagos como “bonito”, “premium” ou “moderno” sem composição, referência
e critérios observáveis.

---

## 4. Stack proporcional

Nunca inclua automaticamente:

- Supabase;
- auth;
- PostHog;
- Sentry;
- Resend;
- Stripe;
- gateway de LLM;
- painel admin;
- `llms.txt`;
- `ai-summary.md`.

Cada item precisa de necessidade, ambiente, responsável, custo e critério de sucesso.

Frontend-first com mock é um caminho válido. Banco entra quando persistência real for
necessária.

---

## 5. Prompt de Plan mode

```text
MODO: Plan. Não altere código.

Analise [objetivo] usando o Project Knowledge e o estado atual.
Preserve [áreas].
Não adicione [stack/features/efeitos proibidos].

Entregue:
1. diagnóstico;
2. decisões e trade-offs;
3. arquivos afetados;
4. sequência atômica;
5. testes;
6. rollback;
7. perguntas somente se forem bloqueantes.

Não implemente nem publique.
```

---

## 6. Prompt de Agent mode

```text
MODO: Agent. Não publique.

ESTADO
[último estado verificado]

TASK ÚNICA
[uma mudança]

PRESERVE
[lista]

CRITÉRIOS
- [resultado observável]
- [estado/edge case]
- [mobile/a11y/performance quando aplicável]

Ao terminar, liste arquivos alterados e como verificar.
```

---

## 7. Prompt de verificação

```text
Verifique apenas a task recém-concluída.

Escolha o teste adequado e informe evidências:
- build/typecheck/lint;
- frontend test;
- browser testing;
- backend/edge test;
- security scan.

Cheque console/rede quando aplicável.
Não publique, não envie dados reais e não corrija silenciosamente outro escopo.
```

---

## 8. Tratamento de retorno

### Sucesso

Registre critério atendido e prossiga para a próxima unidade.

### Erro

```text
EVIDÊNCIA
[o que falhou]

CAUSA PROVÁVEL
[hipótese sustentada]

CORREÇÃO MÍNIMA
[prompt atômico]

REGRESSÃO A EVITAR
[o que preservar]
```

### Parcial

Não chame de pronto. Liste pendência, impacto e decisão: corrigir agora ou backlog
explícito.

---

## 9. Reancoragem

Quando houver drift:

- atualize Project Knowledge;
- confira o plano aprovado;
- referencie os arquivos relevantes;
- diga a divergência observada;
- peça correção mínima.

Não use reancoragem para reenviar o projeto inteiro em todo prompt.

---

## 10. Release

Preview e publish são etapas distintas. Antes do publish:

- versão candidata vista por humano;
- testes frescos;
- segurança/privacidade proporcionais;
- conteúdo factual revisado;
- rollback;
- autorização explícita.

Configurar Search Console, analytics, domínio, checkout ou email é trabalho separado do
deploy.
