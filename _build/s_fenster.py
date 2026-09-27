# -*- coding: utf-8 -*-
from chrome import *
import json

def ld(slug, name, desc, crumb):
    return '<script type="application/ld+json">%s</script>' % json.dumps({
      "@context": "https://schema.org",
      "@graph": [
        {"@type": "Service", "name": name, "description": desc,
         "serviceType": name, "url": SITE + "/" + slug,
         "provider": {"@type": "LocalBusiness", "name": FIRMA, "telephone": "+49 177 5266889",
                      "address": {"@type": "PostalAddress", "streetAddress": STRASSE, "postalCode": PLZ,
                                  "addressLocality": ORT, "addressCountry": "DE"}},
         "areaServed": {"@type": "AdministrativeArea", "name": "Landkreis Rottal-Inn und Umgebung"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": SITE + "/" + slug}]}
      ]}, ensure_ascii=False)


def page_head(eyebrow, h1, lead, crumb_items, leistung=""):
    href = "kontakt.html" + ("?leistung=" + leistung if leistung else "")
    return """<section class="page-head">
  <div class="wrap">
    {cr}
    <div class="page-head-in">
      <p class="eyebrow on-dark" data-reveal>{e}</p>
      <h1 class="h1" data-reveal data-delay="1">{h}</h1>
      <p class="lead" data-reveal data-delay="2">{l}</p>
      <div class="actions" data-reveal data-delay="3">
        <a class="btn btn-amber" href="{href}">Kostenloses Aufmaß anfragen</a>
        <a class="btn btn-ghost" href="tel:{telh}">{phone}{telt}</a>
      </div>
    </div>
  </div>
</section>""".format(cr=crumbs(crumb_items), e=eyebrow, h=h1, l=lead, href=href,
                     telh=TEL_HREF, telt=TEL_TXT, phone=ICON["phone"])


def build():
    return head(
      "Fenster &amp; Fenstertausch | FB Montagebetrieb Bayerbach",
      "Fenster aus Kunststoff, Holz und Aluminium f\u00fcr Bayerbach und das Rottal: Dreifachglas, "
      "Schallschutz, RC2, Montage nach RAL und Entsorgung der Altfenster.",
      "fenster.html",
      ld("fenster.html", "Fenstermontage und Fenstertausch",
         "Lieferung und fachgerechte Montage von Kunststoff-, Holz- und Aluminiumfenstern inklusive "
         "Aufmaß, Demontage und Entsorgung der Altfenster.", "Fenster")
    ) + header("fenster.html") + """

{ph}

<section class="pad">
  <div class="wrap">
    <div class="split">
      <div data-reveal>
        <p class="eyebrow">Material</p>
        <h2 class="h2">Kunststoff, Holz oder Aluminium?</h2>
        <p class="lead">Es gibt kein bestes Material – nur ein passendes. Wir schauen uns Ihre Fassade, die Himmelsrichtung, das Budget und Ihre Pflegebereitschaft an und sagen Ihnen ehrlich, was wir einbauen würden.</p>
        <ul class="checklist">
          <li><b>Kunststoff</b> – das beste Verhältnis aus Preis, Dämmwert und Pflegeaufwand. In Weiß, in Farbe oder in Holzdekor.</li>
          <li><b>Holz</b> – warm, reparierbar, bauphysikalisch stark. Braucht alle paar Jahre einen Anstrich.</li>
          <li><b>Aluminium</b> – schmale Ansichten für große Glasflächen, sehr witterungsfest, ideal für Schiebeelemente.</li>
          <li><b>Holz-Alu</b> – innen Holz, außen wartungsfreie Schale. Die teuerste, aber langlebigste Lösung.</li>
        </ul>
      </div>
      <div class="split-media" data-reveal data-delay="1">{img1}</div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Verglasung</p>
    <h2 class="h2" data-reveal>Drei Zahlen entscheiden über Ihr Fenster.</h2>
    <p class="lead" data-reveal style="max-width:56ch">Wer sie kennt, kann Angebote wirklich vergleichen. Wir schreiben sie deshalb in jedes Angebot.</p>
    <div class="cards" style="margin-top:40px">
      <article class="card" data-reveal>
        <span class="card-icon">{ic_thermo}</span>
        <h3 class="h4">Uw-Wert: Wärmeverlust</h3>
        <p>Wie viel Wärme durch das ganze Fenster entweicht, Rahmen inklusive. Je kleiner, desto besser. Neubau heute: 0,8 bis 1,0. Ein Fenster von 1985 liegt oft bei 2,8 und mehr.</p>
      </article>
      <article class="card" data-reveal data-delay="1">
        <span class="card-icon">{ic_sound}</span>
        <h3 class="h4">Rw-Wert: Schalldämmung</h3>
        <p>Wie viele Dezibel das Fenster schluckt. Standard-Dreifachglas schafft rund 35 dB, Schallschutzklasse 4 rund 42 dB. Zehn Dezibel weniger empfinden wir als halb so laut.</p>
      </article>
      <article class="card" data-reveal data-delay="2">
        <span class="card-icon">{ic_shield}</span>
        <h3 class="h4">RC-Klasse: Einbruchhemmung</h3>
        <p>RC2 ist der sinnvolle Standard für Erdgeschoss und leicht erreichbare Fenster: Pilzkopfverriegelung, Sicherheitsglas, abschließbarer Griff. Hält einen Gelegenheitstäter auf.</p>
      </article>
    </div>
    <table class="table-spec" data-reveal>
      <caption class="sr-only">Typische Kennwerte verschiedener Fensteraufbauten</caption>
      <thead><tr><th scope="col">Aufbau</th><th scope="col">Uw ungefähr</th><th scope="col">Rw ungefähr</th><th scope="col">Passt wofür</th></tr></thead>
      <tbody>
        <tr><th scope="row">Zweifachglas, Standard</th><td>1,3 W/(m²K)</td><td>32–35 dB</td><td>Nebenräume, Garage, Budget</td></tr>
        <tr><th scope="row">Dreifachglas, Standard</th><td>0,9–1,0</td><td>34–36 dB</td><td>der heutige Regelfall im Wohnhaus</td></tr>
        <tr><th scope="row">Dreifachglas mit Schallschutz</th><td>0,9–1,0</td><td>40–45 dB</td><td>Schlafzimmer an der Straße, Bahnlinie</td></tr>
        <tr><th scope="row">Dreifachglas mit RC2</th><td>0,9–1,0</td><td>35–42 dB</td><td>Erdgeschoss, Terrassentüren</td></tr>
      </tbody>
    </table>
    <p class="disclaimer">Richtwerte für gängige Systeme. Die verbindlichen Kennwerte stehen im Datenblatt des jeweiligen Herstellers und in Ihrem Angebot.</p>
  </div>
</section>

<section class="dark pad">
  <div class="wrap">
    <div class="split">
      <div class="split-media" data-reveal>{img2}</div>
      <div data-reveal data-delay="1">
        <p class="eyebrow on-dark">Montage</p>
        <h2 class="h2">Das beste Fenster nützt nichts, wenn die Fuge undicht ist.</h2>
        <p class="lead">Die Hälfte der Wärmeverluste eines neuen Fensters entsteht nicht im Glas, sondern am Anschluss zur Wand. Wir bauen nach dem Prinzip der RAL-Montage ein.</p>
        <ul class="checklist">
          <li><b>Innen dichter als außen.</b> Innen luftdicht, außen schlagregendicht und diffusionsoffen – damit Feuchtigkeit nach draußen kann und nicht in die Fuge zieht.</li>
          <li><b>Gedämmte Mitte.</b> Die Fuge wird vollständig gedämmt, nicht nur mit Schaum zugeblasen.</li>
          <li><b>Tragende Befestigung.</b> Dübel und Konsolen nach Gewicht und Elementgröße, nicht nach Gefühl.</li>
          <li><b>Justiert übergeben.</b> Zum Schluss stellen wir Beschläge und Andruck ein und zeigen Ihnen, wie Sie später selbst nachstellen.</li>
        </ul>
        <div class="actions"><a class="link-arrow" href="index.html#anatomie">Den Aufbau im Schnitt ansehen</a></div>
      </div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Auch das gehört dazu</p>
    <h2 class="h2" data-reveal>Was wir rund ums Fenster mitmachen.</h2>
    <div class="cards" style="margin-top:38px">
      <article class="card" data-reveal><h3 class="h4">Demontage und Entsorgung</h3><p>Alte Elemente raus, abtransportiert, fachgerecht entsorgt. Als eigene Position im Angebot.</p></article>
      <article class="card" data-reveal data-delay="1"><h3 class="h4">Fensterbänke innen und außen</h3><p>Alu, Naturstein oder Kunststein – passend zur Laibung und mit sauberem Anschluss.</p></article>
      <article class="card" data-reveal data-delay="2"><h3 class="h4">Rollladen und Raffstore</h3><p>Aufsatz- oder Vorbaukasten, Gurt oder Motor. <a class="link-arrow" href="insektenschutz.html">Mehr dazu</a></p></article>
      <article class="card" data-reveal data-delay="3"><h3 class="h4">Laibung wiederherstellen</h3><p>Verputzen, Trockenbauanschluss, Anstrich – damit nach der Montage nichts offen bleibt.</p></article>
      <article class="card" data-reveal><h3 class="h4">Insektenschutz</h3><p>Maßgefertigt, direkt beim Aufmaß mitgemessen. Später nachrüsten kostet mehr.</p></article>
      <article class="card" data-reveal data-delay="1"><h3 class="h4">Einzelne Reparaturen</h3><p>Beschlag klemmt, Scheibe blind, Dichtung porös: oft reicht ein Termin statt eines neuen Fensters.</p></article>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <p class="eyebrow center" data-reveal>Fenster in Ihrer Nähe</p>
    <h2 class="h2 center" data-reveal>Wo wir montieren.</h2>
    <div class="prose" style="margin:26px auto 0" data-reveal>
      <p>Unsere Werkstatt steht in {ort} im Landkreis Rottal-Inn. Von hier aus fahren wir täglich in die Orte der Umgebung: <b>Bad Birnbach</b>, <b>Pfarrkirchen</b>, <b>Eggenfelden</b>, <b>Simbach am Inn</b>, <b>Rotthalmünster</b>, <b>Bad Griesbach</b>, <b>Tann</b>, <b>Triftern</b> und bis nach <b>Passau</b>. Weil wir nur zu zweit sind, planen wir Termine ehrlich: Wenn wir einen Auftrag nicht in Ihrem Zeitrahmen schaffen, sagen wir das am Telefon und nicht erst nach der Unterschrift.</p>
      <p>Sie sind außerhalb dieses Gebiets? Fragen Sie trotzdem an. Bei größeren Aufträgen fahren wir auch weiter.</p>
    </div>
  </div>
</section>

{cta}
""".format(
      ph=page_head("Fenster", "Fenster, die halten, was das Datenblatt verspricht.",
        "Kunststoff, Holz, Aluminium. Zweifach oder dreifach verglast, mit Schallschutz oder Einbruchhemmung. "
        "Wir messen auf, liefern, montieren nach RAL und nehmen die alten Fenster mit.",
        [("index.html", "Start"), (None, "Fenster")], "Fenster"),
      img1=img("fenster-kunststoff-fassade", "Weißes Kunststofffenster in einer verputzten Fassade", w=960, h=1280),
      img2=img("montage-hebebuehne", "Fenstermontage im Obergeschoss mit Hebebühne", w=960, h=1280),
      ic_thermo=ICON["thermo"], ic_sound=ICON["sound"], ic_shield=ICON["shield"], ort=ORT,
      cta=cta_final("Ihre Fenster, durchgerechnet und mit Festpreis.",
                    "Wir kommen vorbei, messen jedes Element einzeln auf und zeigen Ihnen zwei bis drei Varianten.",
                    "Fenster"),
    ) + footer()
