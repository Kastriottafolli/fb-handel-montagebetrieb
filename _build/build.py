# -*- coding: utf-8 -*-
"""Erzeugt alle HTML-Seiten im Ordner darueber.

    python3 _build/build.py

Die fertigen Dateien liegen danach direkt in fb-handel/ und brauchen
zum Betrieb der Website nichts aus diesem Ordner.
"""
import io, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from chrome import SITE
import s_index, s_fenster, s_tueren, s_boeden, s_insekt, s_rest, s_kontakt

PAGES = [
    ("index.html",        s_index.build,        "1.0",  "weekly"),
    ("leistungen.html",   s_rest.leistungen,    "0.9",  "monthly"),
    ("fenster.html",      s_fenster.build,      "0.9",  "monthly"),
    ("tueren.html",       s_tueren.build,       "0.9",  "monthly"),
    ("boeden.html",       s_boeden.build,       "0.8",  "monthly"),
    ("insektenschutz.html", s_insekt.build,     "0.8",  "monthly"),
    ("projekte.html",     s_rest.projekte,      "0.8",  "monthly"),
    ("ueber-uns.html",    s_rest.ueber_uns,     "0.7",  "yearly"),
    ("kontakt.html",      s_kontakt.kontakt,    "0.9",  "yearly"),
    ("impressum.html",    s_kontakt.impressum,  "0.2",  "yearly"),
    ("datenschutz.html",  s_kontakt.datenschutz, "0.2", "yearly"),
]

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="13" fill="#14161a"/>
<rect x="13" y="12" width="38" height="40" rx="2.5" fill="none" stroke="#f5f5f3" stroke-width="4"/>
<path d="M32 12v40M13 32h38" stroke="#f5f5f3" stroke-width="4"/>
<rect x="17.5" y="16.5" width="10" height="11" fill="#e8a33d"/>
</svg>'''

MANIFEST = '''{
  "name": "FB Handel und Montagebetrieb",
  "short_name": "FB Montage",
  "description": "Fenster, T\\u00fcren, B\\u00f6den und Insektenschutz in Bayerbach.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0a0b0d",
  "theme_color": "#0a0b0d",
  "lang": "de",
  "icons": [
    { "src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml" },
    { "src": "assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png" }
  ]
}
'''

ROBOTS = "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE


def write(name, text):
    with io.open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return len(text.encode("utf-8"))


def main():
    heute = datetime.date.today().isoformat()
    total = 0
    for name, fn, prio, freq in PAGES:
        n = write(name, fn())
        total += n
        print("  %-22s %7d Bytes" % (name, n))

    urls = "".join(
        "  <url><loc>%s/%s</loc><lastmod>%s</lastmod>"
        "<changefreq>%s</changefreq><priority>%s</priority></url>\n"
        % (SITE, "" if name == "index.html" else name, heute, freq, prio)
        for name, _, prio, freq in PAGES)
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    write("robots.txt", ROBOTS)
    write("site.webmanifest", MANIFEST)
    write(os.path.join("assets", "img", "favicon.svg"), FAVICON)
    write(".nojekyll", "")
    print("  sitemap.xml, robots.txt, site.webmanifest, favicon.svg")
    print("Gesamt HTML: %.1f KB" % (total / 1024.0))


if __name__ == "__main__":
    main()
