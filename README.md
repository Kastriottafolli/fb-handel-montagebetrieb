# 2bfensterwerk

Responsive Website für 2bfensterwerk, Inhaber Faton Bytyci, Au 21a, 94137 Bayerbach. Kontakt: info@2bfensterwerk.de · 0177 5266889. Zieldomain: https://www.2bfensterwerk.de.

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
- Responsive Navigation, native FAQ, Bilderdialog und per Tastatur bedienbarer Vorher-Nachher-Regler.
- Scroll- und Bildanimationen beachten die Systemeinstellung „Bewegung reduzieren“. Inhalte bleiben ohne JavaScript sichtbar; Projektplaner und Rechner benötigen JavaScript.

## Bilder

Das vom Betreiber gelieferte Logo liegt unter `assets/img/2bfensterwerk-logo.png`. Projektbilder stammen aus dem bisherigen Repository. Die KI-generierte Architekturvisualisierung ist auf der Startseite und im Impressum entsprechend gekennzeichnet und ist keine Referenzaufnahme.

Hero-Datei: `assets/img/architektur-hero.webp`.
Generiert mit dem integrierten Imagegen-Werkzeug. Der vollständige Prompt steht in `docs/image-prompt.txt`.

## Veröffentlichung

`.openai/hosting.json` enthält die private Sites-Vorschau. `dist/` wird nicht ins Git aufgenommen, sondern beim Packaging erzeugt. Der bestehende GitHub-Pages-Workflow bleibt für einen späteren Merge nach `main` erhalten; Änderungen werden auf `codex/2bfensterwerk-redesign` zur Prüfung bereitgestellt.

Die eigene Domain ist als Ziel in Canonical-Tags und Sitemap eingetragen. DNS, Domainverbindung und E-Mail-Postfach werden durch den Seitencode nicht eingerichtet. Die private Vorschau ändert die aktuelle Firmenwebsite nicht.

Vor einem öffentlichen Betrieb sind die Unternehmensangaben abschließend zu prüfen: Das Logo enthält „OG“, bestätigt wurde der bisherige Inhaber Faton Bytyci. Eine andere Rechtsform oder Registerangabe wurde daher nicht erfunden. Die Umsatzsteuer-/Wirtschafts-Identifikationsnummern und Kammerangaben aus dem alten Repository wurden mangels gesonderter Bestätigung nicht übernommen. Falls einschlägig, sind sie im Impressum zu ergänzen. Die Datenschutzhinweise müssen an den tatsächlich eingesetzten Hosting- und E-Mail-Dienst und die betrieblichen Fristen angepasst werden. Die vorhandene GitHub-Pages-Konfiguration setzt keine Domain-DNS-Einträge.

## Prüfung

`npm run check` kontrolliert auf allen HTML-Seiten interne Links, Bilddateien, Fragmente, Seitensprache, Metadaten, eindeutige IDs, eine H1 pro Seite und veraltete Kontaktadressen. Zusätzlich werden Projektplaner, Eingabevalidierung, Datenübernahme, Energierechner, Bilderdialog und die mobile Darstellung im Browser geprüft.
