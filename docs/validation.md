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
