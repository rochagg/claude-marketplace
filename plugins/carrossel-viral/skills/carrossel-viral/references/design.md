# Design system: carrossel editorial

O visual parece uma revista digital: fundo chapado (claro, escuro ou cor de marca), tipografia grotesca grande e apertada, uma única cor de destaque, fotos editoriais de retrato e um cabeçalho fino repetido em todos os slides. O "chamativo" vem do contraste e da alternância, não de enfeites.

## Princípios

As cores e fontes são **sempre as do projeto** (ver "Identidade visual" no SKILL.md). Os princípios abaixo descrevem como usá-las; as cores das referências originais não são padrão.

1. **Alternância de fundo** a cada 1 ou 2 slides (claro → escuro → claro → escuro → cor da marca). A mudança de cor é o que faz a pessoa sentir que "avançou".
2. **Uma cor de destaque** (a principal da marca, `--accent`), usada em uma expressão por título e em fechos de raciocínio. No escuro, o destaque secundário é `--butter` (a segunda cor da marca ou um tom claro da principal).
3. **Cabeçalho de revista** em todo slide: tag/marca à esquerda, @ no centro, edição ("Outubro 2026 ®") à direita, 19px. Dá cara de publicação séria.
4. **Paginação em bolinhas** na base, mostrando que há mais slides.
5. **Fotos de retrato editoriais**: rosto, fundo de cor sólida, luz de estúdio, olhar para a câmera. Prefira fotos cujo fundo ou roupa conversem com a paleta da marca. Use só imagens com licença de uso (skill `imagens-gratis`).
6. **Respiro**: o texto do slide 2 fica em cima e a lista "O que muda" no rodapé, com vazio no meio. O vazio é intencional.
7. Nada de ícones, gradientes decorativos, emojis no design, sombras pesadas ou molduras. A exceção é o "✕" na lista de mitos e as setas "→".

## Tokens

`base.css` traz só valores neutros de segurança. Cada projeto tem o seu `tema.css` (modelo em `assets/templates/tema-exemplo.css`), carregado depois do `base.css`:

| Token | Vem de | Uso |
|---|---|---|
| `--accent` / `--on-accent` | cor principal da marca / texto legível sobre ela | destaque, fundo do slide de case, ✕ |
| `--butter` | 2ª cor da marca ou tom claro da principal | destaque em fundo escuro |
| `--ink` | escuro da marca ou quase-preto puxado para ela | fundo escuro e texto no claro |
| `--paper` | claro/off-white da marca | fundo claro |
| `--hl-light` / `--hl-dark` | opcionais, quando `--accent` não tem contraste como texto | destaque de texto |
| `--sans` | fonte de texto da marca (padrão Inter Tight) | títulos e corpo dos slides internos |
| `--display` | fonte condensada/display da marca (padrão Anton) | título da capa de impacto |
| `--serif` | serifa da marca (padrão Instrument Serif) | capa editorial |

Marcas com cor principal clara (amarelo, verde-limão, ciano) funcionam melhor com ela de fundo (slide `destaque`, pílulas) e uma versão mais escura para texto em `--hl-light`. Marcas com cor principal escura (marinho, vinho) usam a cor como `--ink` e escolhem a segunda cor como `--accent`.

Tamanhos de referência no canvas 1080×1350: título interno 60–78px, corpo 38px, listas 31–33px, título de capa 100–120px, margem lateral 48px.

## Templates (`assets/templates/`)

| Arquivo | Uso | Fundo |
|---|---|---|
| `capa-impacto.html` | capa padrão: foto sangrada, @ em pílula, título Anton em caixa alta com a última linha na cor de destaque, subtítulo "→" | foto + degradê |
| `capa-editorial.html` | capa sóbria/analítica: serifa, primeira frase em itálico na cor de destaque | foto escura |
| `capa-marcador.html` | capa "guia definitivo": caixas pretas atrás do texto + meme/imagem pop | claro |
| `texto-claro.html` | armadilha de retenção: afirmação + "O que muda:" com setas | claro |
| `texto-escuro.html` | fonte/autoridade + frase de fecho amarela | escuro |
| `imagem-claro.html` | título + imagem + lista ✕ (mitos) ou numerada | claro |
| `imagem-escuro.html` | entrega técnica com termos nomeados | escuro |
| `destaque.html` | prova/case em cartão branco, conclusões sublinhadas | cor de marca |
| `grade-anatomia.html` | framework salvável: 8 miniaturas + etapas | escuro |
| `cta.html` | data/oferta, provocação, foto e pílula "Comenta PALAVRA" | claro |

Placeholders: `{{TAG}}` (texto do canto esquerdo, ex.: nome da marca ou série), `{{HANDLE}}`, `{{DATA}}` (mês e ano), `{{I}}` (número do slide) e `{{N}}` (total de slides). Blocos `.ph` trazem a descrição da foto ideal (use-a como termo de busca na skill `imagens-gratis`) e **sempre** são trocados por `<img class="img" src="..." style="height:400px">` (ou `class="full-bleed"` nas capas).

## Ritmo sugerido de fundos (10 slides)

`capa (foto) → claro → escuro → claro → escuro → cor da marca → escuro → claro → escuro → claro (CTA)`

## Erros comuns

- Usar a paleta das referências em vez da do projeto.
- Entregar slide com espaço de imagem vazio.
- Mais de uma cor de destaque por slide ou destaque em frases inteiras: perde o efeito.
- Título interno em caixa alta: só a capa usa caixa alta.
- Texto pequeno demais para caber mais coisa: corte o texto, não a fonte (mínimo 30px).
- Foto genérica de banco de imagem (aperto de mão, pessoa apontando para gráfico): use retrato com personalidade ou cena real.
