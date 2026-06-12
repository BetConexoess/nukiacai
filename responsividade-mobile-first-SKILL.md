# Skill: Responsividade Mobile-First para QR Code e WhatsApp

## Objetivo

Criar, revisar e corrigir interfaces web pensando primeiro no celular, especialmente quando a maioria dos acessos vem de **QR code**, **WhatsApp**, cardápio digital, landing page, link em bio ou navegador mobile.

Esta skill deve garantir que a página funcione bem em tela pequena, rede móvel instável, toque com dedo, teclado virtual, navegador embutido do WhatsApp/Instagram e dispositivos Android/iPhone reais.

Use esta skill sempre que o projeto envolver:

- landing page acessada por QR code;
- cardápio digital;
- botão de pedido pelo WhatsApp;
- página de produto ou vitrine mobile;
- fluxo rápido de conversão;
- revisão de HTML, CSS ou JavaScript para responsividade;
- layout que precisa funcionar primeiro no celular e só depois no desktop.

---

## Princípio central

**Mobile-first não é “fazer caber no celular depois”.**

Mobile-first significa:

1. A versão base do CSS é feita para celular.
2. O layout começa em uma coluna.
3. O conteúdo principal aparece rápido.
4. O botão principal fica fácil de tocar.
5. O site continua útil mesmo em rede ruim.
6. Desktop é uma expansão, não a base.

Sempre construir primeiro para telas entre **320px e 430px** de largura.

---

## Regras obrigatórias

### 1. CSS base deve ser mobile

Nunca criar o layout base pensando em desktop para depois “consertar” no celular.

Correto:

```css
.cardapio-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

@media (min-width: 768px) {
  .cardapio-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .cardapio-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
```

Errado:

```css
.cardapio-grid {
  grid-template-columns: repeat(4, 1fr);
}

@media (max-width: 768px) {
  .cardapio-grid {
    grid-template-columns: 1fr;
  }
}
```

---

### 2. Usar `min-width`, não `max-width`, como padrão

Media queries devem crescer junto com a tela.

Preferir:

```css
@media (min-width: 600px) {}
@media (min-width: 768px) {}
@media (min-width: 1024px) {}
```

Evitar basear toda a responsividade em:

```css
@media (max-width: 768px) {}
```

`max-width` só deve ser usado para correções pontuais, não como arquitetura principal.

---

### 3. Nunca depender apenas de hover

Celular não tem hover real. Todo efeito importante precisa funcionar com toque, foco e estado ativo.

Use:

```css
.button:hover,
.button:focus-visible,
.button:active {
  transform: translateY(-1px);
}
```

Não esconda informações essenciais atrás de `:hover`.

---

### 4. Área de toque mínima

Botões, cards clicáveis, ícones e links importantes devem ter no mínimo:

```css
min-height: 44px;
min-width: 44px;
```

Preferência para CTA principal:

```css
min-height: 48px;
```

---

### 5. Evitar texto e botão pequenos

Base recomendada:

```css
body {
  font-size: 16px;
  line-height: 1.5;
}
```

Texto secundário não deve ficar menor que `0.875rem` sem motivo forte.

---

### 6. Nada deve vazar horizontalmente

A página não pode criar rolagem lateral no celular.

Regra global recomendada:

```css
*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  width: 100%;
  max-width: 100%;
  overflow-x: hidden;
}

img,
svg,
video,
canvas {
  max-width: 100%;
  height: auto;
}
```

Durante revisão, procurar causas comuns de overflow:

- `width: 100vw` dentro de elementos com padding;
- imagens sem `max-width: 100%`;
- grids com colunas fixas;
- cards com `min-width` exagerado;
- elementos absolutos saindo da tela;
- animações com `translateX` sem limite;
- textos longos sem quebra.

---

### 7. Cuidado com `100vh`

Em celular, a barra do navegador e o teclado virtual alteram a altura disponível.

Preferir:

```css
.hero {
  min-height: 100dvh;
}
```

Fallback:

```css
.hero {
  min-height: 100vh;
  min-height: 100dvh;
}
```

---

### 8. Respeitar notch e safe area

Quando houver barra fixa embaixo ou layout full-screen, usar `env(safe-area-inset-*)`.

```css
.mobile-order-bar {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 0.75rem 1rem;
  padding-bottom: max(0.75rem, env(safe-area-inset-bottom));
}
```

---

### 9. CTA principal deve ser óbvia no mobile

Para QR code e WhatsApp, o usuário precisa entender rapidamente o que fazer.

Regras:

- uma ação principal por tela;
- botão grande;
- texto direto;
- evitar excesso de botões competindo;
- em cardápio, botão de pedido deve estar sempre fácil de acessar;
- em landing page, CTA deve aparecer antes do usuário precisar pensar demais.

Exemplo:

```html
<a class="primary-cta" href="https://wa.me/5500000000000?text=Ol%C3%A1%2C%20quero%20fazer%20um%20pedido">
  Pedir pelo WhatsApp
</a>
```

---

### 10. URLs de QR e WhatsApp não devem carregar dados sensíveis

Nunca colocar CPF, telefone do cliente, endereço, token permanente ou dados privados na URL.

Correto:

```text
/cardapio?src=qr&campaign=cartao-fisico
```

Aceitável com backend seguro:

```text
/pedido?t=abc123temporario
```

Errado:

```text
/pedido?cliente=Joao&telefone=11999999999&endereco=Rua...
```

---

## Estrutura recomendada de layout mobile

### Página de entrada

Ordem ideal:

1. Logo ou identificação da marca.
2. Frase curta de valor.
3. Produto/oferta principal.
4. CTA principal.
5. Prova visual ou social.
6. Cardápio/benefícios.
7. CTA repetida.
8. Informações finais.

### Cardápio mobile

Ordem ideal:

1. Cabeçalho compacto.
2. Categorias com rolagem horizontal controlada.
3. Cards verticais de produto.
4. Imagem otimizada.
5. Nome do produto.
6. Preço/descrição curta.
7. Botão “Adicionar” ou “Pedir”.
8. Barra fixa inferior com resumo/WhatsApp.

---

## Breakpoints recomendados

Não usar breakpoints aleatórios. Começar com poucos.

```css
:root {
  --bp-xs: 360px;
  --bp-sm: 430px;
  --bp-md: 600px;
  --bp-lg: 768px;
  --bp-xl: 1024px;
  --bp-2xl: 1280px;
}
```

Uso prático:

```css
/* base: 320px até 599px */
.section {
  padding: 1rem;
}

/* celular grande / tablet pequeno */
@media (min-width: 600px) {
  .section {
    padding: 1.5rem;
  }
}

/* tablet */
@media (min-width: 768px) {
  .section {
    padding: 2rem;
  }
}

/* desktop */
@media (min-width: 1024px) {
  .section {
    padding: 3rem;
  }
}
```

---

## Tipografia responsiva

Usar `clamp()` para títulos e textos importantes.

```css
h1 {
  font-size: clamp(2rem, 10vw, 4.5rem);
  line-height: 0.95;
}

h2 {
  font-size: clamp(1.5rem, 6vw, 3rem);
  line-height: 1.05;
}

p {
  font-size: clamp(1rem, 3vw, 1.125rem);
}
```

Evitar títulos enormes que quebram a tela ou empurram o CTA para longe.

---

## Espaçamento responsivo

Criar tokens de espaçamento.

```css
:root {
  --space-xs: 0.5rem;
  --space-sm: 0.75rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;
}
```

Usar `clamp()` em seções:

```css
.section {
  padding-block: clamp(2rem, 8vw, 5rem);
  padding-inline: clamp(1rem, 4vw, 2rem);
}
```

---

## Containers

Nunca deixar conteúdo grudado na borda.

```css
.container {
  width: min(100% - 2rem, 1120px);
  margin-inline: auto;
}
```

Para páginas muito focadas em celular:

```css
.mobile-shell {
  width: min(100%, 430px);
  margin-inline: auto;
}
```

---

## Imagens responsivas

Toda imagem importante deve ter:

- `width` e `height` definidos;
- `alt` correto;
- formato leve quando possível: AVIF/WebP;
- versões menores para mobile;
- `loading="lazy"` quando estiver abaixo da dobra;
- `fetchpriority="high"` só na imagem principal acima da dobra.

Exemplo:

```html
<picture>
  <source
    type="image/avif"
    srcset="/img/produto-320.avif 320w, /img/produto-640.avif 640w"
    sizes="(max-width: 600px) 90vw, 320px"
  />
  <source
    type="image/webp"
    srcset="/img/produto-320.webp 320w, /img/produto-640.webp 640w"
    sizes="(max-width: 600px) 90vw, 320px"
  />
  <img
    src="/img/produto-640.png"
    alt="Copo de açaí com frutas"
    width="640"
    height="640"
    loading="lazy"
    decoding="async"
  />
</picture>
```

---

## Formulários mobile

Todo input deve facilitar o teclado correto.

Telefone:

```html
<input
  type="tel"
  inputmode="tel"
  autocomplete="tel"
  enterkeyhint="next"
/>
```

Nome:

```html
<input
  type="text"
  autocomplete="name"
  enterkeyhint="next"
/>
```

E-mail:

```html
<input
  type="email"
  inputmode="email"
  autocomplete="email"
  enterkeyhint="next"
/>
```

Número:

```html
<input
  type="text"
  inputmode="numeric"
  enterkeyhint="done"
/>
```

Regras:

- label visível, não apenas placeholder;
- erro perto do campo;
- teclado não pode esconder o botão final;
- evitar formulários longos;
- dividir em etapas quando necessário;
- não pedir dados antes de explicar valor.

---

## WhatsApp mobile-first

### Link oficial simples

```html
<a
  class="whatsapp-button"
  href="https://wa.me/5500000000000?text=Ol%C3%A1%2C%20quero%20fazer%20um%20pedido"
>
  Pedir pelo WhatsApp
</a>
```

### Função JavaScript

```js
function abrirWhatsApp(numero, mensagem) {
  const telefone = String(numero).replace(/\D/g, "");
  const texto = encodeURIComponent(mensagem);
  window.location.href = `https://wa.me/${telefone}?text=${texto}`;
}
```

### Boas práticas

- Normalizar número com DDI e DDD.
- Pré-preencher mensagem curta.
- Não abrir mil popups.
- Não depender de `window.open` em webview.
- Preferir `location.href` ou link direto.
- Manter CTA visível.
- Se o usuário volta do WhatsApp, preservar estado da página.

---

## QR code mobile-first

### Parâmetros úteis

```text
/cardapio?src=qr&campaign=cartao-fisico
/cardapio?src=qr&campaign=balcao
/cardapio?src=qr&campaign=mesa-01
```

### Captura simples de origem

```js
const params = new URLSearchParams(window.location.search);
const src = params.get("src") || "direct";
const campaign = params.get("campaign") || "default";

sessionStorage.setItem("entry_src", src);
sessionStorage.setItem("entry_campaign", campaign);
```

### Regras

- QR deve abrir uma página leve.
- A primeira tela precisa carregar rápido.
- Não exigir cadastro logo de cara.
- Não esconder o botão de ação.
- Se tiver campanha, medir origem.
- Não colocar dados sensíveis na URL.

---

## Performance obrigatória

Metas mínimas para páginas de entrada:

| Métrica | Meta |
|---|---:|
| LCP | até 2.5s |
| INP | até 200ms |
| CLS | até 0.1 |
| JS inicial gzip | idealmente até 150KB |
| CSS crítico gzip | idealmente até 25KB |
| Imagens acima da dobra | idealmente até 120KB totais |

Regras:

- Não carregar biblioteca pesada sem necessidade.
- Não animar tudo ao mesmo tempo.
- Não usar imagens gigantes no mobile.
- Não bloquear renderização com scripts grandes.
- Usar `defer` em scripts não críticos.
- Carregar imagens abaixo da dobra com lazy load.
- Reduzir fontes externas.
- Evitar carrosséis pesados na primeira tela.

---

## Animações mobile

Animações devem melhorar a experiência, não travar o celular.

Regras:

- animar preferencialmente `transform` e `opacity`;
- evitar animar `width`, `height`, `top`, `left`, `box-shadow` pesado;
- reduzir animações em aparelhos fracos;
- respeitar `prefers-reduced-motion`;
- pausar animações fora da tela;
- não deixar animação impedir clique;
- não usar partículas demais no mobile.

Exemplo:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
  }
}
```

---

## Acessibilidade mobile

Checklist obrigatório:

- `html lang="pt-BR"`;
- botões reais com `<button>` quando houver ação;
- links reais com `<a>` quando houver navegação;
- foco visível;
- contraste suficiente;
- textos legíveis;
- botões grandes;
- sem ação dependente só de hover;
- imagens com `alt`;
- campos com `label`;
- mensagens de erro claras;
- navegação possível por teclado;
- evitar CAPTCHA difícil;
- não impedir copiar/colar em campos importantes.

---

## Segurança e privacidade

Regras básicas:

- HTTPS obrigatório.
- Não colocar dados pessoais em URL.
- Não colocar token permanente em QR code.
- Usar token curto e expirável quando necessário.
- Evitar dados sensíveis no `localStorage`.
- Usar cookies seguros quando houver sessão.
- Cuidar com analytics capturando parâmetros privados.

Cookies de sessão, quando usados pelo backend:

```http
Set-Cookie: session=...; HttpOnly; Secure; SameSite=Lax; Path=/
```

---

## Padrão visual para mobile

Para landing/cardápio premium:

- fundo com boa profundidade, mas leve;
- contraste alto entre texto e fundo;
- CTA com cor dominante;
- cards com sombra moderada;
- bordas arredondadas consistentes;
- imagens otimizadas;
- espaço suficiente entre botões;
- hierarquia clara: título, descrição, preço, ação;
- barra inferior fixa apenas quando realmente ajuda.

---

## Checklist de revisão em arquivos existentes

Quando revisar um projeto, verificar nesta ordem:

1. Existe `<meta name="viewport" content="width=device-width, initial-scale=1">`?
2. O CSS base é mobile-first?
3. Há rolagem lateral indesejada?
4. Imagens têm `max-width: 100%`?
5. Grids começam com uma coluna?
6. Botões têm área mínima de toque?
7. CTA principal aparece rápido no celular?
8. O teclado virtual quebra o layout?
9. Barra inferior respeita safe area?
10. Textos estão legíveis em 320px?
11. Cards cabem em 360px?
12. WhatsApp abre com link correto?
13. QR code usa URL curta e sem dados sensíveis?
14. Imagens estão leves?
15. Animações usam `transform`/`opacity`?
16. Existe suporte a `prefers-reduced-motion`?
17. O layout funciona em 320, 360, 390, 430, 768 e 1024px?
18. A página funciona sem hover?
19. A página continua utilizável se JS demorar?
20. O fluxo está claro para usuário vindo de QR/WhatsApp?

---

## Checklist de teste manual

Testar no navegador com estas larguras:

- 320px
- 360px
- 375px
- 390px
- 414px
- 430px
- 768px
- 1024px

Testar cenários:

- abrir por link normal;
- abrir por QR code real;
- abrir pelo WhatsApp;
- abrir no navegador embutido;
- girar tela;
- abrir teclado em formulário;
- tocar nos botões com uma mão;
- usar rede lenta no DevTools;
- voltar do WhatsApp para a página;
- testar Android e iPhone se possível.

---

## Padrão de resposta da IA ao aplicar esta skill

Quando a IA usar esta skill, ela deve responder com:

1. **Diagnóstico mobile-first**
   - O que está certo.
   - O que está quebrando no celular.
   - Prioridade dos problemas.

2. **Correções feitas ou propostas**
   - Arquivos alterados.
   - Seletores ajustados.
   - Motivo técnico.

3. **Checklist final**
   - 320px OK ou não.
   - WhatsApp OK ou não.
   - QR flow OK ou não.
   - CTA mobile OK ou não.
   - Performance OK ou não.

4. **Próximo passo recomendado**
   - Apenas uma próxima ação clara.

---

## Prompt pronto para usar no Codex ou Claude Code

Use este prompt quando quiser que a IA aplique a skill no projeto:

```text
Você deve atuar usando a skill “Responsividade Mobile-First para QR Code e WhatsApp”.

Contexto: este projeto será acessado principalmente por celular, via QR code, WhatsApp e navegador mobile. A versão mobile é a versão principal. Desktop é apenas expansão.

Sua tarefa:
1. Analise os arquivos HTML, CSS e JavaScript do projeto.
2. Verifique se a estrutura é realmente mobile-first.
3. Corrija problemas de responsividade, overflow horizontal, botões pequenos, imagens grandes, grids desktop-first, uso ruim de 100vh, barra fixa sem safe-area, textos ilegíveis e CTAs difíceis de tocar.
4. Preserve o design visual existente sempre que possível.
5. Não redesenhe tudo sem necessidade.
6. Não remova animações boas, apenas otimize para mobile.
7. Garanta que o layout funcione bem em 320px, 360px, 390px, 430px, 768px e 1024px.
8. Garanta que o botão de WhatsApp fique funcional e fácil de acessar.
9. Se encontrar problemas grandes, corrija por prioridade: primeiro usabilidade mobile, depois performance, depois refinamento visual.

Regras obrigatórias:
- CSS base deve ser mobile-first.
- Usar media queries com min-width como padrão.
- Evitar hover como única interação.
- Botões importantes com no mínimo 44px/48px de altura.
- Não permitir rolagem horizontal.
- Usar safe-area em barras fixas inferiores.
- Usar 100dvh quando necessário.
- Imagens devem ser responsivas.
- Formulários devem usar inputmode, autocomplete e enterkeyhint quando aplicável.
- Não colocar dados sensíveis em URLs de QR ou WhatsApp.

Ao finalizar, entregue:
- resumo do que foi alterado;
- arquivos modificados;
- problemas encontrados;
- checklist mobile final;
- próximos ajustes recomendados.
```

---

## Critério de pronto

A skill só considera a responsividade pronta quando:

- não existe overflow horizontal;
- a primeira tela funciona em 320px;
- o CTA principal é visível e tocável;
- o usuário consegue pedir/continuar pelo WhatsApp;
- imagens não quebram o layout;
- grids se adaptam sem esmagar cards;
- textos são legíveis;
- a barra inferior não cobre conteúdo importante;
- o teclado virtual não destrói o formulário;
- animações não travam a navegação;
- desktop continua bom como expansão;
- o fluxo via QR/WhatsApp é claro e rápido.
