---
name: carrossel-viral
description: Cria carrosséis de Instagram no método editorial de alta retenção (capa de quebra de padrão, armadilha de retenção, entrega técnica, gatilhos de salvamento e CTA por palavra-chave nos comentários), com design de revista e exportação em PNG/PDF. Serve para qualquer nicho ou operação (infoproduto, serviço local, B2B, e-commerce, profissional liberal). Use quando pedirem "carrossel viral", "carrossel no estilo editorial", "carrossel que gera comentário/salvamento", "carrossel de newsjacking" ou um carrossel para vender um produto, evento ou serviço.
---

# Carrossel Viral (método editorial de retenção)

Produz carrosséis prontos para postar: tese, roteiro slide a slide, copy, design em HTML/CSS, PNGs 1080×1350, PDF e legenda.

O método foi destilado de perfis brasileiros de análise de marcas e marketing que fazem carrosséis com dezenas de milhares de curtidas e milhares de comentários. **Use o método, não a identidade de ninguém**: nunca copie nome, @, assinatura, fotos ou textos de outro perfil. A marca é sempre a do usuário.

Antes de escrever, leia:
- `references/estrategia.md`: anatomia do post, fórmulas de capa, tipos de slide e CTA.
- `references/design.md`: design system (tipografia, cores, grid, variações de capa) e como usar os templates.

## 1. Briefing (pergunte só o que faltar)

- **Nicho e operação**: o que o perfil vende (produto, serviço, evento, mentoria, loja) e para quem.
- **Objetivo do post**: alcance/compartilhamento, salvamento, comentários com palavra-chave (lead), ou venda direta (evento, lote, oferta).
- **Oferta e palavra-chave**: se houver CTA de comentário, qual produto ele leva e qual palavra (uma palavra curta em caixa alta, ex.: `MAQUINA`, `PLANO`, `LISTA`).
- **Marca**: @, nome curto para o cabeçalho, cor de destaque (padrão: vermelho-laranja) e se usa o tema claro, escuro ou os dois.
- **Tema**: se o usuário não trouxer, proponha 3 teses usando as fórmulas de `estrategia.md` (uma de newsjacking, uma de "morte/fim de algo", uma de guia definitivo) e deixe escolher.
- **Imagens**: fotos próprias, links, ou deixar espaços marcados para o usuário trocar. Não invente prints de perfis, números ou resultados.

Se o projeto tiver arquivo de marca (`brand.md`, `design.md`, `product-marketing.md`), leia antes de perguntar.

## 2. Tese e pesquisa

Todo carrossel defende **uma tese contraintuitiva** ("ter 100 mil seguidores pode ser um péssimo negócio"). Escreva-a em uma frase antes do roteiro.

- Dados, datas, números e citações precisam de fonte real. Pesquise quando possível; se não confirmar, marque `[VERIFICAR]` e avise o usuário. Nunca invente estatística, "estudo" ou declaração de pessoa real.
- Newsjacking com pessoa ou marca famosa: fale do fato público e extraia a lição de negócio. Não atribua falas, intenções ou números que não estejam em fonte confiável.

## 3. Roteiro

Siga a anatomia de `estrategia.md` (padrão de 10 slides, aceite de 7 a 12). Para cada slide entregue: tipo de slide, título, corpo, imagem sugerida e tema (claro, escuro ou destaque).

Mostre o roteiro em texto para aprovação **antes** de desenhar, a não ser que o usuário peça tudo de uma vez.

## 4. Design e renderização

1. Crie uma pasta de trabalho (ex.: `carrossel-<tema>/slides/`) e copie `assets/templates/base.css` para ela.
2. Para cada slide, parta do template correspondente em `assets/templates/` (lista em `design.md`) e salve como `slide-01.html`, `slide-02.html`… Troque `{{HANDLE}}`, `{{TAG}}`, `{{DATA}}` e o conteúdo. A paginação (bolinhas) é marcada pelo índice do slide.
3. Imagens: use arquivos locais ou URLs que o usuário passou. Sem imagem, deixe o bloco `.ph` (placeholder com a descrição da foto ideal).
4. Renderize:
   ```bash
   bash <dir-da-skill>/scripts/render.sh carrossel-<tema>/slides
   ```
   Gera `png/slide-XX.png` (1080×1350) e `carrossel.pdf`.
5. Abra 2 ou 3 PNGs (capa, um slide denso e o CTA) e confira: texto cortado, sobreposição, contraste, hierarquia. Corrija e renderize de novo.

## 5. Legenda

Estrutura: gancho de 1 linha diferente da capa → 2 ou 3 linhas reforçando a tese → CTA repetido (palavra-chave ou "salva e manda pra quem precisa") → 3 a 5 hashtags de nicho, no máximo.

## 6. Checklist final

- [ ] Capa entende-se em 1 segundo, sem precisar ler o subtítulo.
- [ ] Slides 2 e 3 prometem algo que só será entregue depois (laço aberto).
- [ ] Cada slide tem uma ideia só e um destaque de cor no máximo por bloco.
- [ ] Existe pelo menos um slide "salvável" (framework, checklist, anatomia, lista).
- [ ] CTA único e claro; se for por comentário, a palavra aparece em caixa alta e entre aspas.
- [ ] Nada de dado inventado; pendências marcadas com `[VERIFICAR]`.
- [ ] Marca do usuário, sem nome, @ ou assinatura de terceiros.
