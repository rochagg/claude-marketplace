# Design system: carrossel editorial

O visual parece uma revista digital: fundo chapado (claro, escuro ou cor de marca), tipografia grotesca grande e apertada, uma única cor de destaque, fotos editoriais de retrato e um cabeçalho fino repetido em todos os slides. O "chamativo" vem do contraste e da alternância, não de enfeites.

## Princípios

1. **Alternância de fundo** a cada 1 ou 2 slides (claro → escuro → claro → escuro → cor de marca). A mudança de cor é o que faz a pessoa sentir que "avançou".
2. **Uma cor de destaque** (padrão `#ff3d0f`), usada em uma expressão por título e em fechos de raciocínio. No escuro, o destaque secundário é o amarelo-manteiga (`#f3efb4`).
3. **Cabeçalho de revista** em todo slide: tag/marca à esquerda, @ no centro, edição ("Outubro 2026 ®") à direita, 19px. Dá cara de publicação séria.
4. **Paginação em bolinhas** na base, mostrando que há mais slides.
5. **Fotos de retrato editoriais**: rosto, cor de fundo sólida e quente, luz de estúdio, olhar para a câmera. Cultura pop e famosos geram reconhecimento instantâneo; use só imagens com direito de uso.
6. **Respiro**: o texto do slide 2 fica em cima e a lista "O que muda" no rodapé, com vazio no meio. O vazio é intencional.
7. Nada de ícones, gradientes decorativos, emojis no design, sombras pesadas ou molduras. A exceção é o "✕" na lista de mitos e as setas "→".

## Tokens (em `assets/templates/base.css`)

| Token | Padrão | Uso |
|---|---|---|
| `--accent` | `#ff3d0f` | destaque, fundo do slide de case, ✕ |
| `--butter` | `#f3efb4` | destaque em fundo escuro |
| `--ink` | `#0b0b12` | fundo escuro e texto no claro |
| `--paper` | `#f1f1ef` | fundo claro |
| `--display` | Anton | título da capa de impacto (caixa alta condensada) |
| `--sans` | Inter Tight | títulos e corpo dos slides internos (peso 500 nos títulos, 400 no corpo, 800 nos termos) |
| `--serif` | Instrument Serif | capa editorial |

Para adaptar à marca do usuário, troque `--accent` (e, se quiser, `--butter`) e mantenha o resto. Cores que funcionam no método: vermelho-laranja, azul elétrico, verde-limão, magenta. Evite tons pastel como destaque.

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

Placeholders: `{{TAG}}` (texto do canto esquerdo, ex.: nome da marca ou série), `{{HANDLE}}`, `{{DATA}}` (mês e ano), `{{I}}` (número do slide) e `{{N}}` (total de slides). Blocos `.ph` são espaços de imagem com a descrição da foto ideal; troque por `<img class="img" src="..." style="height:400px">` (ou `class="full-bleed"` nas capas).

## Ritmo sugerido de fundos (10 slides)

`capa (foto) → claro → escuro → claro → escuro → cor de marca → escuro → claro → escuro → claro (CTA)`

## Erros comuns

- Mais de uma cor de destaque por slide ou destaque em frases inteiras: perde o efeito.
- Título interno em caixa alta: só a capa usa caixa alta.
- Texto pequeno demais para caber mais coisa: corte o texto, não a fonte (mínimo 30px).
- Foto genérica de banco de imagem (aperto de mão, pessoa apontando para gráfico): use retrato com personalidade ou cena real.
