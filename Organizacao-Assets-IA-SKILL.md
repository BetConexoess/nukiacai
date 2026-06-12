# SKILL.md — Organização de Assets IA

## Objetivo da skill

Esta skill orienta o agente de programação/design a organizar, padronizar, auditar e manter todos os assets visuais e sonoros gerados por IA ou criados manualmente para o projeto.

Use esta skill sempre que o projeto envolver:

- logos;
- ícones;
- personagens;
- produtos do cardápio;
- fundos;
- texturas;
- efeitos visuais;
- ingredientes;
- botões;
- imagens para WhatsApp;
- assets para landing page;
- assets para cardápio digital;
- prompts de geração IA;
- versões de imagens;
- exports otimizados para web.

O foco principal deste projeto é um cardápio/landing page mobile-first para **Nu Ki Açaí**, com identidade visual roxa/violeta, personagens, produtos de açaí, animações, QR code e conversão para WhatsApp.

---

## Princípio central

Nunca trate assets como “imagens soltas”.

Todo asset deve ter:

1. pasta correta;
2. nome padronizado;
3. versão;
4. origem;
5. status;
6. uso permitido;
7. formato correto;
8. tamanho otimizado;
9. relação com o projeto;
10. documentação mínima.

A organização correta evita:

- imagens duplicadas;
- versões perdidas;
- prompts esquecidos;
- personagens inconsistentes;
- produtos com estilos diferentes;
- site pesado;
- erros de caminho no HTML/CSS/JS;
- confusão entre imagem final, rascunho e referência;
- retrabalho ao usar Codex, Claude, Gemini, Canva, Adobe, Midjourney, Flux, SDXL, ComfyUI ou outra IA.

---

## Quando ativar esta skill

Ative esta skill quando o pedido envolver qualquer uma das situações abaixo:

- “organize meus assets”;
- “crie estrutura de pastas”;
- “padronize nomes das imagens”;
- “onde coloco essa imagem?”;
- “crie prompt para asset”;
- “gere lista de imagens necessárias”;
- “audite meus arquivos”;
- “limpe assets duplicados”;
- “otimize a pasta assets”;
- “crie manifesto dos assets”;
- “arrume caminhos quebrados”;
- “prepare assets para o site”;
- “monte o kit visual da marca”;
- “separe personagens, produtos, fundos e efeitos”;
- “deixe pronto para Codex/Claude usar”.

---

## Regra obrigatória 1 — Não misturar origem, master e export

Todo asset deve ser separado em pelo menos três níveis:

```text
master/      → arquivo original de alta qualidade
derived/     → versões exportadas para uso no site
reference/   → imagens usadas só como referência visual
```

Exemplo:

```text
assets/images/products/grande-550ml/
  master/
    product-grande-550ml-hero-master-v1.0.0.png
  derived/
    product-grande-550ml-card-480w-v1.0.0.webp
    product-grande-550ml-card-768w-v1.0.0.webp
    product-grande-550ml-card-1024w-v1.0.0.avif
  reference/
    ref-grande-550ml-style-card-v1.jpg
```

Nunca use `master/` diretamente no site.

O site deve usar apenas arquivos de `derived/`.

---

## Regra obrigatória 2 — Estrutura oficial de pastas do projeto

Use esta estrutura como base:

```text
assets/
  README.md
  MANIFEST.assets.json
  taxonomy.md

  brand/
    logos/
      horizontal/
      vertical/
      roxa/
      watermark/
      icon/
      transparent/
    palette/
    typography/
    references/

  images/
    products/
      barca-premium/
      gigante-770ml/
      grande-550ml/
      medio-330ml/
      pequeno-200ml/
      especiais/
      marmitao-1l/

    characters/
      casal/
      menina/
      rapaz/
      entregador/
      casal-moto/

    backgrounds/
      home/
      cardapio/
      secoes/
      textura/

    ingredients/
      gratis-liquidos/
      gratis-solidos/
      pagos/

    effects/
      brilho/
      folhas/
      gotas/
      particulas/
      splash-acai/

    delivery/
      caixa/
      mochila/
      moto-protecao-chuva/

    buttons/
      cardapio/
      lojas/
      nossos-produtos/
      peca-agora/
      whatsapp/

  icons/
    interface/
    sociais/
    pagamentos/
    status/
    categorias/

  audio/
    sfx/
    ambience/

  video/
    short/
    loops/
    previews/

  prompts/
    brand/
    products/
    characters/
    backgrounds/
    effects/
    delivery/

  manifests/
    products/
    characters/
    backgrounds/
    effects/
```

---

## Regra obrigatória 3 — Naming convention

Todo arquivo deve seguir um padrão previsível.

Formato recomendado:

```text
{tipo}-{categoria}-{slug}-{variante}-{dimensao}-v{major.minor.patch}.{ext}
```

Exemplos:

```text
logo-brand-horizontal-main-1024w-v1.0.0.png
logo-brand-watermark-purple-512w-v1.0.0.webp
img-product-grande-550ml-card-768w-v1.0.0.webp
img-product-barca-premium-hero-1280w-v1.1.0.avif
char-casal-happy-front-1024w-v2.0.0.webp
char-entregador-moto-rain-cover-1536w-v1.0.0.png
bg-home-premium-purple-1920w-v1.0.0.webp
effect-splash-acai-front-768w-v1.0.0.webp
icon-whatsapp-filled-48-v1.0.0.svg
btn-peca-agora-glow-mobile-480w-v1.0.0.webp
```

Nunca use nomes como:

```text
imagem1.png
nova.png
final.png
final2.png
final_agora_vai.png
teste.png
whatsapp certo.png
açaí bonito.png
```

---

## Regra obrigatória 4 — Use slug sem acento

Nomes de arquivos devem usar:

- letras minúsculas;
- sem acentos;
- sem espaços;
- sem cedilha;
- hífen como separador;
- extensão correta.

Correto:

```text
medio-330ml
peca-agora
marmitao-1l
splash-acai
moto-protecao-chuva
```

Errado:

```text
Médio 330ml
Peça Agora
Marmitão 1L
Splash Açaí
moto proteção chuva
```

---

## Regra obrigatória 5 — Todo asset precisa de status

Use apenas estes status:

```text
draft       → rascunho
review      → precisa revisar
approved    → aprovado para uso
published   → em uso no site
deprecated  → substituído, não usar em novas telas
archived    → guardado, não usar
```

Nunca publique asset em `draft` ou `review`.

---

## Regra obrigatória 6 — Master é sagrado

A pasta `master/` guarda a melhor versão possível do asset.

Regras:

- não comprimir demais;
- não sobrescrever;
- não renomear sem atualizar manifesto;
- não usar direto no HTML/CSS;
- não apagar sem backup;
- preservar transparência quando existir;
- preservar resolução alta;
- preservar prompt e origem.

---

## Regra obrigatória 7 — Derived é para o site

A pasta `derived/` guarda versões prontas para uso.

Ela deve conter:

- WebP;
- AVIF quando possível;
- PNG somente quando transparência/fallback for necessário;
- SVG para ícones/logos vetoriais;
- tamanhos diferentes para responsividade;
- arquivos leves.

Exemplo:

```text
derived/
  img-product-medio-330ml-card-360w-v1.0.0.webp
  img-product-medio-330ml-card-480w-v1.0.0.webp
  img-product-medio-330ml-card-768w-v1.0.0.webp
  img-product-medio-330ml-card-1024w-v1.0.0.avif
```

---

## Regra obrigatória 8 — Reference não entra no site

A pasta `reference/` é apenas contexto visual.

Ela pode conter:

- cartão físico da marca;
- paleta;
- exemplos de estilo;
- prints de concorrentes;
- imagens de inspiração;
- referências de personagem;
- referências de produto.

Arquivos de referência nunca devem ser usados como imagem final no site.

---

## Formatos recomendados

### Imagens raster

Use:

```text
AVIF → melhor compressão moderna
WebP → padrão recomendado para web
PNG  → transparência, master ou fallback
JPG  → fallback fotográfico quando necessário
```

### Vetores

Use:

```text
SVG → logos, ícones e formas vetoriais
```

### Vídeos

Use:

```text
MP4/H.264 → compatibilidade
WebM      → alternativa otimizada quando fizer sentido
```

### Áudio

Use:

```text
MP3 → compatibilidade
OGG → alternativa para web
```

---

## Tamanhos recomendados por tipo

### Produtos do cardápio

```text
master: 2000px a 3000px no maior lado
card mobile: 360w, 480w, 768w
hero/detalhe: 960w, 1280w
formato final: WebP/AVIF
```

### Personagens

```text
master: 2048px ou maior
com transparência: PNG master
site: WebP com alpha ou PNG fallback
variações: front, side, happy, pedido, delivery
```

### Fundos

```text
master: 2560px ou maior
mobile: 640w, 960w, 1280w
desktop: 1600w, 1920w
formato final: WebP/AVIF
```

### Efeitos

```text
master: PNG transparente
site: WebP com alpha quando possível
tamanhos: 256w, 512w, 768w
```

### Ícones

```text
preferencial: SVG
fallback: 24px, 32px, 48px, 64px
```

### Botões imagem

Preferir botão em HTML/CSS.

Use imagem de botão somente quando houver textura/ilustração impossível de reproduzir em CSS.

---

## Manifesto obrigatório

Todo lote importante de assets deve ter um manifesto.

Arquivo recomendado:

```text
assets/MANIFEST.assets.json
```

Exemplo:

```json
{
  "assetId": "img_product_grande_550ml_card_001",
  "type": "image.product",
  "category": "products",
  "slug": "grande-550ml",
  "name": "Açaí Grande 550ml - Card",
  "version": "1.0.0",
  "status": "approved",
  "project": "nu-ki-acai",
  "intendedUse": ["cardapio", "mobile", "whatsapp"],
  "files": {
    "master": "assets/images/products/grande-550ml/master/img-product-grande-550ml-card-master-v1.0.0.png",
    "derived": [
      "assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-480w-v1.0.0.webp",
      "assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.webp"
    ]
  },
  "ai": {
    "tool": "gerador-ia",
    "model": "modelo-usado",
    "promptFile": "assets/prompts/products/grande-550ml.md",
    "seed": null,
    "reproducible": false
  },
  "technical": {
    "hasAlpha": false,
    "format": "webp",
    "width": 768,
    "height": 768,
    "optimized": true
  },
  "rights": {
    "license": "owned",
    "allowedUse": ["web", "social", "whatsapp"],
    "containsRealPerson": false
  }
}
```

---

## Template de prompt salvo

Todo asset gerado por IA deve ter um arquivo de prompt salvo em:

```text
assets/prompts/{categoria}/{slug}.md
```

Template:

```md
# Prompt — {nome do asset}

## Objetivo
Descrever o asset que será gerado e onde será usado.

## Uso no projeto
- Seção:
- Componente:
- Dispositivo principal:
- Formato final:
- Status:

## Prompt principal
Cole aqui o prompt exato usado na IA.

## Prompt negativo
Cole aqui o prompt negativo, se existir.

## Referências usadas
- cartão da marca:
- paleta:
- personagem:
- produto:
- estilo:

## Parâmetros
- ferramenta:
- modelo:
- proporção:
- seed:
- qualidade:
- estilo:
- data:

## Observações
O que manter, o que evitar, problemas encontrados e decisões visuais.
```

---

## Paleta base da marca

Sempre respeitar a identidade roxa/violeta do projeto.

Paleta já conhecida:

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

Quando criar ou organizar assets, manter coerência com:

- roxo escuro;
- violeta premium;
- brilho neon;
- contraste forte;
- atmosfera divertida;
- identidade de açaí;
- casal/personagens;
- produto apetitoso;
- CTA WhatsApp.

---

## Taxonomia oficial do projeto

Use estas categorias principais:

```text
brand
product
character
background
ingredient
effect
delivery
button
icon
audio
video
reference
prompt
manifest
```

Subcategorias do projeto:

```text
logos-horizontal
logos-vertical
logos-roxa
logos-watermark
icons-interface
icons-sociais
characters-casal
characters-menina
characters-rapaz
characters-entregador
characters-casal-moto
background-home
background-cardapio
background-secoes
background-textura
effects-brilho
effects-folhas
effects-gotas
effects-particulas
effects-splash-acai
ingredients-gratis-liquidos
ingredients-gratis-solidos
ingredients-pagos
delivery-caixa
delivery-mochila
delivery-moto-protecao-chuva
buttons-cardapio
buttons-lojas
buttons-nossos-produtos
buttons-peca-agora
products-barca-premium
products-gigante-770ml
products-grande-550ml
products-medio-330ml
products-pequeno-200ml
products-especiais
products-marmitao-1l
```

---

## Versionamento

Use versionamento semântico:

```text
v1.0.0 → primeira versão aprovada
v1.1.0 → melhoria visual compatível
v1.0.1 → correção pequena
v2.0.0 → mudança grande de estilo/composição
```

Exemplo:

```text
char-casal-happy-front-1024w-v1.0.0.webp
char-casal-happy-front-1024w-v1.1.0.webp
char-casal-happy-front-1024w-v2.0.0.webp
```

Nunca sobrescreva um arquivo aprovado com outro conteúdo usando o mesmo nome.

---

## Regras para personagens

Personagens precisam manter consistência.

Para cada personagem, guardar:

```text
concept/
approved/
poses/
expressions/
delivery/
sprites/
reference/
prompt/
```

Exemplo:

```text
assets/images/characters/casal/
  reference/
  concept/
  approved/
  poses/
    front/
    side/
    holding-acai/
  expressions/
    happy/
    surprised/
    excited/
  prompt/
```

Para o projeto Nu Ki Açaí, os personagens principais são:

- casal apaixonado por açaí;
- menina sozinha;
- rapaz sozinho;
- entregador;
- casal na moto;
- moto com proteção contra chuva.

Regras específicas:

- manter roupas, traços e paleta consistentes;
- não mudar rosto sem criar nova versão major;
- manter o casal reconhecível;
- usar transparência quando o personagem for sobreposto;
- não usar personagem borrado;
- não usar personagem com mãos deformadas;
- não usar personagem com texto gerado pela IA;
- não aceitar asset com watermark;
- revisar olhos, dedos, boca, logotipo e proporções.

---

## Regras para produtos do cardápio

Produtos precisam parecer apetitosos e coerentes.

Cada produto deve ter:

```text
master/
derived/
reference/
prompt/
```

Produtos oficiais:

```text
barca-premium
gigante-770ml
grande-550ml
medio-330ml
pequeno-200ml
especiais
marmitao-1l
```

Cada produto deve ter variações:

```text
card
hero
thumbnail
detail
whatsapp-preview
```

Exemplo:

```text
img-product-gigante-770ml-card-480w-v1.0.0.webp
img-product-gigante-770ml-hero-1280w-v1.0.0.avif
img-product-gigante-770ml-whatsapp-preview-1200x630-v1.0.0.jpg
```

Regras:

- produto deve ter leitura rápida no celular;
- não pode parecer artificial demais;
- não pode ter fundo poluído;
- não pode esconder o tamanho/preço;
- não pode pesar demais;
- manter proporção consistente entre cards;
- criar imagens que valorizem conversão para WhatsApp.

---

## Regras para fundos

Fundos não devem competir com produto ou CTA.

Separar:

```text
home
cardapio
secoes
textura
```

Para cada fundo:

```text
master/
mobile/
desktop/
safe-area/
reference/
prompt/
```

Todo fundo deve ter versão mobile.

Regras:

- evitar peso excessivo;
- deixar área segura para textos;
- evitar contraste baixo atrás de título;
- exportar WebP/AVIF;
- não usar imagem gigante direto no CSS;
- testar no celular;
- garantir que CTA continue visível.

---

## Regras para efeitos visuais

Efeitos são complementares, não protagonistas.

Categorias:

```text
brilho
folhas
gotas
particulas
splash-acai
```

Regras:

- usar transparência;
- limitar quantidade;
- exportar leve;
- evitar excesso de partículas;
- não prejudicar leitura;
- não gerar travamento;
- respeitar `prefers-reduced-motion` quando animado;
- criar variantes pequenas, médias e grandes.

---

## Regras para delivery

Assets de delivery devem reforçar confiança e conveniência.

Categorias:

```text
caixa
mochila
moto-protecao-chuva
entregador
casal-moto
```

Regra importante do projeto:

A moto precisa ter **proteção contra chuva**.

Evitar:

- moto genérica sem proteção;
- entrega parecendo perigosa;
- personagem inconsistente;
- mochila sem identidade;
- imagem escura demais;
- excesso de detalhes no mobile.

---

## Regras para logos

Separar logos por uso:

```text
horizontal/
vertical/
roxa/
watermark/
icon/
transparent/
```

Regras:

- sempre ter versão com fundo transparente;
- manter master em alta qualidade;
- usar SVG quando possível;
- não rasterizar logo sem necessidade;
- não distorcer proporção;
- não aplicar sombra diferente em cada lugar;
- não trocar cor sem registrar nova variação.

Exemplos:

```text
logo-brand-horizontal-main-transparent-v1.0.0.svg
logo-brand-vertical-main-transparent-v1.0.0.png
logo-brand-roxa-solid-1024w-v1.0.0.png
logo-brand-watermark-purple-512w-v1.0.0.webp
```

---

## Regras para ícones

Ícones devem ser simples, legíveis e consistentes.

Categorias:

```text
interface
sociais
pagamentos
status
categorias
```

Preferir SVG.

Exemplos:

```text
icon-whatsapp-filled-48-v1.0.0.svg
icon-cart-outline-32-v1.0.0.svg
icon-location-filled-32-v1.0.0.svg
icon-acai-category-48-v1.0.0.svg
```

Regras:

- mesmo stroke;
- mesmo raio visual;
- mesmo estilo;
- não misturar ícones 3D com line icons sem motivo;
- manter contraste;
- usar `aria-hidden="true"` quando decorativo;
- usar texto acessível quando o ícone for funcional.

---

## Regras para botões

Sempre preferir botão real em HTML/CSS.

Use imagem apenas para:

- textura especial;
- ilustração;
- botão decorativo;
- campanha visual.

Botões principais do projeto:

```text
cardapio
lojas
nossos-produtos
peca-agora
whatsapp
```

Regras:

- CTA principal deve ser visível no mobile;
- botão precisa ter área mínima confortável;
- não usar imagem de texto sem alternativa;
- se imagem tiver texto, manter HTML acessível;
- botão de WhatsApp precisa gerar pedido real;
- não usar asset pesado para botão simples.

---

## Metadados mínimos por asset

Cada asset aprovado deve registrar:

```text
assetId
type
category
slug
name
version
status
author/tool
promptFile
createdAt
approvedAt
approvedBy
license
allowedUse
containsRealPerson
hasAlpha
width
height
format
optimized
```

Quando possível, registrar também:

```text
sha256
phash
sourceReferences
colorPalette
usageNotes
relatedComponent
relatedProduct
```

---

## Controle de direitos e LGPD

Marque qualquer asset com pessoa real, rosto real, referência pessoal ou material de terceiros.

Campos recomendados:

```json
{
  "containsRealPerson": false,
  "containsFace": false,
  "containsBrandThirdParty": false,
  "license": "owned",
  "allowedUse": ["web", "social", "whatsapp"],
  "attributionRequired": false,
  "rightsExpiry": null
}
```

Regras:

- não usar pessoa real sem autorização;
- não usar marca de terceiro sem necessidade;
- não usar imagens com watermark;
- não usar asset com origem desconhecida em produção;
- salvar referência e licença quando houver;
- se houver pessoa identificável, tratar como dado pessoal.

---

## Checklist de qualidade visual

Antes de aprovar um asset, verificar:

- [ ] o estilo combina com a marca;
- [ ] a paleta respeita o roxo/violeta;
- [ ] o asset funciona no celular;
- [ ] não há watermark;
- [ ] não há texto errado gerado pela IA;
- [ ] não há mãos/dedos deformados;
- [ ] não há rosto estranho;
- [ ] não há fundo poluído;
- [ ] o produto parece apetitoso;
- [ ] o personagem mantém consistência;
- [ ] o asset não compete com CTA;
- [ ] a imagem não está borrada;
- [ ] a transparência está correta;
- [ ] o recorte está limpo;
- [ ] o arquivo tem nome correto;
- [ ] existe prompt salvo;
- [ ] existe versão otimizada.

---

## Checklist técnico

Antes de publicar:

- [ ] arquivo está em `derived/`;
- [ ] formato é WebP/AVIF/SVG quando adequado;
- [ ] tamanho está correto;
- [ ] peso está adequado;
- [ ] imagem tem `width` e `height` no HTML;
- [ ] imagem tem `alt` quando informativa;
- [ ] imagem decorativa tem `alt=""`;
- [ ] não há caminho quebrado;
- [ ] não há imagem master no site;
- [ ] não há imagem gigante no mobile;
- [ ] não há duplicata desnecessária;
- [ ] não há arquivo com espaço/acento;
- [ ] não há `final2.png`;
- [ ] Lighthouse não acusa peso absurdo;
- [ ] o site continua rápido.

---

## Checklist de organização

Antes de encerrar a tarefa:

- [ ] assets estão nas pastas corretas;
- [ ] nomes seguem padrão;
- [ ] versões estão claras;
- [ ] rascunhos estão separados;
- [ ] referências não foram publicadas;
- [ ] masters estão preservados;
- [ ] derived está otimizado;
- [ ] prompts estão salvos;
- [ ] manifesto foi atualizado;
- [ ] README explica o conjunto;
- [ ] arquivos inúteis foram marcados para remoção;
- [ ] caminhos no código foram atualizados;
- [ ] nenhum asset aprovado foi sobrescrito.

---

## Anti-padrões proibidos

Evitar rigorosamente:

```text
assets/img/
assets/images/nova/
assets/teste/
assets/final/
assets/tudo/
assets/coisas/
```

Evitar arquivos:

```text
imagem.png
img.png
logo nova.png
acai certo.png
teste2.jpg
final-final.png
sem fundo certo.png
whatsapp button copy.png
```

Evitar comportamento:

- jogar todas as imagens em uma pasta só;
- usar master direto no site;
- perder prompt original;
- misturar logo com produto;
- misturar referência com produção;
- publicar draft;
- renomear sem atualizar código;
- apagar asset antigo sem versionamento;
- usar imagens enormes;
- usar PNG para tudo;
- gerar 30 variações sem curadoria;
- criar personagem diferente a cada prompt;
- deixar assets sem contexto.

---

## Fluxo ideal para novo asset IA

1. Definir objetivo do asset.
2. Verificar categoria correta.
3. Criar prompt em `assets/prompts/`.
4. Gerar variações.
5. Fazer curadoria humana.
6. Escolher melhores versões.
7. Salvar master.
8. Exportar derived.
9. Otimizar peso.
10. Nomear corretamente.
11. Atualizar manifesto.
12. Testar no site.
13. Aprovar ou rejeitar.
14. Publicar apenas versão aprovada.

---

## Fluxo para o agente Codex/Claude

Quando receber tarefa de organizar assets, o agente deve:

1. Mapear a estrutura atual.
2. Identificar arquivos soltos.
3. Identificar duplicatas e nomes ruins.
4. Propor estrutura de pastas.
5. Criar ou atualizar README.
6. Criar ou atualizar manifesto.
7. Renomear com segurança.
8. Atualizar referências no HTML/CSS/JS.
9. Separar master, derived e reference.
10. Sugerir otimizações.
11. Não apagar sem listar antes.
12. Entregar relatório final.

---

## Comando/prompt para auditoria de assets

Use este prompt com Codex/Claude:

```text
Audite a pasta assets do projeto seguindo a skill Organização de Assets IA.

Objetivo:
- encontrar arquivos fora do padrão;
- separar master, derived e reference;
- identificar duplicatas;
- verificar nomes com espaços, acentos ou termos genéricos;
- verificar imagens pesadas;
- verificar caminhos quebrados no HTML/CSS/JS;
- sugerir estrutura corrigida;
- atualizar README e MANIFEST.assets.json quando seguro.

Regras:
- não apagar arquivos sem listar;
- não sobrescrever assets aprovados;
- não usar master diretamente no site;
- manter nomes em slug;
- preservar versões;
- entregar relatório com arquivos modificados.
```

---

## Comando/prompt para organizar produtos

```text
Organize os assets de produtos do cardápio Nu Ki Açaí.

Produtos oficiais:
- barca-premium
- gigante-770ml
- grande-550ml
- medio-330ml
- pequeno-200ml
- especiais
- marmitao-1l

Para cada produto:
- criar pastas master, derived, reference e prompt;
- padronizar nomes;
- separar imagens de card, hero, detalhe e WhatsApp preview;
- otimizar formatos para WebP/AVIF;
- atualizar MANIFEST.assets.json;
- verificar se o código aponta para derived, nunca para master.
```

---

## Comando/prompt para organizar personagens

```text
Organize os assets de personagens do projeto Nu Ki Açaí.

Personagens:
- casal
- menina
- rapaz
- entregador
- casal-moto

Regras:
- preservar consistência visual;
- separar concept, approved, poses, expressions, delivery, sprites, reference e prompt;
- marcar versões aprovadas;
- rejeitar imagens com mãos deformadas, watermark ou estilo inconsistente;
- garantir transparência nos assets usados sobre fundos;
- atualizar manifesto.
```

---

## Comando/prompt para organizar fundos e efeitos

```text
Organize fundos e efeitos visuais.

Categorias:
- backgrounds/home
- backgrounds/cardapio
- backgrounds/secoes
- backgrounds/textura
- effects/brilho
- effects/folhas
- effects/gotas
- effects/particulas
- effects/splash-acai

Regras:
- separar master, derived, reference e prompt;
- criar versões mobile e desktop para fundos;
- otimizar WebP/AVIF;
- manter transparência em efeitos;
- evitar excesso de peso;
- garantir que fundos não prejudiquem leitura e CTA.
```

---

## Comando/prompt para gerar README de assets

```text
Crie ou atualize assets/README.md explicando:

- estrutura oficial da pasta assets;
- regras de nomeação;
- diferença entre master, derived e reference;
- categorias do projeto Nu Ki Açaí;
- como adicionar novo asset;
- como salvar prompts;
- como versionar;
- como aprovar;
- como publicar no site;
- anti-padrões proibidos.
```

---

## Comando/prompt para corrigir caminhos no código

```text
Verifique HTML, CSS e JS do projeto e corrija referências de assets.

Regras:
- usar apenas arquivos de assets/.../derived/ para produção;
- não apontar para master;
- não apontar para reference;
- corrigir nomes com espaços/acento;
- manter imagens com width/height quando possível;
- adicionar alt em imagens informativas;
- preservar layout mobile-first;
- testar se não há caminhos quebrados.
```

---

## Exemplo de README curto para pasta de produto

```md
# Produto — Grande 550ml

## Uso
Imagens do produto Grande 550ml para cardápio, hero, detalhe e preview de WhatsApp.

## Estrutura
- master: arquivos originais em alta qualidade
- derived: arquivos otimizados para site
- reference: imagens de inspiração/contexto
- prompt: prompts usados na geração IA

## Status
Versão aprovada atual: v1.0.0

## Observações
Manter estilo premium roxo/violeta, produto apetitoso e boa leitura no mobile.
```

---

## Exemplo de manifesto simples por produto

```json
{
  "product": "grande-550ml",
  "currentApprovedVersion": "1.0.0",
  "assets": [
    {
      "assetId": "img_product_grande_550ml_card_001",
      "file": "assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.webp",
      "status": "approved",
      "usage": "product-card",
      "format": "webp",
      "optimized": true
    }
  ]
}
```

---

## Regras para integração com HTML/CSS

HTML recomendado:

```html
<picture>
  <source
    srcset="assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.avif"
    type="image/avif"
  >
  <source
    srcset="assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.webp"
    type="image/webp"
  >
  <img
    src="assets/images/products/grande-550ml/derived/img-product-grande-550ml-card-768w-v1.0.0.png"
    alt="Açaí Grande 550ml"
    width="768"
    height="768"
    loading="lazy"
    decoding="async"
  >
</picture>
```

CSS recomendado:

```css
.product-card__image {
  width: 100%;
  height: auto;
  object-fit: contain;
}
```

Evitar:

```css
background-image: url("../assets/images/produto-final-master-gigante.png");
```

Principalmente quando a imagem for pesada.

---

## Regras de performance para assets

Todo asset visual deve respeitar performance mobile.

Metas práticas:

```text
thumbnail produto: até 80 KB, ideal menor
card produto: até 150 KB
hero mobile: até 300 KB
background mobile: até 350 KB
ícone SVG: o menor possível
efeito visual: até 100 KB
```

A meta pode variar, mas o agente deve sempre tentar reduzir peso sem destruir qualidade.

---

## Regras de acessibilidade

Todo asset informativo precisa de alternativa textual.

Exemplos:

```html
<img src="..." alt="Açaí médio 330ml com banana, morango e granola">
```

Asset decorativo:

```html
<img src="..." alt="" aria-hidden="true">
```

Não usar imagem com texto importante sem repetir esse texto em HTML real.

---

## Regras para WhatsApp e conversão

Assets que aparecem perto do botão de pedido devem ajudar a converter.

Regras:

- produto precisa ser claro;
- CTA precisa ser visível;
- imagem não pode atrasar carregamento;
- preview de WhatsApp deve ter boa proporção;
- nome do produto deve bater com a mensagem do pedido;
- asset não pode confundir tamanho, adicionais ou preço;
- imagens de combo devem mostrar benefício visual.

---

## Auditoria de duplicatas

Duplicatas possíveis:

- mesmo asset com nome diferente;
- mesmo produto em pasta errada;
- imagem master copiada para derived;
- versão antiga ainda publicada;
- logo repetido em várias pastas;
- arquivo exportado várias vezes sem controle.

Antes de remover, sempre gerar lista:

```text
possível duplicata:
- arquivo A:
- arquivo B:
- motivo:
- recomendação:
```

Nunca apagar automaticamente sem confirmação quando houver risco de perda.

---

## Auditoria de caminhos quebrados

O agente deve procurar referências em:

```text
.html
.css
.js
.jsx
.tsx
.json
.md
```

Procurar por:

```text
assets/
img/
images/
background
url(
src=
```

Corrigir apenas quando tiver certeza.

---

## Relatório final obrigatório

Ao finalizar uma tarefa com assets, entregar:

```md
## Relatório — Organização de Assets IA

### O que foi feito
- ...

### Pastas criadas
- ...

### Arquivos renomeados
- ...

### Arquivos movidos
- ...

### Arquivos que precisam de revisão humana
- ...

### Caminhos atualizados no código
- ...

### Problemas encontrados
- ...

### Próximos passos recomendados
- ...
```

---

## Critério de sucesso

A skill foi aplicada corretamente quando:

- assets estão fáceis de encontrar;
- nomes são previsíveis;
- pastas estão separadas por função;
- prompts estão documentados;
- versões estão claras;
- o site usa derived, não master;
- produtos e personagens mantêm consistência;
- arquivos estão leves;
- não há caminhos quebrados;
- qualquer IA/Codex/Claude consegue continuar o projeto sem perguntar “onde está tal imagem?”.
