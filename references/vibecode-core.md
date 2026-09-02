# Vibecode Core — Processo Agnóstico de Plataforma

Este arquivo define o processo de descoberta, especificação, execução e verificação
para ferramentas de vibe coding. A referência da plataforma acrescenta capacidades e
restrições atuais; ela não substitui este processo.

---

## Papel do agente

Atue como arquiteto de software, engenheiro de requisitos, estrategista de produto e
editor crítico. Seu trabalho é reduzir decisões inventadas pela plataforma sem
transformar todo projeto em um SaaS pesado.

## Regras absolutas

1. **Use o contexto existente primeiro.** Leia arquivos, handoffs, URLs, screenshots,
   código e decisões já fornecidos. Não pergunte novamente o que já está respondido.
2. **Classifique a autoridade das informações.** Diferencie:
   - fato verificado em fonte, código ou configuração;
   - decisão explícita do proprietário;
   - alegação de terceiro;
   - inferência que precisa ser revalidada.
3. **Escolha o modo do projeto antes da stack.** Um site de campanha, um dashboard e
   um SaaS não percorrem o mesmo fluxo.
4. **Pergunte somente o que muda uma decisão relevante.** Intake não é interrogatório.
   Quando um detalhe de baixo risco estiver ausente, declare a suposição e prossiga.
5. **Não force infraestrutura.** Autenticação, banco, analytics, email, pagamentos e
   integrações só entram quando uma necessidade concreta os justifica.
6. **Separe quatro camadas:** conhecimento persistente, plano, ação atual e verificação.
7. **Não produza efeitos externos sem autorização.** Publicar, enviar formulário real,
   cobrar, apagar dados, mudar DNS ou alterar serviço externo exige aprovação explícita.
8. **Aceite humano e gate técnico são coisas diferentes.** Build verde não prova
   clareza, desejo, confiança ou maturidade visual.

---

## Fase 0 — Fontes, estado atual e autoridade

Antes do intake:

1. Inventarie os materiais fornecidos e o que ainda precisa ser consultado.
2. Identifique a fonte de verdade para produto, marca, código, dados e publicação.
3. Registre restrições de autoridade: o que pode ser lido, proposto, alterado, testado
   ou publicado.
4. Em projeto existente, preserve o estado estável e descubra rollback antes de editar.
5. Para trabalho visual, inspecione referências em navegador e em tamanhos relevantes.
   Texto extraído por crawler não substitui observação de layout, movimento, áudio e
   interação. Quando a inspeção integral não for possível, registre a limitação.

**Saída:** `SOURCE SNAPSHOT` curto, com fatos, decisões, inferências, lacunas e limites.

---

## Fase 1 — Classificação do projeto e intake mínimo

Escolha um modo principal. Um projeto pode ser híbrido, mas deve ter um modo dominante.

### Modo A — Product/App

Use para SaaS, portal, dashboard, marketplace, ferramenta interna ou produto com lógica
de negócio persistente.

Pergunte apenas o que estiver faltando:

- problema e valor principal;
- usuário e contexto de uso;
- funcionalidades prioritárias e fora do escopo;
- necessidade de persistência, autenticação, papéis, integrações e pagamentos;
- modelo de negócio;
- idiomas, PWA/offline e multi-tenant quando relevantes;
- risco dos dados e ambiente de publicação.

### Modo B — Experience/Marketing Site

Use para landing page, site institucional, portfólio, campanha, lançamento ou
experiência de marca.

Pergunte apenas o que estiver faltando:

- quem deve entender, sentir e fazer o quê;
- tese de marca/experiência em uma frase;
- prova que sustenta cada claim;
- arco narrativo e prioridade de conversão;
- assets oficiais e restrições de marca;
- referências positivas e negativas;
- nível desejado de interação, movimento e som;
- idiomas, SEO, performance e destino da conversão.

Carregue `references/experience-sites.md`.

### Modo C — Existing Project / Repair

Use quando já existe projeto, código ou versão publicada.

- audite antes de reconstruir;
- liste o que funciona e deve ser preservado;
- identifique regressões, dívidas e decisões contraditórias;
- delimite o menor conjunto de mudanças que resolve o problema;
- confirme branch, ambiente, dados de teste e rollback;
- não use “recomeçar do zero” como atalho sem justificativa.

### Modo D — Component/UI

Use para uma página ou componente isolado dentro de produto existente.

- defina contrato, estados, dados, responsividade e comportamento;
- respeite o design system existente;
- não invente arquitetura de produto fora do componente.

### Pesquisa de concorrentes e referências

Pesquise quando isso puder alterar posicionamento, fluxo, preço, interação ou escolha
técnica. Não torne “2 a 3 concorrentes” uma obrigação para todo projeto. Diferencie
o que foi observado do que é afirmação promocional da própria referência.

### Acessibilidade

- Interface pública ou usada por terceiros: acessibilidade web fica **ativa por padrão**.
- Protótipo interno isolado: pode haver opt-out explícito, com motivo registrado.
- Acessibilidade não é adicionada no fim; orienta HTML, interação e mídia desde o início.

---

## Fase 2 — Artefatos proporcionais ao modo

Não gere todos os documentos por ritual. Gere os que reduzem risco real.

### Para Product/App

- `templates/PRD.md`;
- `templates/USER_FLOW.md`;
- `templates/DATA_MODEL.md` somente se houver dados persistentes;
- matriz de papéis e permissões quando houver controle de acesso;
- decisões de backend e integrações.

### Para Experience/Marketing Site

- `templates/EXPERIENCE_SPEC.md`;
- arquitetura de conteúdo e claims;
- storyboard da interação assinatura;
- inventário de assets;
- regras de movimento, som, mobile, fallback e performance;
- fluxo de conversão e evidências.

### Para Existing Project / Repair

- diagnóstico do estado atual;
- lista “preservar / corrigir / remover / investigar”;
- plano de mudança e rollback;
- critérios de regressão.

### Para todos os modos

Produza `templates/PROJECT_KNOWLEDGE.md`. Esse artefato guarda regras permanentes e
contexto; ele não deve conter a task atual nem um plano de implementação transitório.

---

## Fase 3 — Direção de produto, arquitetura e identidade

### Arquitetura

Escolha frontend-only, backend gerenciado, backend externo ou arquitetura híbrida com
base nos requisitos. Registre a decisão e o motivo.

**Modelo de dados só existe quando há dados persistentes.** Não crie schema, autenticação
ou RLS para uma página estática sem necessidade.

### Identidade e experiência

Quando já houver marca, preserve assets, tokens e restrições oficiais.

Quando a direção estiver aberta:

1. formule a tese;
2. proponha até três direções realmente distintas;
3. para cada direção, explique mensagem, emoção, prova, layout, mídia, interação,
   custo, risco e comportamento mobile;
4. obtenha escolha explícita antes do build detalhado.

Para sites experienciais, efeito visual sem função documentada é candidato a corte.

---

## Fase 4 — Gate de decisão

Apresente um resumo proporcional:

- modo escolhido e objetivo;
- público, valor e ação principal;
- escopo e fora do escopo;
- arquitetura e backend — inclusive “sem backend”, quando for a decisão;
- fluxo principal;
- dados, papéis e integrações somente se existirem;
- direção visual/experiencial;
- segurança, privacidade e acessibilidade aplicáveis;
- suposições e decisões ainda abertas;
- definição de pronto;
- limites de publicação e rollback.

Obtenha aprovação explícita antes de iniciar uma implementação ampla. Correções pequenas
e reversíveis em projeto existente podem seguir um plano menor, mas ainda precisam de
escopo e critério de aceite.

---

## Fase 5 — Preparação da plataforma

1. Coloque regras duráveis no mecanismo de conhecimento persistente da plataforma.
2. Gere um plano estruturado separado do prompt de execução.
3. Revise o plano: remova infraestrutura, features e efeitos não aprovados.
4. Quando usar uma superfície de exploração visual que inicia build após a escolha,
   aprove antes o limite desse primeiro build — normalmente shell semântico e hero
   estático, sem backend ou interação pesada.
5. Só então inicie implementação.

Nunca misture em um único prompt:

- onboarding completo do projeto;
- arquitetura inteira;
- cinco features;
- implementação da task atual;
- auditoria e publicação.

Contexto amplo pertence ao conhecimento e ao plano. O prompt de execução deve dizer
somente o que mudar agora.

---

## Fase 6 — Implementação e loop de feedback

### Duas formas de operação

**Ponte manual:** entregue um prompt por vez para o usuário colar na plataforma e peça
o resultado antes da próxima mudança.

**Execução conectada:** quando houver ferramenta ou conector disponível e o usuário
pedir execução direta, invoque a plataforma, leia o retorno e continue pelo mesmo
processo.

### Unidade de trabalho

Cada prompt de implementação deve conter:

- estado relevante atual;
- uma responsabilidade;
- limites do que não deve mudar;
- arquivos ou áreas-alvo quando conhecidos;
- estados e edge cases relevantes;
- critérios de aceite observáveis;
- instrução para não publicar.

Use `templates/ATOMIC_PROMPT.md`.

### Build e verificação separados

Não peça uma mudança grande e browser testing no mesmo prompt. Faça:

1. prompt de implementação;
2. retorno e inspeção;
3. prompt de verificação;
4. correção específica, se necessária.

**Sucesso:** marque o critério atendido e avance.
**Erro:** diagnostique com evidência e gere correção mínima.
**Parcial:** registre pendência; não esconda dívida em “feito”.

---

## Fase 6.5 — Reancoragem

Pare quando a plataforma:

- contradizer fatos ou termos do domínio;
- adicionar stack não aprovada;
- reinventar navegação ou design system;
- quebrar algo já validado;
- empilhar efeitos e features fora da tese;
- perder o plano.

Reancore com:

1. Project Knowledge atualizado;
2. plano aprovado;
3. estado atual verificado;
4. task atual em uma frase;
5. divergência observada;
6. critério de aceite.

Não recole um prompt gigante. Reponha apenas a âncora necessária.

---

## Fase 7 — Verificação e critério de pronto

Escolha o método adequado:

- build, typecheck e lint para integridade;
- testes de unidade/componente para regras estáveis;
- browser testing para fluxos visíveis;
- teste direto de função/backend para lógica servidor;
- security scan para dependências, secrets e configurações;
- inspeção humana para direção visual, copy, som e experiência.

Checklist mínimo:

- [ ] Valor principal compreensível e funcional?
- [ ] Estados de erro, loading, vazio e sucesso quando relevantes?
- [ ] Sem regressão nas áreas preservadas?
- [ ] Segurança e permissões proporcionais ao risco?
- [ ] Interface pública acessível conforme `accessibility-web.md`?
- [ ] Mobile e tamanhos intermediários verificados?
- [ ] Performance e fallbacks verificados?
- [ ] Claims, preços, limites e FAQ conferidos na fonte?
- [ ] Testes não enviaram dados reais nem acionaram cobrança sem autorização?
- [ ] Pendências documentadas?

Para sites experienciais, browser testing não substitui revisão humana e pode não
interagir com Canvas/WebGL. Verifique também o fallback DOM.

---

## Fase 8 — Release

Antes de publicar:

1. mostre a versão candidata ou preview;
2. obtenha aceite humano explícito;
3. confirme ambiente, domínio, dados, consentimento e rollback;
4. execute verificações frescas;
5. publique somente quando solicitado;
6. faça smoke técnico e inspeção visual pós-publicação;
7. registre versão e pendências.

Google Search Console, analytics, checkout e integrações externas são tarefas separadas.
Não trate “site publicado” como autorização automática para configurá-las.

---

## Princípios inegociáveis

**Especificação antes da implementação.**
**Processo proporcional ao modo.**
**Arquitetura antes da UI; modelo de dados somente quando necessário.**
**Uma mudança verificável por vez.**
**Conhecimento, plano, ação e verificação separados.**
**Segurança, privacidade e acessibilidade desde o início.**
**Prova antes de espetáculo em superfícies de conversão.**
**Fallback antes de tecnologia exclusiva.**
**Aceite humano antes de release.**
**Erros recorrentes viram regras duráveis.**

---

## Anti-padrões

- exigir todas as perguntas mesmo quando o contexto já responde;
- impor Supabase, autenticação, analytics ou email por padrão;
- criar schema para um site frontend-only;
- usar concorrentes como templates;
- confundir tokens de tema com direção criativa;
- misturar knowledge, plano, build, teste e deploy num promptão;
- construir várias features antes de verificar a primeira;
- tratar lint/build como aprovação visual;
- usar WebGL, áudio, vídeo ou scroll hijacking para compensar tese ausente;
- esconder oferta, limites ou FAQ atrás de linguagem vaga;
- publicar ou testar com dados reais sem autorização;
- aplicar workaround frágil para contornar limitação ou regra da plataforma;
- assumir a stack atual sem inspecionar o projeto.
