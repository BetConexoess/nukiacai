# SKILL.md — QA Visual e Revisão Final

## Objetivo da skill

Esta skill orienta o agente de programação/design a executar uma revisão final completa do projeto antes de publicar.

Use esta skill para garantir que o site, landing page ou cardápio digital:

- não esteja quebrado;
- não tenha desalinhamento visual;
- não tenha overflow horizontal;
- funcione bem no celular;
- tenha consistência de cores, fontes, espaçamentos e componentes;
- carregue rápido;
- tenha CTA de WhatsApp funcionando;
- tenha acessibilidade mínima aceitável;
- tenha SEO local básico correto;
- não perca conversão por erro visual, técnico ou de usabilidade.

O foco principal deste projeto é um cardápio/landing page mobile-first da **Nu Ki Açaí**, acessado por QR code, WhatsApp e celular.

---

## Princípio central

QA visual não é “olhar se está bonito”.

QA visual é verificar se a interface está:

1. correta;
2. consistente;
3. responsiva;
4. acessível;
5. rápida;
6. funcional;
7. legível;
8. clicável;
9. alinhada com a marca;
10. pronta para converter visitantes em pedidos reais.

Um site bonito, mas quebrado no celular, não está pronto.

---

## Quando ativar esta skill

Ative esta skill quando o usuário pedir:

- “revise o projeto”;
- “faça QA visual”;
- “verifique se está tudo certo”;
- “revisão final”;
- “antes de publicar”;
- “teste responsividade”;
- “veja se o design está consistente”;
- “corrija desalinhamentos”;
- “veja se está quebrado no mobile”;
- “faça checklist final”;
- “verifique se o botão de WhatsApp funciona”;
- “garanta que está pronto para lançamento”;
- “audite visualmente o projeto”.

Também ative depois de mudanças importantes em:

- HTML;
- CSS;
- JavaScript;
- imagens;
- assets;
- animações;
- cardápio;
- CTA;
- carrinho;
- checkout via WhatsApp;
- formulário;
- SEO;
- performance.

---

## Regra obrigatória 1 — Mobile-first é prioridade

A maioria dos usuários acessará pelo celular.

Prioridade de teste:

```text
1. Mobile pequeno: 320px
2. Mobile comum: 360px / 375px / 390px
3. Mobile grande: 414px / 430px
4. Tablet: 768px
5. Desktop: 1024px / 1280px / 1440px
```

Nunca aprove o projeto testando apenas em desktop.

---

## Regra obrigatória 2 — QR code e WhatsApp são fluxo crítico

O fluxo principal do projeto é:

```text
QR code / WhatsApp / link direto
→ abrir site no celular
→ entender a marca rapidamente
→ navegar cardápio
→ escolher produto
→ clicar em pedir
→ abrir WhatsApp com mensagem correta
→ gerar pedido real
```

Se esse fluxo falhar, o projeto não está pronto.

---

## Regra obrigatória 3 — Não publicar com bug crítico

Bugs críticos bloqueiam publicação.

Exemplos de bug crítico:

- site não abre no celular;
- CTA WhatsApp não funciona;
- número do WhatsApp está errado;
- mensagem do pedido está errada ou vazia;
- página tem overflow horizontal forte;
- cardápio fica ilegível;
- produtos não aparecem;
- botão principal fica coberto;
- fundo impede leitura;
- layout quebra em 320px;
- carrinho ou pedido não funciona;
- performance extremamente ruim;
- imagens principais não carregam;
- erro JavaScript impede interação.

---

## Regra obrigatória 4 — Nunca revisar só “por aparência”

A revisão deve cobrir:

- layout;
- responsividade;
- alinhamento;
- espaçamento;
- tipografia;
- cores;
- contraste;
- acessibilidade;
- clique/toque;
- teclado;
- foco visível;
- imagens;
- performance;
- CTA;
- formulários;
- animações;
- SEO local básico;
- console do navegador;
- links quebrados;
- estados de erro;
- consistência com a marca.

---

## Regra obrigatória 5 — Toda revisão deve gerar relatório

Ao finalizar QA visual, entregar:

```md
## Relatório de QA Visual

### Status geral
Aprovado / Aprovado com ressalvas / Reprovado

### Bugs críticos
- ...

### Bugs altos
- ...

### Bugs médios
- ...

### Bugs baixos
- ...

### Correções feitas
- ...

### Correções pendentes
- ...

### Testes executados
- ...

### Dispositivos/breakpoints verificados
- ...

### Próximos passos
- ...
```

---

## Definição de pronto

O projeto só está pronto quando:

- [ ] abre corretamente em mobile;
- [ ] não existe overflow horizontal;
- [ ] CTA WhatsApp funciona;
- [ ] mensagem do WhatsApp está correta;
- [ ] produtos aparecem corretamente;
- [ ] textos são legíveis;
- [ ] botões são fáceis de tocar;
- [ ] cores e fontes seguem a identidade;
- [ ] imagens estão otimizadas;
- [ ] performance mobile está aceitável;
- [ ] foco visível existe;
- [ ] navegação por teclado não está quebrada;
- [ ] console não mostra erros críticos;
- [ ] links principais funcionam;
- [ ] SEO local básico está presente;
- [ ] Lighthouse não aponta falhas graves;
- [ ] o visual está consistente em todos os breakpoints principais.

---

## Matriz de severidade

Use esta matriz para classificar bugs.

### Crítico — bloqueia publicação

Critérios:

- impede pedido;
- impede acesso;
- quebra fluxo principal;
- deixa site inutilizável;
- afeta WhatsApp;
- quebra mobile principal.

Exemplos:

```text
CTA WhatsApp não abre.
Número de telefone errado.
Cardápio invisível no celular.
Erro JS trava a página.
Botão de pedido fica fora da tela.
```

### Alto — deve corrigir antes de publicar

Critérios:

- prejudica muito a conversão;
- prejudica usabilidade;
- prejudica acessibilidade essencial;
- causa confusão importante.

Exemplos:

```text
Texto do produto difícil de ler.
Contraste baixo no CTA.
Layout desalinhado em 375px.
Imagem principal pesada demais.
Produto importante cortado.
```

### Médio — corrigir antes ou logo após publicação

Critérios:

- incomoda, mas não impede uso;
- reduz qualidade percebida;
- cria inconsistência visual;
- pode afetar parte dos usuários.

Exemplos:

```text
Espaçamento irregular entre cards.
Ícones em estilos diferentes.
Animação levemente exagerada.
Texto secundário truncado.
```

### Baixo — melhoria visual

Critérios:

- cosmético;
- refinamento;
- melhoria opcional.

Exemplos:

```text
Sombra levemente diferente.
Microespaçamento inconsistente.
Ajuste fino de transição.
```

---

## Prioridade de correção

Use esta ordem:

```text
1. Fluxo de pedido e WhatsApp
2. Quebras mobile
3. Leitura e contraste
4. Performance crítica
5. Acessibilidade essencial
6. Consistência visual
7. SEO local básico
8. Refinamentos estéticos
```

---

## Checklist rápido de bloqueio

Antes de qualquer release, responda:

- [ ] O site abre no celular?
- [ ] Dá para ver o cardápio?
- [ ] Dá para clicar nos produtos?
- [ ] Dá para pedir pelo WhatsApp?
- [ ] O número do WhatsApp está certo?
- [ ] A mensagem do pedido está certa?
- [ ] Não existe rolagem horizontal?
- [ ] O CTA principal está visível?
- [ ] O texto está legível?
- [ ] O site carrega rápido o suficiente?
- [ ] Não há erro crítico no console?
- [ ] A página não está visualmente quebrada?

Se qualquer resposta for “não”, não publicar.

---

## Fase 1 — Inventário visual

Antes de revisar, o agente deve mapear:

- páginas;
- seções;
- componentes;
- botões;
- cards;
- menus;
- modais;
- formulários;
- banners;
- imagens;
- fundos;
- personagens;
- efeitos;
- estados de interação;
- links;
- CTAs.

Modelo:

```md
## Inventário visual

### Páginas
- Home
- Cardápio
- Produto
- Pedido
- Contato
- Localização

### Componentes
- Header
- Hero
- Cards de produto
- Botão WhatsApp
- Barra mobile fixa
- Modal de adicionais
- Footer

### Fluxos críticos
- Abrir site via QR code
- Ver produtos
- Selecionar produto
- Adicionar adicionais
- Enviar pedido ao WhatsApp
```

---

## Fase 2 — Baseline visual

Antes de corrigir, registrar como o projeto está.

O agente deve, quando possível:

- capturar estado atual;
- listar arquivos relacionados;
- identificar CSS principal;
- identificar JS de interação;
- identificar assets usados;
- identificar breakpoints existentes;
- identificar componentes duplicados.

Nunca alterar tudo sem antes entender a estrutura.

---

## Fase 3 — Responsividade

Testar e corrigir nos breakpoints:

```text
320px
360px
375px
390px
414px
430px
768px
1024px
1280px
1440px
```

### Verificar em cada breakpoint

- [ ] nenhum conteúdo corta;
- [ ] nenhum texto sai da tela;
- [ ] imagens se ajustam;
- [ ] cards não ficam espremidos;
- [ ] botões mantêm área confortável;
- [ ] header não cobre conteúdo;
- [ ] footer não quebra;
- [ ] barra fixa não cobre produto;
- [ ] modal cabe na tela;
- [ ] WhatsApp CTA fica acessível;
- [ ] animações não causam overflow;
- [ ] não existe scroll horizontal.

### CSS recomendado para debug

```css
* {
  outline: 1px solid rgba(255, 0, 0, 0.15);
}
```

Use apenas temporariamente.

### Snippet para detectar overflow horizontal

```js
[...document.querySelectorAll("*")].filter((el) => {
  const rect = el.getBoundingClientRect();
  return rect.right > window.innerWidth || rect.left < 0;
});
```

Se retornar elementos, investigar.

---

## Fase 4 — Safe area e altura mobile

Em iPhones e navegadores mobile, testar:

- notch;
- barra inferior;
- Safari iOS;
- Chrome Android;
- navegador dentro do WhatsApp;
- teclado virtual;
- orientação landscape.

### CSS recomendado

```css
:root {
  --safe-top: env(safe-area-inset-top, 0px);
  --safe-right: env(safe-area-inset-right, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left: env(safe-area-inset-left, 0px);
}

.mobile-order-bar {
  padding-bottom: max(12px, var(--safe-bottom));
}

.fullscreen-section {
  min-height: 100dvh;
}
```

Evitar depender apenas de:

```css
height: 100vh;
```

Em mobile moderno, preferir `100dvh` quando a seção precisa considerar barras dinâmicas.

---

## Fase 5 — Layout e alinhamento

Verificar:

- grid;
- largura máxima;
- centralização;
- margem;
- padding;
- gap;
- bordas;
- radius;
- sombras;
- altura dos cards;
- alinhamento de ícones;
- alinhamento de preço;
- alinhamento de CTA;
- proporção das imagens.

### Regras visuais

- títulos alinhados com conteúdo;
- cards com espaçamento consistente;
- botões com altura parecida;
- seções com respiro suficiente;
- imagens não podem distorcer;
- sombras não devem parecer aleatórias;
- elementos premium devem seguir a mesma linguagem visual.

### Padrão de spacing recomendado

Use escala consistente:

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
}
```

Evitar dezenas de valores soltos:

```css
margin: 13px;
padding: 27px;
gap: 19px;
```

A não ser que exista motivo visual claro.

---

## Fase 6 — Tipografia

Verificar:

- fonte correta;
- peso correto;
- tamanho correto;
- line-height;
- letter-spacing;
- hierarquia de título;
- legibilidade mobile;
- truncamento;
- contraste;
- excesso de caixa alta.

### Metas práticas

```text
Texto de leitura: mínimo 16px
Texto secundário: evitar abaixo de 14px
Botões: 15px a 18px
Títulos mobile: responsivos com clamp()
Line-height corpo: 1.4 a 1.7
```

### Exemplo recomendado

```css
.hero-title {
  font-size: clamp(2rem, 8vw, 5rem);
  line-height: 1.05;
}

.product-card__description {
  font-size: clamp(0.9rem, 2.8vw, 1rem);
  line-height: 1.5;
}
```

### Anti-padrões

```css
font-size: 10px;
line-height: 1;
letter-spacing: 5px em texto pequeno;
texto longo todo em uppercase;
muitas fontes diferentes;
muitos pesos diferentes;
```

---

## Fase 7 — Cores e identidade

A interface deve respeitar a identidade Nu Ki Açaí.

Paleta base conhecida:

```css
:root {
  --color-bg-black-purple: #0E0122;
  --color-bg-night-grape: #15032E;
  --color-bg-dark-purple: #1C0833;
  --color-card-premium: #2F154C;
  --color-acai-purple: #371857;
  --color-border-violet: #4E118A;
  --color-primary-violet: #6211AF;
}
```

Verificar:

- fundo escuro premium;
- roxos consistentes;
- CTA com destaque;
- contraste forte;
- bordas coerentes;
- brilho neon sem exagero;
- branco legível;
- elementos importantes não somem no fundo.

### Checklist de cor

- [ ] CTA principal se destaca?
- [ ] texto tem contraste suficiente?
- [ ] preço aparece bem?
- [ ] categorias são fáceis de diferenciar?
- [ ] estados de erro usam cor clara e texto?
- [ ] estados de sucesso não dependem apenas de cor?
- [ ] botão desabilitado parece desabilitado?
- [ ] ícones combinam com a paleta?

---

## Fase 8 — Contraste

Verificar contraste para:

- títulos;
- descrição de produtos;
- preços;
- botões;
- texto dentro de cards;
- links;
- badges;
- avisos;
- formulário;
- footer;
- CTA WhatsApp.

### Regras

- texto normal deve ter contraste forte;
- texto pequeno em roxo sobre roxo costuma falhar;
- não usar cinza fraco em fundo escuro;
- CTA precisa ser legível mesmo em tela com brilho baixo;
- links precisam parecer clicáveis;
- placeholder não substitui label.

### Correção comum

Se o texto estiver fraco:

```css
.product-card__description {
  color: rgba(255, 255, 255, 0.86);
}
```

Se o CTA estiver com contraste ruim:

```css
.whatsapp-button {
  color: #ffffff;
  background: linear-gradient(135deg, #6211AF, #8B2CFF);
}
```

---

## Fase 9 — Componentes e estados

Todo componente interativo deve ter estados:

```text
default
hover
focus
active
disabled
loading
error
success
selected
empty
```

### Botões

Verificar:

- [ ] visual padrão;
- [ ] hover desktop;
- [ ] active no toque;
- [ ] focus visível;
- [ ] disabled claro;
- [ ] loading se houver envio;
- [ ] tamanho confortável;
- [ ] ícone alinhado;
- [ ] texto não quebra errado.

### Cards de produto

Verificar:

- [ ] imagem clara;
- [ ] nome legível;
- [ ] preço visível;
- [ ] descrição sem corte estranho;
- [ ] adicionais compreensíveis;
- [ ] CTA claro;
- [ ] card selecionado evidente;
- [ ] alturas consistentes;
- [ ] spacing uniforme.

### Modais

Verificar:

- [ ] abre corretamente;
- [ ] fecha corretamente;
- [ ] fecha com ESC;
- [ ] foco fica dentro do modal;
- [ ] botão de fechar é visível;
- [ ] conteúdo cabe no mobile;
- [ ] fundo não rola de forma problemática;
- [ ] botão final não fica fora da tela.

---

## Fase 10 — CTA WhatsApp

O CTA WhatsApp é elemento crítico.

### Verificar

- [ ] número correto com DDI e DDD;
- [ ] link abre no mobile;
- [ ] link abre no desktop;
- [ ] mensagem pré-preenchida está correta;
- [ ] produto selecionado aparece na mensagem;
- [ ] adicionais aparecem na mensagem;
- [ ] quantidade aparece na mensagem;
- [ ] observações aparecem na mensagem;
- [ ] preço aparece se o projeto usar preço;
- [ ] caracteres especiais não quebram o link;
- [ ] botão é fácil de tocar;
- [ ] CTA não fica coberto por safe-area;
- [ ] evento de analytics, se existir, dispara corretamente.

### Formato recomendado

```js
const phone = "5599999999999";
const message = encodeURIComponent(
  `Olá! Quero fazer um pedido:\n\n` +
  `Produto: Açaí Grande 550ml\n` +
  `Quantidade: 1\n` +
  `Adicionais: Banana, Morango, Granola\n\n` +
  `Pode me confirmar o total?`
);

const url = `https://wa.me/${phone}?text=${message}`;
```

Evitar montar link sem `encodeURIComponent`.

Errado:

```js
const url = "https://wa.me/5599999999999?text=Olá quero açaí grande";
```

---

## Fase 11 — Cardápio e conversão

Verificar se o cardápio ajuda a vender.

### Checklist

- [ ] categorias são claras;
- [ ] produtos mais importantes aparecem primeiro;
- [ ] produtos têm fotos boas;
- [ ] preço é fácil de achar;
- [ ] adicionais são compreensíveis;
- [ ] CTA fica perto da decisão;
- [ ] usuário não precisa procurar como pedir;
- [ ] não existe excesso de texto;
- [ ] combos/destaques são claros;
- [ ] produto premium tem destaque;
- [ ] fluxo não exige etapas demais;
- [ ] WhatsApp recebe mensagem útil.

### Sinais de problema

- usuário vê produto mas não sabe pedir;
- botão parece decorativo;
- foto ocupa demais e esconde informação;
- card bonito, mas sem preço/CTA;
- produto premium não se destaca;
- página exige muito scroll antes do pedido.

---

## Fase 12 — Formulários

Se houver formulário, verificar:

- [ ] labels visíveis;
- [ ] placeholder não substitui label;
- [ ] teclado mobile correto;
- [ ] campo telefone usa `inputmode="tel"`;
- [ ] campo número usa `inputmode="numeric"`;
- [ ] erro aparece perto do campo;
- [ ] erro é legível;
- [ ] erro não depende só de cor;
- [ ] foco vai para campo com erro;
- [ ] envio tem loading;
- [ ] botão evita duplo envio.

### Exemplo recomendado

```html
<label for="customer-phone">Telefone</label>
<input
  id="customer-phone"
  name="phone"
  type="tel"
  inputmode="tel"
  autocomplete="tel"
  required
  aria-describedby="phone-error"
/>
<p id="phone-error" class="field-error" hidden>
  Informe um telefone válido.
</p>
```

---

## Fase 13 — Acessibilidade essencial

Verificar:

- HTML semântico;
- heading order;
- alt em imagens;
- foco visível;
- navegação por teclado;
- contraste;
- labels em campos;
- botões reais;
- links com nome claro;
- aria apenas quando necessário;
- redução de movimento;
- áreas de toque confortáveis.

### Ordem de títulos

Correto:

```html
<h1>Nu Ki Açaí</h1>
<h2>Cardápio</h2>
<h3>Açaí Grande 550ml</h3>
```

Evitar pular níveis sem motivo:

```html
<h1>Nu Ki Açaí</h1>
<h4>Cardápio</h4>
```

### Foco visível

Não fazer:

```css
button:focus {
  outline: none;
}
```

Fazer:

```css
button:focus-visible,
a:focus-visible {
  outline: 3px solid #ffffff;
  outline-offset: 3px;
}
```

### Movimento reduzido

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.001ms !important;
  }
}
```

---

## Fase 14 — Imagens e assets

Verificar:

- [ ] imagens em WebP/AVIF quando possível;
- [ ] PNG apenas quando necessário;
- [ ] SVG para ícones;
- [ ] imagens não estão gigantes;
- [ ] imagens têm dimensões definidas;
- [ ] `loading="lazy"` abaixo da primeira dobra;
- [ ] `decoding="async"` quando adequado;
- [ ] alt correto;
- [ ] assets não estão borrados;
- [ ] fundos não prejudicam leitura;
- [ ] personagens estão consistentes;
- [ ] logos não estão distorcidas;
- [ ] efeitos não poluem a tela;
- [ ] imagens não causam CLS.

### HTML recomendado

```html
<picture>
  <source srcset="assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.avif" type="image/avif">
  <source srcset="assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.webp" type="image/webp">
  <img
    src="assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.png"
    alt="Açaí Grande 550ml com banana, morango e granola"
    width="768"
    height="768"
    loading="lazy"
    decoding="async"
  >
</picture>
```

---

## Fase 15 — Performance visual

Verificar:

- LCP;
- INP;
- CLS;
- tamanho da página;
- peso de imagens;
- quantidade de fontes;
- JS bloqueante;
- animações pesadas;
- scroll travando;
- imagens sem otimização;
- assets carregando antes da hora.

### Metas práticas

```text
LCP: até 2.5s ideal
INP: até 200ms ideal
CLS: até 0.1 ideal
Página inicial: idealmente abaixo de 2 MB
JS total: manter enxuto
Imagens: usar formatos modernos
```

### Checklist

- [ ] hero não é pesado demais;
- [ ] fontes essenciais têm preload;
- [ ] `font-display: swap`;
- [ ] imagens abaixo da dobra têm lazy loading;
- [ ] CSS não usado foi removido quando possível;
- [ ] JS não crítico usa defer;
- [ ] animações usam transform/opacity;
- [ ] não animar width/height/top/left sem necessidade.

---

## Fase 16 — Animações e microinterações

Animação deve melhorar a experiência, não atrapalhar.

Verificar:

- [ ] animação não causa enjoo;
- [ ] não trava scroll;
- [ ] não compete com CTA;
- [ ] não impede clique;
- [ ] não atrasa pedido;
- [ ] respeita `prefers-reduced-motion`;
- [ ] usa `transform` e `opacity`;
- [ ] não causa overflow horizontal;
- [ ] não movimenta texto principal demais;
- [ ] não roda infinitamente sem motivo.

### Bom uso

```css
.product-card {
  transition: transform 180ms ease, box-shadow 180ms ease;
}

.product-card:active {
  transform: scale(0.98);
}
```

### Cuidado

```css
animation: tudo-piscando-girando 1s infinite;
```

---

## Fase 17 — Cross-browser

Testar pelo menos:

```text
Chrome Android
Safari iOS
Chrome Desktop
Edge Desktop
Firefox Desktop quando possível
Navegador interno do WhatsApp
```

### Pontos de atenção

- Safari iOS e `100vh`;
- safe-area;
- autoplay de vídeo;
- formatos de imagem;
- sticky/fixed;
- backdrop-filter;
- inputs mobile;
- scroll dentro de modal;
- teclado virtual;
- fontes carregando.

---

## Fase 18 — Console e erros técnicos

Abrir DevTools e verificar:

- erros JavaScript;
- imagens 404;
- CSS 404;
- fontes 404;
- erros CORS;
- warnings graves;
- links quebrados;
- API inexistente;
- evento duplicado;
- variável indefinida.

### Comandos úteis no console

Ver imagens quebradas:

```js
[...document.images].filter(img => !img.complete || img.naturalWidth === 0);
```

Ver links vazios:

```js
[...document.querySelectorAll("a")].filter(a => !a.getAttribute("href") || a.getAttribute("href") === "#");
```

Ver botões sem texto acessível:

```js
[...document.querySelectorAll("button")].filter(btn => !btn.innerText.trim() && !btn.getAttribute("aria-label"));
```

Ver imagens sem alt:

```js
[...document.querySelectorAll("img")].filter(img => !img.hasAttribute("alt"));
```

---

## Fase 19 — SEO local básico

QA final deve garantir que o site ajuda a loja a ser encontrada.

Verificar:

- [ ] título da página tem marca e serviço;
- [ ] meta description existe;
- [ ] endereço/área de atendimento aparece;
- [ ] telefone/WhatsApp aparece;
- [ ] horário aparece se disponível;
- [ ] Google Maps/link de localização existe se aplicável;
- [ ] termos locais aparecem naturalmente;
- [ ] schema `LocalBusiness` ou `Restaurant` existe quando possível;
- [ ] imagens têm alt útil;
- [ ] site é mobile-friendly;
- [ ] links sociais funcionam.

### Exemplo de title

```html
<title>Nu Ki Açaí — Cardápio e Delivery de Açaí</title>
```

### Exemplo de description

```html
<meta
  name="description"
  content="Conheça o cardápio da Nu Ki Açaí e faça seu pedido pelo WhatsApp. Açaí, adicionais, combos e delivery."
>
```

---

## Fase 20 — Conteúdo e microcopy

Verificar:

- erros de português;
- acentos;
- texto cortado;
- preço confuso;
- CTA genérico demais;
- frases longas;
- instruções pouco claras;
- inconsistência entre “Peça agora”, “Pedir”, “Comprar”;
- texto que promete algo que o fluxo não entrega.

### CTA recomendado

```text
Pedir no WhatsApp
Montar meu açaí
Ver cardápio
Adicionar ao pedido
Finalizar pedido
```

Evitar:

```text
Clique aqui
Enviar
Ok
Saiba mais
```

quando o contexto pede ação comercial direta.

---

## Fase 21 — Estados vazios, erro e carregamento

Verificar se existem estados para:

- lista vazia;
- produto indisponível;
- imagem não carregada;
- erro de pedido;
- erro de formulário;
- carregamento inicial;
- sem internet;
- horário fechado;
- WhatsApp indisponível.

### Exemplo

```html
<p class="empty-state">
  Nenhum produto encontrado nesta categoria.
</p>
```

Estado vazio sem explicação parece bug.

---

## Fase 22 — Checklist por seção

### Header

- [ ] logo correta;
- [ ] logo não distorce;
- [ ] menu funciona;
- [ ] menu cabe no mobile;
- [ ] contraste bom;
- [ ] não cobre conteúdo;
- [ ] sticky não atrapalha.

### Hero

- [ ] mensagem clara;
- [ ] imagem carrega rápido;
- [ ] CTA acima da dobra;
- [ ] fundo não atrapalha texto;
- [ ] animação não pesa;
- [ ] funciona em 320px.

### Cardápio

- [ ] categorias claras;
- [ ] produtos legíveis;
- [ ] imagens consistentes;
- [ ] preços visíveis;
- [ ] adicionais claros;
- [ ] CTA por produto ou CTA global;
- [ ] scroll suave.

### Produto

- [ ] nome correto;
- [ ] descrição correta;
- [ ] preço correto;
- [ ] imagem correta;
- [ ] adicionais funcionam;
- [ ] quantidade funciona;
- [ ] pedido vai para WhatsApp.

### Barra mobile fixa

- [ ] não cobre conteúdo crítico;
- [ ] respeita safe-area;
- [ ] CTA é claro;
- [ ] botão tem tamanho confortável;
- [ ] funciona em telas pequenas.

### Footer

- [ ] telefone/WhatsApp correto;
- [ ] endereço correto se houver;
- [ ] redes sociais funcionam;
- [ ] links não estão quebrados;
- [ ] texto legível.

---

## Fase 23 — QA de consistência da marca

A Nu Ki Açaí deve parecer uma marca única, não um conjunto de peças soltas.

Verificar:

- [ ] roxos/violetas consistentes;
- [ ] cards com mesma linguagem;
- [ ] efeitos combinam;
- [ ] personagens mantêm estilo;
- [ ] produtos mantêm iluminação parecida;
- [ ] logos não mudam de proporção;
- [ ] botões seguem o mesmo padrão;
- [ ] ícones seguem o mesmo estilo;
- [ ] sombras/brilhos não parecem aleatórios;
- [ ] tom visual é divertido, premium e apetitoso.

---

## Fase 24 — QA de arquivos

Verificar no projeto:

- [ ] não há assets soltos sem pasta;
- [ ] nomes não têm acentos/espaços;
- [ ] não há `final2.png`;
- [ ] não há master usado no site;
- [ ] assets publicados vêm de `derived/`;
- [ ] caminhos estão corretos;
- [ ] arquivos antigos não são referenciados;
- [ ] não há duplicatas óbvias;
- [ ] imagens pesadas foram identificadas.

---

## Fase 25 — Teste manual do fluxo real

Executar exatamente como o cliente faria:

```text
1. Abrir câmera do celular.
2. Ler QR code.
3. Abrir site.
4. Esperar primeira tela.
5. Ver cardápio.
6. Escolher um produto.
7. Selecionar adicionais.
8. Clicar em pedir.
9. Abrir WhatsApp.
10. Conferir mensagem.
11. Enviar ou simular envio.
```

Registrar:

- tempo percebido;
- pontos de dúvida;
- cliques desnecessários;
- se o CTA ficou visível;
- se a mensagem ficou correta;
- se algo quebrou.

---

## Critérios de aprovação por área

### Layout

Aprovado quando:

- não há corte;
- não há sobreposição;
- não há overflow horizontal;
- hierarquia visual está clara;
- espaçamentos estão consistentes.

### Conversão

Aprovado quando:

- CTA aparece rápido;
- pedido é fácil;
- WhatsApp abre corretamente;
- mensagem é útil;
- usuário entende o próximo passo.

### Acessibilidade

Aprovado quando:

- contraste é aceitável;
- foco visível existe;
- botões são botões;
- imagens têm alt;
- campos têm label;
- navegação básica por teclado funciona.

### Performance

Aprovado quando:

- primeira tela carrega bem;
- imagens não são exageradas;
- animações não travam;
- Lighthouse não aponta problemas graves;
- Core Web Vitals estão em faixa aceitável ou documentados.

### Marca

Aprovado quando:

- visual segue paleta;
- personagens/produtos são consistentes;
- logo está correta;
- qualidade parece profissional;
- nada parece improvisado.

---

## Anti-padrões proibidos

Não aprovar se houver:

```text
overflow horizontal
CTA WhatsApp quebrado
número de WhatsApp errado
produto sem botão de pedido
imagem gigante no mobile
texto ilegível
contraste baixo no CTA
botão pequeno demais
modal cortado
header cobrindo conteúdo
footer desorganizado
logo distorcida
assets inconsistentes
animação travando
console com erro crítico
link vazio ou "#"
layout testado só em desktop
```

---

## Prompts operacionais para Codex/Claude

### Prompt — QA visual completo

```text
Execute QA visual completo no projeto seguindo a skill "QA Visual e Revisão Final".

Prioridade:
1. mobile-first;
2. fluxo QR code → cardápio → WhatsApp;
3. responsividade;
4. acessibilidade;
5. performance;
6. consistência visual da marca Nu Ki Açaí.

Tarefas:
- mapear páginas, seções e componentes;
- testar breakpoints 320, 360, 375, 390, 414, 430, 768, 1024 e desktop;
- identificar overflow horizontal;
- verificar CTA WhatsApp;
- verificar links quebrados;
- verificar imagens, alt, peso e caminhos;
- verificar contraste, foco, teclado e botões;
- verificar alinhamento, spacing, tipografia e cores;
- revisar console do navegador;
- listar bugs por severidade;
- corrigir bugs seguros;
- não alterar identidade visual sem necessidade;
- entregar relatório final com arquivos alterados.
```

### Prompt — Corrigir overflow horizontal

```text
Procure e corrija qualquer overflow horizontal no projeto.

Regras:
- testar mentalmente/tecnicamente em 320px, 360px, 375px e 390px;
- encontrar elementos com largura maior que viewport;
- corrigir containers, imagens, cards, animações e elementos absolutos;
- evitar usar overflow-x:hidden como única solução se houver causa real;
- manter responsividade mobile-first;
- entregar lista dos seletores corrigidos.
```

### Prompt — Revisar CTA WhatsApp

```text
Revise todo o fluxo de WhatsApp.

Verificar:
- número correto;
- uso de wa.me ou api.whatsapp.com;
- encodeURIComponent na mensagem;
- produto, quantidade, adicionais e observações na mensagem;
- funcionamento no mobile;
- funcionamento no desktop;
- CTA visível e confortável;
- nenhum botão quebrado.

Corrigir o que for seguro e entregar relatório.
```

### Prompt — Revisar visual premium

```text
Revise a consistência visual premium da landing/cardápio Nu Ki Açaí.

Verificar:
- paleta roxa/violeta;
- contraste;
- sombras;
- bordas;
- radius;
- brilho;
- tipografia;
- espaçamento;
- cards;
- botões;
- personagens;
- produtos;
- fundos;
- efeitos.

Corrigir desalinhamentos e inconsistências sem mudar o conceito principal do design.
```

### Prompt — Revisão final antes de publicar

```text
Faça revisão final antes de publicar.

Bloqueie publicação se encontrar:
- CTA WhatsApp quebrado;
- layout quebrado no mobile;
- overflow horizontal;
- erro JS crítico;
- produtos invisíveis;
- texto ilegível;
- performance extremamente ruim;
- links principais quebrados.

Se estiver aprovado, entregue "APROVADO PARA PUBLICAÇÃO" com ressalvas, se houver.
```

---

## Exemplo de teste Playwright

```js
const { test, expect } = require("@playwright/test");

test("home mobile não tem overflow e CTA WhatsApp aparece", async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto("http://localhost:3000");

  const bodyWidth = await page.evaluate(() => document.body.scrollWidth);
  const viewportWidth = await page.evaluate(() => window.innerWidth);

  expect(bodyWidth).toBeLessThanOrEqual(viewportWidth);

  const cta = page.getByRole("link", { name: /whatsapp|pedir/i });
  await expect(cta).toBeVisible();
});
```

---

## Exemplo de teste Cypress

```js
describe("QA visual mobile", () => {
  it("não deve ter overflow horizontal em 375px", () => {
    cy.viewport(375, 812);
    cy.visit("/");

    cy.window().then((win) => {
      expect(win.document.body.scrollWidth).to.be.lte(win.innerWidth);
    });
  });

  it("CTA WhatsApp deve existir", () => {
    cy.viewport(375, 812);
    cy.visit("/");

    cy.contains(/whatsapp|pedir/i)
      .should("be.visible")
      .closest("a")
      .should("have.attr", "href")
      .and("match", /(wa\.me|whatsapp\.com)/);
  });
});
```

---

## Exemplo de relatório de bug

```md
## BUG-001 — CTA WhatsApp não abre no mobile

### Severidade
Crítica

### Prioridade
Urgente

### Ambiente
- Dispositivo: Android Chrome
- Viewport: 390x844
- Página: Cardápio

### Passos para reproduzir
1. Abrir o site.
2. Rolar até o produto Grande 550ml.
3. Clicar em "Pedir no WhatsApp".

### Resultado esperado
Abrir WhatsApp com mensagem preenchida do pedido.

### Resultado atual
O clique não faz nada.

### Impacto
Usuário não consegue pedir. Bloqueia conversão.

### Possível causa
Link sem href ou evento JS interrompido.

### Recomendação
Corrigir href para wa.me com mensagem codificada via encodeURIComponent.
```

---

## Template de relatório final

```md
# Relatório de QA Visual e Revisão Final

## Status geral
Aprovado / Aprovado com ressalvas / Reprovado

## Resumo
Descrever estado geral do projeto.

## Fluxo principal testado
- QR code / acesso mobile
- Home
- Cardápio
- Produto
- Pedido
- WhatsApp

## Breakpoints testados
- 320px
- 360px
- 375px
- 390px
- 414px
- 430px
- 768px
- Desktop

## Bugs críticos
- Nenhum / lista

## Bugs altos
- Nenhum / lista

## Bugs médios
- Nenhum / lista

## Bugs baixos
- Nenhum / lista

## Correções realizadas
- ...

## Arquivos alterados
- ...

## Itens que precisam de revisão humana
- ...

## Performance
- Observações de peso, imagens, LCP, INP, CLS.

## Acessibilidade
- Observações de contraste, foco, alt, labels.

## SEO local
- Observações de title, description, schema, endereço, WhatsApp.

## Veredito
Aprovado para publicação / Não aprovado para publicação.

## Próximos passos
- ...
```

---

## Checklist final compacto

Antes de dizer que terminou, confirmar:

```text
[ ] Mobile 320px testado
[ ] Mobile 375px testado
[ ] Mobile 414px testado
[ ] Tablet testado
[ ] Desktop testado
[ ] Sem overflow horizontal
[ ] CTA WhatsApp correto
[ ] Mensagem WhatsApp correta
[ ] Links principais funcionando
[ ] Console sem erro crítico
[ ] Imagens carregando
[ ] Imagens com alt adequado
[ ] Texto legível
[ ] Contraste aceitável
[ ] Foco visível
[ ] Botões confortáveis
[ ] Formulários usáveis
[ ] Animações suaves
[ ] Sem layout cortado
[ ] SEO local básico presente
[ ] Performance aceitável
[ ] Relatório entregue
```

---

## Critério final de sucesso

A skill foi aplicada corretamente quando o projeto pode ser aberto por um cliente real no celular e ele consegue:

1. entender a marca;
2. ver o cardápio;
3. escolher o produto;
4. clicar sem dificuldade;
5. abrir o WhatsApp;
6. enviar um pedido claro;
7. sem encontrar tela quebrada, texto ilegível, botão perdido ou site lento demais.

Se isso acontecer com consistência visual, boa responsividade e sem bugs críticos, o QA visual foi bem-sucedido.
