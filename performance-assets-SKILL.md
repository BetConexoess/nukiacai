# SKILL.md — Performance e Assets

## Nome da skill

**performance-assets**

## Objetivo

Esta skill orienta qualquer IA de programação, agente de código ou desenvolvedor a transformar um site visualmente bonito em uma experiência **rápida, leve, estável e pronta para converter pedidos**, principalmente em **mobile**, **QR Code** e **WhatsApp**.

Use esta skill no projeto do cardápio digital Nu Ki Açaí sempre que for criar, revisar ou otimizar:

- imagens;
- vídeos;
- fontes;
- animações;
- CSS;
- JavaScript;
- carregamento inicial;
- performance mobile;
- Core Web Vitals;
- assets do cardápio;
- experiência de compra via WhatsApp;
- componentes visuais pesados;
- páginas acessadas por QR Code.

A regra principal é:

> **Bonito só funciona se carregar rápido. Performance também vende.**

---

## Quando ativar esta skill

Ative esta skill sempre que o pedido envolver qualquer uma destas situações:

- melhorar velocidade do site;
- otimizar imagens, fundos, logos, produtos ou ícones;
- corrigir site pesado/lento;
- reduzir travamentos no celular;
- melhorar carregamento no 3G/4G;
- revisar animações;
- revisar carrossel, cards, hero, splash ou efeitos visuais;
- adicionar novas imagens ao projeto;
- exportar assets;
- revisar CSS/JS;
- evitar overflow horizontal;
- melhorar Lighthouse/PageSpeed;
- preparar site para acesso via QR Code;
- melhorar conversão mobile;
- reduzir peso do cardápio digital;
- preparar PWA/cache;
- configurar lazy loading;
- revisar fontes;
- revisar vídeos ou GIFs;
- auditar performance antes de publicar.

---

## Contexto do projeto

O projeto é um cardápio digital/landing page para uma marca de açaí, com foco em:

- acesso majoritário por celular;
- entrada por QR Code, WhatsApp e link direto;
- visual premium roxo/violeta inspirado em açaí;
- imagens de produtos apetitosas;
- animações e efeitos visuais;
- conversão para pedido real via WhatsApp;
- experiência fluida, sem travar;
- botões grandes, claros e acessíveis;
- carrinho ou seleção de produtos com envio estruturado para WhatsApp.

Este projeto pode usar imagens bonitas e efeitos visuais, mas **nunca pode sacrificar velocidade, legibilidade ou conversão**.

---

## Princípios obrigatórios

### 1. Mobile primeiro

Tudo deve ser pensado primeiro para celular.

Não implemente um layout desktop e depois tente adaptar para mobile. O fluxo correto é:

1. mobile pequeno;
2. mobile médio;
3. tablet;
4. desktop.

A experiência principal precisa funcionar perfeitamente em telas entre **320px e 430px**.

---

### 2. Primeira dobra extremamente leve

A primeira tela deve carregar o mais rápido possível.

A primeira dobra não deve depender de:

- imagem enorme;
- vídeo;
- carrossel pesado;
- JavaScript grande;
- fontes externas demoradas;
- animações complexas;
- múltiplas requisições bloqueantes.

Priorize:

- HTML útil imediato;
- CSS crítico pequeno;
- imagem hero otimizada;
- CTA visível;
- texto legível;
- carregamento progressivo.

---

### 3. Cada KB importa

Em cardápio digital, o usuário pode estar:

- na rua;
- no balcão;
- sem Wi-Fi;
- com sinal ruim;
- com pressa;
- usando celular simples;
- vindo de QR Code;
- vindo do WhatsApp.

Por isso, todo asset precisa justificar seu peso.

---

### 4. Visual bonito precisa servir à conversão

Imagem, brilho, animação e efeito visual só devem existir se ajudarem a:

- entender o produto;
- aumentar desejo;
- guiar para o pedido;
- melhorar a experiência;
- reforçar a marca;
- facilitar a escolha;
- aumentar ticket médio.

Remova qualquer elemento visual que deixe o site mais bonito, mas atrapalhe:

- velocidade;
- leitura;
- clique;
- rolagem;
- foco no CTA;
- envio para WhatsApp.

---

### 5. Performance é parte do design

Não trate performance como etapa final.

Ao criar qualquer componente, já defina:

- peso máximo;
- formato de imagem;
- dimensões;
- comportamento mobile;
- lazy loading;
- fallback;
- impacto em LCP/INP/CLS;
- necessidade real de JS.

---

## Metas técnicas principais

### Core Web Vitals

As metas ideais para produção são:

| Métrica | Meta ideal | O que mede |
|---|---:|---|
| LCP | até 2,5s | carregamento do conteúdo principal |
| INP | até 200ms | resposta às interações |
| CLS | até 0,1 | estabilidade visual |

Sempre que revisar performance, pense:

- **LCP ruim**: imagem hero pesada, CSS bloqueante, fonte lenta, servidor lento.
- **INP ruim**: JavaScript pesado, eventos mal otimizados, animações travando.
- **CLS ruim**: imagens sem `width/height`, fontes trocando layout, banners entrando depois.

---

## Orçamento de performance do projeto

Use estes valores como orçamento inicial para páginas principais do cardápio:

| Item | Meta recomendada |
|---|---:|
| Página inicial total | até 2 MB |
| Primeira dobra crítica | até 350 KB |
| JavaScript total inicial | 200–250 KB ou menos |
| CSS total | até 100 KB |
| Imagens totais por página | 1–1,5 MB ou menos |
| Requisições iniciais | ideal até 25, máximo 40 |
| Fontes customizadas | no máximo 1–2 famílias |
| Pesos de fonte | 400 e 700, se possível |
| Imagem LCP | abaixo de 120–180 KB, quando possível |

Se o projeto precisar ultrapassar esses valores, explique o motivo e proponha compensações.

---

## Regras obrigatórias para imagens

### Formatos

Use preferencialmente:

- **AVIF** para máxima compressão, quando compatível;
- **WebP** como padrão seguro;
- **SVG** para ícones, logos simples e formas vetoriais;
- **PNG** apenas quando transparência de alta qualidade for indispensável;
- **JPG/JPEG** apenas como fallback ou para fotos quando WebP/AVIF não estiverem disponíveis.

Evite:

- PNG gigante para fotos;
- JPG sem compressão;
- GIF animado pesado;
- imagem 4K exibida em 300px;
- hero image acima de 500 KB;
- background gigante sem necessidade.

---

### Dimensões recomendadas

Nunca envie imagem maior do que o uso real pede.

| Uso | Dimensão sugerida |
|---|---:|
| Thumbnail de produto mobile | 240–400px |
| Card de produto destaque | 480–720px |
| Hero mobile | 720–1080px de largura |
| Hero desktop | 1440–1920px de largura |
| Logo normal | SVG ou PNG/WebP até 512px |
| Ícone | SVG ou 64–128px |
| Background decorativo | menor possível, com compressão forte |

Se a imagem aparece pequena, exporte pequena.

---

### Imagens responsivas

Sempre que uma imagem importante for exibida em tamanhos diferentes, use `srcset` e `sizes`.

```html
<picture>
  <source
    type="image/avif"
    srcset="
      assets/produtos/acai-320.avif 320w,
      assets/produtos/acai-640.avif 640w,
      assets/produtos/acai-960.avif 960w
    "
    sizes="(max-width: 600px) 90vw, 420px"
  />

  <source
    type="image/webp"
    srcset="
      assets/produtos/acai-320.webp 320w,
      assets/produtos/acai-640.webp 640w,
      assets/produtos/acai-960.webp 960w
    "
    sizes="(max-width: 600px) 90vw, 420px"
  />

  <img
    src="assets/produtos/acai-640.webp"
    alt="Açaí no copo com morango, banana e leite condensado"
    width="640"
    height="640"
    loading="lazy"
    decoding="async"
  />
</picture>
```

---

### Imagem principal/LCP

A imagem mais importante da primeira tela pode precisar de prioridade maior.

Use `fetchpriority="high"` apenas na imagem principal acima da dobra:

```html
<img
  src="assets/hero/acai-hero-mobile.webp"
  alt="Açaí cremoso com frutas frescas"
  width="900"
  height="700"
  fetchpriority="high"
  decoding="async"
/>
```

Não use `loading="lazy"` na imagem principal que representa o LCP da página.

---

### Lazy loading

Use `loading="lazy"` em imagens abaixo da primeira dobra:

```html
<img
  src="assets/produtos/barca-premium.webp"
  alt="Barca premium de açaí"
  width="640"
  height="480"
  loading="lazy"
  decoding="async"
/>
```

Não aplique lazy loading em:

- logo principal acima da dobra;
- imagem hero principal;
- imagem crítica do primeiro produto visível;
- elementos necessários para o primeiro CTA.

---

### Dimensões explícitas

Toda imagem deve ter `width` e `height`.

Isso evita CLS.

Correto:

```html
<img
  src="assets/produtos/copo-550.webp"
  alt="Açaí grande de 550ml"
  width="640"
  height="640"
  loading="lazy"
/>
```

Errado:

```html
<img src="assets/produtos/copo-550.png">
```

---

## Regras obrigatórias para vídeos e animações

### Vídeos

Evite vídeo pesado na primeira dobra.

Se for usar vídeo:

- use MP4/WebM comprimido;
- não use autoplay com som;
- adicione `poster`;
- carregue só quando necessário;
- não bloqueie o CTA;
- ofereça fallback visual;
- evite vídeo acima de 2–4 MB em páginas de entrada.

Exemplo seguro:

```html
<video
  class="hero-video"
  poster="assets/video/poster-acai.webp"
  muted
  playsinline
  preload="none"
>
  <source src="assets/video/acai-loop.webm" type="video/webm">
  <source src="assets/video/acai-loop.mp4" type="video/mp4">
</video>
```

---

### Animações

Animação deve ser leve e fluida.

Prefira animar:

- `transform`;
- `opacity`.

Evite animar:

- `width`;
- `height`;
- `top`;
- `left`;
- `margin`;
- `padding`;
- `box-shadow` pesado em muitos elementos;
- filtros complexos em loop.

Correto:

```css
.product-card {
  transition:
    transform 180ms ease,
    opacity 180ms ease;
}

.product-card:hover {
  transform: translateY(-4px);
}
```

Evite:

```css
.product-card:hover {
  width: 110%;
  margin-top: -20px;
  filter: blur(0);
}
```

---

### Redução de movimento

Sempre respeite `prefers-reduced-motion`.

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

## Regras obrigatórias para fontes

### Limite de fontes

Use no máximo:

- 1 família para textos;
- 1 família para títulos ou marca, se realmente necessário.

Evite:

- 4 ou 5 fontes diferentes;
- muitos pesos;
- fonte decorativa em texto longo;
- fonte externa bloqueando renderização.

---

### `font-display`

Toda fonte carregada manualmente deve usar `font-display: swap`.

```css
@font-face {
  font-family: "BrandFont";
  src: url("../fonts/brand-font.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

---

### Preload de fonte

Só faça preload da fonte realmente usada acima da dobra.

```html
<link
  rel="preload"
  href="/fonts/brand-font.woff2"
  as="font"
  type="font/woff2"
  crossorigin
>
```

Não faça preload de todas as fontes.

---

## Regras obrigatórias para CSS

### CSS mobile-first

Escreva CSS base para mobile e aumente com `min-width`.

```css
.menu-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

@media (min-width: 768px) {
  .menu-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .menu-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
```

---

### Evitar CSS duplicado

Antes de adicionar novo estilo:

1. procure se já existe token;
2. procure se já existe classe;
3. reutilize padrão existente;
4. só crie novo estilo se for necessário.

---

### Tokens de performance visual

Use variáveis para evitar repetição:

```css
:root {
  --color-bg: #0E0122;
  --color-bg-2: #15032E;
  --color-card: #2F154C;
  --color-accent: #6211AF;
  --color-whatsapp: #25D366;
  --color-text: #FFFFFF;

  --radius-card: 1.25rem;
  --shadow-soft: 0 18px 48px rgba(0, 0, 0, 0.35);
  --tap-target: 48px;

  --duration-fast: 160ms;
  --duration-normal: 240ms;
}
```

---

### CSS crítico

Para páginas simples, considere inline critical CSS mínimo no `<head>`.

Mas evite colocar CSS enorme inline.

O objetivo é fazer a primeira dobra aparecer rápido.

---

## Regras obrigatórias para JavaScript

### JavaScript mínimo na entrada

A página deve funcionar de forma útil mesmo com pouco JS.

JS inicial deve ser usado apenas para:

- carrinho;
- seleção de adicionais;
- cálculo do pedido;
- montagem da mensagem do WhatsApp;
- microinterações essenciais;
- analytics leve;
- estado local.

Evite JS pesado para:

- efeitos puramente decorativos;
- carrosséis complexos;
- animações que CSS resolveria;
- bibliotecas grandes sem necessidade;
- renderizar todo o cardápio se HTML estático resolver.

---

### Scripts não críticos

Use `defer` para scripts que não precisam bloquear o HTML.

```html
<script src="js/cardapio.js" defer></script>
```

Evite:

```html
<script src="js/cardapio.js"></script>
```

---

### Dividir responsabilidades

Separe JS por função:

```text
js/
  data.js
  cart.js
  whatsapp.js
  ui.js
  performance.js
```

Não misture tudo em um arquivo gigante se o projeto crescer.

---

### Evitar long tasks

Interações como adicionar produto, abrir carrinho e enviar WhatsApp devem responder imediatamente.

Se houver cálculo pesado:

- divida em funções menores;
- evite loops desnecessários;
- não recalcule o DOM inteiro;
- atualize apenas o necessário;
- use event delegation com cuidado.

---

## Regras para cardápio digital

### Produtos

Cada produto deve ter:

- nome curto e claro;
- volume/tamanho;
- preço visível;
- imagem otimizada;
- descrição curta;
- CTA de adicionar;
- destaque de adicionais;
- informação de disponibilidade quando necessário.

Exemplo de estrutura:

```html
<article class="product-card">
  <img
    src="assets/produtos/grande-550.webp"
    alt="Açaí grande de 550ml com banana e morango"
    width="480"
    height="480"
    loading="lazy"
  >

  <div class="product-card__content">
    <h3>Açaí Grande 550ml</h3>
    <p>Cremoso, gelado e montado com seus adicionais favoritos.</p>
    <strong>R$ 18,00</strong>
    <button type="button" class="product-card__button">
      Adicionar
    </button>
  </div>
</article>
```

---

### CTA para WhatsApp

O CTA de pedido deve ser:

- visível;
- grande;
- fixo no mobile quando houver carrinho;
- claro;
- com feedback;
- sem travar;
- sempre levando a uma mensagem estruturada.

Exemplo:

```js
function createWhatsAppUrl(phone, orderText) {
  const cleanPhone = String(phone).replace(/\D/g, "");
  const encodedText = encodeURIComponent(orderText);
  return `https://wa.me/${cleanPhone}?text=${encodedText}`;
}
```

---

### Mensagem de pedido

A mensagem enviada ao WhatsApp deve ser legível e organizada.

Modelo:

```text
Olá! Quero fazer um pedido:

🧾 Pedido:
1x Açaí Grande 550ml — R$ 18,00
Adicionais: banana, morango, leite condensado

1x Açaí Pequeno 200ml — R$ 9,00
Adicionais: granola

💰 Total: R$ 27,00

📍 Forma de retirada/entrega:
[cliente informa]

👤 Nome:
[cliente informa]
```

---

## Regras para carregamento inteligente

### Preload

Use preload apenas para recursos críticos:

```html
<link rel="preload" as="image" href="/assets/hero/acai-hero-mobile.webp">
```

Não faça preload de:

- imagens abaixo da dobra;
- todas as fontes;
- todos os scripts;
- assets decorativos.

---

### Preconnect

Use `preconnect` apenas para origens externas importantes:

```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

Não use várias origens externas sem necessidade.

---

### Cache

Configure cache forte para assets versionados.

Exemplo conceitual:

```http
Cache-Control: public, max-age=31536000, immutable
```

Use para:

- imagens com hash;
- CSS/JS versionado;
- fontes;
- ícones.

Não use cache longo para HTML dinâmico sem estratégia clara.

---

## Service Worker / PWA

Use Service Worker apenas se fizer sentido para o projeto.

Faz sentido quando:

- o cliente acessa o cardápio várias vezes;
- há recorrência;
- o cardápio deve abrir rápido mesmo em rede ruim;
- assets são estáveis;
- há fallback offline útil.

Não implemente PWA apenas para “parecer moderno”.

### Estratégia recomendada

- Cache-first para assets versionados;
- Stale-while-revalidate para imagens e CSS não crítico;
- Network-first para HTML;
- fallback offline simples.

---

## Acessibilidade ligada à performance

Performance e acessibilidade andam juntas.

Obrigatório:

- imagens com `alt`;
- botões com texto claro;
- foco visível;
- contraste suficiente;
- áreas de toque de pelo menos 44x44px;
- nada depender apenas de animação;
- nada depender apenas de cor;
- feedback textual em ações importantes;
- formulário com label real.

Exemplo:

```html
<button
  type="button"
  class="whatsapp-button"
  aria-label="Finalizar pedido pelo WhatsApp"
>
  Finalizar no WhatsApp
</button>
```

---

## Anti-padrões proibidos

Evite ou remova:

- imagem gigante em PNG/JPG;
- hero image acima de 1 MB;
- vídeo pesado com autoplay;
- GIF animado grande;
- carrossel infinito pesado;
- biblioteca só para efeito simples;
- 5 fontes diferentes;
- 10 pesos de fonte;
- script bloqueando renderização;
- imagem sem `width` e `height`;
- layout que pula ao carregar;
- botão pequeno no mobile;
- excesso de sombra/filtro em muitos cards;
- `100vh` causando corte em mobile;
- assets sem compressão;
- duplicação de CSS;
- animação rodando em loop sem propósito;
- lazy loading na imagem principal;
- preload em tudo;
- script de terceiros sem auditoria;
- console errors em produção.

---

## Ferramentas recomendadas

Use estas ferramentas para auditoria:

- Lighthouse;
- PageSpeed Insights;
- WebPageTest;
- Chrome DevTools Network;
- Chrome DevTools Performance;
- Coverage do DevTools;
- Squoosh;
- TinyPNG/TinyJPG;
- Sharp;
- SVGO;
- Bundle Analyzer;
- Responsively App;
- teste em celulares reais;
- teste com internet fraca.

---

## Checklist antes de publicar

### Imagens

- [ ] Todas as imagens estão em WebP/AVIF quando possível.
- [ ] Nenhuma foto de produto está em PNG gigante.
- [ ] Imagens têm dimensão correta para o uso.
- [ ] Imagens possuem `width` e `height`.
- [ ] Imagens abaixo da dobra usam `loading="lazy"`.
- [ ] Imagem LCP não usa lazy loading.
- [ ] Imagem LCP está comprimida.
- [ ] Logos e ícones simples usam SVG quando possível.
- [ ] Não há imagens duplicadas desnecessárias.

### Fontes

- [ ] Há no máximo 1–2 famílias de fonte.
- [ ] Pesos foram limitados.
- [ ] Fontes usam `font-display: swap`.
- [ ] Apenas fonte crítica usa preload.
- [ ] Existe fallback do sistema.

### CSS

- [ ] CSS é mobile-first.
- [ ] Não há CSS duplicado pesado.
- [ ] Não há animações custosas em massa.
- [ ] Não há overflow horizontal.
- [ ] Breakpoints estão organizados.
- [ ] Tokens visuais foram usados.
- [ ] CSS crítico está controlado.

### JavaScript

- [ ] JS não bloqueia renderização.
- [ ] Scripts usam `defer` quando possível.
- [ ] Não há biblioteca pesada desnecessária.
- [ ] Carrinho responde rápido.
- [ ] Botão WhatsApp responde rápido.
- [ ] Não há erros no console.
- [ ] Não há long tasks perceptíveis.

### Mobile

- [ ] Testado em 320px.
- [ ] Testado em 375px.
- [ ] Testado em 390px.
- [ ] Testado em 430px.
- [ ] Testado em Android real.
- [ ] Testado em iPhone ou Safari mobile.
- [ ] Testado com rede fraca.
- [ ] Botões têm área mínima confortável.
- [ ] CTA não fica escondido por barra inferior.
- [ ] Layout respeita safe area.

### Conversão

- [ ] CTA principal aparece rápido.
- [ ] Cardápio abre sem demora.
- [ ] Fotos dos produtos são leves e nítidas.
- [ ] Pedido pode ser montado sem confusão.
- [ ] Mensagem do WhatsApp sai organizada.
- [ ] Usuário entende o próximo passo.
- [ ] Não há distração excessiva antes do pedido.

### Auditoria

- [ ] Lighthouse mobile ≥ 90 em Performance quando possível.
- [ ] Accessibility ≥ 90.
- [ ] Best Practices ≥ 90.
- [ ] SEO básico correto.
- [ ] LCP abaixo de 2,5s em cenário ideal.
- [ ] INP sem travamentos aparentes.
- [ ] CLS baixo, sem pulos visuais.
- [ ] Peso total revisado.
- [ ] Requisições revisadas.
- [ ] Cache revisado.

---

## Fluxo ideal para adicionar novo asset

Sempre siga este fluxo:

1. **Definir função do asset**
   - Produto?
   - Fundo?
   - Ícone?
   - Decoração?
   - CTA?
   - Logo?

2. **Definir tamanho real de exibição**
   - Mobile?
   - Desktop?
   - Retina?
   - Card pequeno?
   - Hero?

3. **Exportar no formato certo**
   - Foto: WebP/AVIF.
   - Ícone: SVG.
   - Transparência: WebP/PNG somente se necessário.
   - Animação: CSS/Lottie leve/vídeo comprimido.

4. **Comprimir**
   - Squoosh;
   - TinyPNG;
   - Sharp;
   - ferramenta equivalente.

5. **Nomear corretamente**
   - sem espaços;
   - sem acentos;
   - com tamanho/uso claro.

Exemplo:

```text
assets/produtos/acai-grande-550-640.webp
assets/produtos/acai-grande-550-320.webp
assets/hero/home-acai-mobile-900.webp
assets/logos/logo-horizontal.svg
```

6. **Implementar com HTML correto**
   - `alt`;
   - `width`;
   - `height`;
   - `loading`;
   - `decoding`;
   - `srcset` quando necessário.

7. **Testar**
   - mobile;
   - rede fraca;
   - Lighthouse;
   - DevTools Network.

8. **Monitorar**
   - peso total;
   - LCP;
   - CLS;
   - erros.

---

## Estrutura recomendada de pastas

```text
assets/
  logos/
    logo-horizontal.svg
    logo-vertical.svg
    logo-watermark.svg

  icons/
    interface/
    sociais/
    pagamentos/

  produtos/
    pequeno-200/
    medio-330/
    grande-550/
    gigante-770/
    marmitao-1l/
    barca-premium/
    especiais/

  backgrounds/
    home/
    cardapio/
    secoes/
    textura/

  efeitos/
    brilho/
    gotas/
    folhas/
    particulas/
    splash-acai/

  personagens/
    casal/
    menina/
    rapaz/
    entregador/

  delivery/
    moto/
    mochila/
    caixa/

  video/
    posters/
    loops/
```

---

## Nomenclatura obrigatória

Use nomes previsíveis e sem caracteres especiais.

Correto:

```text
acai-grande-550-640.webp
barca-premium-card-480.webp
logo-horizontal-roxa.svg
background-home-mobile-900.webp
splash-acai-01.webp
```

Errado:

```text
Imagem linda final NOVA.png
açaí grande (1).jpg
Design sem título 999.png
fotozapzapfinal.png
```

---

## Auditoria rápida para IA de programação

Ao revisar o projeto, responda sempre nesta estrutura:

```text
## Auditoria de Performance e Assets

### 1. Problemas críticos
- ...

### 2. Problemas médios
- ...

### 3. Melhorias rápidas
- ...

### 4. Arquivos que precisam mudar
- ...

### 5. Plano de correção em etapas
1. ...
2. ...
3. ...

### 6. Checklist final
- [ ] ...
```

---

## Prompt interno para revisão de código

Quando esta skill for usada para auditar o projeto, siga este comando mental:

```text
Revise o projeto com foco em performance e assets.
Identifique imagens pesadas, formatos ruins, falta de lazy loading,
ausência de width/height, CSS duplicado, JS bloqueante, fontes pesadas,
animações custosas, overflow horizontal, impacto em Core Web Vitals,
problemas mobile e pontos que reduzem conversão para WhatsApp.
Depois proponha correções objetivas, por arquivo, sem alterar a identidade visual.
```

---

## Prompt para correção incremental

Use este padrão quando for pedir implementação para uma IA de código:

```text
Aplique a skill performance-assets no projeto.

Objetivo:
Otimizar performance e assets sem destruir o visual premium do cardápio.

Regras:
- Preserve identidade visual roxa/violeta da marca.
- Não remova funcionalidades de pedido.
- Não quebre o fluxo para WhatsApp.
- Priorize mobile.
- Corrija imagens, lazy loading, dimensões, CSS/JS pesado e overflow.
- Faça alterações pequenas e verificáveis.
- Liste todos os arquivos modificados.
- Explique o motivo técnico de cada mudança.
- Ao final, entregue checklist de teste mobile.
```

---

## Regras de ouro

1. **Mobile primeiro.**
2. **Cada KB importa.**
3. **Imagem otimizada converte mais.**
4. **Animação deve encantar, nunca travar.**
5. **Velocidade também vende.**
6. **O CTA precisa aparecer rápido.**
7. **O cardápio precisa abrir sem atrito.**
8. **O WhatsApp precisa receber um pedido claro.**
9. **Bonito, leve e funcional é melhor que bonito e lento.**
10. **Performance não é detalhe; é parte da venda.**

---

## Critério de sucesso da skill

A implementação está correta quando:

- o cardápio abre rápido no celular;
- a primeira tela aparece sem travar;
- as imagens são bonitas, mas leves;
- não há pulos visuais;
- o scroll é suave;
- os botões respondem rápido;
- o CTA do WhatsApp está sempre claro;
- a mensagem do pedido sai organizada;
- o Lighthouse mobile melhora;
- o usuário consegue pedir sem esperar;
- o visual premium continua preservado.
