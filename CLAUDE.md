# bitcoin-uitleg (l3and3r.org)

Nederlandstalige, rustige uitleg over Bitcoin voor mensen zonder technische
achtergrond. Geen investeringsadvies, geen hype.

## Structuur
- `index.html` — homepage; `pages/*.html` — artikelpagina's
- `assets/style.css` — gedeelde stylesheet (donker thema, Bitcoin-oranje `#f7931a`)
- `spaarpot/` — LNbits-spaarpot voor de kinderen (eigen stijl, Baloo 2)
- `widgets/` — interactieve uitlegwidgets (losse HTML-bestanden, embed via iframe)

## Werkwijze
- Statische site, geen buildstap. Deploy via GitHub Pages vanaf `main`
  (custom domain via `CNAME`: l3and3r.org).
- Alle tekst in het Nederlands, je-vorm.
- Nieuwe widgets: gebruik de skill `.claude/skills/l3and3r-widget/` en draai
  `python .claude/skills/l3and3r-widget/scripts/check_widget.py <bestand>`.
- Geen tracking of analytics, geen externe dependencies tenzij nodig.
