# Prüfung des neuen Auftritts

Stand: 3. November 2026.

- 13 HTML-Seiten mit Link-, Fragment-, Bilddatei-, Metadaten-, ID- und Markenprüfung erfolgreich kontrolliert (`python3 scripts/check.py`).
- JavaScript-Syntax geprüft (`node --check assets/js/site.js`).
- Statischer Build nach `dist/` erfolgreich.
- Browserprüfung: Startseite auf Desktop und im 390-Pixel-Iframe, mobile Navigation geöffnet und geschlossen; Galerie inklusive Dialogöffnung über Enter und Schließen mit Escape; Vorher-Nachher-Regler bis 100 per Tastatur.
- Projektplaner: 150 × 200 cm, 3 Elemente → 9,00 m². Breite 0 wurde abgewiesen. Anschließende Übergabe an das Kontaktformular hat Leistung und alle Projektdaten übernommen.
- Energiemodell: Standardwerte → 2.520 kWh/Jahr; 0,6 → 1,0 W/(m²K) → 560 kWh/Jahr Mehrverlust; gleiche U-Werte → 0.
- Es wurde keine Test-E-Mail versendet. Das Formular bereitet eine Nachricht im Mailprogramm des Besuchers vor und meldet keine Versandbestätigung.
- Die private Vorschau ersetzt weder DNS-Konfiguration noch eine abschließende Prüfung der Unternehmens- und Datenschutzhinweise für den öffentlichen Betrieb.

## Ergänzung: Sieben Schichten

Der originale SVG-Fensteraufbau aus dem bisherigen Auftritt wurde auf der Startseite wiederhergestellt und in Silber/Bronze gestaltet. Automatisches Öffnen beim Scrollen, Zusammensetzen per Button und erneutes Öffnen bei Schichtauswahl wurden im Browser geprüft. Nach Auswahl der Mittelscheibe bleibt genau diese hervorgehoben; sechs weitere Schichten werden abgeblendet. Es werden native Buttons mit Tastaturbedienung und Auswahlstatus verwendet. Animationen beachten reduzierte Bewegung; ohne JavaScript bleibt der aufgefächerte Aufbau sichtbar.

## Ergänzung: Logo, Metallfarben und Rollladenanimation

- Transparente PNG-Fassung per Imagegen erstellt und auf hellem und dunklem Hintergrund im Browser geprüft. Alpha an Leinwandecke, Fensteröffnung, B-Innenraum und Zwischenraum jeweils 0. Das Original bleibt erhalten.
- Metallic-Silber und Goldbronze aus direkt abgenommenen Logo-Farbproben als CSS-Variablen/Verläufe verwendet; siehe `docs/brand-colors.md`.
- Neue Rollladenillustration im Browser per Tastatur in Tageslicht-, Sichtschutz- und Abendruhe-Stellung geprüft. Pro Zustand ist genau ein Auswahlbutton aktiv. Beschriftung und Beschreibung wechseln passend zur Stellung.
- Mobile Darstellung bei 390 Pixeln kontrolliert. Bestehende Sieben-Schichten-Animation bleibt erhalten; Meta- und Linkprüfung aller 13 Seiten sowie JavaScript-Syntaxprüfung erfolgreich.

## Ergänzung: Logo-Zeichenanimation

- Animationsprinzip der Referenz ab-bau23.de angesehen: Konturzeichnung, anschließend Überblendung in die fertige Fläche. Für 2bfensterwerk unabhängig mit SVG/CSS umgesetzt, ohne Code, Grafik oder Bibliotheken der Referenz zu übernehmen.
- 25 Konturpfade aus der Alpha-Silhouette des bestehenden Logos erstellt; das PNG selbst bleibt unverändert.
- Im Browser drei Instanzen auf der Startseite bestätigt (Header, Hero, Footer). Header und Hero erreichen den Endzustand „complete“. Wiederholen per Tastatur setzt den Hero erneut auf „drawing“.
- Alle 13 Seiten auf eindeutige SVG-IDs und intakte lokale Verweise geprüft. Mobile Startseite mit größerem Hero-Logo kontrolliert. Reduzierte Bewegung deaktiviert die Zeichenanimation; ohne JavaScript bleibt die PNG-Fassung sichtbar.

## Firmenaktualisierung vom 6. November 2026

Alle 13 Seiten auf alte Namen, Ortsangaben, Anschrift und Rufnummer geprüft. Kontakt-, Datenschutz-, Über-uns- und Impressumsseite verwenden Valon Bytyçi; Telefonlinks führen zu +4915251511101. Vollständige Firmierung und Handelsregisterangaben im Impressum geprüft. Die SVG-Logoanimation wurde aus dem UG-PNG neu abgeleitet (24 Konturen), Replay im Browser geprüft. PNG enthält echte Alphatransparenz. Der ursprüngliche Sieben-Schichten-Abschnitt ist bytegenau unverändert. Kontaktseite bei 390 Pixeln ohne horizontalen Überlauf geprüft. JavaScript-Syntax und interne Website-Prüfung erfolgreich.
