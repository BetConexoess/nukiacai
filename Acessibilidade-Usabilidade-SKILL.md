# SKILL.md — Acessibilidade e Usabilidade Mobile-First

## Nome da skill

**Acessibilidade e Usabilidade para Cardápio Digital, Landing Page e Conversão por WhatsApp**

## Objetivo

Garantir que o projeto seja bonito, rápido, confortável e utilizável por qualquer pessoa, principalmente em celulares acessados por **QR code**, **WhatsApp**, Instagram, tráfego local e links diretos.

Esta skill deve orientar a IA de programação a revisar, criar e corrigir interfaces com foco em:

- contraste visual;
- leitura confortável;
- botões fáceis de tocar;
- navegação por teclado;
- foco visível;
- leitores de tela;
- semântica HTML;
- formulários claros;
- acessibilidade mobile;
- CTA de pedido pelo WhatsApp;
- cardápio digital usável;
- fluxo de pedido sem fricção.

A meta mínima de qualidade é **WCAG 2.2 nível AA**, com adaptação prática para projeto comercial mobile-first.

---

## Quando usar esta skill

Use esta skill sempre que o trabalho envolver:

- landing page;
- cardápio digital;
- seção de produtos;
- botões de pedido;
- carrinho;
- CTA para WhatsApp;
- formulário de entrega;
- modal;
- menu mobile;
- carrossel;
- animações;
- imagens com texto;
- contraste de paleta;
- navegação por teclado;
- revisão visual mobile;
- auditoria antes de publicar.

Também use esta skill quando o usuário pedir algo como:

- “deixe acessível”;
- “melhore usabilidade”;
- “arrume o contraste”;
- “melhore o clique no celular”;
- “garanta leitura”;
- “melhore foco e teclado”;
- “deixe pronto para pessoas com deficiência”;
- “audite acessibilidade”.

---

## Resultado esperado

Ao aplicar esta skill, a IA deve entregar código que:

1. funcione bem em celular real;
2. não tenha texto ilegível;
3. tenha botões confortáveis para toque;
4. seja navegável por teclado;
5. tenha foco visível;
6. use HTML semântico;
7. não dependa apenas de cor para comunicar informação;
8. tenha textos alternativos corretos;
9. tenha formulários claros;
10. tenha CTA de WhatsApp compreensível;
11. não esconda foco atrás de header, barra fixa ou teclado virtual;
12. passe em auditorias básicas de Lighthouse, axe ou equivalente;
13. mantenha a estética premium do projeto sem sacrificar uso real.

---

## Princípios obrigatórios

### 1. HTML nativo antes de ARIA

Sempre prefira elementos HTML nativos:

- use `<button>` para ações;
- use `<a>` para navegação;
- use `<label>` para campos;
- use `<main>`, `<header>`, `<nav>`, `<section>`, `<footer>`;
- use `<h1>` a `<h6>` em ordem lógica;
- use `<ul>` e `<li>` para listas reais.

Não use `div` clicável quando um botão resolver.

Errado:

```html
<div class="btn" onclick="abrirPedido()">Pedir</div>
```

Certo:

```html
<button type="button" class="btn" onclick="abrirPedido()">
  Pedir agora
</button>
```

ARIA só deve ser usada para complementar, não para substituir HTML correto.

---

### 2. Mobile-first real

A interface deve nascer para o celular e depois expandir para telas maiores.

Regras:

- comece o CSS pelo layout mobile;
- use media queries apenas para telas maiores;
- evite desktop-first;
- teste largura de 320px;
- não permita overflow horizontal;
- use botões grandes;
- mantenha distância entre elementos tocáveis;
- respeite safe-area de celulares com notch.

CSS base recomendado:

```css
:root {
  --tap-min: 44px;
  --focus-ring: 3px solid #d8ff4f;
  --focus-offset: 4px;
  --radius-touch: 16px;
  --safe-bottom: env(safe-area-inset-bottom, 0px);
}

html {
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}

body {
  min-width: 320px;
  min-height: 100dvh;
  overflow-x: hidden;
}

button,
a,
input,
select,
textarea {
  font: inherit;
}

button,
.btn,
.cta,
[role="button"] {
  min-height: var(--tap-min);
  min-width: var(--tap-min);
}
```

---

### 3. Foco visível sempre

Nunca remova `outline` sem substituir por foco melhor.

Errado:

```css
*:focus {
  outline: none;
}
```

Certo:

```css
:where(a, button, input, select, textarea, summary, [tabindex]):focus-visible {
  outline: var(--focus-ring);
  outline-offset: var(--focus-offset);
  border-radius: 12px;
}
```

Em páginas com header fixo, barra mobile fixa ou CTA sticky, garanta que o foco não fique escondido.

```css
:target {
  scroll-margin-top: 96px;
}

[id] {
  scroll-margin-top: 96px;
}
```

Para barra inferior mobile:

```css
.mobile-order-bar {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  padding-bottom: calc(12px + var(--safe-bottom));
}

body.has-mobile-bar {
  padding-bottom: calc(88px + var(--safe-bottom));
}
```

---

### 4. Contraste deve vencer a estética

O projeto pode usar roxo, neon, brilho e identidade premium, mas texto e botões precisam ser legíveis.

Critérios práticos:

- texto normal: contraste mínimo aproximado de 4.5:1;
- texto grande: contraste mínimo aproximado de 3:1;
- ícones e bordas importantes: contraste mínimo aproximado de 3:1;
- CTA principal deve ser legível sob luz forte;
- texto roxo sobre fundo roxo escuro só pode ser usado se passar contraste;
- não use opacidade baixa em texto importante;
- placeholder não pode ser a única instrução.

Para este projeto, evitar:

```css
color: rgba(255, 255, 255, 0.45);
```

Em texto funcional, prefira:

```css
color: rgba(255, 255, 255, 0.88);
```

Ou use tokens:

```css
:root {
  --color-bg: #0e0122;
  --color-surface: #1c0833;
  --color-surface-2: #2f154c;
  --color-text: #ffffff;
  --color-text-soft: #f3eaff;
  --color-muted: #d8c7ee;
  --color-accent: #d8ff4f;
  --color-focus: #d8ff4f;
  --color-danger: #ff6b8a;
  --color-success: #5effa1;
}
```

---

### 5. Botões e áreas de toque confortáveis

Qualquer ação importante deve ter área confortável para o dedo.

Regra prática:

- CTA principal: mínimo 48px de altura;
- botões comuns: mínimo 44px;
- ícones clicáveis: mínimo 44x44px;
- distância entre botões pequenos: no mínimo 8px;
- cards clicáveis não devem ter áreas ambíguas;
- evite ícone pequeno isolado para ação crítica.

Exemplo:

```css
.cta-whatsapp,
.add-to-cart,
.category-chip,
.mobile-nav-button {
  min-height: 48px;
  padding: 0.85rem 1rem;
  border-radius: 999px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  touch-action: manipulation;
}
```

---

### 6. Informação não pode depender só de cor

Nunca comunique erro, sucesso, promoção, indisponibilidade ou destaque apenas por cor.

Errado:

```html
<p class="red">Campo inválido</p>
```

Certo:

```html
<p class="field-error" id="telefone-error">
  Erro: informe um WhatsApp com DDD válido.
</p>
```

Promoção correta:

```html
<span class="badge badge-promo" aria-label="Produto em promoção">
  Promoção
</span>
```

Produto indisponível correto:

```html
<button type="button" disabled>
  Indisponível no momento
</button>
```

---

## Estrutura semântica recomendada para landing/cardápio

```html
<body>
  <a class="skip-link" href="#conteudo">Pular para o conteúdo principal</a>

  <header class="site-header">
    <a class="brand" href="/" aria-label="Página inicial Nu Ki Açaí">
      <img src="/assets/logo.svg" alt="Nu Ki Açaí" width="160" height="60" />
    </a>

    <nav aria-label="Navegação principal">
      <button
        type="button"
        class="menu-toggle"
        aria-expanded="false"
        aria-controls="menu-principal"
      >
        Menu
      </button>

      <ul id="menu-principal" hidden>
        <li><a href="#cardapio">Cardápio</a></li>
        <li><a href="#promocoes">Promoções</a></li>
        <li><a href="#lojas">Lojas</a></li>
        <li><a href="#pedido">Pedir agora</a></li>
      </ul>
    </nav>
  </header>

  <main id="conteudo">
    <section class="hero" aria-labelledby="hero-title">
      <h1 id="hero-title">Açaí cremoso, bonito e rápido para pedir</h1>
      <p>Escolha seu tamanho, monte seu pedido e envie pelo WhatsApp.</p>
      <a class="cta-whatsapp" href="#cardapio">Ver cardápio</a>
    </section>

    <section id="cardapio" aria-labelledby="cardapio-title">
      <h2 id="cardapio-title">Cardápio</h2>
      <!-- categorias e produtos -->
    </section>
  </main>

  <footer>
    <p>Nu Ki Açaí</p>
  </footer>
</body>
```

Skip link:

```css
.skip-link {
  position: absolute;
  left: 1rem;
  top: 1rem;
  transform: translateY(-150%);
  z-index: 9999;
  padding: 0.75rem 1rem;
  border-radius: 999px;
  background: var(--color-accent);
  color: #160024;
  font-weight: 800;
}

.skip-link:focus {
  transform: translateY(0);
}
```

---

## Padrão de menu mobile acessível

Regras:

- botão real para abrir/fechar;
- `aria-expanded` atualizado;
- `aria-controls` apontando para o menu;
- menu escondido com `hidden` quando fechado;
- primeiro link recebe foco ao abrir, se fizer sentido;
- tecla Escape fecha;
- foco volta ao botão ao fechar.

```html
<button
  type="button"
  class="menu-toggle"
  aria-expanded="false"
  aria-controls="mobile-menu"
>
  Abrir menu
</button>

<nav id="mobile-menu" hidden aria-label="Menu mobile">
  <a href="#cardapio">Cardápio</a>
  <a href="#promocoes">Promoções</a>
  <a href="#lojas">Lojas</a>
  <a href="#pedido">Pedir agora</a>
</nav>
```

```js
const menuButton = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('#mobile-menu');

function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  mobileMenu.hidden = true;
  menuButton.focus();
}

function openMenu() {
  menuButton.setAttribute('aria-expanded', 'true');
  mobileMenu.hidden = false;
  const firstLink = mobileMenu.querySelector('a, button');
  firstLink?.focus();
}

menuButton?.addEventListener('click', () => {
  const expanded = menuButton.getAttribute('aria-expanded') === 'true';
  expanded ? closeMenu() : openMenu();
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !mobileMenu.hidden) {
    closeMenu();
  }
});
```

---

## Padrão de card de produto acessível

Cada produto deve ter:

- nome claro;
- descrição curta;
- preço em texto real;
- imagem com alt útil ou decorativo correto;
- botão explícito;
- estado de indisponível claro;
- adicionais fáceis de tocar;
- preço não apenas em imagem.

```html
<article class="product-card" aria-labelledby="produto-770-title">
  <img
    src="/assets/produtos/acai-770.webp"
    width="640"
    height="480"
    loading="lazy"
    alt="Copo de açaí gigante de 770 ml com banana, morango e leite em pó"
  />

  <div class="product-content">
    <h3 id="produto-770-title">Açaí Gigante 770 ml</h3>
    <p>Açaí cremoso com até 4 adicionais grátis.</p>
    <p class="price">R$ 24,90</p>

    <button type="button" class="add-to-cart" data-product-id="acai-770">
      Adicionar ao pedido
    </button>
  </div>
</article>
```

Produto indisponível:

```html
<article class="product-card is-unavailable" aria-labelledby="barca-title">
  <h3 id="barca-title">Barca Premium</h3>
  <p>Temporariamente indisponível.</p>
  <button type="button" disabled>Indisponível</button>
</article>
```

---

## Padrão de categorias e chips

Categorias do cardápio devem ser fáceis de tocar e entender.

```html
<nav class="category-nav" aria-label="Categorias do cardápio">
  <a class="category-chip" href="#acais">Açaís</a>
  <a class="category-chip" href="#barcas">Barcas</a>
  <a class="category-chip" href="#combos">Combos</a>
  <a class="category-chip" href="#adicionais">Adicionais</a>
</nav>
```

```css
.category-nav {
  display: flex;
  gap: 0.75rem;
  overflow-x: auto;
  padding: 0.75rem 1rem;
  scroll-snap-type: x proximity;
  scrollbar-width: thin;
}

.category-chip {
  min-height: 44px;
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1rem;
  border-radius: 999px;
  scroll-snap-align: start;
  text-decoration: none;
}
```

Não esconda categoria essencial atrás de carrossel difícil de usar.

---

## CTA para WhatsApp acessível

O CTA de WhatsApp deve:

- ter texto claro;
- não depender só do ícone;
- abrir link válido;
- incluir `rel="noopener noreferrer"` quando abrir em nova aba;
- ter mensagem pré-preenchida legível;
- manter nome acessível coerente com texto visível;
- ser grande o suficiente para toque;
- ser o CTA mais fácil de encontrar no mobile.

```html
<a
  class="cta-whatsapp"
  href="https://wa.me/5599999999999?text=Ol%C3%A1%2C%20quero%20fazer%20um%20pedido%20na%20Nu%20Ki%20A%C3%A7a%C3%AD."
  target="_blank"
  rel="noopener noreferrer"
>
  Fazer pedido pelo WhatsApp
</a>
```

Se tiver ícone:

```html
<a class="cta-whatsapp" href="...">
  <svg aria-hidden="true" focusable="false" width="20" height="20"></svg>
  <span>Fazer pedido pelo WhatsApp</span>
</a>
```

Evite:

```html
<a href="..." aria-label="Enviar"><svg></svg></a>
```

Prefira nome claro:

```html
<a href="..." aria-label="Fazer pedido pelo WhatsApp">
  <svg aria-hidden="true" focusable="false"></svg>
</a>
```

---

## Formulários acessíveis

Todo campo precisa de label real.

Errado:

```html
<input placeholder="Nome" />
```

Certo:

```html
<label for="nome">Nome</label>
<input id="nome" name="nome" type="text" autocomplete="name" />
```

Formulário completo:

```html
<form id="pedido-form" novalidate aria-describedby="pedido-ajuda">
  <p id="pedido-ajuda">Campos marcados com * são obrigatórios.</p>

  <div class="field">
    <label for="nome">Nome *</label>
    <input id="nome" name="nome" type="text" autocomplete="name" required />
  </div>

  <div class="field">
    <label for="telefone">WhatsApp *</label>
    <input
      id="telefone"
      name="telefone"
      type="tel"
      inputmode="tel"
      autocomplete="tel-national"
      aria-describedby="telefone-ajuda telefone-erro"
      required
    />
    <small id="telefone-ajuda">Inclua o DDD. Exemplo: (11) 99999-9999.</small>
    <p id="telefone-erro" class="field-error" hidden></p>
  </div>

  <div class="field">
    <label for="endereco">Endereço de entrega</label>
    <textarea id="endereco" name="endereco" autocomplete="street-address"></textarea>
  </div>

  <button type="submit">Enviar pedido pelo WhatsApp</button>
  <p id="form-status" role="status" aria-live="polite"></p>
</form>
```

Validação recomendada:

```js
const form = document.querySelector('#pedido-form');
const telefone = document.querySelector('#telefone');
const telefoneErro = document.querySelector('#telefone-erro');
const statusEl = document.querySelector('#form-status');

form?.addEventListener('submit', (event) => {
  event.preventDefault();

  telefoneErro.hidden = true;
  telefoneErro.textContent = '';
  telefone.removeAttribute('aria-invalid');

  const digits = telefone.value.replace(/\D/g, '');

  if (digits.length < 10) {
    telefoneErro.textContent = 'Informe um WhatsApp válido com DDD.';
    telefoneErro.hidden = false;
    telefone.setAttribute('aria-invalid', 'true');
    statusEl.textContent = 'Revise os campos com erro antes de enviar.';
    telefone.focus();
    return;
  }

  statusEl.textContent = 'Abrindo o WhatsApp para finalizar o pedido.';
});
```

Regras de formulário:

- erro deve aparecer em texto;
- campo inválido deve receber `aria-invalid="true"`;
- foco deve ir para o primeiro campo com erro;
- o usuário deve entender como corrigir;
- não use apenas borda vermelha;
- não dependa só de máscara;
- autocomplete deve ser usado quando fizer sentido;
- teclado mobile deve ser adequado com `type`, `inputmode` e `autocomplete`.

---

## Modais acessíveis

Se possível, use `<dialog>`.

```html
<button type="button" id="abrir-adicionais">
  Escolher adicionais
</button>

<dialog id="adicionais-dialog" aria-labelledby="adicionais-title">
  <form method="dialog">
    <h2 id="adicionais-title">Escolha seus adicionais</h2>

    <label>
      <input type="checkbox" name="adicionais" value="leite-condensado" />
      Leite condensado
    </label>

    <label>
      <input type="checkbox" name="adicionais" value="morango" />
      Morango
    </label>

    <menu>
      <button value="cancel">Cancelar</button>
      <button value="confirm">Aplicar adicionais</button>
    </menu>
  </form>
</dialog>
```

```js
const abrirAdicionais = document.querySelector('#abrir-adicionais');
const adicionaisDialog = document.querySelector('#adicionais-dialog');

abrirAdicionais?.addEventListener('click', () => {
  adicionaisDialog.showModal();
});

adicionaisDialog?.addEventListener('close', () => {
  abrirAdicionais.focus();
});
```

Regras:

- foco entra no modal ao abrir;
- foco não deve ficar perdido atrás do modal;
- Escape deve fechar quando permitido;
- ao fechar, foco volta para o botão que abriu;
- título do modal deve ser claro;
- não use modal para tudo;
- modal em celular deve caber na tela;
- fundo não deve ser navegável por teclado enquanto modal está aberto.

---

## Carrosséis e animações acessíveis

Carrossel só deve existir se tiver função real. Não use carrossel pesado apenas por estética.

Regras obrigatórias:

- carrossel automático precisa de botão de pausar;
- não avance automaticamente enquanto foco está dentro;
- controles anterior/próximo devem ser botões reais;
- conteúdo importante não pode depender de swipe;
- deve haver alternativa por clique/toque simples;
- respeite `prefers-reduced-motion`.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

Animações do projeto Nu Ki Açaí devem seguir estas regras:

- animação pode encantar, mas não pode bloquear pedido;
- frutas, gotas e potes podem se mover, mas não devem causar enjoo;
- não animar texto principal de forma que prejudique leitura;
- evitar loop agressivo;
- manter performance mobile;
- pausar ou reduzir movimento quando o usuário pedir redução de movimento.

---

## Imagens, ícones e textos alternativos

### Imagem informativa

Use alt descritivo.

```html
<img
  src="/assets/produtos/barca-premium.webp"
  alt="Barca de açaí com morango, banana, leite em pó e cobertura de chocolate"
  width="800"
  height="600"
  loading="lazy"
/>
```

### Imagem decorativa

Use alt vazio.

```html
<img src="/assets/decoracoes/gotas-acai.svg" alt="" aria-hidden="true" />
```

### Logo

Se o link já tem contexto, alt pode ser o nome da marca.

```html
<a href="/" aria-label="Página inicial Nu Ki Açaí">
  <img src="/assets/logos/logo-horizontal.svg" alt="Nu Ki Açaí" />
</a>
```

### Ícone dentro de botão com texto

```html
<button type="button">
  <svg aria-hidden="true" focusable="false"></svg>
  <span>Adicionar ao pedido</span>
</button>
```

### Ícone sozinho

```html
<button type="button" aria-label="Remover Açaí 770 ml do pedido">
  <svg aria-hidden="true" focusable="false"></svg>
</button>
```

---

## Legibilidade e tipografia

Regras:

- corpo de texto mobile: mínimo 16px;
- descrições: preferencialmente 15px ou mais;
- evitar blocos longos centralizados;
- evitar texto fino demais em fundo escuro;
- evitar letras em caixa alta para parágrafos;
- usar line-height confortável;
- manter espaçamento entre seções;
- não colocar preço importante pequeno demais;
- não usar texto dentro de imagem para informações essenciais.

CSS recomendado:

```css
body {
  font-size: 16px;
  line-height: 1.5;
  color: var(--color-text);
  background: var(--color-bg);
}

p,
li {
  line-height: 1.55;
}

.product-description {
  font-size: 0.95rem;
  color: var(--color-muted);
}

.price {
  font-size: clamp(1.15rem, 4vw, 1.5rem);
  font-weight: 800;
}
```

---

## Usabilidade para cardápio digital

O usuário precisa conseguir fazer estas tarefas sem pensar muito:

1. entender o que a marca vende;
2. abrir o cardápio;
3. escolher tamanho;
4. escolher adicionais;
5. ver preço;
6. revisar pedido;
7. enviar pelo WhatsApp;
8. voltar se errou;
9. entender se algo está indisponível;
10. encontrar loja, horário e entrega.

Regras de UX:

- CTA principal sempre visível ou fácil de alcançar;
- categorias claras;
- produtos com nomes objetivos;
- preço visível;
- adicionais organizados;
- botão “Adicionar” próximo do produto;
- feedback após adicionar item;
- carrinho com resumo claro;
- mensagem de WhatsApp bem formatada;
- sem etapas desnecessárias;
- sem pop-up bloqueando o pedido.

---

## Barra fixa mobile acessível

```html
<div class="mobile-order-bar" role="region" aria-label="Resumo do pedido">
  <p id="order-summary">0 itens no pedido</p>
  <a class="cta-whatsapp" href="#pedido">
    Revisar pedido
  </a>
</div>
```

```css
.mobile-order-bar {
  position: fixed;
  z-index: 50;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.75rem 1rem calc(0.75rem + var(--safe-bottom));
  background: rgba(14, 1, 34, 0.94);
  backdrop-filter: blur(14px);
  border-top: 1px solid rgba(216, 255, 79, 0.28);
}
```

Regras:

- não esconder conteúdo final atrás da barra;
- não cobrir foco;
- texto deve atualizar quando item for adicionado;
- atualização importante deve ser anunciada com `role="status"`.

```html
<p id="cart-status" role="status" aria-live="polite" class="sr-only"></p>
```

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

```js
function announceCartUpdate(productName) {
  const status = document.querySelector('#cart-status');
  if (status) {
    status.textContent = `${productName} foi adicionado ao pedido.`;
  }
}
```

---

## Estados visuais obrigatórios

Todo botão, link, chip, input e card interativo deve ter estados:

- default;
- hover, quando aplicável;
- active;
- focus-visible;
- disabled;
- loading, se houver ação assíncrona;
- error, se houver validação.

Exemplo:

```css
.cta-whatsapp {
  background: linear-gradient(135deg, #d8ff4f, #7cff7a);
  color: #160024;
  font-weight: 900;
  text-decoration: none;
  box-shadow: 0 10px 28px rgba(216, 255, 79, 0.22);
}

.cta-whatsapp:hover {
  transform: translateY(-1px);
}

.cta-whatsapp:active {
  transform: translateY(0);
}

.cta-whatsapp:focus-visible {
  outline: 3px solid #ffffff;
  outline-offset: 4px;
}

.cta-whatsapp[aria-disabled="true"],
.cta-whatsapp.is-disabled {
  opacity: 0.6;
  pointer-events: none;
}
```

---

## Não usar tabindex positivo

Nunca use:

```html
<button tabindex="1">...</button>
```

Regras:

- `tabindex="0"` só quando realmente necessário;
- `tabindex="-1"` pode ser usado para foco programático;
- `tabindex` positivo é proibido;
- ordem do DOM deve seguir a ordem visual e lógica.

---

## Tabelas e listas

Evite tabela para layout.

Para lista de produtos, use lista ou cards semânticos:

```html
<ul class="product-list" aria-label="Produtos de açaí">
  <li>
    <article class="product-card">...</article>
  </li>
</ul>
```

Se precisar de tabela real, use `<th>`, `<caption>` e escopo correto.

---

## Dark mode e tema roxo premium

Como o projeto usa fundo escuro, redobre atenção em:

- contraste de texto;
- contraste de botão;
- contraste de placeholder;
- contraste de borda de campo;
- contraste do foco;
- brilho que atrapalha leitura;
- transparência baixa demais;
- texto neon pequeno.

Regras:

- neon é bom para destaque, ruim para parágrafos longos;
- roxo claro pode ser usado em ícones, não em texto pequeno sobre roxo escuro sem teste;
- CTA principal deve ter contraste máximo;
- feedback de erro deve ser legível e não apenas vermelho.

---

## Acessibilidade cognitiva e clareza

O usuário pode estar:

- com pressa;
- em ambiente com sol;
- usando internet ruim;
- com uma mão só;
- usando celular pequeno;
- com baixa visão;
- sendo idoso;
- não entendendo tecnologia;
- vindo direto do QR code.

Portanto:

- use linguagem simples;
- evite instruções longas;
- explique etapas do pedido;
- mostre resumo antes de enviar;
- evite surpresa;
- mantenha padrões consistentes;
- não mude layout do nada;
- não esconda preço;
- não use botões com nomes vagos como “Enviar” quando o correto é “Enviar pedido pelo WhatsApp”.

---

## Checklist WCAG prático para este projeto

### Estrutura

- [ ] Existe um único `<main>`.
- [ ] Existe `<h1>` claro na página.
- [ ] Títulos seguem hierarquia lógica.
- [ ] Existe skip link para conteúdo principal.
- [ ] Navegação tem `aria-label` quando necessário.
- [ ] Seções importantes têm título visível.

### Contraste

- [ ] Texto normal legível no fundo.
- [ ] Texto pequeno não usa opacidade baixa.
- [ ] CTA principal tem contraste forte.
- [ ] Estado disabled ainda comunica claramente.
- [ ] Erro não depende só de cor.
- [ ] Ícones funcionais têm contraste adequado.

### Teclado e foco

- [ ] Todos os botões recebem foco.
- [ ] Todos os links recebem foco.
- [ ] Ordem do Tab é lógica.
- [ ] Foco é visível.
- [ ] Foco não fica escondido atrás de header/barra fixa.
- [ ] Não há armadilha de teclado.
- [ ] Escape fecha modal/menu quando aplicável.
- [ ] Não existe `tabindex` positivo.

### Mobile e toque

- [ ] Botões principais têm pelo menos 44px de altura.
- [ ] CTA principal tem pelo menos 48px de altura.
- [ ] Ícones clicáveis têm área de toque suficiente.
- [ ] Chips de categoria são fáceis de tocar.
- [ ] Layout funciona em 320px.
- [ ] Não há overflow horizontal.
- [ ] Barra fixa respeita safe-area.

### Formulários

- [ ] Todo input tem label visível.
- [ ] Placeholder não substitui label.
- [ ] Campos obrigatórios são indicados em texto.
- [ ] Erros aparecem em texto.
- [ ] Erros são associados ao campo.
- [ ] Campo inválido usa `aria-invalid`.
- [ ] Primeiro erro recebe foco.
- [ ] Status de envio é anunciado.
- [ ] `autocomplete` é usado quando útil.

### Imagens e ícones

- [ ] Imagens informativas têm `alt` útil.
- [ ] Imagens decorativas têm `alt=""`.
- [ ] SVG decorativo tem `aria-hidden="true"`.
- [ ] Ícone sozinho tem `aria-label` no botão/link.
- [ ] Informação essencial não está apenas em imagem.

### WhatsApp e conversão

- [ ] CTA tem texto claro.
- [ ] Link do WhatsApp está correto.
- [ ] Mensagem pré-preenchida está legível.
- [ ] Botão não depende só do ícone do WhatsApp.
- [ ] Resumo do pedido é claro.
- [ ] Usuário consegue revisar antes de enviar.

### Movimento

- [ ] `prefers-reduced-motion` é respeitado.
- [ ] Animações não impedem leitura.
- [ ] Carrossel automático tem pausa.
- [ ] Swipe não é a única forma de ação.
- [ ] Scroll continua suave em celular real.

---

## Testes obrigatórios antes de publicar

### Teste manual rápido

1. Abrir no celular real.
2. Acessar pelo link como se viesse do WhatsApp.
3. Acessar pelo QR code.
4. Tentar fazer pedido com uma mão só.
5. Aumentar zoom/fonte do celular.
6. Testar em 320px no DevTools.
7. Verificar contraste sob brilho alto.
8. Navegar com teclado no desktop.
9. Ativar leitor de tela básico quando possível.
10. Testar envio do pedido para WhatsApp.

### Teste com teclado

- Tab percorre elementos importantes.
- Shift+Tab volta corretamente.
- Enter ativa links e botões.
- Space ativa botões.
- Escape fecha modal/menu.
- Foco sempre aparece.

### Teste com leitor de tela

Validar pelo menos:

- título da página;
- navegação principal;
- títulos de seção;
- cards de produto;
- preço;
- botões de adicionar;
- carrinho/resumo;
- erros do formulário;
- CTA WhatsApp.

### Teste automatizado sugerido

Instalar ferramentas:

```bash
npm i -D @playwright/test @axe-core/playwright lighthouse pa11y-ci
```

Playwright + axe:

```js
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('home sem violações graves de acessibilidade', async ({ page }) => {
  await page.goto('http://localhost:3000');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
    .analyze();

  const serious = results.violations.filter((violation) =>
    ['serious', 'critical'].includes(violation.impact || '')
  );

  expect(serious).toEqual([]);
});
```

Lighthouse:

```bash
npx lighthouse http://localhost:3000 --view
```

Pa11y:

```bash
npx pa11y-ci --sitemap http://localhost:3000/sitemap.xml
```

---

## Definition of Done

Uma tarefa só está pronta quando:

- [ ] funciona em mobile;
- [ ] funciona sem overflow horizontal;
- [ ] tem foco visível;
- [ ] funciona por teclado;
- [ ] tem contraste aceitável;
- [ ] não depende apenas de cor;
- [ ] botões são confortáveis para toque;
- [ ] formulários têm labels e erros claros;
- [ ] imagens têm alt correto;
- [ ] animações respeitam redução de movimento;
- [ ] CTA WhatsApp é claro e funcional;
- [ ] Lighthouse não aponta problema grave de acessibilidade;
- [ ] axe não aponta violações críticas/sérias nas rotas principais;
- [ ] a experiência permanece bonita sem prejudicar a usabilidade.

---

## Anti-padrões proibidos

Não fazer:

- remover outline globalmente;
- usar `div` como botão;
- colocar botão pequeno demais;
- usar texto roxo escuro em fundo roxo escuro;
- depender só de cor para erro;
- esconder preço em imagem;
- usar placeholder como label;
- usar `tabindex` positivo;
- criar modal sem controle de foco;
- criar menu que não fecha com Escape;
- carrossel automático sem pausa;
- CTA só com ícone;
- imagem sem alt quando informativa;
- animação que trava scroll;
- barra fixa cobrindo o último conteúdo;
- botão disabled sem explicação;
- link “clique aqui” sem contexto;
- usar ARIA para corrigir HTML mal estruturado.

---

## Ordem correta de trabalho da IA

Quando a IA aplicar esta skill, deve seguir esta ordem:

1. Mapear as telas/componentes afetados.
2. Identificar fluxo principal do usuário.
3. Revisar semântica HTML.
4. Revisar foco e teclado.
5. Revisar contraste e estados visuais.
6. Revisar toque mobile.
7. Revisar formulários e mensagens.
8. Revisar CTA WhatsApp.
9. Revisar imagens, ícones e textos alternativos.
10. Revisar movimento e animações.
11. Rodar auditoria automatizada quando possível.
12. Corrigir incrementalmente sem quebrar design.
13. Entregar resumo do que foi corrigido.

---

## Prompt interno para auditoria de código

Use este prompt quando for revisar o projeto:

```text
Audite este projeto como especialista em acessibilidade e usabilidade mobile-first. Priorize WCAG 2.2 AA, cardápio digital, CTA para WhatsApp, contraste, foco visível, navegação por teclado, leitores de tela, toque confortável, formulários, modais, menus, carrosséis e animações. Liste problemas por severidade, explique o impacto para o usuário e aplique correções incrementais no código sem quebrar o design visual premium do projeto.
```

---

## Prompt interno para correção incremental

```text
Corrija a acessibilidade deste componente mantendo o visual atual. Não reescreva tudo sem necessidade. Preserve classes existentes quando possível. Garanta HTML semântico, foco visível, teclado, contraste, labels, alt text, área de toque mínima, aria apenas quando necessário e compatibilidade mobile-first. Ao final, explique quais problemas foram corrigidos e quais ainda precisam de teste manual.
```

---

## Prompt interno para revisão visual mobile

```text
Revise esta tela em mobile-first. Verifique se textos são legíveis, botões são fáceis de tocar, o CTA principal está claro, a barra fixa não cobre conteúdo, não existe overflow horizontal, o foco não fica escondido, os estados hover/focus/active/disabled existem e a experiência continua rápida e confortável no celular.
```

---

## Checklist específico para Nu Ki Açaí

### Home

- [ ] Logo com alt correto.
- [ ] H1 claro.
- [ ] CTA “Ver cardápio” visível.
- [ ] CTA “Pedir pelo WhatsApp” visível.
- [ ] Animações não atrapalham leitura.
- [ ] `prefers-reduced-motion` aplicado.
- [ ] Foco não fica escondido.

### Cardápio

- [ ] Categorias tocáveis.
- [ ] Produtos têm nome, descrição e preço reais.
- [ ] Imagens têm alt útil.
- [ ] Botões “Adicionar” são grandes.
- [ ] Itens indisponíveis são claros.
- [ ] Adicionais têm checkboxes/radios acessíveis.

### Carrinho

- [ ] Resumo do pedido é claro.
- [ ] Total é fácil de encontrar.
- [ ] Remover item tem nome acessível.
- [ ] Alterar quantidade funciona por botão.
- [ ] Atualização do carrinho é anunciada.
- [ ] CTA WhatsApp é o principal.

### WhatsApp

- [ ] Mensagem final inclui itens.
- [ ] Mensagem final inclui adicionais.
- [ ] Mensagem final inclui total, se houver.
- [ ] Mensagem final inclui retirada/entrega, se houver.
- [ ] Link abre corretamente no celular.

### Lojas/contato

- [ ] Telefone clicável.
- [ ] Endereço em texto real.
- [ ] Horário de funcionamento claro.
- [ ] Mapa não é a única fonte do endereço.
- [ ] Redes sociais têm nomes acessíveis.

---

## Exemplo de mensagem de pedido acessível e legível

A mensagem gerada para WhatsApp deve ser organizada:

```text
Olá, quero fazer um pedido na Nu Ki Açaí.

Pedido:
1x Açaí Gigante 770 ml
Adicionais: banana, morango, leite em pó
Observação: sem leite condensado

Entrega: Rua Exemplo, 123
Nome: Davi
Pagamento: Pix

Total estimado: R$ 24,90
```

Ao montar link:

```js
function buildWhatsAppLink(phone, message) {
  const cleanPhone = phone.replace(/\D/g, '');
  const encodedMessage = encodeURIComponent(message.trim());
  return `https://wa.me/${cleanPhone}?text=${encodedMessage}`;
}
```

---

## Referências técnicas para consulta

Prioridade de consulta:

1. WCAG 2.2 — Web Content Accessibility Guidelines.
2. WAI-ARIA Authoring Practices Guide.
3. WAI Tutorials para formulários e imagens.
4. MDN Web Docs para HTML, CSS, ARIA e APIs.
5. Lighthouse Accessibility.
6. axe-core.
7. Pa11y.
8. Playwright accessibility testing.
9. Lei Brasileira de Inclusão — Lei 13.146/2015.
10. eMAG para referência brasileira de acessibilidade digital.

---

## Regra final da skill

**Design bonito só está aprovado quando também é legível, clicável, navegável, compreensível e rápido para pedir.**

No projeto Nu Ki Açaí, acessibilidade não é detalhe técnico: é parte direta da conversão. Se a pessoa não consegue ler, tocar, entender ou finalizar o pedido, o design falhou.
