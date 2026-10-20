---
name: imagens-gratis
description: Busca, escolhe e baixa fotos e vídeos gratuitos com licença de uso comercial (Pexels, Unsplash, Pixabay, Openverse, Wikimedia Commons), registrando os créditos. Use sempre que um criativo estático, carrossel, post, anúncio, landing page, apresentação ou vídeo precisar de imagem ou vídeo de apoio, em vez de deixar espaços vazios ou placeholders.
---

# Imagens grátis para criativos

Regra: **criativo não sai com espaço vazio esperando imagem.** Durante a produção, encontre a imagem, baixe, encaixe e registre o crédito. Placeholder só se o usuário pedir para usar fotos próprias.

## 1. Defina o que procurar

Para cada espaço de imagem, escreva antes:
- **Cena** em 3 a 6 palavras **em inglês** (os bancos indexam em inglês): `woman portrait orange background`, `hands holding phone laptop`, `accountant desk documents`.
- **Orientação**: `vertical` (retratos, capas 4:5), `horizontal` (faixas de imagem dentro do slide) ou `quadrada`.
- **Clima/cor**: combine com a paleta do projeto (ex.: projeto azul → fundo azul ou neutro; evite brigar com a cor de destaque).

Bons termos: retrato com fundo de cor sólida (`studio portrait colored background`), cenas reais de trabalho, close de mãos e objetos, texturas. Evite termos que trazem clichê de banco de imagem (`business success`, `handshake`, `teamwork`).

## 2. Baixe candidatos

```bash
python3 -I <dir-da-skill>/scripts/buscar.py "studio portrait colored background" \
  --saida <projeto>/imagens --orientacao vertical --n 6
```

- `--tipo video` busca vídeos (Pexels e Pixabay) para Reels, Remotion ou HyperFrames.
- `--fontes` escolhe a ordem (padrão: `pexels,unsplash,pixabay,openverse,wikimedia`). Fontes sem chave são puladas.
- Cada arquivo baixado entra em `<saida>/creditos.json` (fonte, autor, licença, página).

Depois **olhe os candidatos** (leia as imagens) e escolha pelo critério: foco no assunto, espaço para o texto, cor compatível com a paleta, sem marca d'água, sem logos de terceiros em destaque. Apague os descartados.

## 3. Encaixe e crédito

- Recorte com CSS (`object-fit: cover; object-position: ...`) em vez de editar o arquivo.
- Licenças CC BY e CC BY-SA (Openverse, Wikimedia) **exigem crédito**: coloque "Foto: Autor / Fonte (licença)" na legenda do post ou em letra pequena no slide. Pexels, Unsplash e Pixabay não exigem, mas o crédito é recomendado.
- Ao entregar, liste as imagens usadas com autor e licença (de `creditos.json`).

## Fontes

| Fonte | Tem | Chave | Observação |
|---|---|---|---|
| **Pexels** | fotos e vídeos | grátis (pexels.com/api) | melhor qualidade "editorial" para redes sociais |
| **Unsplash** | fotos | grátis (unsplash.com/developers) | retratos e estilo de vida premium |
| **Pixabay** | fotos, vídeos, ilustrações | grátis (pixabay.com/api/docs) | bom volume, qualidade variável |
| Openverse | fotos CC (Flickr e outros) | não precisa | exige crédito; API às vezes lenta (até ~60 s) |
| Wikimedia Commons | fotos de pessoas públicas, lugares, eventos, obras | não precisa | ideal para newsjacking com famosos; exige crédito em CC BY/BY-SA |

As chaves ficam em `~/.config/imagens-gratis/keys.env`:
```
PEXELS_API_KEY=...
UNSPLASH_ACCESS_KEY=...
PIXABAY_API_KEY=...
```
Criar a conta e copiar a chave é com o usuário (Claude não cria contas). Sem chaves, o script usa Openverse e Wikimedia, que funcionam mas têm acervo mais fraco para estilo de vida; avise o usuário quando a qualidade ficar abaixo do esperado e sugira criar a chave do Pexels (é instantâneo).

Outras bibliotecas gratuitas para buscar manualmente ou pelo navegador quando a API não resolver:
- **Vídeo**: Pexels Videos, Pixabay Videos, Mixkit, Coverr.
- **Ilustração**: unDraw (sem crédito), Storyset (com crédito), Open Peeps, Humaaans.
- **Ícones**: Lucide, Phosphor, Iconoir, Tabler (licenças MIT/ISC).
- **Texturas e 3D**: Poly Haven e ambientCG (CC0).
- **Música e efeitos**: Pixabay Music, Free Music Archive (verificar licença de cada faixa), Freesound (CC0 ou CC BY).

## Pinterest e similares

Pinterest, Google Imagens e Behance servem **só como referência de estilo** (moodboard): as imagens pertencem a terceiros e não têm licença de uso. Não baixe de lá para publicar. Use a referência para escrever melhores termos de busca nas fontes acima.

## Quando nada servir

1. Refaça a busca com outros termos (mais simples, sinônimos, outra orientação).
2. Use foto real do cliente ou do projeto, se houver.
3. Gere a imagem com uma ferramenta de geração conectada (ex.: Canva `generate-image` ou Figma `generate_image`), avisando o usuário de que é imagem gerada por IA. Nunca gere rosto de pessoa real.
