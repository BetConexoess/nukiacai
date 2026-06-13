---
name: organizar-assets
description: Organiza, classifica e audita imagens do projeto Nu Ki Acai, preservando originais, planejando nomes, recortando, otimizando, atualizando referencias e gerando relatorio. Use esta skill somente para tarefas relacionadas a organizacao de assets de imagem dentro deste repositorio. Nunca mova, renomeie, recorte, converta, otimize ou apague imagens sem aprovacao explicita do usuario.
---

# Skill: organizar-assets

Use esta skill para organizar imagens do projeto nuKIacai dentro da pasta `assets/`, preservando originais, atualizando referencias e evitando alteracoes destrutivas.

## Escopo obrigatorio

- Trabalhar somente dentro do projeto.
- Nao acessar, copiar, mover, renomear ou apagar arquivos fora do projeto.
- Nao fazer commit.
- Nao enviar nada ao GitHub.
- Nao apagar imagens originais.
- Nao alterar precos.
- Nao alterar numero do WhatsApp.

## Fluxo obrigatorio

Execute as etapas nesta ordem:

1. Inventariar
   - Confirmar pasta atual e branch Git.
   - Ler a estrutura do projeto.
   - Ler `package.json`, se existir, e identificar a tecnologia usada.
   - Localizar imagens PNG, JPG, JPEG, WebP, AVIF, SVG e GIF.
   - Identificar referencias no HTML, CSS, JavaScript, Markdown e demais arquivos relevantes.
   - Criar ou atualizar `assets/manifests/assets-inventory.md` antes de mover qualquer arquivo.

2. Classificar
   - Classificar cada imagem por uso e conteudo.
   - Usar as categorias adotadas pelo projeto quando houver arquivos correspondentes:
     - `assets/logos/`
     - `assets/characters/`
     - `assets/backgrounds/`
     - `assets/effects/`
     - `assets/ingredients/`
     - `assets/delivery/`
     - `assets/buttons/`
     - `assets/products/`
     - `assets/originals/`
     - `assets/manifests/`
   - Criar subpastas somente quando existirem arquivos correspondentes.
   - Marcar como pendencia qualquer imagem que nao possa ser classificada com seguranca.

3. Preservar originais
   - Antes de recortar, otimizar, converter ou renomear, copiar o arquivo original para `assets/originals/`.
   - Nunca sobrescrever a unica versao original.
   - Nunca apagar os arquivos originais.

4. Planejar nomes
   - Planejar o nome final antes de mover.
   - Usar nomes com letras minusculas, sem espacos, sem acentos, com palavras separadas por hifen.
   - Usar nomes descritivos e preservar a extensao correta quando nao houver conversao aprovada.
   - Exemplo: `produto-gigante-770ml-frontal.png`.

5. Organizar
   - Mover ou renomear somente depois de apresentar o plano e receber aprovacao.
   - Manter as imagens dentro das categorias aprovadas.
   - Registrar cada origem e destino no inventario.

6. Recortar
   - Recortar somente depois de preservar o original.
   - Remover apenas espacos vazios ou transparencia excessiva.
   - Preservar margem de seguranca.
   - Nao cortar maos, cabelo, frutas, folhas, respingos, sombras, produtos, letras ou partes dos personagens.
   - Nao distorcer a proporcao.
   - Preservar transparencia.
   - Nao fazer recorte automatico quando nao houver seguranca.
   - Gerar imagem comparativa antes/depois para revisao.
   - Registrar recortes complexos como pendencia em vez de danificar a imagem.

7. Otimizar
   - Otimizar sem comprometer qualidade visual.
   - Preservar transparencia quando existir.
   - Registrar no inventario se a imagem foi otimizada.
   - Nao instalar dependencias sem aprovacao.

8. Atualizar referencias
   - Atualizar imports, `src`, `srcset`, `href`, CSS `url()` e referencias em JavaScript.
   - Procurar referencias antigas apos mover ou renomear.
   - Confirmar que nenhuma imagem usada pelo site ficou quebrada.

9. Testar
   - Executar build, lint e testes disponiveis.
   - Se nao houver scripts de teste, registrar essa ausencia no relatorio.
   - Fazer verificacao manual de caminhos e arquivos referenciados.

10. Revisar
    - Revisar `git diff`.
    - Confirmar que nenhum arquivo fora do escopo foi alterado.
    - Confirmar que originais foram preservados.
    - Confirmar que referencias antigas nao permanecem no codigo ativo.

11. Gerar relatorio
    - Atualizar `assets/manifests/assets-inventory.md`.
    - Informar nome original, nome final, pasta final, dimensoes, formato, transparencia, local de uso, recortada ou nao, otimizada ou nao e observacoes.
    - Listar pendencias e imagens que exigem revisao manual.

## Regra de parada

Antes de mover, renomear, recortar, otimizar, converter ou apagar qualquer imagem, apresente o inventario e o plano encontrado ao usuario e aguarde aprovacao explicita.
