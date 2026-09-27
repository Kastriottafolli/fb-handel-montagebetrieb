# -*- coding: utf-8 -*-
"""Gemeinsame Bausteine aller Seiten (Kopf, Navigation, Fusszeile, Symbole)."""

SITE = "https://www.fb-handel-montagebetrieb.de"
FIRMA = "FB Handel und Montagebetrieb"
TEL_TXT = "0177 5266889"
TEL_HREF = "+491775266889"
MAIL = "fbmontagebetrieb@gmx.de"
STRASSE = "Au 21a"
PLZ = "94137"
ORT = "Bayerbach"
VER = "2"

NAV = [
    ("leistungen.html", "Leistungen"),
    ("fenster.html", "Fenster"),
    ("tueren.html", "Türen"),
    ("projekte.html", "Projekte"),
    ("ueber-uns.html", "Über uns"),
]

ICON = {
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4.5 12.5l5 5L19.5 7"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6.5 3h3l1.6 4-2.2 1.4a12 12 0 0 0 5.7 5.7L16 11.9l4 1.6v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 3.4 5.2 2 2 0 0 1 5.4 3z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.6 6.6 12 12.6l8.4-6"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>',
 "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5.4l3.4 2"/></svg>',
 "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
 "drag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9.5 8 6 12l3.5 4M14.5 8l3.5 4-3.5 4"/></svg>',
 "window": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="1.6"/><path d="M12 3.5v17M3.5 12h17"/></svg>',
 "door": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 21V4.2a1.2 1.2 0 0 1 1-1.2l10-1a1.2 1.2 0 0 1 1.4 1.2V21"/><path d="M3.5 21h17"/><circle cx="14.2" cy="12.4" r="1"/></svg>',
 "floor": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 7.5h19M2.5 12h19M2.5 16.5h19M8 7.5V12M15 12v4.5M11 3v4.5M17 16.5V21"/></svg>',
 "bug": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="2"/><path d="M3.5 9h17M3.5 14.5h17M9 3.5v17M14.5 3.5v17"/></svg>',
 "tools": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14.5 6.2a3.8 3.8 0 0 0 5 5L14 16.8l-3.4-3.4z"/><path d="M9.6 13.2 4.3 18.5a1.9 1.9 0 0 0 2.7 2.7l5.3-5.3"/><path d="M6.5 3.5 4 6l2.6 2.6L9.2 6z"/></svg>',
 "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.8 4.8 5.6v6c0 4.4 3 8.1 7.2 9.6 4.2-1.5 7.2-5.2 7.2-9.6v-6z"/><path d="M8.8 12.2l2.2 2.2 4.2-4.4"/></svg>',
 "sound": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.2L12 5.3v13.4L7.2 14.5H4z"/><path d="M15.6 9a4.2 4.2 0 0 1 0 6"/><path d="M18.4 6.4a8 8 0 0 1 0 11.2"/></svg>',
 "thermo": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13.8 13.6V5a2.2 2.2 0 1 0-4.4 0v8.6a4.4 4.4 0 1 0 4.4 0z"/><path d="M11.6 8.4v6.4"/></svg>',
}


def head(title, desc, slug, extra_ld="", og_img="assets/img/og.jpg", noindex=False):
    canonical = SITE + "/" + ("" if slug == "index.html" else slug)
    robots = '<meta name="robots" content="noindex, follow">' if noindex else \
             '<meta name="robots" content="index, follow, max-image-preview:large">'
    return """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{canonical}">
<meta name="author" content="{firma}">
<meta name="geo.region" content="DE-BY">
<meta name="geo.placename" content="{ort}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{firma}">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site}/{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a0b0d">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="stylesheet" href="assets/css/site.css?v={ver}">
{ld}
</head>
<body>
<a class="skip-link" href="#main">Zum Inhalt springen</a>
""".format(title=title, desc=desc, robots=robots, canonical=canonical, firma=FIRMA, ort=ORT,
           site=SITE, og=og_img, ver=VER, ld=extra_ld)


def header(active):
    links = "".join(
        '<a href="{h}"{cur}>{t}</a>'.format(h=h, t=t, cur=' aria-current="page"' if h == active else "")
        for h, t in NAV)
    return """<header class="head">
  <div class="wrap head-in">
    <a class="brand" href="index.html" aria-label="{firma} – zur Startseite">
      <img src="assets/img/logo.svg" alt="{firma}" width="500" height="266">
    </a>
    <button class="burger" type="button" aria-expanded="false" aria-controls="hauptmenue" aria-label="Menü">
      <span></span>
    </button>
    <nav class="nav" id="hauptmenue" aria-label="Hauptmenü">
      {links}
      <div class="nav-actions">
        <a class="btn btn-line" href="tel:{telh}">Anrufen</a>
        <a class="btn btn-amber" href="kontakt.html">Angebot anfordern</a>
      </div>
    </nav>
    <div class="head-cta">
      <a class="head-tel" href="tel:{telh}">{phone}{telt}</a>
      <a class="btn btn-amber btn-s" href="kontakt.html">Angebot anfordern</a>
    </div>
  </div>
</header>
<main id="main">
""".format(firma=FIRMA, links=links, telh=TEL_HREF, telt=TEL_TXT, phone=ICON["phone"])


def footer(scripts=("site.js",)):
    js = "".join('<script src="assets/js/{f}?v={v}" defer></script>'.format(f=f, v=VER) for f in scripts)
    return """</main>
<div class="action-bar">
  <a class="btn btn-line" href="tel:{telh}">Anrufen</a>
  <a class="btn btn-amber" href="kontakt.html">Angebot anfordern</a>
</div>
<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="foot-logo" src="assets/img/logo-light.svg" alt="{firma}" width="500" height="266">
        <p class="muted">Fenster, Türen, Böden und Insektenschutz für {ort} und den Landkreis Rottal-Inn. Zwei Handwerker, ein Ansprechpartner.</p>
      </div>
      <div>
        <h3>Leistungen</h3>
        <ul>
          <li><a href="fenster.html">Fenster</a></li>
          <li><a href="tueren.html">Türen</a></li>
          <li><a href="boeden.html">Bodenbeläge</a></li>
          <li><a href="insektenschutz.html">Insektenschutz &amp; Rollläden</a></li>
          <li><a href="leistungen.html">Alle Leistungen</a></li>
        </ul>
      </div>
      <div>
        <h3>Betrieb</h3>
        <ul>
          <li><a href="ueber-uns.html">Über uns</a></li>
          <li><a href="projekte.html">Projekte</a></li>
          <li><a href="kontakt.html">Kontakt</a></li>
          <li><a href="impressum.html">Impressum</a></li>
          <li><a href="datenschutz.html">Datenschutz</a></li>
        </ul>
      </div>
      <div>
        <h3>Kontakt</h3>
        <ul>
          <li><a href="tel:{telh}">{telt}</a></li>
          <li><a href="mailto:{mail}">{mail}</a></li>
          <li>{strasse}, {plz} {ort}</li>
        </ul>
        <h3 style="margin-top:22px">Öffnungszeiten</h3>
        <ul>
          <li>Mo–Do 07:00–17:00 Uhr</li>
          <li>Fr 07:00–14:00 Uhr</li>
          <li>Sa–So geschlossen</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span data-year>2026</span> {firma}</span>
      <a href="impressum.html">Impressum</a>
      <a href="datenschutz.html">Datenschutz</a>
      <span class="spacer">Einsatzgebiet: {ort}, Bad Birnbach, Pfarrkirchen, Eggenfelden, Simbach, Passau</span>
    </div>
  </div>
</footer>
{js}
</body>
</html>
""".format(firma=FIRMA, ort=ORT, telh=TEL_HREF, telt=TEL_TXT, mail=MAIL, strasse=STRASSE, plz=PLZ, js=js)


def crumbs(items):
    """items: Liste (href, text); letzter Eintrag ohne Link."""
    parts = []
    for i, (href, txt) in enumerate(items):
        if i:
            parts.append("<span>/</span>")
        parts.append(txt if href is None else '<a href="%s">%s</a>' % (href, txt))
    return '<nav class="crumbs" aria-label="Brotkrumen">%s</nav>' % "".join(parts)


def img(slug, alt, cls="", sizes="(max-width: 900px) 100vw, 50vw", loading="lazy", w=1600, h=1200):
    return ('<img src="assets/img/{s}-800.webp" srcset="assets/img/{s}-800.webp 800w, '
            'assets/img/{s}-1600.webp 1600w" sizes="{sz}" alt="{a}"{c} loading="{l}" '
            'decoding="async" width="{w}" height="{h}">').format(
        s=slug, a=alt, sz=sizes, c=(' class="%s"' % cls) if cls else "", l=loading, w=w, h=h)


def shot(slug, alt, caption, tall=False):
    return ('<figure class="shot{t}" data-full="assets/img/{s}-1600.webp">'
            '<img src="assets/img/{s}-800.webp" alt="{a}" loading="lazy" decoding="async" '
            'width="800" height="600"><figcaption>{c}</figcaption></figure>').format(
        s=slug, a=alt, c=caption, t=" tall" if tall else "")


LIGHTBOX = ('<div class="lightbox" role="dialog" aria-modal="true" aria-label="Bild in Großansicht">'
            '<button class="lightbox-close" type="button" aria-label="Schließen">' + ICON["close"] + '</button>'
            '<div><img src="" alt=""><p></p></div></div>')


def cta_final(titel, text, leistung=""):
    href = "kontakt.html" + ("?leistung=" + leistung if leistung else "")
    return """<section class="cta-final pad">
  <div class="wrap">
    <div class="cta-box">
      <div data-reveal>
        <p class="eyebrow on-dark">Der nächste Schritt</p>
        <h2 class="h2">{t}</h2>
        <p class="lead">{x}</p>
      </div>
      <div class="actions" data-reveal data-delay="1" style="margin:0">
        <a class="btn btn-amber" href="{h}">Kostenloses Aufmaß anfragen</a>
        <a class="btn btn-ghost" href="tel:{telh}">{phone}{telt}</a>
      </div>
    </div>
  </div>
</section>""".format(t=titel, x=text, h=href, telh=TEL_HREF, telt=TEL_TXT, phone=ICON["phone"])
