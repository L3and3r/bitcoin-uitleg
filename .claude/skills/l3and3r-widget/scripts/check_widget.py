#!/usr/bin/env python3
"""Controleert een l3and3r-widget op de harde regels uit SKILL.md.

Gebruik: python scripts/check_widget.py <bestand>.html
Exitcode 1 bij één of meer FOUT-meldingen.
"""
import re
import sys
from pathlib import Path

TOEGESTANE_SCRIPT_HOSTS = ("cdnjs.cloudflare.com", "cdn.jsdelivr.net")
TOEGESTANE_STYLE_HOSTS = ("fonts.googleapis.com", "fonts.gstatic.com")
TRACKERS = ("google-analytics", "googletagmanager", "gtag(", "plausible", "matomo",
            "hotjar", "facebook.net", "clarity.ms", "segment.com")
HYPE = ("to the moon", "gegarandeerd", "lambo", "wen moon", "100x", "kan niet missen")
ALTCOIN = (r"\bcrypto\b", r"\bethereum\b", r"\bsolana\b", r"\baltcoin")
DATA_API = ("api.coingecko", "api.coinbase", "api.kraken", "mempool.space/api", "blockchain.info")
VULPLEKKEN = ("<!-- VUL", "TITEL |", ">KOP<", ">CONTEXT<")


def check(pad: Path) -> int:
    html = pad.read_text(encoding="utf-8")
    laag = html.lower()
    fouten, waarschuwingen = [], []

    if not re.search(r'<html[^>]*lang="nl', html):
        fouten.append('<html lang="nl"> ontbreekt.')
    if 'name="viewport"' not in html:
        fouten.append("viewport-meta ontbreekt (nodig voor telefoonbreedte).")
    if "--bg:#0a0a0a" not in html.replace(" ", "").lower():
        fouten.append("Achtergrondtoken --bg:#0a0a0a ontbreekt (widget moet de donkere site-stijl volgen).")
    if "fonts.googleapis.com" in laag and "baloo" not in laag:
        waarschuwingen.append("Webfont geladen; de site gebruikt systeemfonts (alleen Baloo 2 voor kinderwidgets).")

    for src in re.findall(r'<script[^>]+src="([^"]+)"', html):
        if src.startswith("http") and not any(h in src for h in TOEGESTANE_SCRIPT_HOSTS):
            fouten.append(f"Extern script van niet-toegestane host: {src}")
    for href in re.findall(r'<link[^>]+rel="stylesheet"[^>]*href="([^"]+)"', html) + \
                re.findall(r'<link[^>]+href="([^"]+)"[^>]*rel="stylesheet"', html):
        if href.startswith("http") and not any(h in href for h in TOEGESTANE_STYLE_HOSTS):
            fouten.append(f"Externe stylesheet van niet-toegestane host: {href}")

    for t in TRACKERS:
        if t in laag:
            fouten.append(f"Tracking/analytics gevonden: {t}")

    # localStorage alleen binnen try/catch
    for m in re.finditer(r"localStorage\.(getItem|setItem|removeItem|clear)", html):
        venster = html[max(0, m.start() - 200):m.start()]
        if "try" not in venster:
            fouten.append("localStorage-aanroep zonder omliggende try/catch.")
            break

    for v in VULPLEKKEN:
        if v in html:
            fouten.append(f"Niet-ingevulde templateplek: {v.strip()}")

    for h in HYPE:
        if h in laag:
            fouten.append(f"Hype-taal: '{h}'")

    for a in ALTCOIN:
        if re.search(a, laag):
            waarschuwingen.append(f"Term gevonden ({a.strip(chr(92)+'b')}); alleen ok als het leerdoel om dat contrast gaat.")

    if any(d in laag for d in DATA_API):
        waarschuwingen.append("Live data-API gevonden; alleen toegestaan als daar expliciet om gevraagd is.")

    rekent = bool(re.search(r"€|eur\(|currency", html))
    if rekent and "geen financieel advies" not in laag:
        fouten.append("Rekenwidget zonder disclaimer 'geen financieel advies'.")
    if rekent and "peildatum" not in laag:
        waarschuwingen.append("Geen peildatum vermeld.")

    engels = re.findall(r">\s*(Submit|Next|Previous|Reset|Result|Error|Loading)\s*<", html)
    for w in engels:
        fouten.append(f"Engels label in de interface: '{w}'")

    if len(html.encode()) > 300_000:
        waarschuwingen.append("Bestand groter dan 300 kB; overweeg te vereenvoudigen.")

    for f in fouten:
        print(f"FOUT: {f}")
    for w in waarschuwingen:
        print(f"WAARSCHUWING: {w}")
    if not fouten and not waarschuwingen:
        print("OK: geen problemen gevonden.")
    elif not fouten:
        print(f"OK met {len(waarschuwingen)} waarschuwing(en).")
    return 1 if fouten else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(check(Path(sys.argv[1])))
