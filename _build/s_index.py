# -*- coding: utf-8 -*-
from chrome import *
import io, json

ANATOMY = io.open("anatomy.svg", encoding="utf-8").read()
LOGO = io.open("logo-inline.svg", encoding="utf-8").read()

FAQ = [
 ("Was kostet ein neues Fenster?",
  "Das hängt an Maß, Material, Verglasung und Einbausituation – seriös lässt sich das erst nach dem "
  "Aufmaß sagen. Wir messen kostenlos vor Ort, zeigen Ihnen zwei bis drei Varianten und schreiben ein Angebot, "
  "in dem jede Position einzeln steht: Element, Montage, Entsorgung, Innen- und Außenanschluss."),
 ("Wie lange dauert der Fenstertausch in einem Einfamilienhaus?",
  "Die Montage selbst dauert meist ein bis zwei Tage. Rechnen Sie ab Auftrag mit sechs bis zehn Wochen Lieferzeit "
  "für die Elemente – die genaue Zeit nennen wir Ihnen beim Angebot, weil sie vom Hersteller abhängt."),
 ("Muss ich während der Arbeiten ausziehen?",
  "Nein. Wir arbeiten raumweise, decken Boden und Möbel ab und schließen jede geöffnete Wand noch am selben Tag. "
  "Abends ist Ihr Haus wieder dicht."),
 ("Was passiert mit den alten Fenstern?",
  "Wir bauen sie aus, transportieren sie ab und entsorgen sie fachgerecht. Das steht als eigene Position im Angebot, "
  "damit Sie wissen, was es kostet."),
 ("Lohnen sich Schallschutzfenster auch ohne Hauptstraße vor der Tür?",
  "Oft ja. Schon ein Unterschied von 5 bis 10 Dezibel entscheidet darüber, ob Sie bei gekipptem Fenster schlafen "
  "können. Welche Schallschutzklasse sinnvoll ist, rechnen wir mit Ihnen am konkreten Standort durch."),
 ("In welchem Umkreis arbeiten Sie?",
  "Von Bayerbach aus im Umkreis von rund 50 Kilometern: Bad Birnbach, Pfarrkirchen, Eggenfelden, Simbach am Inn, "
  "Rotthalmünster, Griesbach und Passau. Fragen Sie auch darüber hinaus an – wir sagen Ihnen ehrlich, ob es passt."),
]

LD = json.dumps({
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
      "@id": SITE + "/#betrieb",
      "name": FIRMA,
      "description": "Fachbetrieb für Fenster, Türen, Bodenbeläge, Insektenschutz und Renovierung in "
                     "Bayerbach im Landkreis Rottal-Inn.",
      "url": SITE + "/",
      "telephone": "+49 177 5266889",
      "email": MAIL,
      "image": SITE + "/assets/img/og.jpg",
      "logo": SITE + "/assets/img/logo.png",
      "foundingDate": "2022",
      "address": {"@type": "PostalAddress", "streetAddress": STRASSE, "postalCode": PLZ,
                  "addressLocality": ORT, "addressRegion": "Bayern", "addressCountry": "DE"},
      "areaServed": [{"@type": "City", "name": n} for n in
                     ["Bayerbach", "Bad Birnbach", "Pfarrkirchen", "Eggenfelden", "Simbach am Inn",
                      "Rotthalmünster", "Bad Griesbach", "Passau"]],
      "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
         "opens": "07:00", "closes": "17:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Friday"], "opens": "07:00", "closes": "14:00"}],
      "hasOfferCatalog": {
        "@type": "OfferCatalog", "name": "Leistungen",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
                            ["Fenstermontage und Fenstertausch", "Haustüren und Innentüren",
                             "Bodenbeläge verlegen", "Insektenschutz und Rollläden",
                             "Renovierungsarbeiten"]]}
    },
    {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": FIRMA,
     "inLanguage": "de-DE", "publisher": {"@id": SITE + "/#betrieb"}},
    {"@type": "FAQPage", "mainEntity": [
      {"@type": "Question", "name": q,
       "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
  ]}, ensure_ascii=False, indent=None)


def build():
    faq_html = "".join(
        '<details{o}><summary>{q}</summary><div class="answer">{a}</div></details>'.format(
            q=q, a=a, o=" open" if i == 0 else "") for i, (q, a) in enumerate(FAQ))

    return head(
        "Fenster, Türen &amp; Böden | FB Montagebetrieb Bayerbach",
        "Fenster, T\u00fcren, B\u00f6den und Insektenschutz vom Fachbetrieb in Bayerbach. Aufma\u00df, Montage "
        "und Entsorgung aus einer Hand. Kostenloses Aufma\u00df: " + TEL_TXT + ".",
        "index.html", '<script type="application/ld+json">%s</script>' % LD
    ) + header("index.html") + """

<section class="hero">
  <div class="hero-bg">
    <img src="assets/img/grossfenster-abend-1600.webp" alt="Gro\u00dfes Fenster mit grauem Rahmen in der Abendd\u00e4mmerung" fetchpriority="high" width="1024" height="768">
  </div>
  <div class="wrap hero-in">
    {logo}
    <span class="hero-badge" data-reveal><b>Seit 2022</b> Fenster &middot; Türen &middot; Böden in Bayerbach</span>
    <h1 class="display" data-reveal data-delay="1">Wärme bleibt drin.<br><span class="grad-text">Lärm bleibt draußen.</span></h1>
    <p class="lead" data-reveal data-delay="2">Wir liefern und montieren Fenster, Türen, Böden und Insektenschutz – in Bayerbach, im Rottal und rund um Passau. Zwei gelernte Handwerker, ein Ansprechpartner, eine saubere Baustelle.</p>
    <div class="actions" data-reveal data-delay="3">
      <a class="btn btn-amber" href="kontakt.html">Kostenloses Aufmaß anfragen</a>
      <a class="btn btn-ghost" href="tel:{telh}">{phone}{telt}</a>
    </div>
    <ul class="hero-trust" data-reveal data-delay="4">
      <li>{check} Aufmaß, Montage und Entsorgung aus einer Hand</li>
      <li>{check} Kurzfristige Termine möglich</li>
      <li>{check} Festpreis vor Arbeitsbeginn</li>
    </ul>
  </div>
</section>

<section class="dark pad-s">
  <div class="wrap">
    <p class="words" data-reveal>Ein Fenster ist kein Möbelstück. Es entscheidet, <mark>wie warm, wie leise und wie sicher</mark> Sie wohnen.</p>
  </div>
</section>

<section class="anatomy" id="anatomie" aria-labelledby="anatomie-titel">
  <div class="anatomy-in">
    <div class="anatomy-copy">
      <p class="eyebrow on-dark">Anatomie eines Fensters</p>
      <h2 class="h2" id="anatomie-titel">Sieben Schichten<br>zwischen Ihnen und dem Lärm.</h2>
      <p class="lead">Von außen sieht man einen Rahmen und eine Scheibe. Dazwischen arbeitet ein ganzes System aus Glas, Edelgas, Beschichtung und Dichtung. Jede Schicht hat eine Aufgabe – erst zusammen halten sie Kälte, Zugluft und Straßenlärm draußen.</p>
      <ol class="layer-list">
        <li><b>Außenscheibe, 6 mm ESG</b><span>Nimmt Wetter, Hagel und den ersten Teil des Schalls auf. Auf Wunsch mit Sonnenschutz.</span></li>
        <li><b>Argon mit warmer Kante</b><span>Edelgas statt Luft leitet weniger Wärme. Der Abstandhalter aus Kunststoff verhindert die kalte Ecke.</span></li>
        <li><b>Schallschutz-Mittelscheibe</b><span>Bewusst anders dick als die Nachbarscheiben. Diese Asymmetrie bricht die Schallwelle.</span></li>
        <li><b>Zweiter Argon-Raum</b><span>Die zweite Kammer. Sie macht aus gutem Wärmeschutz sehr guten.</span></li>
        <li><b>Innenscheibe mit Low-E</b><span>Eine hauchdünne Metallschicht wirft die Heizwärme in den Raum zurück.</span></li>
        <li><b>Drei Dichtungsebenen</b><span>Die Mitteldichtung ist die wichtigste: Sie stoppt Zugluft, bevor sie überhaupt ankommt.</span></li>
        <li><b>Rahmen mit Dämmkern</b><span>Mehrkammerprofil, thermisch getrennt – und ein Einbau nach RAL: innen luftdicht, außen schlagregendicht, in der Mitte gedämmt.</span></li>
      </ol>
      <div class="anatomy-controls">
        <button class="btn btn-ghost btn-s" type="button" data-anatomy-toggle data-label-play="Aufbau zeigen" data-label-reset="Wieder zusammensetzen">Wieder zusammensetzen</button>
        <a class="link-arrow" href="fenster.html">Alles zu unseren Fenstern</a>
      </div>
      <p class="anatomy-note">Zeigen Sie auf eine Zeile, um die Schicht hervorzuheben. Der genaue Aufbau hängt vom gewählten System ab.</p>
    </div>
    <div class="anatomy-art">{anatomy}</div>
  </div>
</section>

<section class="pad" id="leistungen">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Was wir machen</p>
    <h2 class="h2" data-reveal>Fünf Bereiche, ein Ansprechpartner.</h2>
    <p class="lead" data-reveal style="max-width:54ch">Vom einzelnen Kellerfenster bis zum kompletten Haus. Wir planen, liefern, montieren und räumen auf.</p>
    <div class="bento" style="margin-top:44px">
      <article class="tile photo tile-span-3 tile-tall" data-reveal>
        {img_fenster}
        <h3 class="h3">Fenster</h3>
        <p>Kunststoff, Holz und Aluminium. Zweifach oder dreifach verglast, auf Wunsch mit Schallschutz und Einbruchhemmung.</p>
        <a class="link-arrow tile-link" href="fenster.html">Fenster ansehen</a>
      </article>
      <article class="tile photo tile-span-3 tile-tall" data-reveal data-delay="1">
        {img_tuer}
        <h3 class="h3">Türen</h3>
        <p>Haustüren, Wohnungseingangs- und Terrassentüren. Vom Aufmaß bis zum justierten Beschlag.</p>
        <a class="link-arrow tile-link" href="tueren.html">Türen ansehen</a>
      </article>
      <article class="tile tile-span-2" data-reveal>
        <span class="tile-icon">{ic_floor}</span>
        <h3 class="h3">Bodenbeläge</h3>
        <p>Laminat, Parkett, Vinyl und Designbeläge – inklusive Untergrundprüfung und Sockelleisten.</p>
        <a class="link-arrow tile-link" href="boeden.html">Böden ansehen</a>
      </article>
      <article class="tile tile-span-2" data-reveal data-delay="1">
        <span class="tile-icon">{ic_bug}</span>
        <h3 class="h3">Insektenschutz &amp; Rollläden</h3>
        <p>Maßgefertigte Gitter, Plissées und Rollläden. Passgenau, meist ohne Bohren in den Rahmen.</p>
        <a class="link-arrow tile-link" href="insektenschutz.html">Schutz ansehen</a>
      </article>
      <article class="tile tile-span-2" data-reveal data-delay="2">
        <span class="tile-icon">{ic_tools}</span>
        <h3 class="h3">Renovierung</h3>
        <p>Wenn beim Fenstertausch mehr zu tun ist: Laibungen, Anschlüsse, kleine Umbauten. Aus einer Hand.</p>
        <a class="link-arrow tile-link" href="leistungen.html#renovierung">Renovierung ansehen</a>
      </article>
    </div>
  </div>
</section>

<section class="dark-2 pad" id="schall">
  <div class="wrap">
    <p class="eyebrow on-dark" data-reveal>Rechner</p>
    <h2 class="h2" data-reveal>Wie leise wird es bei Ihnen?</h2>
    <p class="lead" data-reveal style="max-width:52ch">Wählen Sie, was draußen los ist und was heute im Rahmen steckt. Der Rechner zeigt, was ein neuer Aufbau bringt.</p>
    <div class="tool" style="margin-top:40px" data-reveal>
      <div class="tool-in">
        <div class="field">
          <label for="schall-aussen">Was hören Sie draußen?</label>
          <select id="schall-aussen">
            <option value="55">Ruhige Wohnstraße (ca. 55 dB)</option>
            <option value="60" selected>Wohnstraße mit Verkehr (ca. 60 dB)</option>
            <option value="65">Ortsdurchfahrt (ca. 65 dB)</option>
            <option value="70">Stark befahrene Straße (ca. 70 dB)</option>
            <option value="75">Bahnlinie oder Lkw-Verkehr (ca. 75 dB)</option>
          </select>
        </div>
        <div class="field">
          <label for="schall-alt">Was ist heute eingebaut?</label>
          <select id="schall-alt">
            <option value="27">Altes Einfachglas</option>
            <option value="32" selected>Zweifachglas, älter als 20 Jahre</option>
            <option value="35">Modernes Zweifachglas</option>
          </select>
        </div>
        <div class="field">
          <label for="schall-neu">Was soll rein?</label>
          <select id="schall-neu">
            <option value="35">Dreifachglas, Standard (Rw ca. 35 dB)</option>
            <option value="37">Schallschutzklasse 3 (Rw ca. 37 dB)</option>
            <option value="42" selected>Schallschutzklasse 4 (Rw ca. 42 dB)</option>
            <option value="45">Schallschutzklasse 5 (Rw ca. 45 dB)</option>
          </select>
        </div>
      </div>
      <div class="tool-out">
        <svg class="db-visual" viewBox="0 0 320 96" aria-hidden="true">
          <g fill="none" stroke-linecap="round">
            <path class="sw sw-out" d="M18 48c10-26 20-26 30 0s20 26 30 0" stroke="#e8a33d" stroke-width="3"/>
            <path class="sw sw-out" d="M78 48c10-20 20-20 30 0s20 20 30 0" stroke="#e8a33d" stroke-width="3"/>
            <rect x="146" y="12" width="14" height="72" rx="3" fill="#2a2e35" stroke="none"/>
            <rect x="164" y="12" width="14" height="72" rx="3" fill="#2a2e35" stroke="none"/>
            <path class="sw sw-in" d="M188 48c10-9 20-9 30 0s20 9 30 0" stroke="#8fd7e6" stroke-width="2"/>
            <path class="sw sw-in" d="M248 48c10-6 20-6 30 0s20 6 30 0" stroke="#8fd7e6" stroke-width="2"/>
          </g>
        </svg>
        <p class="muted" style="font-size:14px;margin:0 0 12px">draußen → Fenster → drinnen</p>
        <p class="result-big"><span id="schall-innen">26</span> <small>dB im Raum</small></p>
        <p id="schall-klasse" class="muted" style="margin-top:10px"></p>
        <div class="db-meter">
          <div class="db-bar"><b id="schall-bar" style="width:20%"></b></div>
          <div class="db-scale"><span>25 dB sehr leise</span><span>65 dB störend</span></div>
        </div>
        <ul class="result-rows">
          <li><span>Heute im Raum</span><b><span id="schall-alt-out">36</span> dB</b></li>
          <li><span>Unterschied</span><b>−<span id="schall-diff">10</span> dB</b></li>
          <li><span>Empfundene Lautstärke</span><b>rund <span id="schall-mal">2</span>× leiser</b></li>
        </ul>
        <a class="btn btn-amber" id="schall-cta" href="kontakt.html" style="margin-top:26px">Diesen Aufbau anfragen</a>
        <p class="disclaimer">Richtwert. Gerechnet wird mit dem bewerteten Schalldämm-Maß des Fensters und einem pauschalen Zuschlag von 8 Dezibel für das Verhältnis von Fensterfläche zu Raumgröße. Nach unten begrenzen wir bei 25 Dezibel, dem üblichen Grundgeräusch eines ruhigen Wohnraums. Rollladenkasten, Fassade und Lüftung wirken zusätzlich mit. Zehn Dezibel weniger nehmen wir ungefähr als halb so laut wahr. Das verbindliche Ergebnis kommt aus dem Aufmaß vor Ort.</p>
      </div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Ablauf</p>
    <h2 class="h2" data-reveal>Vom Anruf bis zum letzten Handgriff.</h2>
    <div class="steps">
      <span class="steps-line" aria-hidden="true"><b></b></span>
      <div class="step" data-reveal><span class="step-n">1</span><h3 class="h4">Anruf und Termin</h3><p>Sie schildern kurz, worum es geht. Wir sagen am Telefon, ob und wann wir es machen können.</p></div>
      <div class="step" data-reveal data-delay="1"><span class="step-n">2</span><h3 class="h4">Aufmaß und Beratung</h3><p>Wir messen vor Ort, prüfen den Anschluss und besprechen Material, Verglasung und Farbe. Kostenlos.</p></div>
      <div class="step" data-reveal data-delay="2"><span class="step-n">3</span><h3 class="h4">Angebot mit Festpreis</h3><p>Jede Position einzeln aufgeführt: Element, Montage, Entsorgung, Anschluss. Keine Überraschungen.</p></div>
      <div class="step" data-reveal data-delay="3"><span class="step-n">4</span><h3 class="h4">Montage und Übergabe</h3><p>Abgedeckt, sauber, termintreu. Am Ende gehen wir gemeinsam durch und justieren alles nach.</p></div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <div class="split">
      <div data-reveal>
        <p class="eyebrow">Vorher und nachher</p>
        <h2 class="h2">Aus Glasbausteinen wird Tageslicht.</h2>
        <p class="lead">Bei diesem Haus saßen über dem Eingang noch Glasbausteine. Heute steht dort ein schlankes Fensterelement in Anthrazit – mehr Licht, dichter Anschluss, saubere Laibung.</p>
        <div class="actions"><a class="btn btn-dark" href="projekte.html">Mehr Projekte ansehen</a></div>
      </div>
      <div class="ba" data-reveal data-delay="1" style="--pos:50%">
        <img src="assets/img/ba-vorher-glasbausteine-800.webp" alt="Hausfassade mit Glasbausteinen über dem Eingang vor dem Umbau" loading="lazy" decoding="async" width="537" height="430">
        <img class="after" src="assets/img/ba-nachher-fensterelement-800.webp" alt="Dieselbe Fassade mit neuem schlankem Fensterelement in Anthrazit" loading="lazy" decoding="async" width="537" height="430">
        <span class="ba-tag l">Vorher</span><span class="ba-tag r">Nachher</span>
        <span class="ba-handle" aria-hidden="true"><span class="ba-knob">{drag}</span></span>
        <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Vergleich vorher und nachher verschieben">
      </div>
    </div>
  </div>
</section>

<section class="dark pad">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><b>2022</b><span>gegründet in Bayerbach</span></div>
      <div class="stat"><b data-count="2">2</b><span>feste Ansprechpartner</span></div>
      <div class="stat"><b data-count="5">5</b><span>Leistungsbereiche</span></div>
      <div class="stat"><b data-count="50" data-suffix=" km">50 km</b><span>Einsatzradius um Bayerbach</span></div>
    </div>
    <p class="muted" style="margin-top:22px;font-size:14px">Zahlen aus dem Betrieb. Wir schreiben hier keine erfundenen Auszeichnungen und keine erfundenen Bewertungen hin.</p>
  </div>
</section>

<section class="pad" id="energie">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Rechner</p>
    <h2 class="h2" data-reveal>Was ein Fenstertausch im Jahr spart.</h2>
    <p class="lead" data-reveal style="max-width:52ch">Alte Fenster sind oft der größte einzelne Wärmeverlust im Haus. Schieben Sie Ihre Fensterfläche ein.</p>
    <div class="tool" style="margin-top:40px" data-reveal>
      <div class="tool-in">
        <div class="field">
          <label for="e-flaeche">Fensterfläche insgesamt: <span id="e-flaeche-out" class="amber-text">22 m²</span></label>
          <input type="range" id="e-flaeche" min="4" max="60" step="1" value="22">
          <p class="hint">Faustwert: ein normales Wohnzimmerfenster hat rund 2 m². Ein Einfamilienhaus kommt oft auf 20 bis 30 m².</p>
        </div>
        <div class="field">
          <label for="e-alt">Was ist heute eingebaut?</label>
          <select id="e-alt">
            <option value="5.0">Einfachglas, vor 1978</option>
            <option value="2.9" selected>Isolierglas, 1978 bis 1995</option>
            <option value="1.6">Zweifach-Wärmedammglas, ab 1995</option>
            <option value="1.3">Modernes Zweifachglas</option>
          </select>
        </div>
        <div class="field">
          <label for="e-neu">Was soll rein?</label>
          <select id="e-neu">
            <option value="1.30">Zweifachglas, aktueller Standard (Uw 1,3)</option>
            <option value="0.95" selected>Dreifachglas (Uw 0,95)</option>
            <option value="0.80">Dreifachglas mit gutem Rahmen (Uw 0,8)</option>
          </select>
        </div>
        <div class="field">
          <label for="e-preis">Ihr Energiepreis in Euro je Kilowattstunde</label>
          <input type="number" id="e-preis" min="0.02" max="0.9" step="0.01" value="0.11">
          <p class="hint">Voreingestellt ist ein Erdgaspreis. Bei Strom oder Öl den eigenen Wert eintragen.</p>
        </div>
      </div>
      <div class="tool-out">
        <p class="eyebrow">Ersparnis im Jahr</p>
        <p class="result-big"><span id="e-euro">0</span> <small>Euro</small></p>
        <ul class="result-rows">
          <li><span>Weniger Heizenergie</span><b><span id="e-kwh">0</span> kWh</b></li>
          <li><span>Weniger CO₂</span><b><span id="e-co2">0</span> kg</b></li>
          <li><span>In zehn Jahren</span><b>rund <span id="e-10j">0</span> Euro</b></li>
        </ul>
        <a class="btn btn-amber" id="e-cta" href="kontakt.html" style="margin-top:26px">Angebot für diesen Tausch</a>
        <p class="disclaimer">Richtwert für die Transmissionswärme durch die Fensterfläche. Gerechnet mit 84 Kilokelvinstunden Heizgradstunden je Jahr und einem Anlagennutzungsgrad von 0,9. Lüftungsverluste, Sonneneintrag und Förderungen sind nicht enthalten. Wir ersetzen damit keine Energieberatung.</p>
      </div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Aus unseren Projekten</p>
    <h2 class="h2" data-reveal>Arbeiten aus Bayerbach und Umgebung.</h2>
    <div class="gallery" style="margin-top:38px" data-reveal>
      {gal}
    </div>
    <div class="actions"><a class="btn btn-dark" href="projekte.html">Alle Projekte ansehen</a></div>
  </div>
</section>

<section class="pad" id="konfig">
  <div class="wrap wrap-narrow">
    <p class="eyebrow center" data-reveal>Schnellcheck</p>
    <h2 class="h2 center" data-reveal>Drei Fragen, dann ist Ihre Anfrage fertig.</h2>
    <div style="margin-top:38px" data-reveal>
      <div class="field">
        <span class="field-label">1. Worum geht es?</span>
        <div class="choice">
          <button class="btn btn-line btn-s" type="button" data-konfig="vorhaben" data-value="Fenster tauschen" aria-pressed="false">Fenster tauschen</button>
          <button class="btn btn-line btn-s" type="button" data-konfig="vorhaben" data-value="Haustür oder Innentüren" aria-pressed="false">Haustür oder Innentüren</button>
          <button class="btn btn-line btn-s" type="button" data-konfig="vorhaben" data-value="Bodenbelag verlegen" aria-pressed="false">Bodenbelag verlegen</button>
          <button class="btn btn-line btn-s" type="button" data-konfig="vorhaben" data-value="Insektenschutz oder Rollladen" aria-pressed="false">Insektenschutz oder Rollladen</button>
        </div>
      </div>
      <div class="field">
        <span class="field-label">2. Wie groß ist der Umfang?</span>
        <div class="choice">
          <button class="btn btn-line btn-s" type="button" data-konfig="umfang" data-value="Ein einzelnes Element" aria-pressed="false">Ein einzelnes Element</button>
          <button class="btn btn-line btn-s" type="button" data-konfig="umfang" data-value="Mehrere Räume" aria-pressed="false">Mehrere Räume</button>
          <button class="btn btn-line btn-s" type="button" data-konfig="umfang" data-value="Ganzes Haus oder Neubau" aria-pressed="false">Ganzes Haus oder Neubau</button>
        </div>
      </div>
      <div class="field">
        <span class="field-label">3. Wann soll es passieren?</span>
        <div class="choice">
          <button class="btn btn-line btn-s" type="button" data-konfig="zeit" data-value="So bald wie möglich" aria-pressed="false">So bald wie möglich</button>
          <button class="btn btn-line btn-s" type="button" data-konfig="zeit" data-value="In den nächsten Monaten" aria-pressed="false">In den nächsten Monaten</button>
          <button class="btn btn-line btn-s" type="button" data-konfig="zeit" data-value="Ich plane erst" aria-pressed="false">Ich plane erst</button>
        </div>
      </div>
      <div id="konfig-out" hidden>
        <div class="note"><b>Ihre Anfrage</b><span id="konfig-summary"></span></div>
        <div class="actions"><a class="btn btn-amber" id="konfig-cta" href="kontakt.html">Anfrage jetzt absenden</a>
        <a class="btn btn-line" href="tel:{telh}">Lieber anrufen</a></div>
      </div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <p class="eyebrow center" data-reveal>Häufige Fragen</p>
    <h2 class="h2 center" data-reveal>Das fragen uns Kundinnen und Kunden am häufigsten.</h2>
    <div class="faq" data-reveal>{faq}</div>
  </div>
</section>

{cta}
{lightbox}
""".format(
        logo=LOGO, telh=TEL_HREF, telt=TEL_TXT, phone=ICON["phone"], check=ICON["check"], drag=ICON["drag"],
        ic_floor=ICON["floor"], ic_bug=ICON["bug"], ic_tools=ICON["tools"],
        anatomy=ANATOMY,
        img_fenster=img("grossfenster-abend", "Großes Fenster mit grauem Rahmen in der Abenddämmerung", sizes="(max-width: 900px) 100vw, 50vw", w=1024, h=768),
        img_tuer=img("haustuer-weiss", "Weiße zweiflügelige Haustür mit Seitenteil", sizes="(max-width: 900px) 100vw, 50vw", w=1024, h=768),
        gal="".join([
            shot("terrassentuer-festverglasung", "Große Terrassentür mit Festverglasung von innen", "Terrassentür mit Festverglasung, Blick auf die Terrasse"),
            shot("fenster-jalousie-wohnraum", "Zweiflügeliges Fenster mit integrierter Jalousie im Wohnraum", "Fenster mit integriertem Sonnenschutz"),
            shot("panoramafenster-rohbau", "Großes Schiebeelement im Rohbau", "Schiebeelement im Rohbau, kurz nach dem Einsetzen"),
            shot("fenster-holzdekor", "Fenster in Holzdekor in einer weißen Putzfassade", "Fenster in Holzdekor, Ansicht von außen"),
            shot("fenstertausch-rohbau", "Neu eingebaute Fenster mit noch offenen Laibungen", "Fenstertausch am Einfamilienhaus, vor dem Verputzen"),
            shot("wohnraum-boden-treppe", "Wohnraum mit Holztreppe und neu verlegtem Dielenboden", "Bodenbelag im Wohnraum, frisch verlegt"),
        ]),
        faq=faq_html,
        cta=cta_final("Lassen Sie uns messen – das kostet Sie nichts.",
                      "Ein Termin, ein Aufmaß, ein Angebot mit Festpreis. Danach entscheiden Sie in Ruhe."),
        lightbox=LIGHTBOX,
    ) + footer(("site.js", "tools.js"))
