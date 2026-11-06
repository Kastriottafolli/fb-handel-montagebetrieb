# 2bfensterwerk

Responsive Website für die 2B Fensterwerk UG (haftungsbeschränkt), Geschäftsführer Valon Bytyçi, Lindhofstraße 14, 84307 Eggenfelden. Amtsgericht Landshut, HRB 15577. Kontakt: info@2bfensterwerk.de · 0152 515 11101. Produktionsdomain: https://2bfensterwerk.de.

## Starten und prüfen

Die Website benötigt keine npm-Abhängigkeiten und keinen externen Schrift- oder Analysedienst. Python 3 genügt:

```sh
npm run dev
# http://localhost:4173
npm run check
npm run build
```

Alternativ die Python-Kommandos in `package.json` direkt verwenden. `dist/` enthält nach dem Build die auslieferbare Website. Die HTML-Seiten liegen auch direkt im Repository und funktionieren unter einem Unterverzeichnis, etwa auf GitHub Pages.

## Inhalte bearbeiten

`scripts/render.py` enthält gemeinsame Navigation, Footer, Leistungsinhalte und Seitentemplates. Nach Änderungen `python3 scripts/render.py`, danach `npm run check` und `npm run build` ausführen. Gestaltung: `assets/css/site.css`; Interaktionen: `assets/js/site.js`.

13 Seiten: Startseite, Leistungen, Fenster, Türen, Insektenschutz, Rollläden, Projekte, Über uns, Projektplaner/Rechner, Kontakt, Impressum, Datenschutz sowie eine erhaltene Einstiegsseite für die alte Böden-URL.

## Funktionen

- Originale Sieben-Schichten-Fensteranimation auf der Startseite: öffnet sich beim Scrollen, lässt sich zusammensetzen und hebt Schichten per Maus, Tastatur oder Antippen hervor. Das SVG aus dem bisherigen Auftritt liegt im neuen Abschnitt unter `scripts/sections/anatomy.html`.
- Dreistufiger Projektplaner mit Maßprüfung und Flächenberechnung. Aus 150 × 200 cm und 3 gleichen Elementen entstehen 9,00 m². Die Zusammenfassung wird per URL-Parameter ins Kontaktformular übernommen; persönliche Kontaktdaten stehen nicht in der URL.
- Modellrechnung zum Transmissionswärmeverlust: `Fläche × (Uw alt − Uw neu) × Heizgradstunden / 1000`. Bei 20 m², 2,8 → 1,0 W/(m²K) und 70.000 Kh/a ergibt sich 2.520 kWh/a. Höhere neue U-Werte werden als Mehrverlust ausgegeben. Keine Kosten- oder Verbrauchsprognose.
- Kontaktformular mit HTML-Validierung: öffnet einen E-Mail-Entwurf an info@2bfensterwerk.de. Der Besucher versendet diesen selbst. Alternativ lässt sich der Text kopieren. Es gibt keinen serverseitigen E-Mail-Versand, keinen Formularserver und keine dauerhafte lokale Speicherung. E-Mail-Übertragung im System-Mailprogramm muss auf dem jeweiligen Endgerät eingerichtet sein.
- Logoanimation nach dem Prinzip „Konturen zeichnen, Metallic-Logo einblenden“: 24 aus der vorhandenen Alpha-Silhouette abgeleitete SVG-Konturen, danach die unveränderte PNG-Fassung. Auf der Startseite mit Wiederholen-Button, im Header beim Laden und im Footer beim Erscheinen. Ohne JavaScript oder bei reduzierter Bewegung ist das Logo sofort sichtbar. Das SVG liegt in `scripts/sections/logo-motion.svg`; zur optionalen Neuberechnung der Konturen dient `scripts/trace_logo.py` (Pillow erforderlich).
- Interaktive Rollladenillustration mit Tageslicht, Sichtschutz und Abendruhe, einmaligem Bewegungsablauf beim Erscheinen und manueller Wiederholung. Zusätzlich metallische Lichtreflexe und Zeichenanimationen; neue Bewegungen beachten reduzierte Bewegung.
- Responsive Navigation, native FAQ, Bilderdialog und per Tastatur bedienbarer Vorher-Nachher-Regler.
- Scroll- und Bildanimationen beachten die Systemeinstellung „Bewegung reduzieren“. Inhalte bleiben ohne JavaScript sichtbar; Projektplaner und Rechner benötigen JavaScript.

## Bilder

Der Auftritt verwendet die freigestellte RGBA-PNG-Fassung `assets/img/2bfensterwerk-logo-ug-transparent.png` mit „UG“; Hintergrund und innere Freiräume sind transparent. Die bisherigen PNG-/WebP-Pfade enthalten dieselbe aktualisierte Fassung. Das ursprünglich gelieferte OG-Logo ist in der Git-Historie erhalten. Korrektur mit dem integrierten Imagegen-Werkzeug, Prompt in `docs/logo-ug-prompt.txt`; die ursprüngliche Freistellung ist in `docs/logo-background-prompt.txt` dokumentiert. Die RGB-Farbproben für die Silber- und Goldbronze-Verläufe sind in `docs/brand-colors.md` dokumentiert; Gestaltung in `assets/css/metallic.css`. Projektbilder stammen aus dem bisherigen Repository. Die KI-generierte Architekturvisualisierung ist auf der Startseite und im Impressum entsprechend gekennzeichnet und ist keine Referenzaufnahme.

Hero-Datei: `assets/img/architektur-hero.webp`.
Generiert mit dem integrierten Imagegen-Werkzeug. Der vollständige Prompt steht in `docs/image-prompt.txt`.

## Veröffentlichung

Die statische Website wurde am 3. November 2026 im bestehenden DreamHost-Tarif Web Hosting Launch, EU-West Amsterdam, in das Webverzeichnis für `2bfensterwerk.de` hochgeladen. Der genaue Stand und die noch ausstehende öffentliche Domain-/SSL-Aktivierung stehen in `docs/dreamhost-deployment.md`. Canonical-Tags, Sitemap und Datenschutzhinweise sind auf DreamHost und `https://2bfensterwerk.de` abgestimmt. `.htaccess` setzt den Verzeichnisindex, unterbindet Verzeichnislisten und ergänzt HTTP-Sicherheitsheader.

Für ein Update `npm run check` und `npm run build` ausführen und den Inhalt von `dist/` einschließlich `.htaccess` in das Domainverzeichnis hochladen. Keine Quelltexte, `.git`, `.openai` oder Zugangsdaten hochladen. Das Kontaktformular öffnet weiterhin einen E-Mail-Entwurf; es hat keinen serverseitigen Versand.

`.openai/hosting.json` gehört zur bisherigen privaten Sites-Vorschau. `dist/` wird nicht ins Git aufgenommen. Der bestehende GitHub-Pages-Workflow bleibt für einen späteren Merge nach `main` erhalten; er ist nicht mit DreamHost verbunden. Der Quellstand liegt auf `codex/2bfensterwerk-redesign`.

Firmierung, Sitz, Geschäftsanschrift, Registergericht und HRB-Nummer wurden am 6. November 2026 anhand des vom Betreiber gelieferten Handelsregisterauszugs aktualisiert. Die Schreibweise „Valon Bytyçi“ hat der Betreiber ausdrücklich bestätigt; der vorgelegte Auszug schreibt „Bytyqi“. Das Impressum nennt ihn als Geschäftsführer. Geburtsdatum und privater Wohnort aus dem Registerauszug werden nicht veröffentlicht. Nicht vorliegende Steuer- und Kammerangaben wurden nicht ergänzt. Alle sichtbaren Logo-Fassungen und die gezeichneten Konturen verwenden „UG“.

## Prüfung

`npm run check` kontrolliert auf allen HTML-Seiten interne Links, Bilddateien, Fragmente, Seitensprache, Metadaten, eindeutige IDs, eine H1 pro Seite und veraltete Kontaktadressen. Zusätzlich werden Projektplaner, Eingabevalidierung, Datenübernahme, Energierechner, Bilderdialog und die mobile Darstellung im Browser geprüft.
