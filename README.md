# FB Handel und Montagebetrieb – neue Website

Statische Website für **FB Handel und Montagebetrieb**, Au 21a, 94137 Bayerbach.
Schwerpunkt: **Fenster und Türen**. Kein Baukasten, kein CMS, keine Abos, keine externen
Dienste – nur HTML, CSS und etwas JavaScript.

## Vorschau

```
python3 -m http.server 8080
```

und `http://localhost:8080/` im Browser öffnen. Alternativ `index.html` direkt öffnen.

## Hochladen

Alle Dateien dieses Projekts **außer `_build/` und `.github/`** in das Webverzeichnis des
Hosters legen:

```
index.html  leistungen.html  fenster.html  tueren.html  boeden.html
insektenschutz.html  projekte.html  ueber-uns.html  kontakt.html
impressum.html  datenschutz.html
robots.txt  sitemap.xml  site.webmanifest  .nojekyll
assets/
```

Danach die Domain verbinden und HTTPS aktivieren.

## Veroeffentlichung ueber GitHub Pages

Dieses Repository veröffentlicht sich selbst: Der Arbeitsablauf
`.github/workflows/pages.yml` läuft bei jedem Push auf `main`, sammelt die Website-Dateien
ein (ohne `_build/` und `.github/`) und stellt sie auf GitHub Pages. Pages wird beim ersten
Lauf automatisch eingeschaltet.

Adresse: `https://kastriottafolli.github.io/fb-handel-montagebetrieb/`

Für die eigene Domain `fb-handel-montagebetrieb.de` später eine Datei `CNAME` mit der
Domain anlegen und beim Domain-Anbieter die DNS-Einträge auf GitHub Pages zeigen lassen.
Solange das nicht passiert ist, bleiben `canonical`, `og:url` und die `sitemap.xml` auf die
Zieldomain gesetzt – das ist Absicht, damit Suchmaschinen später die richtige Adresse
indexieren. Wer stattdessen dauerhaft unter der github.io-Adresse bleiben will, ändert
`SITE` in `_build/chrome.py` und baut neu.

## Seitenstruktur

| Seite | Inhalt |
|---|---|
| `index.html` | Start: Hero, „Anatomie eines Fensters“, Leistungen, Schallschutz-Rechner, Ablauf, Vorher/Nachher, Kennzahlen, Energierechner, Projekte, Schnellcheck, FAQ |
| `leistungen.html` | Übersicht aller Bereiche + Renovierung + reiner Handel ohne Montage |
| `fenster.html` | Material, Uw/Rw/RC-Werte, Vergleichstabelle, RAL-Montage, Einsatzgebiet |
| `tueren.html` | Haus-, Wohnungseingangs-, Zimmer-, Schiebe- und Terrassentüren, FAQ |
| `boeden.html` | Untergrund, Materialvergleich, Leistungsumfang |
| `insektenschutz.html` | Insektenschutz, Rollläden, Raffstore, textiler Sonnenschutz |
| `projekte.html` | Vorher/Nachher-Regler und Galerie mit Großansicht |
| `ueber-uns.html` | Betrieb, Arbeitsweise, Einsatzgebiet |
| `kontakt.html` | Anfrageformular, Kontaktdaten, Öffnungszeiten, Ablauf |
| `impressum.html`, `datenschutz.html` | rechtliche Seiten |

## Die 3D-Animation: Anatomie eines Fensters

Auf der Startseite (`#anatomie`). Ein isometrisch gezeichnetes Fensterelement fährt beim
Scrollen in sieben Schichten auseinander und erklärt das System aus **Wärmedämmung und
Schallschutz**:

1. Außenscheibe, 6 mm ESG
2. Argon-Füllung mit warmer Kante
3. Schallschutz-Mittelscheibe (asymmetrisch)
4. Zweiter Argon-Raum
5. Innenscheibe mit Low-E-Beschichtung
6. Drei Dichtungsebenen
7. Rahmen mit Dämmkern und RAL-Montage

Technisch ist es ein **Inline-SVG** ohne Bibliothek: Die Schichten werden per CSS-`transform`
versetzt, die Beschriftungen blenden nacheinander ein, Schallwellen laufen von außen auf die
erste Scheibe. Zeigt man auf eine Zeile der Liste, tritt die passende Schicht hervor; auf
Desktop folgt die Zeichnung leicht dem Mauszeiger. Die Schaltfläche setzt sie wieder zusammen.
Auf schmalen Bildschirmen blendet `site.js` die Beschriftungen aus und stellt die `viewBox`
um, damit die Zeichnung die volle Breite nutzt. Bei aktivierter Systemeinstellung
„Bewegung reduzieren“ ist sofort der Endzustand zu sehen.

Die Zeichnung wird von `_build/gen_anatomy.py` erzeugt (Geometrie, Schichtdicken, Beschriftungen)
und liegt als `_build/anatomy.svg` bereit. Nach Änderungen: `python3 _build/gen_anatomy.py`
im Ordner `_build`, dann `python3 _build/build.py`.

## Logo-Animation im Hero

Das Logo des Betriebs lag nur als PNG mit 500 Pixel Breite vor und war in der Kopfzeile
sichtbar unscharf. Es ist jetzt eine Vektorgrafik (`assets/img/logo.svg` für helle,
`logo-light.svg` für dunkle Flächen) und damit in jeder Größe scharf.

Auf der Startseite steht dasselbe Logo als Inline-SVG über der Überschrift und baut sich
beim Laden auf:

1. Die Konturen zeichnen sich in Bernstein nach – erst die beiden Kästen mit F und B,
   dann die Flügel.
2. Die Flügel schwingen dabei aus der geschlossenen Stellung auf, das Fenster öffnet sich.
3. Die Flächen laufen ein, die Kontur verschwindet.
4. F und B springen hinein.
5. Der Schriftzug „Handel & Montagebetrieb“ wird von links nach rechts aufgedeckt.

Parallel dazu steigen Badge, Überschrift, Text und Schaltflächen nacheinander ein.
Bei der Systemeinstellung „Bewegung reduzieren“ erscheint sofort der Endzustand.

Technisch: reine CSS-Animationen mit gestaffelten Verzögerungen. `site.js` misst je Pfad die
Länge mit `getTotalLength()` und setzt sie als CSS-Variable `--len`, damit sich die
Strichlinie sauber abrollt. Keine Bibliothek.

Die Vektorfassung entstand aus dem PNG: hochskalieren, weichzeichnen, `potrace`, danach
Kurven auflösen und mit Douglas-Peucker vereinfachen. Die Skripte dafür sind nicht Teil der
Website; die fertige Inline-Fassung liegt in `_build/logo-inline.svg`.

## Rechner

- **Schallschutz-Rechner** (`#schall`, `assets/js/tools.js`): Außenpegel und Fensteraufbau →
  Pegel im Raum. Gerechnet mit dem bewerteten Schalldämm-Maß plus 8 dB Zuschlag für das
  Verhältnis von Fensterfläche zu Raumgröße, nach unten begrenzt bei 25 dB.
- **Energierechner** (`#energie`): Ersparnis beim Fenstertausch. Transmissionswärme mit
  84 kKh/a Heizgradstunden und Anlagennutzungsgrad 0,9; CO₂ mit 0,201 kg/kWh Erdgas.
- **Projekt-Schnellcheck** (`#konfig`): drei Fragen → fertig vorbelegte Anfrage.

Alle drei schreiben ihr Ergebnis in einen Link auf `kontakt.html?leistung=…&nachricht=…`.
Das Formular übernimmt die Werte. Jedes Ergebnis steht mit Annahmen und Hinweis „Richtwert“ da.

## Kontaktformular

Das Formular läuft vollständig im Browser und öffnet das E-Mail-Programm mit fertiger
Nachricht an `fbmontagebetrieb@gmx.de`. Es überträgt nichts an einen Server und speichert
nichts. Wer ein direkt versendendes Formular möchte, bindet später einen Formulardienst
oder einen eigenen Endpunkt an – dann muss auch die Datenschutzerklärung angepasst werden.

## Vor der Veröffentlichung prüfen

- [ ] **Impressum**: Die Angaben stammen von der bisherigen Website, die den Inhabernamen
      verschlüsselt ausliefert. **Schreibweise des Inhabernamens, Umsatzsteuer-Identifikations-
      nummer, Wirtschafts-Identifikationsnummer und die Angaben zur Handwerkskammer bitte
      gegenlesen und korrigieren.** Ein Hinweis dazu steht auch als Kommentar im Quelltext.
- [ ] **Datenschutzerklärung**: beschreibt die Website im heutigen Zustand (keine Cookies,
      keine Analyse, keine externen Schriftarten oder Karten). Bei Änderungen anpassen und
      vor der Veröffentlichung rechtlich prüfen lassen.
- [ ] **Fotos**: Alle Projektbilder stammen von der bisherigen Website des Betriebs. Bitte
      bestätigen, dass die Nutzungsrechte beim Betrieb liegen. Das Stockfoto der alten Seite
      wurde bewusst nicht übernommen.
- [ ] **Zahlen**: „seit 2022“, „zwei Ansprechpartner“, „fünf Leistungsbereiche“,
      „50 km Einsatzradius“ stammen aus den Angaben des Betriebs. Bei Bedarf in `index.html`
      im Abschnitt `.stats` ändern. Es stehen bewusst **keine erfundenen Bewertungen,
      Auszeichnungen oder Projektzahlen** auf der Seite.
- [ ] **Technische Werte** (Uw, Rw, RC) sind Richtwerte gängiger Systeme und als solche
      gekennzeichnet. Verbindlich sind die Datenblätter der Hersteller.

## Gestaltung

Graphit als Grundton, Bernstein als einziger Akzent – die Farbe steht für die Wärme, die
drinnen bleiben soll. Große Typografie, ruhige Flächen, Systemschriften (kein Nachladen von
Google Fonts). Alle Symbole sind Inline-SVG, keine Unicode-Sonderzeichen, weil iOS die sonst
als farbige Emoji darstellt.

Farben und Maße stehen als CSS-Variablen ganz oben in `assets/css/site.css`.

## Technik

- Reines HTML/CSS/JS, keine Abhängigkeiten, kein Build-Schritt zum Betrieb nötig
- Bilder als WebP in zwei Größen (800/1600 px) mit `srcset`, `loading="lazy"`
- `prefers-reduced-motion` wird überall beachtet, Fokusmarkierungen sind sichtbar
- SEO: eigener Titel und eigene Beschreibung je Seite, Canonical, Open Graph,
  JSON-LD (LocalBusiness, Service, FAQPage, BreadcrumbList, ContactPage),
  `sitemap.xml`, `robots.txt`
- Nach Änderungen an CSS oder JS die Versionsnummer `VER` in `_build/chrome.py` erhöhen und
  neu bauen, damit Browser nichts aus dem Zwischenspeicher laden

## Ordner `_build/`

Erzeugt die HTML-Dateien aus gemeinsamen Bausteinen (Kopfzeile, Fußzeile, Symbole), damit
Navigation und Fußzeile nicht in elf Dateien einzeln gepflegt werden müssen.

```
python3 _build/build.py
```

Der Ordner gehört **nicht** auf den Webserver. Wer lieber direkt im HTML arbeitet, kann das
tun und `_build/` ignorieren – dann aber Änderungen an Navigation und Fußzeile in allen
Seiten nachziehen.

## Urheber

Konzept, Gestaltung und Entwicklung: Kastriot Tafolli, Softwareingenieur – www.tafolli.net
