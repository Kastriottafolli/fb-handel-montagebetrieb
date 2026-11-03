# DreamHost-Veröffentlichung

Stand: 3. November 2026, Europe/Berlin.

## Hochgeladen und geprüft

- Domain: `2bfensterwerk.de`, Hosting im bestehenden Web Hosting Launch, EU-West Amsterdam.
- Webverzeichnis: `/home/dh_v3kehy/2bfensterwerk.de`.
- Ursprung-IP laut DreamHost-DNS: `66.33.214.21` für Domain und www.
- ZIP-Inhalt aus `dist/` mit DreamHost File Manager hochgeladen und entpackt; vorab befanden sich nur DreamHost-Diagnose- und leere Favicon-Dateien im Verzeichnis.
- Alle 13 HTML-Seiten und sieben zentrale Ressourcen am HTTP-Ursprungsserver mit Host-Header `2bfensterwerk.de` abgerufen: HTTP 200 und exakte Übereinstimmung mit den lokalen Dateien. Darunter beide Stylesheets, JavaScript, transparentes Logo, Hero-Bild, Sitemap und robots.txt.
- `python3 scripts/check.py` und `node --check assets/js/site.js` erfolgreich.
- Kein Zugangsschlüssel und kein Quellarchiv im öffentlichen Webverzeichnis. Keine Änderung an Mailkonten oder MX-Einträgen.

## Noch ausstehend

DreamHost meldet die Registrierung als Active, den Registranten als Verified und DreamHost-Nameserver als ausgewählt. Die DreamHost-Nameserver liefern bereits den A-Record. Die öffentliche .de-Zone (`f.nic.de`) und Resolver `1.1.1.1` lieferten bei der Abschlussprüfung noch NXDOMAIN. Die Domain ist deshalb noch nicht öffentlich erreichbar; dies ist keine erfolgreiche öffentliche HTTPS-Prüfung.

Das automatisch angeforderte SSL-Zertifikat steht im DreamHost-Panel auf Pending. Der direkte TLS-Abruf liefert derzeit ein selbstsigniertes Zertifikat und wird regulär abgelehnt. Zertifikatsprüfung wurde nicht umgangen. Es wurde keine HTTPS-Weiterleitung auf einen noch ungültigen Endpunkt gesetzt.

Sobald die Delegation öffentlich ist, Domain und www sowie gültiges HTTPS erneut prüfen. Sollte die Delegation weiter fehlen, muss DreamHost den Registrierungs-/Delegationsstatus prüfen. Kontakt zu Support wurde nicht aufgenommen.

## Wiederholbare Prüfung

```sh
# Öffentliche Delegation und Auflösung
dig @f.nic.de 2bfensterwerk.de NS
dig @1.1.1.1 2bfensterwerk.de A
# Öffentliche Website und gültiges Zertifikat
curl --fail --silent --show-error --output /dev/null --write-out '%{http_code}\n' https://2bfensterwerk.de/
```

Der Build benötigt keinen Formularserver. Anfragen werden vom Besucher mit seinem E-Mail-Programm versendet.
