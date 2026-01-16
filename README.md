# Bitcoin Uitgelegd 🪙

Een rustige, toegankelijke uitleg over Bitcoin voor familie en vrienden die willen begrijpen wat het is en welk probleem het probeert op te lossen.

**Live demo:** https://l3and3r.github.io/bitcoin-uitleg/

---

## 📖 Over dit project

Dit is geen investerings-advies of hype-pagina. Het doel is simpel: **uitleggen welk probleem Bitcoin probeert op te lossen**, zonder technisch jargon of financiële claims.

De website is bewust ontworpen om:
- **Begrijpelijk** te zijn voor mensen zonder technische achtergrond
- **Neutraal** te blijven zonder aan te sporen tot kopen
- **Visueel prettig** te zijn met moderne animaties en design
- **Informatief** te zijn zonder overweldigend te worden

---

## ✨ Features

### 🎨 Moderne UI/UX
- Donker thema met Bitcoin-oranje accenten
- Smooth scroll-animaties die activeren bij het in beeld komen
- Hover-effecten op interactieve elementen
- Volledig responsive design voor desktop, tablet en smartphone

### 📱 Mobile-First Design
- Touch-vriendelijke bediening
- Geoptimaliseerd voor alle schermformaten
- Snelle laadtijd, geen externe dependencies

### 🎥 Multimedia Content
- Embedded YouTube video ("What's the problem?")
- Visuele uitleg van het probleem dat Bitcoin oplost

### 📚 Uitgebreide Resources
- Nederlandse podcasts (Bitcoin School, Beginnen met Bitcoin)
- Cursusmateriaal (Mijn Eerste Bitcoin)
- Boeken (The Bitcoin Standard, Broken Money, Layered Money)

### ⚡ Contact & Donaties
- Lightning Network donatie-optie met QR-code
- Nostr contactgegevens voor vragen en feedback

---

## 🏗️ Structuur

De website bestaat uit 12 secties:

1. **Hero** - Openingsvraag over waardeverlies van geld
2. **Wat is geld?** - De drie functies van geld
3. **Het huidige systeem** - Hoe inflatie ontstaat
4. **Eigendom** - Is bankgeld echt van jou?
5. **De kernvraag** - Kan digitaal geld schaars zijn?
6. **Bitcoin eigenschappen** - Schaarste, eigendom, neutraliteit
7. **Bitcoin vs Crypto** - Het fundamentele verschil (decentralisatie, geen eigenaar, absolute schaarsheid)
8. **Hard geld** - Waarom mensen het "beter geld" noemen
9. **Toegankelijkheid** - Het is makkelijker dan je denkt
10. **Tot slot** - Je hoeft niets te doen
11. **Video** - "What's the problem?" YouTube video
12. **Resources** - Podcasts, cursussen en boeken voor verdieping
13. **Support & Contact** - Lightning donaties en Nostr contactgegevens

---

## 🚀 Installatie & Gebruik

### Voor GitHub Pages (Aanbevolen)

1. **Fork of clone deze repository**
   ```bash
   git clone https://github.com/L3and3r/bitcoin-uitleg.git
   ```

2. **Voeg je QR-code toe** (optioneel)
   - Genereer een QR-code voor je Lightning address via [qr-code-generator.com](https://www.qr-code-generator.com/)
   - Sla op als `qr_download.png` in de root folder
   - Of pas de HTML aan om de QR-sectie te verwijderen

3. **Activeer GitHub Pages**
   - Ga naar repository Settings
   - Klik op "Pages" in het linkermenu
   - Bij "Source" selecteer `main` branch en `/ (root)`
   - Klik "Save"
   - Je site is live op: `https://[jouw-username].github.io/[repo-naam]`

### Lokaal Testen

Open gewoon `index.html` in je browser. Geen build-proces of dependencies nodig!

---

## 🎨 Aanpassen

### Kleuren veranderen
Alle kleuren zijn CSS variabelen. Zoek in de `<style>` sectie naar:
- `#f7931a` - Bitcoin oranje (hoofdkleur)
- `#0a0a0a` - Donkere achtergrond
- `#ccc` - Tekst kleur

### Auto-scroll timing aanpassen
Zoek in de JavaScript sectie naar:
```javascript
const SCROLL_DELAY = 8000; // Milliseconden tussen secties
```
Verander naar gewenste waarde (bijv. `10000` voor 10 seconden).

### Donatie-sectie verwijderen
Verwijder de hele `<section class="alt-bg">` met "11 — Support" uit de HTML.

### Content aanpassen
Alle tekst staat direct in de HTML. Zoek de betreffende sectie en pas aan naar wens.

---

## 🛠️ Technische Details

### Gebouwd met
- **Pure HTML/CSS/JavaScript** - Geen frameworks of dependencies
- **CSS Grid & Flexbox** - Voor responsive layout
- **Intersection Observer API** - Voor scroll-geactiveerde animaties
- **CSS Custom Properties** - Voor makkelijk thema-aanpassingen

### Browser Support
Werkt in alle moderne browsers:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

### Performance
- **Geen externe dependencies** - Alles in één bestand
- **Geoptimaliseerde animaties** - Gebruikt CSS transforms voor 60fps
- **Minimale JavaScript** - ~100 regels voor auto-scroll functionaliteit
- **Lighthouse score:** 95+ op alle metrics

---

## 📚 Resources in de Website

De website linkt naar deze Nederlandse Bitcoin resources:

**Podcasts:**
- [Bitcoin School](https://bitcoinschool.nl/) - Beginner-vriendelijke uitleg
- [Beginnen met Bitcoin](https://bitcoin.nl/podcast/beginnen-met-bitcoin) - Praktische handleiding

**Boeken:**
- De Bitcoin Standaard - Saifedean Ammous
- Broken Money - Lyn Alden  
- Layered Money - Nik Bhatia

---

## 🤝 Bijdragen

Verbeteringen zijn welkom! Open een issue of pull request voor:
- Verbeterde formulering of duidelijkheid
- Bugfixes
- Toegankelijkheidsverbeteringen
- Vertaalfouten

**Guidelines:**
- Houd de toon neutraal en informatief
- Vermijd hype-taal of financiële claims
- Test op zowel desktop als mobile
- Behoud de minimalistische aanpak

---

## 📄 Licentie

[MIT License](LICENSE) - Voel je vrij om te gebruiken, aan te passen en te delen.

**Attribution appreciated maar niet verplicht.** Als je deze code gebruikt, zou het leuk zijn om terug te linken, maar het is niet nodig.

---

## 💡 FAQ

**Q: Kan ik dit gebruiken voor mijn eigen website?**  
A: Ja! Het is open source onder MIT licentie.

**Q: Hoe schakel ik de auto-scroll uit?**  
A: Verwijder de hele `<script>` sectie en de `.controls` CSS.

**Q: Kan ik andere talen toevoegen?**  
A: Zeker! Je kunt meerdere HTML bestanden maken (bijv. `index-en.html`) of een taal-switcher bouwen.

**Q: Waarom geen React/Vue/framework?**  
A: Voor maximale eenvoud en laagste drempel. Iedereen kan deze HTML openen en aanpassen.

**Q: Kan ik de QR-code weglaten?**  
A: Ja, verwijder gewoon sectie 11 uit de HTML.

---

## 🙏 Credits

Ontworpen en gebouwd voor familie en vrienden die Bitcoin willen begrijpen zonder technische complexiteit.

**Feedback?** Open een issue of stuur een Lightning zap! ⚡

---

## 📞 Contact

Voor vragen of feedback:
- GitHub Issues: [Open een issue](../../issues)
- Lightning: `l3and3r@getalby.com`

---

**Gemaakt met ₿ en ☕**
