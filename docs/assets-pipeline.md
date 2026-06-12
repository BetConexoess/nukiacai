# Pipeline de Assets — Nu Ki Açaí

Documentação completa do pipeline de processamento de imagens do projeto Nu Ki Açaí.

---

## Visão Geral

O pipeline classifica, processa e organiza todos os assets visuais do projeto em uma estrutura padronizada. Cada imagem passa por regras específicas dependendo da sua categoria.

---

## Quais imagens recebem remoção de fundo

As seguintes categorias têm o fundo **removido automaticamente** via `rembg`:

| Categoria | Exemplos | Destino Final |
|---|---|---|
| `product` | Copos de açaí, tigelas, barcas, marmitão | `assets/images/products/` |
| `fruit` | Morango, banana, kiwi, manga, abacaxi | `assets/images/ingredients/fruits/` |
| `topping` | Granola, castanha, coco ralado, chocolate, nutella | `assets/images/ingredients/toppings/` |
| `leaf` | Folhas tropicais, palmeiras, decorações vegetais | `assets/images/leaves/` |
| `character` | Personagens animados da marca | `assets/images/characters/` |
| `delivery-object` | Moto, caixa, mochila de entrega | `assets/images/delivery/` |

> [!IMPORTANT]
> Imagens que **já possuem transparência** (canal alpha detectado) **NÃO passam pelo rembg**. São apenas convertidas para WebP preservando o alpha.

---

## Quais imagens NÃO recebem remoção de fundo

| Categoria | Exemplos | Motivo |
|---|---|---|
| `background` | Fotos de praia, pôr do sol, céu | São fundos de seção — precisam do fundo inteiro |
| `texture` | Areia, texturas decorativas | São padrões de superfície |
| `effect` | Splashes, gotas, partículas | Geralmente já têm transparência |
| `icon` | Ícones SVG | Formato vetorial, sem necessidade |
| `animation` | Lottie JSON, WebM | Formato de animação, sem conversão |

---

## Formatos finais

| Tipo | Formato | Qualidade |
|---|---|---|
| Imagens com transparência | `.webp` (com alpha) | 85% |
| Imagens opacas (backgrounds) | `.webp` (RGB) | 85% |
| Ícones | `.svg` | Original |
| Animações | `.json` / `.lottie` / `.webm` | Original |

---

## Dimensões máximas

| Categoria | Largura Máxima |
|---|---|
| Backgrounds / Texturas | 1920px |
| Produtos hero | 1200px |
| Cards de produto | 1000px |
| Frutas / Folhas / Efeitos / Toppings | 700px |
| Ícones SVG | Original (vetorial) |

---

## Estrutura de diretórios

```
assets/
├── images/
│   ├── _raw/              ← Cópias intactas dos originais
│   ├── _review/            ← Arquivos duvidosos para revisão manual
│   ├── backgrounds/        ← Fundos de seção (WebP sem remoção)
│   ├── home/               ← Hero backgrounds
│   ├── textures/           ← Texturas decorativas
│   ├── products/           ← Produtos com fundo removido
│   ├── ingredients/
│   │   ├── fruits/         ← Frutas com fundo removido
│   │   └── toppings/       ← Toppings com fundo removido
│   ├── leaves/             ← Folhas com fundo removido
│   ├── effects/            ← Splashes, gotas, partículas
│   ├── characters/         ← Personagens
│   └── delivery/           ← Elementos de delivery
├── icons/
│   ├── interface/          ← Ícones de UI
│   ├── social/             ← WhatsApp, Instagram
│   └── badges/             ← Selos e tags
└── animations/
    ├── lottie/             ← Arquivos .json
    └── webm/               ← Vídeos leves
```

---

## Como usar o pipeline

### 1. Instalar dependências

```bash
pip install Pillow rembg onnxruntime
```

> [!NOTE]
> Na primeira execução do `rembg`, o modelo U2-Net (~170 MB) será baixado automaticamente. Precisa de internet.

### 2. Auditar assets

```bash
python scripts/audit-assets.py
```

Gera `reports/assets-report.json` e `reports/assets-report.csv` sem modificar nenhum arquivo.

### 3. Processar assets

```bash
python scripts/process-assets.py
```

Cria a estrutura de pastas, copia originais para `_raw/`, processa cada arquivo conforme sua categoria.

### 4. Gerar relatório visual

```bash
python scripts/generate-asset-report.py
```

Gera `reports/assets-gallery.html` com galeria interativa.

### 5. Revisar visualmente

```bash
start reports/assets-gallery.html
```

---

## Como revisar a galeria

1. Abra `reports/assets-gallery.html` no navegador
2. Use os **filtros por categoria** para navegar
3. Clique em **🔍 Review** para ver apenas os arquivos duvidosos
4. Para cada card, compare:
   - **Original** (miniatura à esquerda) vs **Final** (miniatura à direita)
   - **Status**: ✅ OK, 🔍 Review, ❌ Erro
   - **Dimensões** e **peso** antes/depois
   - **Observações** em amarelo

---

## Como corrigir arquivos ruins

### Arquivo em `_review/`

1. Abra a imagem original em `assets/images/_raw/[categoria]/`
2. Edite manualmente no editor de imagens (GIMP, Photoshop, etc.)
3. Salve como `.webp` com transparência na pasta de destino correta
4. Remova o arquivo de `_review/`

### Recorte com serrilhado

1. Abra o original e remova o fundo manualmente
2. Use *feather* de 1-2px na borda para suavizar
3. Salve como WebP com transparência

### Background que perdeu o fundo

Isso **não deveria acontecer** (backgrounds não passam por rembg). Se aconteceu:
1. Use a cópia original em `assets/images/_raw/background/`
2. Converta manualmente para WebP

---

## Como adicionar novas imagens

### Opção A — Usar o pipeline completo

1. Coloque as novas imagens na pasta `Downloads/` (ou numa subpasta descritiva)
2. Execute a auditoria: `python scripts/audit-assets.py`
3. Revise o relatório JSON para confirmar a classificação
4. Execute o processamento: `python scripts/process-assets.py`
5. Gere o relatório: `python scripts/generate-asset-report.py`
6. Confira visualmente na galeria

### Opção B — Manualmente

1. Coloque a imagem original em `assets/images/_raw/[categoria]/`
2. Processe manualmente (remover fundo se necessário, converter WebP)
3. Salve na pasta de destino correta com:
   - Largura dentro dos limites da tabela acima
   - Formato `.webp`
   - Transparência se for produto/fruta/folha

---

## Referência de categorias

| Palavra-chave no nome | Categoria |
|---|---|
| `raw-bg-` | background |
| `raw-textura-` | texture |
| `raw-produto-` | product |
| `raw-hero-` | product |
| `raw-fx-` | effect |
| `raw-leaf-` | leaf |
| `raw-topping-` | topping |
| `icon-` | icon |
| `lottie-` | animation |
| `istockphoto-` | review |

| Pasta pai | Categoria |
|---|---|
| abacaxi, banana, kiwi, manga, morangos | fruit |
| castanha, coco-ralado, chocolate, nutella, ingredientes | topping |
| folhas palmeiras, folhas-moldura, folhas-tropicais | leaf |
| particulas, water | effect |
| frutas-caindo | effect |
