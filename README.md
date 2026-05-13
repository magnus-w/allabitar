# Alla Bitar

Poddsajt för Alla Bitar. Statisk sajt på GitHub Pages med en lokal editor för innehållsredigering.

## Redigera innehåll

### Krav
- Chrome eller Edge (editorn använder File System Access API för direktsparning)
- Git installerat

### Arbetsflöde

**1. Synka lokalt repo med GitHub**
```bash
git pull
```

**2. Öppna editorn**

Öppna `editor.html` direkt i Chrome från Finder — ingen server behövs för redigering.

**3. Ladda innehållsfilen**

Klicka **Öppna data.json** och navigera till repomappen. Välj `data.json`.

**4. Redigera**

Editorn har tre flikar:
- **Programinfo** — poddnamn, tagline och hero-beskrivningen
- **Senaste** — det senaste avsnittet (visas större överst)
- **Avsnitt** — alla övriga avsnitt

Ändringar sparas automatiskt tillbaka till `data.json` efter 500 ms. `⌘S` sparar manuellt.

**5. Publicera**
```bash
git add data.json
git commit -m "Nytt avsnitt: Avsnitt 43 – Gästnamn"
git push
```

GitHub Pages uppdateras inom ~30 sekunder.

---

## Lägga till bilder

Lägg bildfilen i mappen `images/` i repot och referera till den i editorn som `images/filnamn.jpg`. Externa URL:er (https://…) fungerar också.

```bash
# Exempel
cp ~/Downloads/ep43.jpg images/
git add images/ep43.jpg
git commit -m "Lägg till bild för avsnitt 43"
git push
```

---

## Förhandsgranskning med live preview

Om du vill se en live-preview av sajten medan du redigerar behöver du starta en lokal server:

```bash
python3 start-server.py
```

Öppna sedan editorn på `http://localhost:8000/editor.html` istället för direkt från Finder. Sparning och allt annat fungerar på samma sätt.

---

## Filstruktur

```
allabitar/
  index.html        Sajten (läses av GitHub Pages)
  editor.html       Innehållseditor (används lokalt)
  data.json         Allt textinnehåll
  images/           Bilder för avsnittskort och hero
  start-server.py   Lokal server för live-preview
```
