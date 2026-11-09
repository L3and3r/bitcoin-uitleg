---
name: l3and3r-widget
description: Gebruik bij het maken of aanpassen van een interactieve Bitcoin-uitlegwidget (calculator, simulatie, quiz, visualisatie) voor l3and3r.org — Nederlandstalig, één HTML-bestand, GitHub Pages.
---

# l3and3r-widget

Bouwt interactieve, Nederlandstalige Bitcoin-uitlegwidgets voor l3and3r.org
(repo `L3and3r/bitcoin-uitleg`, GitHub Pages, branch `main`).

## Werkwijze

1. **Scherp het leerdoel aan.** Formuleer in één zin wat de lezer na afloop
   snapt ("Na deze widget snap je dat…"). Vraag het na als het onduidelijk is.
   Eén widget = één inzicht.
2. **Lees de didactiek**: `references/didactiek.md`. Kies daar een patroon
   (schuifregelaar-verkenning, voor/na-vergelijking, stap-voor-stap, quiz).
3. **Lees de huisstijl**: `references/huisstijl.md` (kleuren, typografie,
   toon, getalnotatie).
4. **Start vanaf de template**: kopieer `assets/template.html` en vul de
   gemarkeerde blokken. Wijk alleen af van de structuur als het leerdoel dat vraagt.
5. **Controleer** met `python scripts/check_widget.py <bestand>.html` en los
   alle FOUT-meldingen op. WAARSCHUWINGEN beoordeel je zelf.
6. **Lever op** met: het bestand, de voorgestelde plek in de repo
   (`widgets/<slug>.html`), en een embed-snippet (iframe) voor een artikel.

## Harde regels

- Alles in het Nederlands, inclusief foutmeldingen en labels.
- Eén zelfstandig HTML-bestand, geen buildstap. Externe scripts alleen van
  cdnjs.cloudflare.com of cdn.jsdelivr.net.
- Geen tracking, geen analytics. Systeemfonts, geen webfonts (uitzondering: Baloo 2 voor kinderwidgets).
- Geen live koersdata tenzij expliciet gevraagd; gebruik een instelbare
  standaardwaarde en vermeld de peildatum.
- Geen financieel advies: rekenwidgets tonen een korte disclaimer onderaan.
- Werkt op telefoonbreedte (360px) en volgt de donkere site-stijl (`--bg:#0a0a0a`).
- `localStorage` alleen binnen try/catch, en de widget werkt ook zonder.

## Wat je níét doet

- Geen altcoins of "crypto" als verzamelterm, tenzij het leerdoel om dat
  contrast gaat.
- Geen hype-taal ("to the moon", "gegarandeerd"); de toon is uitleggend en nuchter.
