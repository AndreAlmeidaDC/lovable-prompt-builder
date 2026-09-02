# Arquétipos de Projeto — Classifique Antes de Escolher a Arquitetura

Este guia classifica o trabalho antes da plataforma e da stack. Capacidades comerciais
de builders mudam rápido; verifique documentação oficial atual antes de recomendar uma
ferramenta com base em preço, exportação, backend ou recursos específicos.

---

## 1. Experience / Marketing Site

Landing page, site institucional, portfólio, campanha, lançamento ou experiência de
marca.

Sinais:

- conversão e compreensão são o valor principal;
- narrativa, direção de arte ou interação importam;
- pode ser frontend-only;
- conteúdo, prova, performance e acessibilidade têm mais peso que schema de banco.

No Lovable, use Design Guidance quando a direção estiver aberta, depois
`references/experience-sites.md`.

---

## 2. Product / App Web

SaaS, portal, dashboard, marketplace ou produto com lógica persistente.

Sinais:

- usuário retorna e mantém estado;
- há dados, autenticação, papéis ou integrações;
- regras de negócio precisam de teste;
- segurança e operação continuam após o lançamento.

No Lovable, escolha backend somente após definir necessidade e governança.

---

## 3. Ferramenta Interna / Protótipo

Fluxo para equipe restrita ou validação rápida.

Sinais:

- público controlado;
- menor necessidade de SEO;
- velocidade importa, mas dados reais ainda exigem segurança;
- pode começar com mock e frontend-only.

Acessibilidade pode ter opt-out explícito apenas se for realmente interno e isolado.

---

## 4. Component / UI

Componente, seção ou página para integrar em projeto existente.

Sinais:

- escopo local;
- design system e stack já existem;
- contrato de props/dados importa;
- não deve reinventar produto ou backend.

---

## 5. Existing Project / Repair

Projeto já iniciado, publicado ou com dívida.

Sinais:

- há comportamento a preservar;
- o problema pode ser drift de contexto, regressão ou arquitetura;
- recomeçar é mais arriscado que auditar;
- branch, backup e rollback são parte do escopo.

---

## 6. Mobile Nativo

Aplicativo iOS/Android com APIs e distribuição nativas.

Lovable é orientado a web responsiva/PWA. Quando o requisito for binário nativo, App
Store/Play, APIs nativas profundas ou experiência offline nativa, verifique e escolha
uma ferramenta mobile apropriada. Não descreva responsive web como app nativo.

---

## Perguntas de seleção

1. O resultado roda em navegador ou precisa ser binário nativo?
2. O valor é conteúdo/conversão, operação persistente ou componente isolado?
3. Precisa de backend, auth, storage, realtime ou pagamentos agora?
4. Quem precisa possuir e revisar o código?
5. Há restrição de framework, hospedagem, dados ou compliance?
6. Qual nível de direção visual e interação é necessário?
7. A ferramenta possui preview, versionamento, testes e rollback adequados?
8. O custo/lock-in foi verificado na documentação atual?

---

## Árvore rápida

```text
Qual é o resultado principal?

├── Landing, portfólio, campanha, site de marca
│   └── Experience / Marketing Site
├── SaaS, dashboard, portal, marketplace
│   └── Product / App Web
├── Ferramenta restrita ou validação
│   └── Ferramenta Interna / Protótipo
├── Componente ou página em projeto existente
│   └── Component / UI
├── Projeto já construído com problema
│   └── Existing Project / Repair
└── Binário iOS/Android e APIs nativas
    └── Mobile Nativo
```

A escolha de arquétipo determina os artefatos e gates. Ela não obriga uma plataforma.
