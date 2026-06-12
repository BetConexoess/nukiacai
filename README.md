# Nu Ki Açaí

Base inicial do projeto **Nu Ki Açaí**, feita com HTML, CSS e JavaScript puro.

## O que existe nesta base

- `index.html`: página principal com hero, cardápio interativo, resumo do pedido e fluxo de uso.
- `css/base.css`: variáveis, reset leve, estados globais e atmosfera visual.
- `css/cardapio.css`: layout principal, cards dos produtos, resumo e responsividade.
- `css/animacoes.css`: animações simples e suporte a `prefers-reduced-motion`.
- `js/app.js`: renderização dos produtos, filtros, carrinho local com persistência em `localStorage` e montagem do texto do pedido.
- `assets/`: pasta reservada para imagens, ícones e mídias.

## Como usar

1. Abra `index.html` em um navegador.
2. Edite os arquivos em `css/` e `js/` conforme a evolução do layout.
3. Coloque mídias novas dentro de `assets/`.

## Observações

- O `AGENTS.md` foi preservado.
- O botão do WhatsApp está pronto para receber o número quando ele for aprovado. O ponto de entrada é `data-whatsapp-number` no `<body>` de `index.html`.
- Os preços ainda estão como placeholder, para não alterar valores sem aprovação.
- A base foi criada para evolução futura do cardápio interativo e do pedido via WhatsApp.
