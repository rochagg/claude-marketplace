---
name: awesome-design-md
description: Biblioteca de 84 DESIGN.md (sistemas de design analisados de marcas como Stripe, Linear, Apple, Notion, Vercel, Airbnb, Spotify, Tesla, Figma, Supabase, Raycast) com cores, tipografia, espaçamento, componentes e regras. Use quando o usuário pedir uma página, app ou componente "no estilo de"/"parecido com" uma marca ou site conhecido, quiser um DESIGN.md pronto para o projeto, ou precisar de uma referência visual concreta para fugir do visual genérico.
---

# Awesome DESIGN.md

Coleção de arquivos DESIGN.md (formato do Google Stitch) extraídos de sites reais. Cada arquivo traz tokens (cores, tipografia, raios, sombras, espaçamento), padrões de layout, componentes e regras do que fazer e evitar.

## Como usar

1. **Escolher a referência.** Se o usuário citou uma marca, abra `designs/<marca>.md`. Se não citou, leia `INDEX.md` (uma linha por marca com o resumo da linguagem visual) e proponha 2–3 opções que combinem com o produto, o público e o tom. Não leia vários DESIGN.md inteiros só para comparar; o índice basta.
2. **Ler o DESIGN.md escolhido por inteiro** antes de escrever código. Ele é a fonte de verdade de tokens e regras.
3. **Aplicar.** Se o projeto ainda não tem um DESIGN.md, copie o arquivo para a raiz do projeto como `DESIGN.md` (quando o usuário quiser manter a referência) e gere a UI seguindo-o: transforme os tokens em variáveis CSS/Tailwind e respeite as regras de componentes e os "não faça".
4. **Adaptar, não clonar.** Use a linguagem visual como inspiração para o projeto do usuário: troque nome, logo, textos e imagens da marca de origem pelos do usuário, e ajuste a cor primária à paleta dele se ele tiver uma. Não reproduza logotipos, marcas registradas nem textos da marca original, e não monte páginas que possam se passar pela empresa real.
5. **Fontes proprietárias** (ex.: Söhne, SF Pro, Airbnb Cereal) não estão disponíveis livremente: use a alternativa sugerida no próprio arquivo ou uma equivalente do Google Fonts e avise o usuário.

## Combinação com outras skills

- Para direção de arte e checagem visual, use junto com `taste-skill` ou `impeccable`; este pacote fornece a referência concreta de sistema.
- Para revisar o resultado, use `web-design-guidelines`.

## Créditos

Conteúdo de [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md), licença MIT (ver `LICENSE-VoltAgent`). As análises são interpretações inspiradas; as marcas pertencem aos seus donos.
