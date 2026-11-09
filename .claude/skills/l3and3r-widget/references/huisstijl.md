# Huisstijl l3and3r.org

Afgeleid uit `assets/style.css` van de site. De site is **altijd donker**;
widgets volgen dat, zodat ze naadloos in een artikel passen (ook als iframe).
Geen light-modevariant nodig.

## Kleuren (CSS-tokens)

| Token          | Waarde                     | Gebruik                                |
|----------------|----------------------------|----------------------------------------|
| `--bg`         | `#0a0a0a`                  | achtergrond (gelijk aan de site)       |
| `--fg`         | `#cccccc`                  | lopende tekst                          |
| `--kop`        | `#ffffff`                  | koppen en grote resultaten             |
| `--muted`      | `#999999`                  | bijschriften                           |
| `--subtiel`    | `#666666`                  | voetnoten, uitgeschakelde elementen    |
| `--accent`     | `#f7931a`                  | Bitcoin-oranje: hoofdactie, Bitcoin-lijn |
| `--accent-hover` | `#ffa726`                | hover op knoppen/links                 |
| `--accent-2`   | `#63a4ff`                  | vergelijkingslijn (fiat) — eigen keuze, komt niet op de site voor |
| `--card`       | `rgba(255,255,255,0.03)`   | kaarten / panelen                      |
| `--card-accent`| `rgba(247,147,26,0.05)`    | uitgelichte kaart                      |
| `--border`     | `rgba(247,147,26,0.2)`     | randen (oranje getint, zoals de nav)   |

Fiat tegenover Bitcoin: fiat altijd `--accent-2`, Bitcoin altijd `--accent`.

## Typografie

- Tekst: systeemfonts, net als de site:
  `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`.
  Geen webfonts laden.
- Regelhoogte `1.6`.
- Getallen in resultaten: `font-variant-numeric: tabular-nums`.
- Codes, adressen en seed-woorden: `ui-monospace, 'Cascadia Code', Consolas, monospace`.
- Uitzondering: widgets voor kinderen (zoals de spaarpot) mogen `Baloo 2`
  (Google Fonts) gebruiken.

## Getalnotatie (nl-NL)

- Euro: `€ 1.234,56`, via `Intl.NumberFormat('nl-NL', {style:'currency', currency:'EUR'})`.
- Sats: `12.345 sats` (punt als duizendtal, geen decimalen).
- BTC: maximaal 8 decimalen, met komma: `0,00012345 BTC`.
- Percentages: `7,2%`.

## Toon

- Je-vorm, korte zinnen, actief.
- Eerst het inzicht, daarna de techniek.
- Vaktermen bij eerste gebruik kort uitleggen, met een `<abbr title>`.
