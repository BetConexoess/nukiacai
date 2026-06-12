# Skill: Cardápio e Conversão para WhatsApp

## Objetivo

Criar, revisar, corrigir e evoluir um **cardápio digital mobile-first** que transforme visual bonito em **pedido real pelo WhatsApp**.

Esta skill deve ser usada em projetos onde o usuário chega por:

- QR code;
- link do WhatsApp;
- Instagram;
- link em bio;
- cartão físico;
- Google Perfil da Empresa;
- panfleto, embalagem ou balcão;
- campanha local.

O foco não é apenas deixar o cardápio bonito. O foco é conduzir a pessoa até uma ação clara:

> escolher produto → personalizar → revisar pedido → abrir WhatsApp com mensagem pronta → finalizar atendimento/pagamento.

---

## Princípio central

**Cardápio bonito que não gera pedido é vitrine sem caixa.**

Toda decisão de layout, animação, texto, imagem, botão e fluxo deve responder a uma pergunta:

> Isso ajuda o cliente a pedir mais rápido, com menos dúvida e menos retrabalho no WhatsApp?

Se não ajudar, simplifique ou remova.

---

## Quando ativar esta skill

Use esta skill sempre que o projeto envolver:

- cardápio digital;
- landing page de restaurante, lanchonete, açaí, pizzaria, hamburgueria, cafeteria ou delivery;
- botão “Pedir no WhatsApp”;
- montagem de pedido no site;
- carrinho simples;
- mensagem automática para WhatsApp;
- QR code de mesa, cartão ou panfleto;
- aumento de conversão;
- upsell, adicionais, combos e ticket médio;
- revisão de UX para venda mobile;
- copy de CTA para pedido;
- fluxo de pedido por WhatsApp Business.

---

## Resultado esperado

Ao final da implementação, o usuário deve conseguir:

1. Abrir o cardápio no celular sem dificuldade.
2. Entender rapidamente o que a loja vende.
3. Ver produtos, tamanhos, preços e adicionais.
4. Adicionar itens ao pedido.
5. Revisar subtotal, entrega/retirada e observações.
6. Tocar em um CTA claro.
7. Abrir o WhatsApp com uma mensagem organizada e pronta para enviar.
8. A loja receber um pedido fácil de ler, sem precisar perguntar tudo de novo.

---

## Funil obrigatório

O funil base deve seguir esta ordem:

```text
Entrada
  ↓
Cardápio mobile-first
  ↓
Categorias claras
  ↓
Produto com foto, preço e CTA
  ↓
Personalização: tamanho, adicionais e observação
  ↓
Carrinho/resumo
  ↓
CTA “Pedir no WhatsApp”
  ↓
Mensagem pré-preenchida
  ↓
Atendimento, pagamento e confirmação
```

Nunca jogar o usuário direto no WhatsApp antes de ele montar minimamente o pedido, exceto em CTAs secundários como “tirar dúvida”.

---

## Regra de ouro do WhatsApp

O WhatsApp deve receber **contexto**, não apenas intenção.

Ruim:

```text
Olá, quero fazer um pedido.
```

Bom:

```text
Olá! Quero fazer este pedido:

• 1x Açaí Grande 550ml — R$ 24,90
  Adicionais: Leite Ninho, Morango, Granola
  Observação: sem banana

• 1x Açaí Pequeno 200ml — R$ 12,90
  Adicionais: Paçoca

Subtotal: R$ 37,80
Entrega ou retirada: Entrega
Nome: Davi
Endereço: Rua Exemplo, 123
Pagamento: Pix

Pode confirmar, por favor?
```

A mensagem deve reduzir perguntas manuais e acelerar a venda.

---

## Hierarquia de conversão

A tela mobile deve priorizar nesta ordem:

1. Produto.
2. Preço.
3. Benefício/desejo.
4. Adicionar ao pedido.
5. Carrinho/resumo.
6. WhatsApp.

Elementos institucionais, animações, textos longos e decoração nunca devem empurrar o produto e o CTA para longe demais.

---

## Arquitetura recomendada da página

### 1. Header compacto

Deve conter apenas o essencial:

- logo ou nome da marca;
- status: aberto/fechado;
- tempo médio: “Entrega 35–50 min”;
- link curto para localização ou unidade, se necessário.

Evitar header gigante no cardápio. O usuário entrou para comprar, não para ler manifesto.

### 2. Hero curto

O hero deve vender rapidamente a proposta.

Exemplo:

```text
Monte seu açaí do seu jeito 💜
Escolha o tamanho, os adicionais e finalize pelo WhatsApp.
```

CTA opcional:

```text
Ver mais pedidos
```

### 3. Categorias visíveis

Categorias devem ficar fáceis de alcançar no celular.

Exemplos para açaí:

- Mais pedidos;
- Tradicionais;
- Especiais;
- Barcas;
- Copos;
- Cremes;
- Adicionais;
- Bebidas.

Boas práticas:

- usar navegação horizontal com scroll suave;
- manter categoria ativa visível;
- permitir pular direto para seção;
- evitar menu escondido demais.

### 4. Vitrine de produtos

Cada card deve mostrar:

- foto otimizada;
- nome claro;
- descrição curta;
- preço inicial;
- selo quando fizer sentido;
- CTA “Adicionar” ou “Montar”.

Exemplo:

```text
Açaí Grande 550ml
Cremoso, gelado e com até 4 adicionais.
A partir de R$ 24,90
[Montar]
```

### 5. Tela/drawer de personalização

Ao tocar em “Montar”, abrir uma área com:

- tamanho;
- quantidade;
- adicionais grátis;
- adicionais pagos;
- observação;
- preço atualizado;
- botão “Adicionar ao pedido”.

O usuário não deve precisar escrever tudo no WhatsApp.

### 6. Carrinho sticky

No mobile, o carrinho deve ficar sempre reencontrável.

Exemplo:

```text
2 itens · R$ 48,80 · Pedir no WhatsApp
```

Este CTA deve ficar no rodapé, respeitando safe-area do iPhone.

---

## Regras de UX para cardápio

### 1. O primeiro produto deve aparecer rápido

Em mobile, o usuário deve ver produto real sem rolar demais.

Evitar:

- hero enorme;
- vídeo pesado no topo;
- carrossel obrigatório;
- texto institucional longo;
- animação antes do cardápio;
- botão escondido no fim da página.

### 2. CTA deve dizer a ação real

Preferir:

```text
Montar
Adicionar ao pedido
Ver opções
Pedir no WhatsApp
Confirmar pedido
```

Evitar:

```text
Saiba mais
Enviar
Avançar
Clique aqui
Comprar agora
```

“Comprar agora” pode parecer pagamento imediato. Para WhatsApp, “Pedir no WhatsApp” costuma ser mais claro.

### 3. Mostrar preço cedo

Não esconder preço. Em cardápio, preço escondido gera dúvida e abandono.

Sempre exibir:

- preço base;
- adicionais pagos;
- subtotal no carrinho;
- total estimado quando possível.

### 4. Produtos principais devem ter destaque

Usar seções como:

- “Mais pedidos”;
- “Combos que valem mais”;
- “Favoritos da casa”;
- “Perfeito para dividir”;
- “Novo”.

Não destacar tudo. Se tudo chama atenção, nada chama atenção.

### 5. Reduzir escolhas no primeiro contato

Muitas opções sem orientação travam o pedido.

Para cardápio de açaí, organizar por intenção:

```text
Quero algo rápido → Mais pedidos
Quero montar → Monte seu açaí
Quero dividir → Barcas
Quero maior quantidade → 770ml / 1L
Quero promoção → Combos
```

---

## Menu engineering para aumentar ticket médio

### Estratégias permitidas

Use técnicas éticas de aumento de ticket médio:

1. **Combo recomendado**
   - “Açaí Grande + adicional premium + bebida”.

2. **Upgrade de tamanho**
   - “Por +R$ 5, leve 770ml em vez de 550ml”.

3. **Adicional contextual**
   - Mostrar leite em pó, morango, paçoca ou Nutella quando fizer sentido.

4. **Produto para dividir**
   - Barcas, marmitão, combos família.

5. **Mais pedido como atalho**
   - Reduz decisão e acelera conversão.

6. **Cross-sell no carrinho**
   - “Quer adicionar uma água ou refrigerante?”

### Regras

- Não usar técnica enganosa.
- Não esconder preço adicional.
- Não adicionar item automaticamente sem consentimento.
- Não confundir adicional grátis com adicional pago.
- Não forçar upsell antes do usuário conseguir montar o pedido base.

---

## Estrutura de dados recomendada

### Produto

```js
const product = {
  id: "acai-grande-550",
  name: "Açaí Grande 550ml",
  category: "Copos",
  description: "Açaí cremoso com até 4 adicionais.",
  basePrice: 24.9,
  image: "assets/produtos/grande-550ml.webp",
  badges: ["Mais pedido"],
  options: {
    freeToppingsLimit: 4,
    freeToppings: ["Banana", "Granola", "Leite em pó", "Morango"],
    paidToppings: [
      { id: "nutella", name: "Nutella", price: 4.0 },
      { id: "creme-ninho", name: "Creme de Ninho", price: 3.5 }
    ]
  },
  active: true
};
```

### Item no carrinho

```js
const cartItem = {
  productId: "acai-grande-550",
  name: "Açaí Grande 550ml",
  quantity: 1,
  basePrice: 24.9,
  freeToppings: ["Banana", "Granola", "Leite em pó"],
  paidToppings: [
    { name: "Nutella", price: 4.0 }
  ],
  note: "Sem xarope",
  total: 28.9
};
```

### Pedido

```js
const order = {
  customer: {
    name: "Davi",
    phone: "",
    address: "Rua Exemplo, 123"
  },
  fulfillment: "delivery",
  payment: "pix",
  items: [],
  subtotal: 0,
  deliveryFee: 0,
  total: 0,
  source: "qr-code-card",
  createdAt: new Date().toISOString()
};
```

---

## Geração da mensagem para WhatsApp

### Função base

```js
function formatBRL(value) {
  return new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL"
  }).format(value || 0);
}

function buildWhatsAppMessage(order) {
  const lines = [];

  lines.push("Olá! Quero fazer este pedido:");
  lines.push("");

  order.items.forEach((item) => {
    lines.push(`• ${item.quantity}x ${item.name} — ${formatBRL(item.total)}`);

    if (item.freeToppings?.length) {
      lines.push(`  Adicionais grátis: ${item.freeToppings.join(", ")}`);
    }

    if (item.paidToppings?.length) {
      const paid = item.paidToppings
        .map((extra) => `${extra.name} (${formatBRL(extra.price)})`)
        .join(", ");
      lines.push(`  Adicionais pagos: ${paid}`);
    }

    if (item.note) {
      lines.push(`  Observação: ${item.note}`);
    }

    lines.push("");
  });

  lines.push(`Subtotal: ${formatBRL(order.subtotal)}`);

  if (order.deliveryFee > 0) {
    lines.push(`Taxa de entrega: ${formatBRL(order.deliveryFee)}`);
  }

  lines.push(`Total estimado: ${formatBRL(order.total)}`);
  lines.push(`Entrega ou retirada: ${order.fulfillment === "delivery" ? "Entrega" : "Retirada"}`);

  if (order.customer?.name) {
    lines.push(`Nome: ${order.customer.name}`);
  }

  if (order.fulfillment === "delivery" && order.customer?.address) {
    lines.push(`Endereço: ${order.customer.address}`);
  }

  if (order.payment) {
    lines.push(`Pagamento: ${order.payment}`);
  }

  lines.push("");
  lines.push("Pode confirmar, por favor?");

  return lines.join("\n");
}
```

### Gerar link `wa.me`

```js
function buildWhatsAppUrl(phoneNumber, message) {
  const cleanPhone = String(phoneNumber).replace(/\D/g, "");
  return `https://wa.me/${cleanPhone}?text=${encodeURIComponent(message)}`;
}

function openWhatsAppOrder(order, phoneNumber) {
  const message = buildWhatsAppMessage(order);
  const url = buildWhatsAppUrl(phoneNumber, message);

  window.open(url, "_blank", "noopener,noreferrer");
}
```

### Regras para o número

O número deve estar em formato internacional, sem `+`, sem espaço e sem pontuação.

Correto:

```text
5511999999999
```

Errado:

```text
+55 (11) 99999-9999
```

No código, limpe o número antes de montar o link.

---

## HTML recomendado para CTA final

```html
<button class="order-bar__button" type="button" data-action="send-whatsapp-order">
  <span class="order-bar__summary">2 itens · R$ 48,80</span>
  <strong>Pedir no WhatsApp</strong>
</button>
```

Evitar link solto sem estado de pedido:

```html
<a href="https://wa.me/5511999999999">WhatsApp</a>
```

O link simples pode existir como CTA secundário para dúvidas, mas não deve substituir o fluxo de pedido.

---

## CSS recomendado para barra de pedido mobile

```css
.order-bar {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1000;
  padding: 0.75rem 1rem;
  padding-bottom: max(0.75rem, env(safe-area-inset-bottom));
  background: rgba(14, 1, 34, 0.94);
  backdrop-filter: blur(16px);
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}

.order-bar__button {
  width: 100%;
  min-height: 52px;
  border: 0;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.85rem 1rem;
  font: inherit;
  font-weight: 700;
  cursor: pointer;
}

.order-bar__summary {
  font-size: 0.875rem;
  opacity: 0.92;
}

@media (min-width: 768px) {
  .order-bar {
    left: 50%;
    right: auto;
    width: min(680px, calc(100% - 2rem));
    transform: translateX(-50%);
    bottom: 1rem;
    border-radius: 999px;
  }
}
```

---

## CSS para cards de produto

```css
.menu-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}

.product-card {
  display: grid;
  grid-template-columns: 96px 1fr;
  gap: 0.9rem;
  align-items: center;
  padding: 0.85rem;
  border-radius: 1.25rem;
  background: rgba(47, 21, 76, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.product-card__image {
  width: 96px;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 1rem;
}

.product-card__title {
  margin: 0;
  font-size: 1rem;
  line-height: 1.2;
}

.product-card__description {
  margin: 0.25rem 0 0;
  font-size: 0.875rem;
  line-height: 1.35;
  opacity: 0.84;
}

.product-card__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-top: 0.65rem;
}

.product-card__price {
  font-weight: 800;
}

.product-card__button {
  min-height: 44px;
  min-width: 44px;
  border-radius: 999px;
  padding: 0.65rem 0.9rem;
  border: 0;
  font-weight: 700;
}

@media (min-width: 768px) {
  .menu-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1120px) {
  .menu-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}
```

---

## Regra de imagens de produto

Imagens vendem, mas imagem pesada mata conversão.

Obrigatório:

- usar `.webp` ou `.avif` quando possível;
- definir `width` e `height` ou `aspect-ratio`;
- usar `loading="lazy"` nos produtos fora da primeira dobra;
- não aplicar lazy-load agressivo na imagem principal visível no topo;
- usar `alt` útil para produtos reais;
- usar `alt=""` para imagens puramente decorativas.

Exemplo:

```html
<img
  src="assets/produtos/acai-grande-550.webp"
  width="320"
  height="320"
  alt="Açaí grande de 550ml com morango, leite em pó e granola"
  loading="lazy"
  decoding="async"
/>
```

---

## Regras para categorias

Categorias devem resolver intenção de compra, não apenas organizar estoque.

Ruim:

```text
Categoria 1
Categoria 2
Diversos
Outros
```

Bom:

```text
Mais pedidos
Monte seu açaí
Copos
Barcas
Especiais
Adicionais
Bebidas
```

### Categoria “Mais pedidos”

Sempre que houver dados ou escolha comercial, criar uma categoria de atalhos.

Ela pode aumentar conversão porque reduz esforço de decisão.

---

## Regras para produtos

### Nome

Deve ser curto e reconhecível.

Bom:

```text
Açaí Grande 550ml
Barca Premium
Marmitão 1L
```

Ruim:

```text
Produto especial delicioso da casa tamanho família roxo premium
```

### Descrição

A descrição deve ajudar a decidir, não apenas decorar.

Modelo:

```text
[benefício principal] + [quantidade/tamanho] + [limite ou diferencial]
```

Exemplo:

```text
Copo generoso de 550ml com até 4 adicionais grátis.
```

### Preço

Usar `A partir de` somente quando há variação real.

```text
A partir de R$ 19,90
```

Se o produto tem preço fixo, mostrar preço direto.

```text
R$ 24,90
```

---

## Regras para adicionais

Separar claramente:

1. adicionais grátis;
2. adicionais pagos;
3. limite de adicionais;
4. preço incremental.

Exemplo:

```text
Escolha até 4 adicionais grátis
```

Se passar do limite:

```text
Você já escolheu 4 adicionais grátis. Remova um item ou escolha adicionais pagos.
```

Adicional pago deve exibir preço no próprio botão:

```text
Nutella +R$ 4,00
```

---

## Validação de pedido

Antes de abrir o WhatsApp, validar:

- carrinho não está vazio;
- item obrigatório foi escolhido;
- limite de adicionais grátis foi respeitado;
- total foi calculado;
- modo de recebimento foi escolhido, se necessário;
- endereço foi preenchido, se for entrega;
- mensagem final não está vazia;
- número do WhatsApp está configurado.

Exemplo:

```js
function validateOrder(order) {
  const errors = [];

  if (!order.items?.length) {
    errors.push("Adicione pelo menos um item ao pedido.");
  }

  if (!order.fulfillment) {
    errors.push("Escolha entrega ou retirada.");
  }

  if (order.fulfillment === "delivery" && !order.customer?.address?.trim()) {
    errors.push("Informe o endereço para entrega.");
  }

  if (!Number.isFinite(order.total) || order.total <= 0) {
    errors.push("Não foi possível calcular o total do pedido.");
  }

  return errors;
}
```

---

## Fluxo para entrega e retirada

### Entrega

Coletar somente o necessário:

- nome;
- endereço;
- complemento, se houver;
- referência, se houver;
- forma de pagamento preferida.

Não pedir CPF, data de nascimento ou dados sensíveis sem necessidade real.

### Retirada

Coletar:

- nome;
- unidade, se houver mais de uma;
- horário desejado, se aplicável;
- forma de pagamento preferida.

---

## Copywriting de conversão

### CTAs recomendados

Use textos com verbo claro:

```text
Montar meu açaí
Adicionar ao pedido
Ver barcas
Pedir no WhatsApp
Confirmar pedido
Escolher adicionais
Retirar no balcão
Receber em casa
```

### Microcopy para reduzir dúvida

```text
Você revisa tudo antes de enviar.
```

```text
O pedido será enviado pronto para nosso WhatsApp.
```

```text
Pagamento combinado na confirmação do pedido.
```

```text
Tempo estimado pode variar conforme demanda e endereço.
```

### Mensagens de erro humanas

Ruim:

```text
Erro inválido.
```

Bom:

```text
Escolha pelo menos um tamanho para continuar.
```

---

## WhatsApp: regras práticas

### 1. CTA de pedido e CTA de dúvida devem ser diferentes

Pedido:

```text
Pedir no WhatsApp
```

Dúvida:

```text
Tirar dúvida no WhatsApp
```

Nunca misturar os dois no mesmo botão quando o carrinho existe.

### 2. Preservar origem

Adicionar origem no pedido ajuda a medir conversão.

Exemplo:

```text
Origem: QR Code cartão
```

Ou internamente:

```js
source: "qr-card"
```

### 3. Mensagem deve ser legível no celular do atendente

Usar:

- quebras de linha;
- bullets;
- subtotal;
- total;
- modo de entrega;
- observações por item.

Evitar mensagem em linha única gigante.

### 4. Não prometer automação que não existe

Se o pedido ainda será confirmado manualmente, escrever:

```text
Pode confirmar, por favor?
```

Não escrever:

```text
Pedido confirmado automaticamente.
```

---

## WhatsApp Business API: quando considerar

Para MVP, `wa.me` com mensagem pronta é suficiente.

Considere WhatsApp Business Platform, Cloud API ou BSP quando precisar de:

- múltiplos atendentes;
- bot;
- templates aprovados;
- recuperação de carrinho;
- mensagens de status;
- webhooks;
- CRM;
- histórico estruturado;
- métricas por etapa;
- fila de atendimento;
- integração com pagamento;
- integração com produção/cozinha.

Para uma landing page/cardápio inicial, não começar pela API se isso atrasar o lançamento sem necessidade.

---

## Compliance e privacidade

### Regras obrigatórias

- Coletar apenas dados necessários ao pedido.
- Não pedir número completo de cartão pelo WhatsApp.
- Não pedir documento sem necessidade operacional/legal.
- Informar quando dados forem usados para atendimento.
- Ter link de política de privacidade se coletar dados no site.
- Não enviar marketing sem consentimento.
- Respeitar pedido de saída/opt-out.

### Frase simples para rodapé

```text
Usamos seus dados apenas para montar, enviar e acompanhar seu pedido. Ao continuar, você concorda em enviar essas informações pelo WhatsApp.
```

---

## Pagamento

### Para MVP

Permitir escolher:

- Pix;
- dinheiro;
- cartão na entrega;
- combinar no WhatsApp.

### Para fluxo mais avançado

Integrar:

- Pix copia e cola;
- QR Code Pix;
- link de pagamento;
- webhook de confirmação;
- status do pedido.

### Regra

Pagamento não deve travar o pedido se a operação ainda confirma manualmente.

Exemplo de campo:

```text
Forma de pagamento preferida
```

Não escrever:

```text
Pagamento obrigatório agora
```

A menos que o sistema realmente faça checkout.

---

## Eventos de analytics

Registrar eventos para medir conversão.

Eventos mínimos:

```text
view_menu
view_item
select_category
add_to_cart
remove_from_cart
begin_checkout
send_to_whatsapp
whatsapp_click
order_message_generated
```

Eventos avançados:

```text
select_upsell
add_paid_extra
choose_delivery
choose_pickup
payment_method_selected
payment_link_created
payment_approved
purchase
cart_abandoned
cart_recovered
```

Exemplo:

```js
function trackEvent(name, params = {}) {
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ event: name, ...params });
}

trackEvent("send_to_whatsapp", {
  value: order.total,
  currency: "BRL",
  items_count: order.items.length,
  source: order.source
});
```

---

## Métricas para acompanhar

Acompanhar:

- visitantes do cardápio;
- cliques em produto;
- taxa de adicionar ao carrinho;
- abandono no carrinho;
- cliques em “Pedir no WhatsApp”;
- pedidos realmente recebidos;
- ticket médio;
- produtos mais pedidos;
- adicionais mais vendidos;
- taxa de upsell;
- tempo médio até finalizar pedido;
- origem com melhor conversão: QR, Instagram, WhatsApp, Google.

Fórmulas úteis:

```text
Taxa de pedido no WhatsApp = cliques em pedir / visitantes do cardápio
```

```text
Taxa de carrinho para WhatsApp = cliques em pedir / usuários que adicionaram item
```

```text
Ticket médio = faturamento / número de pedidos
```

---

## Testes A/B recomendados

Testar uma mudança por vez.

Prioridade:

1. Texto do CTA:
   - “Pedir no WhatsApp” vs “Enviar pedido”.

2. Barra sticky:
   - com subtotal vs sem subtotal.

3. Ordem das categorias:
   - “Mais pedidos” primeiro vs ordem tradicional.

4. Produto destaque:
   - combo primeiro vs produto individual primeiro.

5. Upsell:
   - antes do carrinho vs dentro do carrinho.

6. Mensagem do WhatsApp:
   - curta vs detalhada.

7. Pagamento:
   - Pix destacado vs pagamento combinado.

Nunca mudar tudo ao mesmo tempo, senão não será possível saber o que melhorou.

---

## Acessibilidade mínima obrigatória

O cardápio deve funcionar para pessoas com dificuldades visuais, motoras ou cognitivas.

Obrigatório:

- botões com no mínimo 44px de altura;
- contraste suficiente;
- foco visível;
- labels em campos;
- imagens informativas com `alt`;
- imagens decorativas com `alt=""`;
- texto mínimo legível;
- sem depender só de cor para indicar erro;
- sem depender de hover;
- navegação possível por teclado;
- mensagens de erro claras.

Exemplo:

```html
<label for="customer-address">Endereço de entrega</label>
<input
  id="customer-address"
  name="address"
  type="text"
  autocomplete="street-address"
  placeholder="Rua, número e bairro"
/>
```

---

## Performance obrigatória

O cardápio deve ser leve porque muitos acessos virão de celular e rede móvel.

### Regras

- Evitar imagens enormes.
- Evitar JavaScript desnecessário.
- Evitar bibliotecas pesadas para carrinho simples.
- Carregar primeiro o essencial.
- Usar lazy-load para produtos fora da dobra.
- Não bloquear a página com animações longas.
- Não usar vídeo pesado como elemento principal do cardápio.
- Evitar carrossel pesado.
- Evitar fontes demais.

### Metas práticas

- primeiro conteúdo visível rápido;
- CTA acessível sem travar;
- rolagem fluida;
- sem layout pulando;
- imagens dimensionadas corretamente;
- mensagem do WhatsApp gerada instantaneamente.

---

## Animações no cardápio

Animações podem aumentar desejo, mas não podem atrapalhar pedido.

Permitido:

- brilho sutil no produto destaque;
- entrada leve dos cards;
- feedback ao adicionar no carrinho;
- microinteração no botão;
- partículas leves em áreas decorativas;
- movimento suave em elementos da marca.

Evitar:

- animação que atrasa o produto;
- loader desnecessário;
- card pulando durante leitura;
- botão se mexendo demais;
- animação contínua pesada;
- efeito que cria overflow horizontal;
- bloquear scroll.

Sempre respeitar `prefers-reduced-motion`:

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

---

## Estados obrigatórios da interface

Todo fluxo de pedido deve ter estados claros.

### Produto

- disponível;
- indisponível;
- destaque;
- promoção;
- novo.

### Carrinho

- vazio;
- com itens;
- erro de validação;
- pronto para WhatsApp.

### CTA

- ativo;
- carregando;
- desabilitado;
- erro.

### Loja

- aberta;
- fechada;
- alta demanda;
- retirada apenas;
- entrega indisponível.

Exemplo:

```text
Estamos fechados agora, mas você pode montar seu pedido para enviar quando abrirmos.
```

---

## Antipadrões proibidos

Não fazer:

- cardápio bonito sem preço;
- botão de WhatsApp genérico sem pedido montado;
- pedir para o cliente escrever tudo manualmente;
- esconder adicionais pagos;
- empurrar produto para baixo com hero gigante;
- usar imagens pesadas sem otimização;
- depender de hover;
- deixar carrinho invisível;
- abrir WhatsApp com texto vazio;
- usar `alert()` para erros importantes;
- criar rolagem horizontal;
- forçar cadastro antes do pedido;
- pedir dados sensíveis sem necessidade;
- colocar muitos CTAs competindo;
- usar “comprar agora” se a compra ainda depende de confirmação manual;
- prometer tempo exato se a loja não controla isso.

---

## Checklist de implementação

### Estrutura

- [ ] Header compacto.
- [ ] Status da loja visível.
- [ ] Categorias claras.
- [ ] Produtos com foto, nome, descrição e preço.
- [ ] Produto destaque ou “mais pedidos”.
- [ ] Tela de personalização.
- [ ] Carrinho persistente.
- [ ] CTA final para WhatsApp.
- [ ] Mensagem estruturada.
- [ ] Rodapé com contato e política, se necessário.

### Conversão

- [ ] O primeiro produto aparece sem rolar demais.
- [ ] CTA principal é óbvio.
- [ ] Preços aparecem antes do WhatsApp.
- [ ] Adicionais pagos são claros.
- [ ] Upsell não atrapalha o pedido.
- [ ] Cliente revisa antes de enviar.
- [ ] Pedido chega legível no WhatsApp.

### Mobile

- [ ] Funciona em 320px, 360px, 390px, 414px e 430px.
- [ ] Não há overflow horizontal.
- [ ] Botões têm área de toque adequada.
- [ ] Teclado virtual não cobre campos críticos.
- [ ] Barra fixa respeita safe-area.
- [ ] Não depende de hover.

### WhatsApp

- [ ] Número configurado em formato internacional.
- [ ] Mensagem usa `encodeURIComponent`.
- [ ] Link abre em Android e iPhone.
- [ ] Mensagem contém itens, quantidades, adicionais, subtotal e modo de entrega.
- [ ] CTA secundário de dúvida não interfere no pedido.
- [ ] Origem do pedido pode ser identificada.

### Performance

- [ ] Imagens otimizadas.
- [ ] Lazy-load fora da primeira dobra.
- [ ] Sem script pesado desnecessário.
- [ ] Sem animação bloqueante.
- [ ] Layout não pula durante carregamento.
- [ ] Fontes limitadas.

### Acessibilidade

- [ ] Contraste suficiente.
- [ ] Foco visível.
- [ ] Inputs com labels.
- [ ] Erros claros.
- [ ] Alvos de toque adequados.
- [ ] `alt` correto nas imagens.
- [ ] Suporte a `prefers-reduced-motion`.

### Privacidade

- [ ] Coleta apenas dados necessários.
- [ ] Não pede cartão completo no WhatsApp.
- [ ] Não coleta CPF sem necessidade.
- [ ] Tem aviso simples sobre uso dos dados.
- [ ] Marketing só com consentimento.

### Analytics

- [ ] Evento de visualização do cardápio.
- [ ] Evento de visualização de produto.
- [ ] Evento de adicionar ao carrinho.
- [ ] Evento de início de checkout.
- [ ] Evento de clique no WhatsApp.
- [ ] Valor do pedido enviado nos eventos.

---

## Checklist de auditoria para IA

Ao revisar um projeto existente, a IA deve verificar:

1. Existe carrinho ou apenas botão genérico para WhatsApp?
2. O pedido enviado ao WhatsApp está completo?
3. O cliente vê preço antes de chamar no WhatsApp?
4. O CTA principal aparece no mobile sem esforço?
5. A página funciona bem em 360px?
6. Há overflow horizontal?
7. Os cards de produto são fáceis de tocar?
8. Os adicionais estão claros?
9. O fluxo diferencia entrega e retirada?
10. As imagens estão otimizadas?
11. A mensagem final usa `encodeURIComponent`?
12. O número do WhatsApp está limpo?
13. Há tracking mínimo de conversão?
14. Existe risco de coletar dado demais?
15. Há textos confusos como “comprar agora” quando é apenas pedido por WhatsApp?

---

## Prompt interno para Codex/Claude ao aplicar esta skill

Use este modelo quando for pedir para a IA revisar ou implementar:

```text
Você está trabalhando em um cardápio digital mobile-first com conversão para WhatsApp.

Aplique a skill “Cardápio e Conversão para WhatsApp”.

Objetivo:
Transformar o cardápio em um fluxo real de pedido: produto → personalização → carrinho → mensagem estruturada para WhatsApp.

Regras obrigatórias:
- Não criar apenas botão genérico para WhatsApp.
- O pedido precisa chegar no WhatsApp com itens, quantidades, adicionais, observações, subtotal, entrega/retirada e pagamento preferido.
- O layout base deve ser mobile-first.
- O CTA final precisa ser claro e reencontrável no celular.
- Não esconder preços.
- Não depender de hover.
- Não criar overflow horizontal.
- Não pedir dados sensíveis desnecessários.
- Otimizar imagens e manter boa performance.

Antes de alterar arquivos, analise o fluxo atual e diga:
1. Como o usuário escolhe produto hoje.
2. Onde a conversão para WhatsApp acontece.
3. O que está faltando para virar pedido real.
4. Quais arquivos precisam ser alterados.

Depois implemente com mudanças pequenas, seguras e testáveis.
```

---

## Prompt de auditoria rápida

```text
Revise este projeto como especialista em cardápio digital e conversão para WhatsApp.

Procure problemas em:
- fluxo de pedido;
- CTA mobile;
- mensagem enviada para WhatsApp;
- carrinho;
- adicionais;
- preço e subtotal;
- responsividade;
- performance;
- acessibilidade;
- coleta de dados;
- analytics.

Entregue:
1. Problemas encontrados.
2. Impacto na conversão.
3. Correção recomendada.
4. Arquivos e seletores/funções que devem ser alterados.
5. Prioridade: alta, média ou baixa.
```

---

## Definition of Done

A implementação só está pronta quando:

- o cliente consegue montar um pedido completo no celular;
- o carrinho mostra quantidade e valor;
- o botão “Pedir no WhatsApp” abre com mensagem estruturada;
- a loja recebe informação suficiente para confirmar sem refazer todo atendimento;
- o layout funciona em telas pequenas;
- não existe rolagem horizontal;
- produtos, preços e adicionais estão claros;
- imagens não deixam o site pesado;
- o CTA principal é fácil de tocar;
- eventos mínimos de conversão existem ou foram planejados;
- dados pessoais são coletados apenas quando necessários.

---

## Resumo operacional

Sempre que trabalhar nessa skill, lembre:

```text
Bonito chama atenção.
Claro gera confiança.
Rápido reduz abandono.
Mensagem estruturada vende mais.
WhatsApp sem contexto cria retrabalho.
```

O objetivo final é simples:

> fazer o cliente pedir com menos esforço e fazer a loja vender com menos conversa repetida.
