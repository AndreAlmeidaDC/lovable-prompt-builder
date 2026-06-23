# Acessibilidade Web (Referência Opcional)

> Estrutura inspirada no A11Y.md de Felipe A. Carriço (github.com/fecarrico/A11Y.md),
> licença MIT. Reescrita para o contexto desta família de skills, não copiada.

Esta referência só se aplica a **UI web (DOM, SPA)** e só quando o gate de
acessibilidade foi ativado na Fase 1 do intake. Se o gate não foi ativado, ignore
este arquivo por completo. Não cobre mobile nativo (ver "Fora de escopo" no fim).

Alvo: WCAG 2.2 nível AA.

---

## Princípio Central

HTML semântico correto entrega a maior parte da acessibilidade de graça. O leitor de
tela (NVDA, JAWS, VoiceOver) já existe no dispositivo do usuário e lê qualquer página
SE a página for construída certo. Acessibilidade não é feature que se liga: é
consequência direta de como o código é escrito. Cravar ARIA por cima de HTML errado
piora, não conserta.

---

## Regras Determinísticas (não-negociáveis quando o gate está ativo)

### 1. HTML semântico primeiro
- `button` real para ação, `a` para navegação. Nunca `div`/`span` clicável com onClick.
- Um `h1` por página. Headings em ordem, sem pular nível (não vá de h2 para h4).
- Landmarks: `header`, `nav`, `main`, `footer`. Conteúdo principal dentro de `main`.
- Lista é `ul`/`ol`/`li`. Tabela de dados é `table` com `th` e escopo.

### 2. Imagem e mídia
- Toda `img` tem `alt`. Decorativa: `alt=""`. Informativa: descreve função ou conteúdo.
- Ícone clicável isolado precisa de nome acessível (`aria-label`).
- Vídeo precisa de legenda. Áudio precisa de transcrição.

### 3. Foco
- Foco sempre visível. Nunca `outline: none` sem um indicador substituto claro.
- Ordem de foco segue a ordem visual e lógica da página.
- Em SPA: ao trocar de rota, mova o foco para o topo ou para o `h1` da nova view.
- Modal: foco entra no modal, fica preso dentro enquanto aberto, ESC fecha, e o foco
  retorna ao elemento que abriu ao fechar.

### 4. Teclado
- Tudo que funciona no mouse funciona no teclado (Tab, Enter, Espaço, Esc, setas).
- Sem armadilha de teclado: o foco que entra em algo sempre consegue sair.
- Skip link para o conteúdo principal em páginas com navegação extensa.

### 5. ARIA (regra de ouro: menos é mais)
- HTML nativo SEMPRE antes de ARIA. ARIA não conserta HTML semântico errado.
- Primeira regra do ARIA: se existe elemento nativo que faz o trabalho, use o nativo.
- `aria-live="polite"` para conteúdo que muda sem reload (toast, resultado de busca,
  mensagem de validação). `assertive` só para o que é urgente de fato.
- Estado dinâmico reflete o real: `aria-expanded`, `aria-selected`, `aria-checked`.
- Não coloque `aria-label` em elemento que já tem texto visível coerente.

### 6. Contraste
- Texto normal: contraste mínimo 4.5:1 contra o fundo.
- Texto grande (cerca de 24px, ou 19px em bold) e componentes de UI: 3:1.
- Informação nunca transmitida só por cor. Erro não é só vermelho: tem ícone ou texto.

### 7. Formulário
- Todo campo tem `label` associado (`for`/`id`). Placeholder não é label.
- Erro vinculado ao campo (`aria-describedby`), com texto claro do que corrigir.
- Campo obrigatório marcado de forma programática, não só visual.
- Campos relacionados agrupados em `fieldset`/`legend`.

---

## Protocolo de Componente Complexo

Antes de construir algo custom (dropdown, tabs, accordion, combobox, date picker,
tooltip, menu):

1. Existe primitiva nativa ou de biblioteca acessível (Radix, shadcn/ui, React Aria,
   Headless UI)? Use ela. Não reinvente acessibilidade do zero.
2. Se for custom mesmo: consulte o padrão do componente no ARIA Authoring Practices
   Guide (APG, w3.org/WAI/ARIA/apg). Implemente os roles, estados e a navegação de
   teclado que o padrão exige.
3. Componente custom sem o padrão APG completo é componente inacessível. Não entregue.

---

## Checklist de Acessibilidade (rodar quando o gate está ativo)

- [ ] Navegação completa só por teclado funciona
- [ ] Foco visível em todo elemento interativo
- [ ] Toda imagem informativa tem `alt`; decorativa tem `alt=""`
- [ ] Headings em ordem, um `h1`, landmarks presentes
- [ ] Contraste 4.5:1 (texto normal) e 3:1 (texto grande e UI)
- [ ] Formulário com label associado e erro acessível
- [ ] Modal prende o foco, ESC fecha, foco retorna ao gatilho
- [ ] Conteúdo dinâmico anunciado (`aria-live` onde muda sem reload)
- [ ] Nenhuma informação transmitida apenas por cor
- [ ] Componente custom segue o padrão ARIA APG ou usa primitiva acessível

---

## Fora de escopo desta referência

Mobile nativo (iOS, Android) tem outro modelo de acessibilidade: touch target,
screen reader nativo (TalkBack, VoiceOver iOS), contraste e gestos próprios. Esta
referência cobre só web com DOM. Para apps mobile (a0.dev, lado mobile do emergent),
acessibilidade nativa é assunto separado e não está coberta aqui.
