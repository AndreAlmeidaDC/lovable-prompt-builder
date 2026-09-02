# Experience Sites — Landing Pages e Experiências Interativas

Carregue esta referência para landing pages, sites institucionais, portfólios,
campanhas e experiências de marca em que direção visual, narrativa ou interação sejam
parte relevante do valor.

O objetivo não é “colocar mais animação”. É concentrar complexidade em uma experiência
assinatura que torne a mensagem mais clara, desejável e memorável.

---

## 1. Tese antes da interface

Preencha esta matriz antes do build:

| Elemento | Decisão |
|---|---|
| Mensagem | O que o visitante deve entender em uma frase? |
| Emoção | O que deve sentir? Escolha uma emoção dominante. |
| Prova | O que demonstra que a mensagem é verdadeira? |
| Narrativa | Qual transformação ocorre do primeiro contato ao CTA? |
| Mídia | Qual função exclusiva têm imagem, vídeo, 3D e ilustração? |
| Interação | Que ação revela o mecanismo ou a promessa? |
| Som | Existe função semântica? Se não, não use. |
| CTA | Qual ação é apropriada ao estágio comercial real? |

Se um elemento não provar a tese, ele sai.

---

## 2. Três direções realmente distintas

Quando a direção estiver aberta, apresente no máximo três propostas. Elas devem mudar a
lógica da experiência, não apenas paleta ou fonte.

Para cada uma, documente:

- nome e tese;
- composição do hero;
- arco narrativo;
- interação assinatura;
- linguagem de movimento;
- papel dos assets;
- comportamento mobile;
- fallback;
- custo e risco técnico;
- impacto esperado em compreensão e conversão;
- o que a direção deliberadamente não fará.

Só avance após escolha humana explícita. Se a ferramenta iniciar o build ao submeter
a direção, delimite antecipadamente o primeiro build para não transformar o preview em
autorização para construir a experiência inteira.

---

## 3. Arquitetura narrativa

Uma estrutura comum, adaptável:

1. **Impacto e promessa:** uma ideia, pouca copy, ação clara.
2. **Demonstração:** o visitante vê ou provoca o mecanismo central.
3. **Exploração:** detalhes podem ser abertos sem quebrar a narrativa.
4. **Evidência:** exemplos, fontes, limites, screenshots ou resultados.
5. **Decisão:** oferta, escopo, preço/condições quando autorizados, FAQ e CTA.
6. **Confiança:** privacidade, termos, contato e expectativas pós-CTA.

O site pode ser cinematográfico no início e calmo na decisão. Não mantenha o mesmo
nível de estímulo em todas as seções.

---

## 4. Interação assinatura

Escolha **uma mecânica principal**. Exemplos:

- briefing que se transforma em fluxo visual;
- mapa explorável de capacidades;
- comparação que responde à ação do visitante;
- narrativa espacial guiada;
- demonstração de produto com estados verificáveis.

Defina:

| Campo | Conteúdo |
|---|---|
| Entrada | clique, escolha, texto, scroll, voz ou outro |
| Estados | idle, preparando, executando, sucesso, falha, reset |
| Informação revelada | o que fica mais compreensível em cada estado |
| Controle | pausar, reiniciar, pular, silenciar |
| Teclado | operação equivalente sem ponteiro |
| Reduced motion | versão alternativa |
| Fallback | versão DOM/estática sem Canvas/WebGL |
| Mobile | composição e gestos próprios |
| Métrica | compreensão, conclusão, CTA, tempo ou outra |

Microinterações secundárias devem usar a mesma gramática. Não crie uma mecânica nova em
cada seção.

---

## 5. Inventário de assets

Antes de gerar ou escolher mídia:

| Asset | Origem/licença | Função única | Onde aparece | Mobile | Alt/transcrição | Peso |
|---|---|---|---|---|---|---|

Regras:

- nunca repetir a mesma mídia apenas para preencher espaço;
- não improvisar logo, símbolo ou personagem quando existe marca oficial;
- não usar asset sem origem/licença conhecida;
- imagens decorativas têm `alt=""`; mídia informativa precisa de alternativa;
- vídeo e áudio exigem legenda/transcrição quando carregam informação;
- cada asset deve justificar custo de carregamento.

---

## 6. Movimento e som

### Movimento

Defina uma gramática:

- o que entra, sai, expande, conecta ou muda de estado;
- duração e easing por categoria;
- quais movimentos são feedback e quais são narrativa;
- quais são removidos em `prefers-reduced-motion`;
- nenhuma informação essencial depende exclusivamente de animação.

Evite scroll hijacking. Preserve navegação nativa, histórico, teclado e controle do
visitante.

### Som

Som começa desligado. Só use quando houver função reconhecível, por exemplo mudança de
estado, confirmação, erro ou identidade de uma ação.

- controle visível de ligar/desligar;
- nada de autoplay ou loop ambiente;
- respeitar preferência e volume do usuário;
- não repetir alerta sonoro sem necessidade;
- fornecer alternativa visual/textual;
- nunca bloquear uso quando áudio falhar.

---

## 7. Performance e fallback

Defina orçamento antes de escolher tecnologia:

| Métrica/recurso | Meta do projeto | Candidata medida | Ação se exceder |
|---|---|---|---|
| LCP | até 2,5 s no contexto-alvo | | |
| CLS | abaixo de 0,1 | | |
| INP | até 200 ms | | |
| JS inicial | orçamento definido pelo projeto | | |
| Imagem/vídeo inicial | orçamento definido pelo projeto | | |
| WebGL/Canvas | opcional e progressivo | | |

Regras:

- conteúdo e CTA essenciais existem fora da camada gráfica;
- carregamento pesado é progressivo e não bloqueia leitura;
- detectar falha de WebGL/Canvas e mostrar fallback;
- mobile não recebe uma miniatura engasgada do desktop;
- respeitar `prefers-reduced-motion` e, quando possível, economia de dados;
- testar rede lenta e dispositivo modesto, não só máquina de desenvolvimento.

---

## 8. Conversão e prova

A experiência deve responder, de forma direta:

- o que é;
- como funciona;
- para quem serve;
- o que não faz;
- que evidência existe;
- que custos, dependências e limites permanecem;
- o que acontece depois do CTA.

Não invente urgência, desconto, escassez, depoimento, benchmark ou número. Alegação de
terceiro não vira fato do produto.

---

## 9. Gates

### Antes do código

- [ ] tese e emoção dominante aprovadas;
- [ ] três direções comparadas quando necessário;
- [ ] storyboard e interação assinatura definidos;
- [ ] assets inventariados;
- [ ] copy factual e CTA compatíveis com o estágio comercial;
- [ ] mobile, reduced motion, fallback e orçamento documentados.

### Antes do release

- [ ] revisão humana em desktop e mobile;
- [ ] navegação por teclado;
- [ ] fallback sem WebGL/Canvas;
- [ ] áudio opt-in e controlável;
- [ ] performance medida;
- [ ] claims e FAQ verificados;
- [ ] preview aprovado;
- [ ] rollback confirmado.

Browser testing ajuda em cliques, formulários, console e screenshots, mas não é confiável
para julgar sutilezas visuais e pode não operar Canvas. A aprovação estética permanece
humana.
