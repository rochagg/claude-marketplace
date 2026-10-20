#!/usr/bin/env python3
"""Busca e baixa fotos/vídeos gratuitos com licença de uso comercial.

Uso:
  python3 -I buscar.py "consulta em inglês" --saida pasta [--tipo foto|video]
         [--orientacao vertical|horizontal|quadrada] [--n 6] [--fontes pexels,openverse]

Fontes: pexels, pixabay, unsplash (precisam de chave gratuita) e openverse,
wikimedia (sem chave). Chaves vêm das variáveis PEXELS_API_KEY,
PIXABAY_API_KEY, UNSPLASH_ACCESS_KEY ou do arquivo
~/.config/imagens-gratis/keys.env (formato CHAVE=valor).

Grava os arquivos em --saida e acrescenta os créditos em --saida/creditos.json.
Só usa a biblioteca padrão do Python.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "imagens-gratis-skill/1.0 (uso pessoal)"
KEYS_FILE = os.path.expanduser("~/.config/imagens-gratis/keys.env")
WIKI_OK = ("cc0", "public domain", "pd", "cc by", "cc-by")


def load_keys():
    keys = {}
    if os.path.exists(KEYS_FILE):
        for line in open(KEYS_FILE, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                keys[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("PEXELS_API_KEY", "PIXABAY_API_KEY", "UNSPLASH_ACCESS_KEY"):
        if os.environ.get(k):
            keys[k] = os.environ[k]
    return keys


def fetch(url, headers=None, timeout=45):
    """GET com até 3 tentativas (servidores gratuitos limitam e oscilam)."""
    for tentativa in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.HTTPError, TimeoutError, urllib.error.URLError) as e:
            if tentativa == 2 or getattr(e, "code", 429) not in (429, 500, 502, 503, 504):
                raise
            time.sleep(3 * (tentativa + 1))


def get_json(url, headers=None):
    return json.loads(fetch(url, headers, timeout=100))


def q(params):
    return urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})


def pexels(query, tipo, orient, n, key):
    o = {"vertical": "portrait", "horizontal": "landscape", "quadrada": "square"}.get(orient)
    if tipo == "video":
        d = get_json("https://api.pexels.com/videos/search?" + q({"query": query, "orientation": o, "per_page": n}),
                     {"Authorization": key})
        out = []
        for v in d.get("videos", []):
            files = sorted([f for f in v["video_files"] if f.get("file_type") == "video/mp4" and f.get("width")],
                           key=lambda f: abs((f["height"] or 0) - 1920))
            if files:
                out.append(dict(url=files[0]["link"], ext="mp4", autor=v["user"]["name"], pagina=v["url"],
                                licenca="Pexels License (uso comercial, sem atribuição obrigatória)"))
        return out
    d = get_json("https://api.pexels.com/v1/search?" + q({"query": query, "orientation": o, "per_page": n}),
                 {"Authorization": key})
    return [dict(url=p["src"]["large2x"], ext="jpg", autor=p["photographer"], pagina=p["url"],
                 licenca="Pexels License (uso comercial, sem atribuição obrigatória)", alt=p.get("alt"))
            for p in d.get("photos", [])]


def pixabay(query, tipo, orient, n, key):
    o = {"vertical": "vertical", "horizontal": "horizontal"}.get(orient)
    n = max(3, n)
    if tipo == "video":
        d = get_json("https://pixabay.com/api/videos/?" + q({"key": key, "q": query, "per_page": n}))
        return [dict(url=(h["videos"].get("large") or h["videos"]["medium"])["url"], ext="mp4", autor=h["user"],
                     pagina=h["pageURL"], licenca="Pixabay Content License (uso comercial)") for h in d.get("hits", [])]
    d = get_json("https://pixabay.com/api/?" + q({"key": key, "q": query, "image_type": "photo",
                                                   "orientation": o, "per_page": n, "safesearch": "true"}))
    return [dict(url=h["largeImageURL"], ext="jpg", autor=h["user"], pagina=h["pageURL"],
                 licenca="Pixabay Content License (uso comercial)", alt=h.get("tags")) for h in d.get("hits", [])]


def unsplash(query, tipo, orient, n, key):
    if tipo == "video":
        return []
    o = {"vertical": "portrait", "horizontal": "landscape", "quadrada": "squarish"}.get(orient)
    h = {"Authorization": "Client-ID " + key}
    d = get_json("https://api.unsplash.com/search/photos?" + q({"query": query, "orientation": o, "per_page": n}), h)
    out = []
    for r in d.get("results", []):
        try:  # exigido pelas diretrizes da API ao usar a foto
            get_json(r["links"]["download_location"], h)
        except Exception:
            pass
        out.append(dict(url=r["urls"]["regular"], ext="jpg", autor=r["user"]["name"],
                        pagina=r["links"]["html"] + "?utm_source=imagens_gratis&utm_medium=referral",
                        licenca="Unsplash License (uso comercial, crédito recomendado)", alt=r.get("alt_description")))
    return out


def openverse(query, tipo, orient, n, _key):
    if tipo == "video":
        return []
    ar = {"vertical": "tall", "horizontal": "wide", "quadrada": "square"}.get(orient)
    d = get_json("https://api.openverse.org/v1/images/?" + q({"q": query, "license_type": "commercial,modification",
                                                             "aspect_ratio": ar, "page_size": n, "mature": "false"}))
    return [dict(url=r["url"], ext=(r.get("filetype") or "jpg"), autor=r.get("creator") or "desconhecido",
                 pagina=r.get("foreign_landing_url"), alt=r.get("title"),
                 licenca=f"CC {r['license'].upper()} {r.get('license_version') or ''}".strip())
            for r in d.get("results", [])]


def wikimedia(query, tipo, orient, n, _key):
    if tipo == "video":
        return []
    d = get_json("https://commons.wikimedia.org/w/api.php?" + q({
        "action": "query", "generator": "search", "gsrnamespace": 6, "gsrsearch": query + " filetype:bitmap",
        "gsrlimit": n * 2, "prop": "imageinfo", "iiprop": "url|extmetadata|size", "iiurlwidth": 1600,
        "format": "json"}))
    out = []
    for p in (d.get("query") or {}).get("pages", {}).values():
        ii = p["imageinfo"][0]
        meta = ii.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "")
        if not lic.lower().startswith(WIKI_OK):
            continue
        w, h = ii.get("width", 1), ii.get("height", 1)
        if orient == "vertical" and w > h or orient == "horizontal" and h > w:
            continue
        autor = re.sub("<[^>]+>", "", meta.get("Artist", {}).get("value", "desconhecido")).strip()
        out.append(dict(url=ii.get("thumburl") or ii["url"], ext="jpg", autor=autor, pagina=ii["descriptionurl"],
                        licenca=lic, alt=p.get("title")))
    return out[:n]


FONTES = {"pexels": (pexels, "PEXELS_API_KEY"), "pixabay": (pixabay, "PIXABAY_API_KEY"),
          "unsplash": (unsplash, "UNSPLASH_ACCESS_KEY"), "openverse": (openverse, None),
          "wikimedia": (wikimedia, None)}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("consulta")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--tipo", choices=["foto", "video"], default="foto")
    ap.add_argument("--orientacao", choices=["vertical", "horizontal", "quadrada"])
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--fontes", default="pexels,unsplash,pixabay,openverse,wikimedia")
    a = ap.parse_args()

    keys = load_keys()
    os.makedirs(a.saida, exist_ok=True)
    cred_path = os.path.join(a.saida, "creditos.json")
    creditos = json.load(open(cred_path, encoding="utf-8")) if os.path.exists(cred_path) else []

    baixados, pulos = 0, []
    for nome in [f.strip() for f in a.fontes.split(",") if f.strip()]:
        if baixados >= a.n:
            break
        fn, key_name = FONTES[nome]
        key = keys.get(key_name) if key_name else None
        if key_name and not key:
            pulos.append(f"{nome} (sem chave {key_name})")
            continue
        try:
            itens = fn(a.consulta, a.tipo, a.orientacao, a.n - baixados, key)
        except Exception as e:
            pulos.append(f"{nome} (erro: {e})")
            continue
        for it in itens:
            if baixados >= a.n:
                break
            arq = f"{slug(a.consulta)}-{nome}-{len(creditos) + 1:02d}.{it['ext'].split('?')[0][:4]}"
            destino = os.path.join(a.saida, arq)
            try:
                dados = fetch(it["url"], timeout=90)
                with open(destino, "wb") as f:
                    f.write(dados)
                time.sleep(1)
            except Exception as e:
                pulos.append(f"{nome}: falha ao baixar ({e})")
                continue
            creditos.append({"arquivo": arq, "fonte": nome, "consulta": a.consulta, **{k: v for k, v in it.items() if k != "ext"}})
            baixados += 1
            print(f"{destino}\t{nome}\t{it['licenca']}\t{it['autor']}")

    json.dump(creditos, open(cred_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if pulos:
        print("Fontes puladas: " + "; ".join(pulos), file=sys.stderr)
    if not baixados:
        print("Nada encontrado. Tente termos mais simples em inglês ou outra fonte.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
