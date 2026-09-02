# Acessibilidade Web

> Estrutura inspirada no A11Y.md de Felipe A. Carriço
> (github.com/fecarrico/A11Y.md), licença MIT, reescrita para esta família de skills.

Alvo padrão: WCAG 2.2 nível AA.

Esta referência se aplica por padrão a sites e aplicações web públicas ou usadas por
terceiros. Protótipos internos isolados podem optar por não ativá-la, desde que o motivo
seja explícito e não exista público externo.

Acessibilidade não é acabamento. Ela define HTML, foco, teclado, mídia, movimento e
fallback desde o primeiro componente.

---

## 1. HTML semântico

- `button` para ação e `a` para navegação.
- Um `h1` principal por página; headings em hierarquia lógica.
- `header`, `nav`, `main`, `footer` e outros landmarks adequados.
- Listas e tabelas usam elementos nativos.
- Não transforme `div` ou `span` em controle clicável.
- ARIA só entra quando HTML nativo não resolve.

---

## 2. Nomes, estados e feedback

- Controles precisam de nome acessível coerente com o texto visível.
- Ícone isolado precisa de `aria-label` ou texto oculto adequado.
- Estados dinâmicos refletem o real: `aria-expanded`, `aria-selected`,
  `aria-checked`, `aria-current`.
- Mensagens de validação e resultados assíncronos usam região viva adequada.
- Não duplique texto visível com `aria-label` divergente.

---

## 3. Foco e teclado

- Foco sempre visível e com contraste suficiente.
- Nada de `outline: none` sem substituto.
- Ordem de foco segue a ordem lógica.
- Tudo que funciona com ponteiro funciona com teclado.
- Modal: foco entra, fica contido, ESC fecha e o foco volta ao gatilho.
- Mudança de rota SPA reposiciona o foco de forma previsível.
- Skip link em páginas com navegação repetida.
- Conteúdo sticky, banners e modais não podem ocultar o elemento focado.

---

## 4. Formulários

- Todo campo tem `label` associado; placeholder não é label.
- Obrigatoriedade e formato são programáticos e visuais.
- Erro é claro, ligado ao campo e informa como corrigir.
- Validação no cliente melhora UX; validação servidor/banco continua obrigatória para
  segurança.
- Campos relacionados usam `fieldset` e `legend`.
- Não apague dados já digitados após erro recuperável.

---

## 5. Imagens, vídeo e áudio

- Imagem informativa tem `alt` que descreve conteúdo/função.
- Imagem decorativa usa `alt=""`.
- Vídeo informativo tem legenda; áudio informativo tem transcrição.
- Som começa desligado e possui controle visível.
- Nada de autoplay com áudio.
- Feedback sonoro sempre tem equivalente visual/textual.
- Controles de mídia são operáveis por teclado.

---

## 6. Movimento, scroll e experiência imersiva

- Respeite `prefers-reduced-motion`.
- A versão reduced-motion não pode perder conteúdo ou ação.
- Não dependa de parallax, gesto, hover ou animação para transmitir informação.
- Evite scroll hijacking; preserve rolagem, histórico e controle do usuário.
- Animações disparadas por interação devem poder ser pausadas, puladas ou reiniciadas
  quando duradouras.
- Conteúdo piscando deve respeitar limites de segurança e ser evitado.

### Canvas, WebGL e 3D

- Canvas/WebGL nunca é a única forma de acessar conteúdo ou CTA.
- Forneça alternativa DOM/estática equivalente.
- Controles da experiência precisam de operação por teclado fora da superfície gráfica
  quando necessário.
- Estado e resultado importantes devem ser anunciados em texto.
- Falha de GPU, WebGL ou carregamento ativa fallback automaticamente.
- Browser testing pode não operar Canvas; faça teste manual e do fallback.

---

## 7. Contraste, tamanho e reflow

- Texto normal: contraste mínimo 4,5:1.
- Texto grande e componentes gráficos essenciais: 3:1 quando a WCAG permitir.
- Foco e estados interativos também precisam de contraste.
- Informação nunca depende só de cor.
- Alvos de ponteiro seguem WCAG 2.2: pelo menos 24 × 24 CSS px, salvo exceções.
- Layout deve refluír em largura equivalente a 320 CSS px e suportar zoom de 400% sem
  perda de conteúdo ou operação, salvo exceções legítimas.
- Texto deve permitir espaçamento ampliado sem quebra funcional.

---

## 8. Componentes complexos

Antes de criar dropdown, tabs, accordion, combobox, date picker, tooltip ou menu:

1. use primitiva nativa ou biblioteca acessível quando possível;
2. consulte o padrão do WAI-ARIA Authoring Practices Guide;
3. implemente teclado, roles, estados e foco completos;
4. não entregue componente custom incompleto por parecer visualmente correto.

---

## 9. Teste

Automação ajuda, mas não certifica conformidade.

- [ ] navegação completa por teclado;
- [ ] foco visível e não oculto;
- [ ] headings e landmarks;
- [ ] imagens e mídia com alternativas;
- [ ] formulários e erros acessíveis;
- [ ] contraste e informação não dependente de cor;
- [ ] reflow/zoom;
- [ ] reduced motion;
- [ ] fallback de Canvas/WebGL;
- [ ] teste automatizado com axe ou equivalente;
- [ ] amostra manual com leitor de tela;
- [ ] mobile e orientação/tamanhos relevantes;
- [ ] conteúdo dinâmico anunciado.

Não declare “WCAG compliant” apenas porque Lighthouse ou axe não encontrou erro.

---

## Fora de escopo

Aplicativos mobile nativos têm modelo próprio de acessibilidade, incluindo leitores de
tela nativos, gestos, touch targets e APIs da plataforma. Esta referência cobre web.
