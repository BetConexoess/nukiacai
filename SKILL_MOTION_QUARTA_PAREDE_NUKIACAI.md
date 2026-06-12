# SKILL — Motion Design e Microinterações Nu Ki Açaí

## Nome da Skill

`SKILL_MOTION_QUARTA_PAREDE_NUKIACAI.md`

## Objetivo

Esta skill orienta agentes de IA, designers e desenvolvedores a criarem **motion design**, animações e microinterações para a landing page da **Nu Ki Açaí**.

A página deve parecer:

* Viva.
* Premium.
* Responsiva.
* Apetitosa.
* Divertida.
* Fluida.
* Leve.
* Memorável.
* Consciente da presença do visitante.

A regra central:

**O movimento deve fazer o site parecer vivo, sem deixar o site pesado.**

A quebra da 4ª parede é obrigatória, mas deve acontecer de forma visual, sutil e estratégica. A interface pode reagir ao visitante, apontar caminhos, brincar com o clique e fazer o produto “se exibir”, mas nunca pode atrapalhar leitura, compra, preço, CTA ou WhatsApp.

---

# 1. Princípio Supremo

A ordem de prioridade do motion da Nu Ki Açaí é:

```txt
1. Clareza do produto
2. Clareza do CTA
3. Feedback da ação
4. Sensação premium
5. Quebra da 4ª parede
6. Encanto visual
7. Decoração
```

Nunca animar apenas porque “fica bonito”.

Toda animação precisa responder pelo menos uma pergunta:

```txt
O que acabou de acontecer?
Onde devo olhar?
O que posso clicar?
Qual item foi escolhido?
Qual é o próximo passo?
A página percebeu minha ação?
```

Se a animação não ajuda em nada disso, ela deve ser removida ou reduzida.

---

# 2. Personalidade do Motion Nu Ki Açaí

O motion da marca deve parecer:

```txt
Roxo, cremoso, elástico, apetitoso, suave, vivo e premium.
```

A sensação não deve ser mecânica.
Deve parecer que o site tem corpo, sabor e presença.

## Palavras que definem o movimento

```txt
Cremoso
Maciez
Brilho
Respiração
Flutuação leve
Entrada suave
Reação rápida
Toque elástico
Produto vivo
Personagem atento
```

## Palavras que NÃO definem o movimento

```txt
Caótico
Pesado
Piscando
Nervoso
Infantil
Aleatório
Travado
Exagerado
Barulhento
Cansativo
```

O site não deve parecer um parque de diversões.
Deve parecer uma vitrine premium que sabe brincar.

---

# 3. Quebra da 4ª Parede no Motion

Neste projeto, quebrar a 4ª parede com motion significa:

```txt
A página reage visualmente à presença, rolagem, clique, pausa ou escolha do visitante.
```

Exemplos:

* O personagem olha para o botão depois que o Hero termina de entrar.
* Um card dá uma leve levantada quando o visitante para nele.
* Um topping cai perto do produto em destaque.
* O botão WhatsApp “respira” quando aparece na tela.
* Um selo “mais pedido” surge como se estivesse chamando atenção.
* O personagem aponta discretamente para o CTA.
* O produto selecionado dá um microbalanço como se tivesse gostado da escolha.
* O cardápio revela os cards como se estivesse montando uma vitrine para o visitante.

## Regra

A quebra da 4ª parede deve parecer:

```txt
“Eu percebi você.”
```

Mas nunca:

```txt
“Eu estou te vigiando.”
```

---

# 4. Intensidade do Motion

Toda animação deve ser classificada em um dos níveis abaixo.

## Nível 1 — Funcional

Serve para confirmar ação ou orientar.

Usar em:

```txt
Botões
Cards
Filtros
WhatsApp
Formulários
Estados de sucesso
Estados de erro
```

Exemplo:

```txt
Botão afunda levemente ao clicar.
Card selecionado recebe borda e brilho.
Filtro ativo desliza suavemente.
```

## Nível 2 — Premium

Serve para dar acabamento visual.

Usar em:

```txt
Hero
Cards destacados
Combos
Produtos premium
Selos
Transições entre seções
```

Exemplo:

```txt
Produto entra com fade + leve subida.
Glow violeta aparece atrás do bowl.
Card levanta no hover.
```

## Nível 3 — Quarta parede

Serve para fazer a página parecer viva.

Usar em:

```txt
Personagem
CTA principal
Produto em destaque
Card parado em viewport
Seção de WhatsApp
Momento de escolha
```

Exemplo:

```txt
Personagem olha para o CTA.
Produto balança quando o usuário adiciona ao pedido.
Botão responde com microcopy visual.
```

## Nível 4 — Cinemático

Usar raramente.

Só em:

```txt
Primeira entrada do Hero
Abertura especial
Campanha promocional
Momento de destaque premium
```

Exemplo:

```txt
Bowl aparece em camadas com frutas, brilho e texto.
```

Não usar motion cinematográfico em todas as seções.

---

# 5. Durações Recomendadas

Usar durações curtas e naturais.

```txt
Feedback instantâneo: 80ms a 140ms
Hover e botão: 140ms a 220ms
Card e chip: 180ms a 280ms
Reveal de seção: 280ms a 520ms
Hero principal: 500ms a 900ms
Loop ambiente: 2400ms a 6000ms
```

## Regras

```txt
Botão precisa responder rápido.
Card pode ser um pouco mais suave.
Hero pode ser mais dramático.
Loop deve ser lento e discreto.
Erro não deve ter animação divertida.
WhatsApp deve parecer rápido e confiável.
```

## Evitar

```txt
Animações abaixo de 80ms que parecem corte seco.
Animações acima de 1000ms em ações comuns.
Loops rápidos que cansam.
Vários elementos entrando ao mesmo tempo.
```

---

# 6. Curvas de Movimento / Easing

Usar easing para deixar o movimento natural.

## Padrões recomendados

```css
--ease-standard: cubic-bezier(.2, .8, .2, 1);
--ease-soft: cubic-bezier(.4, 0, .2, 1);
--ease-out: cubic-bezier(0, 0, .2, 1);
--ease-in: cubic-bezier(.4, 0, 1, 1);
--ease-spring-soft: cubic-bezier(.18, .89, .32, 1.12);
```

## Quando usar

### `ease-out`

Usar quando algo aparece ou responde ao usuário.

```txt
Card entrando
Botão levantando
Produto aparecendo
Tooltip surgindo
```

### `ease-in`

Usar quando algo sai.

```txt
Tooltip desaparecendo
Modal fechando
Mensagem sumindo
```

### `ease-standard`

Usar para transições gerais.

```txt
Filtro
Cards
Seções
Menu mobile
```

### `spring-soft`

Usar com cuidado para dar sensação de toque.

```txt
Botão pressionado
Produto selecionado
Selo aparecendo
Microcelebração
```

Não usar spring exagerado em textos longos, layout inteiro ou seções grandes.

---

# 7. Propriedades Permitidas e Proibidas

Para performance, priorizar:

```css
transform
opacity
```

Essas propriedades geralmente são mais seguras para animação.

## Pode animar

```txt
transform: translate
transform: scale
transform: rotate
opacity
background-color em elementos pequenos
box-shadow com moderação
filter apenas em elementos pequenos
```

## Evitar animar

```txt
width
height
top
left
right
bottom
margin
padding
border-width
font-size
large blur
large backdrop-filter
background-position em área grande
```

## Regra

Se a animação muda o tamanho real do layout, provavelmente é perigosa.

Preferir:

```css
transform: translateY(12px);
```

Em vez de:

```css
top: 12px;
```

---

# 8. Tokens Globais de Motion

Todo projeto deve usar tokens.
Não espalhar números aleatórios no CSS.

```css
:root {
  --motion-duration-instant: 100ms;
  --motion-duration-fast: 160ms;
  --motion-duration-base: 260ms;
  --motion-duration-slow: 480ms;
  --motion-duration-hero: 760ms;
  --motion-duration-loop: 3600ms;

  --motion-ease-standard: cubic-bezier(.2, .8, .2, 1);
  --motion-ease-soft: cubic-bezier(.4, 0, .2, 1);
  --motion-ease-out: cubic-bezier(0, 0, .2, 1);
  --motion-ease-spring-soft: cubic-bezier(.18, .89, .32, 1.12);

  --motion-distance-xs: 3px;
  --motion-distance-sm: 6px;
  --motion-distance-md: 14px;
  --motion-distance-lg: 28px;

  --motion-scale-hover: 1.015;
  --motion-scale-press: .975;
  --motion-scale-selected: 1.025;
}
```

Todos os componentes devem usar esses tokens.

---

# 9. Arquivos Recomendados

Organizar motion assim:

```txt
css/
├─ animacoes.css
├─ base.css
├─ layout.css
└─ cardapio.css

js/
├─ animacoes.js
└─ app.js
```

## `animacoes.css`

Deve conter:

```txt
tokens de motion
keyframes
classes reutilizáveis
prefers-reduced-motion
hover states
reveal states
loops leves
microinterações visuais
```

## `animacoes.js`

Deve conter:

```txt
IntersectionObserver
controle de reveal
detecção de reduced motion
efeitos de cursor apenas desktop
ativação de estados
microinterações progressivas
```

---

# 10. Classes Padrão

Usar nomes consistentes.

```txt
.motion-reveal
.motion-fade
.motion-lift
.motion-press
.motion-breath
.motion-float
.motion-glow
.motion-splash
.motion-character
.motion-product
.motion-card
.motion-cta
.motion-whatsapp
```

## Estados

```txt
.is-visible
.is-active
.is-selected
.is-pressed
.is-loading
.is-success
.is-error
.is-idle
.is-reduced
```

## Atributos

```html
data-reveal
data-motion="hero"
data-motion="card"
data-motion="cta"
data-motion="character"
data-motion="ambient"
```

---

# 11. Sistema de Reveal

Usar reveal para entrada de seções e cards.

## Regra

O conteúdo deve existir e ser legível mesmo sem JavaScript.

CSS base:

```css
.motion-reveal {
  opacity: 1;
  transform: none;
}

.js .motion-reveal {
  opacity: 0;
  transform: translateY(var(--motion-distance-md));
  transition:
    opacity var(--motion-duration-base) var(--motion-ease-out),
    transform var(--motion-duration-base) var(--motion-ease-standard);
}

.js .motion-reveal.is-visible {
  opacity: 1;
  transform: none;
}
```

JS:

```js
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealItems = document.querySelectorAll('[data-reveal]');

if (!prefersReducedMotion && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      obs.unobserve(entry.target);
    });
  }, {
    threshold: 0.16,
    rootMargin: '0px 0px -8% 0px'
  });

  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add('is-visible'));
}
```

---

# 12. Hero Motion

O Hero é a cena principal.

Ele deve ter entrada em camadas:

```txt
1. Fundo roxo/glow aparece
2. Headline entra
3. Subheadline entra
4. Produto entra
5. Frutas/toppings entram
6. CTA aparece
7. Personagem reage ao CTA
```

## Exemplo de intenção

```txt
A página abriu.
O açaí percebeu.
O produto se apresentou.
O personagem apontou o caminho.
```

## Regras

```txt
Hero não pode demorar para mostrar CTA.
Headline precisa aparecer rápido.
Produto pode ter movimento mais premium.
Personagem entra depois, não antes.
Frutas não podem distrair do CTA.
```

## Durações

```txt
Headline: 400ms a 600ms
Produto: 600ms a 900ms
CTA: 300ms a 500ms
Personagem: 500ms a 800ms
Frutas: 600ms a 1000ms
```

## Movimento recomendado

```txt
Headline: fade + translateY leve
Produto: fade + scale 0.96 para 1
Frutas: fade + translateY ou rotate pequeno
CTA: fade + lift
Personagem: fade + olhar/apontar
```

Evitar entrada com rotação exagerada.

---

# 13. Produto Vivo

Produtos devem parecer apetitosos e presentes.

## Microinterações permitidas

```txt
Leve flutuação
Glow atrás do produto
Brilho suave
Entrada com escala
Balanço leve ao selecionar
Partícula discreta
```

## Exemplo

```css
.product-float {
  animation: productFloat 4200ms ease-in-out infinite;
}

@keyframes productFloat {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-6px) rotate(-0.6deg);
  }
}
```

## Regra

No máximo um produto com loop forte por tela.

Se todos os produtos se mexerem, nenhum parece especial.

---

# 14. Cards de Produto

Card precisa parecer clicável.

## Estado normal

```txt
Card parado
Produto em destaque
Sombra premium
Preço claro
CTA claro
```

## Hover desktop

```txt
Card sobe 4px a 8px
Glow aparece
Produto aumenta 1% a 2%
Selo fica mais visível
```

## Active / clique

```txt
Card comprime levemente
CTA responde rápido
Produto dá microbalanço
```

## Selecionado

```txt
Borda violeta
Glow controlado
Selo ou check aparece
Mensagem curta opcional
```

CSS base:

```css
.card-produto {
  transition:
    transform var(--motion-duration-fast) var(--motion-ease-out),
    box-shadow var(--motion-duration-fast) var(--motion-ease-out),
    border-color var(--motion-duration-fast) var(--motion-ease-out);
}

@media (hover: hover) and (pointer: fine) {
  .card-produto:hover {
    transform: translateY(-6px) scale(1.01);
  }

  .card-produto:hover .produto-img {
    transform: scale(1.025) rotate(-0.5deg);
  }
}

.card-produto:active {
  transform: scale(.985);
}

.card-produto.is-selected {
  transform: scale(1.015);
}
```

---

# 15. Botões

Botão é ponto de conversão.
Ele deve responder imediatamente.

## Estado hover

```txt
Leve elevação
Glow violeta
Brilho na borda
```

## Estado active

```txt
Compressão rápida
Sombra reduzida
Sensação de toque
```

## Estado foco

```txt
Outline claro e visível
Sem depender apenas de cor
```

CSS:

```css
.button {
  transition:
    transform var(--motion-duration-fast) var(--motion-ease-out),
    box-shadow var(--motion-duration-fast) var(--motion-ease-out),
    background-color var(--motion-duration-fast) var(--motion-ease-out);
}

@media (hover: hover) and (pointer: fine) {
  .button:hover {
    transform: translateY(-3px);
  }
}

.button:active {
  transform: scale(var(--motion-scale-press));
}

.button:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}
```

## Regra

Botão não pode sair do lugar demais.

O usuário precisa sentir toque, não perseguição.

---

# 16. CTA WhatsApp

O botão de WhatsApp é o principal canal comercial.

Ele deve ser:

```txt
Visível
Rápido
Confiável
Clicável
Chamativo sem ser desesperado
```

## Motion recomendado

```txt
Respiração discreta
Hover com lift
Active com compressão
Confirmação textual
Glow suave
```

## Não fazer

```txt
Botão pulando sem parar
Shake agressivo
Piscar verde
Sumir atrás de animação
Depender de JS para funcionar
```

## Regra

O CTA do WhatsApp deve funcionar como link puro, mesmo sem JavaScript.

```html
<a class="button button--whatsapp" href="https://wa.me/55NUMERO?text=MENSAGEM" target="_blank" rel="noopener">
  Pedir pelo WhatsApp
</a>
```

Motion é melhoria, não dependência.

---

# 17. Personagem e Quarta Parede

O personagem é anfitrião visual, não protagonista absoluto.

## O personagem pode

```txt
Olhar para o visitante
Apontar para CTA
Reagir a produto selecionado
Piscar raramente
Aparecer em momentos estratégicos
Comentar visualmente escolhas
Guiar o visitante
```

## O personagem não pode

```txt
Cobrir produto
Cobrir preço
Cobrir CTA
Falar demais
Se mover o tempo todo
Parecer propaganda invasiva
Atrapalhar leitura
```

## Frequência

```txt
Piscar: raro
Aceno: somente em momento especial
Apontar CTA: uma vez por seção
Reação a clique: curta
Loop idle: quase imperceptível
```

## Exemplos de gestos

```txt
Hero: personagem olha para o CTA.
Cardápio: personagem aponta para filtros.
Combos: personagem reage ao combo em destaque.
WhatsApp: personagem segura/indica o botão.
Rodapé: personagem faz despedida visual leve.
```

## Regra de ouro

O personagem deve parecer vivo, não carente.

---

# 18. Frutas, Toppings e Splash

Frutas e toppings são elementos de sabor.

## Usar para

```txt
Criar profundidade
Marcar seção
Destacar card
Celebrar seleção
Reforçar produto
```

## Não usar para

```txt
Tampar texto
Passar na frente do CTA
Cair o tempo inteiro
Virar chuva visual
Aumentar peso da página
```

## Movimento recomendado

```txt
Queda curta
Rotação leve
Fade rápido
Parallax mínimo
Entrada em diagonal
Splash discreto
```

## Regra

Cada fruta deve ter motivo.

Exemplo bom:

```txt
Morango cai perto do card de morango quando ele entra em destaque.
```

Exemplo ruim:

```txt
Morango caindo em todas as seções sem função.
```

---

# 19. Microinterações de Scroll

Scroll deve revelar a página como narrativa.

## Permitido

```txt
Fade-in de seção
Cards entrando em stagger
Produto subindo levemente
Glow aparecendo
Barra de progresso discreta
Personagem mudando pose em pontos específicos
```

## Evitar

```txt
Parallax forte
Texto preso demais
Seção travando scroll
Muitos elementos seguindo o mouse
Animação dependente de scroll em mobile fraco
```

## Stagger recomendado

```txt
Cards em grid: 40ms a 80ms entre itens
Seções grandes: 80ms a 140ms
Nunca passar de 500ms para aparecer tudo
```

Exemplo:

```css
.card-produto:nth-child(1) { transition-delay: 0ms; }
.card-produto:nth-child(2) { transition-delay: 60ms; }
.card-produto:nth-child(3) { transition-delay: 120ms; }
.card-produto:nth-child(4) { transition-delay: 180ms; }
```

---

# 20. Estados de Loading

Loading precisa parecer premium, mas não pode irritar.

## Usar

```txt
Skeleton suave
Pulse leve
Fade
Texto claro
```

## Evitar

```txt
Spinner genérico sozinho
Splash gigante
Loop muito rápido
Texto engraçado em carregamento crítico
```

## Frases possíveis

```txt
Montando o cardápio...
Chamando os toppings...
Preparando os destaques...
Organizando a vitrine roxa...
```

## Regra

Se carregar mais de poucos segundos, oferecer alternativa:

```txt
Falar com a loja pelo WhatsApp
Recarregar cardápio
```

---

# 21. Estados de Sucesso

Sucesso pode ter celebração leve.

## Exemplos

```txt
Produto adicionado
Pedido enviado para WhatsApp
Combo selecionado
Adicional escolhido
```

## Motion recomendado

```txt
Check aparece
Card brilha rápido
Botão comprime e volta
Selo surge
Microconfete mínimo
```

## Duração

```txt
200ms a 500ms
```

## Não fazer

```txt
Confete enorme
Som obrigatório
Animação longa
Bloquear tela
```

Mensagem visual deve ser anunciável:

```html
<p role="status" aria-atomic="true" class="sr-only" id="statusPedido"></p>
```

---

# 22. Estados de Erro

Erro não é lugar de brincadeira.

## Motion permitido

```txt
Borda vermelha/violeta de alerta
Ícone aparece
Mensagem entra com fade
Leve deslocamento de 2px se necessário
```

## Evitar

```txt
Shake forte
Piada
Emoji
Animação exagerada
Som
Personagem rindo
```

## Regra

Erro precisa dizer:

```txt
O que aconteceu
Como corrigir
```

Exemplo:

```txt
Não foi possível abrir o WhatsApp. Copie a mensagem e envie manualmente.
```

---

# 23. Acessibilidade de Motion

Sempre respeitar `prefers-reduced-motion`.

CSS obrigatório:

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

  .motion-loop,
  .motion-float,
  .motion-breath,
  .motion-splash {
    animation: none !important;
  }
}
```

Versão melhor para preservar elegância:

```css
@media (prefers-reduced-motion: reduce) {
  .motion-reveal {
    transform: none !important;
    opacity: 1 !important;
    transition: opacity 120ms linear !important;
  }

  .motion-loop,
  .motion-float,
  .motion-breath {
    animation: none !important;
  }
}
```

## Regra

Reduzir movimento não significa deixar feio.

Significa substituir deslocamento por:

```txt
Fade
Cor
Borda
Ícone
Texto
Estado estático bonito
```

---

# 24. Performance

O site precisa ser bonito e leve.

## Regras principais

```txt
Animar transform e opacity.
Evitar animações de layout.
Não usar muitos loops simultâneos.
Não usar vídeo/GIF pesado no Hero.
Não animar blur grande.
Não deixar will-change permanente em vários elementos.
Não usar JS para tudo.
Usar CSS primeiro.
Usar JS apenas para estado, viewport e interações especiais.
```

## `will-change`

Usar só quando necessário.

Errado:

```css
* {
  will-change: transform;
}
```

Certo:

```js
element.addEventListener('pointerenter', () => {
  element.style.willChange = 'transform';
});

element.addEventListener('pointerleave', () => {
  element.style.willChange = 'auto';
});
```

## Imagens

```txt
Hero principal: carregar cedo.
Imagens abaixo da dobra: lazy loading.
Sempre definir width e height.
Preferir WebP/AVIF.
Evitar PNG enorme.
```

---

# 25. Core Web Vitals

Motion não pode prejudicar:

```txt
LCP: carregamento do conteúdo principal
INP: resposta às interações
CLS: estabilidade visual
```

## Metas

```txt
LCP: até 2.5s
INP: até 200ms
CLS: até 0.1
```

## Regra prática

Se uma animação piora clique, leitura ou carregamento, ela deve sair.

O visitante veio pedir açaí, não assistir benchmark travando.

---

# 26. Motion por Seção

## Hero

```txt
Entrada premium
Produto em destaque
Personagem com reação curta
CTA sempre visível
```

## Cardápio

```txt
Cards revelam em sequência
Filtros respondem rápido
Produto selecionado brilha
Sem animação exagerada
```

## Produtos em destaque

```txt
Mais motion premium
Glow
Selo animado
Produto com leve flutuação
```

## Combos

```txt
Cards maiores
Seleção com feedback forte
Badge aparece
Preço muda com fade
```

## Delivery

```txt
Movimento funcional
Ícone ou personagem indicando entrega
CTA WhatsApp destacado
```

## Lojas

```txt
Motion mínimo
Clareza acima de encanto
Mapa/endereço não devem ser escondidos
```

## Rodapé

```txt
Pouco movimento
Despedida visual leve
Nada que distraia
```

---

# 27. Biblioteca de Microinterações

## Botão CTA

```txt
Hover: sobe 3px
Active: scale 0.975
Focus: outline claro
Success: brilho rápido
```

## Card de produto

```txt
Hover: sobe 6px
Imagem: scale 1.025
Selecionado: borda violeta + check
Adicionado: microbalanço
```

## Filtro

```txt
Ativo: pill desliza/realça
Clique: compressão curta
Mudança: cards fazem fade
```

## Produto

```txt
Idle: flutuação leve
Destaque: glow atrás
Seleção: bounce pequeno
```

## Personagem

```txt
Idle: piscada rara
CTA visível: olhar para botão
Produto selecionado: aceno curto
WhatsApp: aponta para botão
```

## WhatsApp

```txt
Idle: respiração discreta
Hover: lift + glow
Click: compressão
Status: texto para leitor de tela
```

## Empty state

```txt
Ícone aparece com fade
Mensagem entra sem deslocamento grande
CTA aparece logo abaixo
```

## Loading

```txt
Skeleton com pulse lento
Sem spinner agressivo
Sem piada em carregamento crítico
```

---

# 28. Padrões de Quarta Parede com Motion

## Padrão 1 — “O site percebeu que você chegou”

Usar no Hero.

```txt
Headline entra.
Produto aparece.
Personagem olha para o usuário.
CTA brilha levemente.
```

## Padrão 2 — “O card percebeu seu interesse”

Usar em card de produto.

```txt
Usuário passa mouse ou card entra no centro da tela.
Card sobe levemente.
Produto brilha.
Microcopy aparece.
```

## Padrão 3 — “O botão está esperando”

Usar em CTA.

```txt
CTA fica visível.
Depois de alguns segundos, respira uma vez.
Não repetir infinitamente de forma agressiva.
```

## Padrão 4 — “O combo se apresentou”

Usar em combos.

```txt
Combo destacado entra com selo.
Preço aparece com fade.
Imagem dá leve scale.
```

## Padrão 5 — “O personagem guia sem interromper”

Usar com personagem.

```txt
Personagem aparece pequeno.
Aponta para ação.
Depois volta ao estado parado.
```

---

# 29. Anti-padrões

Não fazer:

```txt
Animação em tudo.
Todos os cards flutuando ao mesmo tempo.
Hero pesado com vídeo grande.
CTA pulando sem parar.
Personagem falando/mexendo em toda seção.
Shake em erro.
Parallax forte no mobile.
Texto entrando letra por letra em tudo.
Scroll travado por animação.
Hover essencial que não existe no mobile.
Animação que depende de JS para mostrar conteúdo.
```

## Regra

Se o visitante nota a animação mais do que o produto, a animação falhou.

---

# 30. Snippet Base Completo

## HTML

```html
<section class="hero" data-motion="hero">
  <div class="hero__content motion-reveal" data-reveal>
    <p class="eyebrow">Nu Ki Açaí</p>
    <h1>Você chegou. O açaí percebeu.</h1>
    <p>Monte seu pedido com tamanhos, adicionais e combos. Depois envie tudo pelo WhatsApp.</p>

    <a class="button button--primary motion-cta" href="#cardapio">
      Ver cardápio
    </a>

    <a class="button button--whatsapp motion-whatsapp" href="https://wa.me/55NUMERO" target="_blank" rel="noopener">
      Pedir pelo WhatsApp
    </a>
  </div>

  <div class="hero__visual motion-reveal" data-reveal>
    <img class="hero__product motion-product" src="assets/produtos/hero-acai.webp" alt="Açaí Nu Ki com frutas" width="800" height="800">
  </div>
</section>
```

## CSS

```css
.motion-product {
  transform-origin: center;
}

@media (hover: hover) and (pointer: fine) {
  .motion-product:hover {
    transform: scale(1.025) rotate(-0.5deg);
  }
}

.motion-whatsapp {
  animation: ctaBreath 4200ms ease-in-out infinite;
}

@keyframes ctaBreath {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 0 0 rgba(161, 92, 255, 0);
  }

  50% {
    transform: scale(1.015);
    box-shadow: 0 0 24px rgba(161, 92, 255, .28);
  }
}

@media (prefers-reduced-motion: reduce) {
  .motion-whatsapp {
    animation: none;
  }
}
```

---

# 31. Checklist de Aprovação

Antes de aprovar qualquer motion, verificar:

```txt
A animação ajuda o usuário?
O CTA continua claro?
O preço continua visível?
O produto continua protagonista?
Funciona no mobile?
Funciona sem hover?
Funciona sem JavaScript?
Respeita prefers-reduced-motion?
Não piora performance?
Não causa layout shift?
Não parece infantil?
Não parece exagerada?
A quebra da 4ª parede está natural?
O personagem não está atrapalhando?
O WhatsApp continua fácil?
```

Se qualquer resposta essencial for “não”, ajustar.

---

# 32. Regras para Agentes de IA

Quando um agente for criar motion para Nu Ki Açaí, ele deve seguir este fluxo:

```txt
1. Identificar o componente.
2. Identificar a ação do usuário.
3. Definir o objetivo da animação.
4. Escolher intensidade: funcional, premium, quarta parede ou cinematográfica.
5. Usar tokens globais.
6. Priorizar transform e opacity.
7. Criar fallback para reduced motion.
8. Garantir que sem JS o conteúdo continue visível.
9. Testar mobile.
10. Remover qualquer motion decorativo demais.
```

O agente nunca deve implementar animações pesadas sem justificar a função.

---

# 33. Frase Guia

A frase guia desta skill é:

```txt
O movimento da Nu Ki Açaí deve parecer sabor em ação, não efeito jogado na tela.
```

A landing page deve fazer o visitante sentir:

```txt
“O site percebeu que eu cheguei.”
```

Mas a experiência precisa continuar simples:

```txt
Ver produto.
Escolher.
Pedir pelo WhatsApp.
```

O motion existe para tornar essa jornada mais viva, premium e memorável.
