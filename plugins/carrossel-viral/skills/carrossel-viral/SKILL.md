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
- **Marca**: @ e nome curto para o cabeçalho. A paleta e as fontes saem da identidade visual do projeto (seção 2), nunca de um padrão da skill.
- **Tema**: se o usuário não trouxer, proponha 3 teses usando as fórmulas de `estrategia.md` (uma de newsjacking, uma de "morte/fim de algo", uma de guia definitivo) e deixe escolher.
- **Imagens**: pergunte só se há fotos próprias (equipe, produto, clientes com autorização). O resto você busca em bancos gratuitos (seção 5). Não invente prints de perfis, números ou resultados.

Se o projeto tiver arquivo de marca (`brand.md`, `design.md`, `product-marketing.md`), leia antes de perguntar.

## 2. Identidade visual do projeto (obrigatória)

O método é fixo, mas **as cores e fontes são sempre as do projeto**. Nunca use a paleta das referências (vermelho-laranja, azul-noite e amarelo-manteiga) a não ser que seja a paleta do próprio projeto.

Descubra a identidade nesta ordem e pare na primeira que responder:
1. Arquivos de marca no projeto: `brand.md`, `design.md`, manual de marca em PDF, `tailwind.config.*`, variáveis CSS (`:root { --... }`), `theme.*`, tokens do design system.
2. Site do projeto (local ou publicado): leia o CSS e extraia cores e fontes reais.
3. Logo ou posts já publicados: leia a imagem e identifique as cores dominantes.
4. Pergunte ao usuário (cores em hex e fontes). Se não houver identidade nenhuma, proponha 2 opções e espere a escolha.

Mapeie para os tokens de `assets/templates/tema-exemplo.css`:
- `--accent`: cor principal da marca. `--on-accent`: texto legível sobre ela.
- `--butter`: segunda cor da marca (ou um tom claro da principal) para destaque no fundo escuro.
- `--ink` e `--paper`: os escuros e claros da marca (ou quase-preto e off-white puxados para a cor dela).
- Fontes da marca em `--sans` (e `--display`/`--serif`, se houver). Sem fonte de marca, mantenha as padrões.

Confira o contraste: texto destacado precisa de pelo menos 3:1 sobre o fundo (títulos grandes) e 4,5:1 nos textos de corpo. Se a cor da marca não passar (ex.: amarelo sobre branco), defina `--hl-light`/`--hl-dark` com um tom que passe e use a cor original só como fundo.

Salve o resultado como `tema.css` numa pasta reutilizável do projeto (ex.: `<projeto>/marca/tema.css`) e copie para cada carrossel. O `render.sh` não renderiza sem `tema.css`.

## 3. Tese e pesquisa

Todo carrossel defende **uma tese contraintuitiva** ("ter 100 mil seguidores pode ser um péssimo negócio"). Escreva-a em uma frase antes do roteiro.

- Dados, datas, números e citações precisam de fonte real. Pesquise quando possível; se não confirmar, marque `[VERIFICAR]` e avise o usuário. Nunca invente estatística, "estudo" ou declaração de pessoa real.
- Newsjacking com pessoa ou marca famosa: fale do fato público e extraia a lição de negócio. Não atribua falas, intenções ou números que não estejam em fonte confiável.

## 4. Roteiro

Siga a anatomia de `estrategia.md` (padrão de 10 slides, aceite de 7 a 12). Para cada slide entregue: tipo de slide, título, corpo, imagem sugerida e tema (claro, escuro ou destaque).

Mostre o roteiro em texto para aprovação **antes** de desenhar, a não ser que o usuário peça tudo de uma vez.

## 5. Design, imagens e renderização

1. Crie uma pasta de trabalho (ex.: `carrossel-<tema>/slides/`) e copie para ela `assets/templates/base.css` e o `tema.css` do projeto (seção 2).
2. Para cada slide, parta do template correspondente em `assets/templates/` (lista em `design.md`) e salve como `slide-01.html`, `slide-02.html`… Troque `{{HANDLE}}`, `{{TAG}}`, `{{DATA}}` e o conteúdo. A paginação (bolinhas) é marcada pelo índice do slide.
3. **Imagens: nenhum slide sai com espaço vazio.** Use as fotos do usuário quando houver. Para o resto, siga a skill `imagens-gratis` (se não estiver carregada, use o script dela: `python3 -I <dir-imagens-gratis>/scripts/buscar.py "<cena em inglês>" --saida carrossel-<tema>/slides/img --orientacao vertical --n 6`). Leia os candidatos, escolha os que combinam com a paleta e o assunto e troque cada `.ph` por `<img class="img" src="img/arquivo.jpg" style="height:400px">` (ou `class="full-bleed"` nas capas). Para pessoas famosas em newsjacking, busque no Wikimedia Commons. Registre os créditos na legenda quando a licença exigir.
4. Renderize:
   ```bash
   bash <dir-da-skill>/scripts/render.sh carrossel-<tema>/slides
   ```
   Gera `png/slide-XX.png` (1080×1350) e `carrossel.pdf`.
5. Abra 2 ou 3 PNGs (capa, um slide denso e o CTA) e confira: texto cortado, sobreposição, contraste, hierarquia. Corrija e renderize de novo.

## 6. Legenda

Estrutura: gancho de 1 linha diferente da capa → 2 ou 3 linhas reforçando a tese → CTA repetido (palavra-chave ou "salva e manda pra quem precisa") → 3 a 5 hashtags de nicho, no máximo.

## 7. Checklist final

- [ ] Capa entende-se em 1 segundo, sem precisar ler o subtítulo.
- [ ] Slides 2 e 3 prometem algo que só será entregue depois (laço aberto).
- [ ] Cada slide tem uma ideia só e um destaque de cor no máximo por bloco.
- [ ] Existe pelo menos um slide "salvável" (framework, checklist, anatomia, lista).
- [ ] CTA único e claro; se for por comentário, a palavra aparece em caixa alta e entre aspas.
- [ ] Nada de dado inventado; pendências marcadas com `[VERIFICAR]`.
- [ ] Paleta e fontes vindas da identidade do projeto, com contraste conferido.
- [ ] Nenhum `.ph` restante: todas as imagens encaixadas e com licença de uso comercial; créditos listados.
- [ ] Marca do usuário, sem nome, @ ou assinatura de terceiros.
