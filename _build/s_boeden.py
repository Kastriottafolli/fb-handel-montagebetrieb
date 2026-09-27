# -*- coding: utf-8 -*-
from chrome import *
from s_fenster import ld, page_head

def build():
    return head(
      "Bodenbeläge verlegen | FB Montagebetrieb Bayerbach",
      "Laminat, Parkett, Vinyl und Designbel\u00e4ge fachgerecht verlegt in Bayerbach und im Rottal \u2013 "
      "mit gepr\u00fcftem Untergrund, Trittschall und sauberen \u00dcberg\u00e4ngen.",
      "boeden.html",
      ld("boeden.html", "Bodenbeläge verlegen",
         "Verlegung von Laminat, Parkett, Vinyl und Designbelägen inklusive Untergrundvorbereitung.",
         "Bodenbeläge")
    ) + header("leistungen.html") + """

{ph}

<section class="pad">
  <div class="wrap">
    <div class="split">
      <div data-reveal>
        <p class="eyebrow">Untergrund</p>
        <h2 class="h2">Der Boden entscheidet sich unter dem Boden.</h2>
        <p class="lead">Ob ein Belag nach fünf Jahren noch schließt, liegt selten am Belag. Es liegt am Untergrund. Deshalb messen wir, bevor wir verlegen – und sagen es Ihnen, wenn erst etwas anderes passieren muss.</p>
        <ul class="checklist">
          <li><b>Restfeuchte messen.</b> Bei Estrich prüfen wir, ob er belegreif ist. Zu früh verlegt heißt: Schüsseln, Fugen, Schimmel.</li>
          <li><b>Ebenheit prüfen.</b> Ab einer gewissen Abweichung wird gespachtelt, sonst arbeitet die Klickverbindung sich auf.</li>
          <li><b>Trittschall einplanen.</b> Im Obergeschoss und in Mietwohnungen ist die Dämmunterlage kein Zubehör, sondern Pflicht.</li>
          <li><b>Randfuge einhalten.</b> Jeder Belag arbeitet. Wer bis an die Wand verlegt, bekommt Beulen.</li>
        </ul>
      </div>
      <div class="split-media" data-reveal data-delay="1">{img1}</div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Materialien</p>
    <h2 class="h2" data-reveal>Was wann passt.</h2>
    <table class="table-spec" data-reveal>
      <caption class="sr-only">Vergleich gängiger Bodenbeläge</caption>
      <thead><tr><th scope="col">Belag</th><th scope="col">Stärke</th><th scope="col">Achtung bei</th><th scope="col">Fußbodenheizung</th></tr></thead>
      <tbody>
        <tr><th scope="row">Laminat</th><td>günstig, robust, riesige Dekorauswahl</td><td>Nässe – im Bad ungeeignet</td><td>ja, mit passender Unterlage</td></tr>
        <tr><th scope="row">Parkett</th><td>echtes Holz, mehrfach abschleifbar</td><td>Kratzer, sehr trockene Raumluft</td><td>ja, bei geeigneter Holzart</td></tr>
        <tr><th scope="row">Vinyl / Designbelag</th><td>wasserfest, leise, fußwarm</td><td>weiche Untergründe, Punktlasten</td><td>ja, ideal</td></tr>
        <tr><th scope="row">Klick-Vinyl auf Träger</th><td>verlegefreundlich, gleicht viel aus</td><td>Bauhöhe an Türen</td><td>eingeschränkt</td></tr>
      </tbody>
    </table>
    <p class="disclaimer">Allgemeine Orientierung. Maßgeblich sind die Verlegehinweise des jeweiligen Herstellers, die wir vor dem Verlegen mit Ihnen durchgehen.</p>
  </div>
</section>

<section class="dark pad">
  <div class="wrap">
    <div class="split flip">
      <div data-reveal>
        <p class="eyebrow on-dark">Leistungsumfang</p>
        <h2 class="h2">Wir hören nicht am Belag auf.</h2>
        <ul class="checklist">
          <li>Alten Belag aufnehmen und entsorgen</li>
          <li>Untergrund reinigen, grundieren, bei Bedarf spachteln</li>
          <li>Trittschall- oder Dampfsperrunterlage einbauen</li>
          <li>Belag verlegen, auf Wunsch im Fischgrät- oder Schiffsbodenmuster</li>
          <li>Sockelleisten, Übergangsschienen und Anschlüsse an Türzargen</li>
          <li>Türblätter kürzen, wenn die neue Aufbauhöhe es nötig macht</li>
        </ul>
        <div class="actions"><a class="btn btn-amber" href="kontakt.html?leistung=Bodenbelag">Boden anfragen</a></div>
      </div>
      <div class="split-media" data-reveal data-delay="1">{img2}</div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap wrap-narrow prose" data-reveal>
    <h2 class="h2">Boden und Fenster in einem Zug</h2>
    <p>Wenn ohnehin gearbeitet wird, ist der Boden der richtige Moment. Beim Fenstertausch wird die Laibung geöffnet, danach muss oft der Anschluss zum Boden neu gemacht werden. Wer beides nacheinander von zwei Betrieben machen lässt, zahlt zweimal An- und Abfahrt und hat zweimal Staub in der Wohnung.</p>
    <p>Wir planen das deshalb zusammen: erst Fenster und Türen, dann Laibung und Anschluss, dann der Boden. Ein Ansprechpartner, eine Terminkette, ein Angebot. Das ist der Vorteil, wenn ein Betrieb beides kann – und der Grund, warum wir beide Bereiche anbieten.</p>
    <p><a class="link-arrow" href="leistungen.html">Alle Leistungen im Überblick</a></p>
  </div>
</section>

{cta}
""".format(
      ph=page_head("Bodenbeläge", "Böden, die auch in zehn Jahren noch schließen.",
        "Laminat, Parkett, Vinyl und Designbeläge – fachgerecht verlegt, mit geprüftem Untergrund, "
        "Trittschall, sauberen Sockelleisten und passenden Übergängen.",
        [("index.html", "Start"), ("leistungen.html", "Leistungen"), (None, "Bodenbeläge")], "Bodenbelag"),
      img1=img("bodenaufbau-randdaemmung", "Bodenaufbau mit Randdämmstreifen vor dem Verlegen", w=719, h=676),
      img2=img("wohnraum-boden-treppe", "Wohnraum mit Holztreppe und neu verlegtem Dielenboden", w=1280, h=720),
      cta=cta_final("Welcher Boden passt in Ihre Räume?",
                    "Wir schauen uns den Untergrund an, bringen Muster mit und rechnen den Quadratmeterpreis "
                    "inklusive aller Nebenarbeiten aus.", "Bodenbelag"),
    ) + footer()
