# -*- coding: utf-8 -*-
from chrome import *
from s_fenster import ld, page_head
import json


def leistungen():
    return head(
      "Leistungen im Überblick | FB Montagebetrieb Bayerbach",
      "Fenstertausch, Haustüren, Innentüren, Bodenbeläge, Insektenschutz, Rollläden und "
      "Renovierung – alle Leistungen für Bayerbach und den Landkreis Rottal-Inn.",
      "leistungen.html",
      '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Start", "item": SITE + "/"},
          {"@type": "ListItem", "position": 2, "name": "Leistungen", "item": SITE + "/leistungen.html"}]},
        ensure_ascii=False)
    ) + header("leistungen.html") + """

{ph}

<section class="pad">
  <div class="wrap">
    <div class="bento">
      <article class="tile photo tile-span-4 tile-tall" data-reveal>
        {i1}
        <span class="tile-icon">{ic_win}</span>
        <h2 class="h3">Fenster</h2>
        <p>Kunststoff, Holz und Aluminium. Zweifach- oder Dreifachverglasung, Schallschutz bis Klasse 5, Einbruchhemmung RC2. Inklusive Demontage, Entsorgung und Anschluss nach RAL.</p>
        <a class="link-arrow tile-link" href="fenster.html">Zu den Fenstern</a>
      </article>
      <article class="tile photo tile-span-2 tile-tall" data-reveal data-delay="1">
        {i2}
        <span class="tile-icon">{ic_door}</span>
        <h2 class="h3">Türen</h2>
        <p>Haustüren, Wohnungseingangs-, Zimmer- und Terrassentüren.</p>
        <a class="link-arrow tile-link" href="tueren.html">Zu den Türen</a>
      </article>
      <article class="tile tile-span-3" data-reveal>
        <span class="tile-icon">{ic_floor}</span>
        <h2 class="h3">Bodenbeläge</h2>
        <p>Laminat, Parkett, Vinyl und Designbeläge – mit geprüftem Untergrund, Trittschall und sauberen Übergängen.</p>
        <a class="link-arrow tile-link" href="boeden.html">Zu den Böden</a>
      </article>
      <article class="tile tile-span-3" data-reveal data-delay="1">
        <span class="tile-icon">{ic_bug}</span>
        <h2 class="h3">Insektenschutz &amp; Rollläden</h2>
        <p>Maßgefertigte Gitter und Türen, dazu Rollläden, Raffstore und textiler Sonnenschutz.</p>
        <a class="link-arrow tile-link" href="insektenschutz.html">Zum Schutz</a>
      </article>
    </div>
  </div>
</section>

<section class="paper-2 pad" id="renovierung">
  <div class="wrap">
    <div class="split">
      <div data-reveal>
        <p class="eyebrow">Renovierung</p>
        <h2 class="h2">Das, was nach dem Fenster kommt.</h2>
        <p class="lead">Beim Tausch wird die Laibung geöffnet. Danach muss verputzt, angeschlossen, gestrichen werden – sonst bleibt die Baustelle sichtbar. Wir übernehmen diese Arbeiten mit, statt Sie an den nächsten Betrieb weiterzureichen.</p>
        <ul class="checklist">
          <li>Laibungen verputzen, spachteln und streichen</li>
          <li>Trockenbauanschlüsse und abgehängte Anschlüsse am Rollladenkasten</li>
          <li>Fensterbänke innen und außen setzen</li>
          <li>Kleine Umbauten: Durchbruch anpassen, Öffnung verkleinern oder vergrößern</li>
          <li>Demontage, Abtransport und Entsorgung des Altmaterials</li>
        </ul>
        <div class="actions"><a class="btn btn-dark" href="kontakt.html?leistung=Renovierung">Renovierung anfragen</a></div>
      </div>
      <div class="split-media" data-reveal data-delay="1">{i3}</div>
    </div>
  </div>
</section>

<section class="dark pad">
  <div class="wrap">
    <p class="eyebrow on-dark" data-reveal>Handel</p>
    <h2 class="h2" data-reveal>Nur Material? Auch das geht.</h2>
    <p class="lead" data-reveal style="max-width:56ch">Als Handels- und Montagebetrieb liefern wir Fenster, Türen und Zubehör auch ohne Montage – zum Beispiel, wenn Sie selbst einbauen oder Ihr eigener Handwerker das übernimmt.</p>
    <div class="cards" style="margin-top:38px">
      <article class="card" data-reveal><h3 class="h4">Aufmaß durch Sie</h3><p>Sie liefern die Maße, wir bestellen. Wichtig: Bei Eigenaufmaß tragen Sie das Maßrisiko – wir sagen Ihnen vorher genau, wie gemessen wird.</p></article>
      <article class="card" data-reveal data-delay="1"><h3 class="h4">Aufmaß durch uns</h3><p>Wir messen vor Ort, Sie bauen selbst ein. So stimmt das Maß und Sie sparen die Montagekosten.</p></article>
      <article class="card" data-reveal data-delay="2"><h3 class="h4">Zubehör und Ersatzteile</h3><p>Beschläge, Griffe, Dichtungen, Fensterbänke, Insektenschutzrahmen – auch einzeln.</p></article>
    </div>
  </div>
</section>

{cta}
""".format(
      ph=page_head("Leistungen", "Alles rund um die Öffnungen im Haus.",
        "Fenster, Türen, Böden, Insektenschutz, Rollläden und die Renovierungsarbeiten drumherum – "
        "aus einer Hand, für Bayerbach und den Landkreis Rottal-Inn.",
        [("index.html", "Start"), (None, "Leistungen")]),
      i1=img("grossfenster-abend", "Großes Fenster mit grauem Rahmen in der Abenddämmerung", sizes="(max-width: 900px) 100vw, 66vw", w=1024, h=768),
      i2=img("neubau-haustuer", "Haustür und Fensterelemente an einem Neubau", sizes="(max-width: 900px) 100vw, 34vw", w=1024, h=768),
      i3=img("fenstertausch-rohbau", "Neu eingebaute Fenster mit noch offenen Laibungen", w=1707, h=1280),
      ic_win=ICON["window"], ic_door=ICON["door"], ic_floor=ICON["floor"], ic_bug=ICON["bug"],
      cta=cta_final("Sagen Sie uns, was ansteht.",
                    "Ein Anruf genügt, damit wir einschätzen können, was Ihr Vorhaben bedeutet – "
                    "und ob wir es in Ihrem Zeitrahmen schaffen."),
    ) + footer()


GALERIE = [
  ("fenster-anthrazit-innen", "Anthrazitfarbenes Fenster von innen mit Blick in den Garten",
   "Zweiflügeliges Fenster in Anthrazit, Ansicht von innen", False),
  ("grossfenster-abend", "Großes Fensterelement mit grauem Rahmen in der Abenddämmerung",
   "Großes Fensterelement mit grauem Rahmen", False),
  ("terrassentuer-festverglasung", "Terrassentür mit großer Festverglasung von innen",
   "Terrassentür mit Festverglasung", False),
  ("fenster-jalousie-wohnraum", "Fenster mit integrierter Jalousie im Wohnraum",
   "Fenster mit integriertem Sonnenschutz im Wohnraum", False),
  ("panoramafenster-rohbau", "Großes Schiebeelement im Rohbau kurz nach dem Einsetzen",
   "Schiebeelement im Rohbau, direkt nach der Montage", False),
  ("fenster-holzdekor", "Fenster in Holzdekor in einer weißen Putzfassade",
   "Fenster in Holzdekor, Ansicht von außen", False),
  ("fenster-kunststoff-fassade", "Weißes Kunststofffenster in einer hellen Putzfassade",
   "Kunststofffenster in heller Putzfassade", True),
  ("terrassentuer-garten", "Schmale Terrassentür mit Blick auf die Terrasse",
   "Terrassentür mit direktem Gartenzugang", True),
  ("haustuer-weiss", "Weiße zweiflügelige Haustür mit Seitenteil",
   "Zweiflügelige Haustür mit Seitenteil", False),
  ("neubau-haustuer", "Haustür und Fensterelemente an einem Neubau",
   "Haustür und Fensterelemente am Neubau", False),
  ("fenstertausch-rohbau", "Neu eingebaute Fenster mit noch offenen Laibungen",
   "Fenstertausch am Einfamilienhaus, vor dem Verputzen", False),
  ("montage-hebebuehne", "Fenstermontage im Obergeschoss mit einer Hebebühne",
   "Montage im Obergeschoss mit Hebebühne", True),
  ("neubau-mehrfamilienhaus", "Neubau eines Mehrfamilienhauses mit Transporter davor",
   "Fenster und Türen für ein Mehrfamilienhaus", False),
  ("altfenster-ausbau", "Ausgebaute alte Fensterelemente auf einer Baustelle",
   "Ausgebaute Altfenster – Abtransport und Entsorgung gehören dazu", False),
  ("sonnenschutz-halle", "Textiler Sonnenschutz an einer Gewerbehalle",
   "Textiler Sonnenschutz an einer Gewerbehalle", False),
  ("terrasse-rollladen", "Überdachte Terrasse mit Fenster und Rollladen",
   "Terrassenseite mit Fenster und Rollladen", False),
  ("wohnraum-boden-treppe", "Wohnraum mit Holztreppe und neu verlegtem Dielenboden",
   "Neu verlegter Boden im Wohnraum", False),
  ("bodenaufbau-randdaemmung", "Bodenaufbau mit Randdämmstreifen vor dem Verlegen",
   "Bodenaufbau mit Randdämmstreifen", False),
  ("vorher-altfenster", "Fenster mit rotem Rahmen während der Montage",
   "Fenster mit rotem Rahmen, während der Montage", True),
  ("nachher-neufenster", "Dasselbe Fenster mit neuem Vorbaurollladen in passendem Rot",
   "Dasselbe Fenster mit neuem Vorbaurollladen", True),
  ("fuhrpark", "Zwei Transporter des Betriebs nebeneinander",
   "Unterwegs im Rottal: unsere beiden Fahrzeuge", False),
]


def projekte():
    gal = "".join(shot(s, a, c, t) for s, a, c, t in GALERIE)
    return head(
      "Projekte &amp; Referenzen | FB Montagebetrieb Bayerbach",
      "Ausgeführte Arbeiten aus Bayerbach: Fenstertausch im Altbau, Fenster und Türen im Neubau, "
      "Terrassentüren, Sonnenschutz und Böden im Rottal.",
      "projekte.html",
      '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Start", "item": SITE + "/"},
          {"@type": "ListItem", "position": 2, "name": "Projekte", "item": SITE + "/projekte.html"}]},
        ensure_ascii=False)
    ) + header("projekte.html") + """

{ph}

<section class="pad-s">
  <div class="wrap">
    <div class="split">
      <div data-reveal>
        <p class="eyebrow">Vorher und nachher</p>
        <h2 class="h2">Glasbausteine raus, Tageslicht rein.</h2>
        <p class="lead">Über dem Hauseingang saßen Glasbausteine aus den Siebzigern. Heute steht dort ein schlankes, dreiteiliges Fensterelement in Anthrazit – mit sauberem Anschluss und neuer Laibung.</p>
      </div>
      <div class="ba" data-reveal data-delay="1" style="--pos:50%">
        <img src="assets/img/ba-vorher-glasbausteine-800.webp" alt="Fassade mit Glasbausteinen über dem Eingang vor dem Umbau" loading="lazy" decoding="async" width="537" height="430">
        <img class="after" src="assets/img/ba-nachher-fensterelement-800.webp" alt="Dieselbe Fassade mit neuem Fensterelement in Anthrazit" loading="lazy" decoding="async" width="537" height="430">
        <span class="ba-tag l">Vorher</span><span class="ba-tag r">Nachher</span>
        <span class="ba-handle" aria-hidden="true"><span class="ba-knob">{drag}</span></span>
        <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Vergleich vorher und nachher verschieben">
      </div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Galerie</p>
    <h2 class="h2" data-reveal>Ausgeführte Arbeiten.</h2>
    <p class="lead" data-reveal style="max-width:56ch">Fotos aus abgeschlossenen Aufträgen. Zum Vergrößern anklicken.</p>
    <div class="gallery" style="margin-top:38px" data-reveal>{gal}</div>
    <p class="disclaimer">Alle Bilder stammen aus eigenen Aufträgen. Aus Rücksicht auf unsere Kundinnen und Kunden nennen wir keine Adressen und keine Namen.</p>
  </div>
</section>

{cta}
{lb}
""".format(
      ph=page_head("Projekte", "Was wir gebaut haben, in Bildern.",
        "Fenstertausch im Bestand, komplette Ausstattung im Neubau, Terrassentüren, Sonnenschutz und "
        "Bodenbeläge – Arbeiten aus Bayerbach und dem Landkreis Rottal-Inn.",
        [("index.html", "Start"), (None, "Projekte")]),
      drag=ICON["drag"], gal=gal, lb=LIGHTBOX,
      cta=cta_final("Soll Ihr Haus das nächste sein?",
                    "Erzählen Sie uns kurz, was ansteht. Wir kommen zum Aufmaß und rechnen es durch."),
    ) + footer()


def ueber_uns():
    return head(
      "Über uns | FB Montagebetrieb Bayerbach",
      "Zwei Handwerker aus Bayerbach, seit 2022: Fenster, Türen, Böden und Insektenschutz – "
      "mit Schreinerhintergrund, kurzen Wegen und festem Ansprechpartner.",
      "ueber-uns.html",
      '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "Start", "item": SITE + "/"},
          {"@type": "ListItem", "position": 2, "name": "Über uns", "item": SITE + "/ueber-uns.html"}]},
        ensure_ascii=False)
    ) + header("ueber-uns.html") + """

{ph}

<section class="pad">
  <div class="wrap">
    <div class="split">
      <div class="prose" data-reveal>
        <p class="eyebrow">Der Betrieb</p>
        <h2 class="h2">Klein genug, um ans Telefon zu gehen.</h2>
        <p>{firma} arbeitet seit 2022 in Bayerbach und Umgebung. Wir sind zu zweit – und das ist Absicht. Sie sprechen mit derselben Person, die zum Aufmaß kommt, die das Angebot schreibt und die später auf der Leiter steht. Es gibt keine Abteilung, die den Termin verschiebt, und keinen Außendienst, der etwas verkauft, was die Montage nachher nicht halten kann.</p>
        <p>Unser Hintergrund ist das Schreinerhandwerk. Das merkt man an den Stellen, an denen es nicht nach Katalog geht: bei einer Laibung, die nicht rechtwinklig ist, bei einem Altbausturz, der nachgibt, bei einer Zarge, die nicht mehr im Lot steht. Wir arbeiten mit regionalen Partnern und Herstellern zusammen, damit Ersatzteile auch in zehn Jahren noch lieferbar sind.</p>
        <p>Weil wir klein sind, sagen wir auch ehrlich Nein. Wenn ein Auftrag in Ihrem Zeitrahmen nicht zu schaffen ist, hören Sie das am Telefon – nicht erst, wenn die Anzahlung geflossen ist.</p>
      </div>
      <div class="split-media" data-reveal data-delay="1">{img1}</div>
    </div>
  </div>
</section>

<section class="dark pad">
  <div class="wrap">
    <p class="eyebrow on-dark" data-reveal>Wie wir arbeiten</p>
    <h2 class="h2" data-reveal>Vier Sätze, an denen Sie uns messen können.</h2>
    <div class="cards" style="margin-top:40px">
      <article class="card" data-reveal><h3 class="h4">Wir messen, bevor wir reden.</h3><p>Kein Angebot ohne Aufmaß vor Ort. Alles andere ist geraten – und wird auf der Baustelle teuer.</p></article>
      <article class="card" data-reveal data-delay="1"><h3 class="h4">Jede Position steht einzeln.</h3><p>Element, Montage, Entsorgung, Anschluss. Sie sehen, wofür Sie zahlen, und können Positionen streichen.</p></article>
      <article class="card" data-reveal data-delay="2"><h3 class="h4">Abends ist das Haus dicht.</h3><p>Wir öffnen nur so viel, wie wir am selben Tag wieder schließen können. Boden und Möbel werden abgedeckt.</p></article>
      <article class="card" data-reveal data-delay="3"><h3 class="h4">Wir gehen gemeinsam durch.</h3><p>Zum Schluss stellen wir jeden Flügel ein und zeigen Ihnen, wie Sie später selbst nachjustieren.</p></article>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="split flip">
      <div data-reveal>
        <p class="eyebrow">Einsatzgebiet</p>
        <h2 class="h2">Von Bayerbach aus, im Umkreis von rund 50 Kilometern.</h2>
        <p class="lead">Kurze Wege sind kein Marketing, sondern der Grund dafür, dass wir bei einem klemmenden Beschlag noch einmal vorbeikommen können, ohne dafür einen halben Tag zu berechnen.</p>
        <ul class="checklist">
          <li>Bayerbach, Bad Birnbach, Rotthalmünster, Bad Griesbach</li>
          <li>Pfarrkirchen, Triftern, Tann, Simbach am Inn</li>
          <li>Eggenfelden, Arnstorf, Massing</li>
          <li>Passau und Umgebung</li>
        </ul>
      </div>
      <div class="split-media" data-reveal data-delay="1">{img2}</div>
    </div>
  </div>
</section>

{cta}
""".format(
      ph=page_head("Über uns", "Zwei Handwerker, ein Ansprechpartner.",
        "Seit 2022 in Bayerbach: Fenster, Türen, Böden und Insektenschutz – mit Schreinerhintergrund, "
        "kurzen Wegen und Terminen, die halten.",
        [("index.html", "Start"), (None, "Über uns")]),
      firma=FIRMA,
      img1=img("fuhrpark", "Zwei Transporter des Betriebs nebeneinander geparkt", w=1024, h=683),
      img2=img("neubau-mehrfamilienhaus", "Neubau eines Mehrfamilienhauses mit Transporter davor", w=1707, h=1280),
      cta=cta_final("Reden wir über Ihr Vorhaben.",
                    "Rufen Sie an oder schreiben Sie kurz, worum es geht – wir melden uns zeitnah zurück."),
    ) + footer()
