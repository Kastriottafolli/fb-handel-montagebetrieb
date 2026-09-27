# -*- coding: utf-8 -*-
from chrome import *
from s_fenster import ld, page_head

def build():
    return head(
      "Insektenschutz &amp; Rollläden | FB Montagebetrieb Bayerbach",
      "Ma\u00dfgefertigte Fliegengitter, Insektenschutzt\u00fcren, Pliss\u00e9es, Rolll\u00e4den und Sonnenschutz "
      "f\u00fcr Bayerbach und das Rottal. Aufma\u00df vor Ort, saubere Montage.",
      "insektenschutz.html",
      ld("insektenschutz.html", "Insektenschutz, Rollläden und Sonnenschutz",
         "Maßgefertigter Insektenschutz sowie Rollläden und textiler Sonnenschutz inklusive Montage.",
         "Insektenschutz")
    ) + header("leistungen.html") + """

{ph}

<section class="pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Insektenschutz</p>
    <h2 class="h2" data-reveal>Maßgefertigt statt zurechtgeschnitten.</h2>
    <p class="lead" data-reveal style="max-width:56ch">Zugeschnittene Gitter aus dem Baumarkt halten eine Saison. Ein maßgefertigter Rahmen sitzt spannungsfrei im Falz, lässt sich im Winter abnehmen und hält Jahre.</p>
    <div class="cards" style="margin-top:38px">
      <article class="card" data-reveal>
        <span class="card-icon">{ic_bug}</span>
        <h3 class="h4">Spannrahmen für Fenster</h3>
        <p>Der Klassiker. Wird von außen eingehängt, meist ohne Bohren in den Rahmen, und ist in zwei Handgriffen abgenommen.</p>
      </article>
      <article class="card" data-reveal data-delay="1">
        <h3 class="h4">Drehrahmen-Türen</h3>
        <p>Für Terrassen- und Balkontüren, die oft benutzt werden. Mit Magnetverschluss und Bürstendichtung unten.</p>
      </article>
      <article class="card" data-reveal data-delay="2">
        <h3 class="h4">Plissée und Schiebeanlagen</h3>
        <p>Wenn die Tür breit ist oder kein Platz für einen Drehflügel bleibt. Läuft in einer flachen Bodenschiene.</p>
      </article>
      <article class="card" data-reveal>
        <h3 class="h4">Rollos für Dachfenster</h3>
        <p>Selbstaufrollend, mit Seitenführung – auch für schräge Einbausituationen.</p>
      </article>
      <article class="card" data-reveal data-delay="1">
        <h3 class="h4">Pollenschutzgewebe</h3>
        <p>Feineres Gewebe für Allergiker. Etwas weniger Luftdurchlass, dafür spürbar weniger Pollen im Raum.</p>
      </article>
      <article class="card" data-reveal data-delay="2">
        <h3 class="h4">Lichtschacht-Abdeckungen</h3>
        <p>Gegen Laub, Schnecken und Insekten im Kellerschacht. Begehbar oder zum Abnehmen.</p>
      </article>
    </div>
  </div>
</section>

<section class="dark pad">
  <div class="wrap">
    <div class="split">
      <div class="split-media" data-reveal>{img1}</div>
      <div data-reveal data-delay="1">
        <p class="eyebrow on-dark">Rollläden und Sonnenschutz</p>
        <h2 class="h2">Kühl bleiben, bevor die Wärme im Raum ist.</h2>
        <p class="lead">Innenliegende Vorhänge bremsen Sonne erst, wenn sie schon durch das Glas ist. Außenliegender Schutz hält sie davor ab – das ist der ganze Unterschied zwischen einem warmen und einem heißen Zimmer.</p>
        <ul class="checklist">
          <li><b>Aufsatzrollladen</b> – wird beim Fenstertausch gleich mitgeliefert und verschwindet in der Laibung.</li>
          <li><b>Vorbaurollladen</b> – die Lösung zum Nachrüsten, ohne das Fenster anzufassen.</li>
          <li><b>Raffstore</b> – Lamellen zum Drehen: Licht rein, Hitze draußen, Sichtschutz trotzdem.</li>
          <li><b>Textiler Sonnenschutz</b> – für große Glasflächen an Wohnhaus und Gewerbehalle.</li>
          <li><b>Motor und Zeitschaltung</b> – nachrüstbar, auch bei vorhandenen Gürteln.</li>
        </ul>
        <div class="actions"><a class="btn btn-amber" href="kontakt.html?leistung=Rollladen%20und%20Sonnenschutz">Sonnenschutz anfragen</a></div>
      </div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <div class="split">
      <div class="split-media portrait" data-reveal>{img2}</div>
      <div data-reveal data-delay="1">
        <p class="eyebrow">Nachger\u00fcstet</p>
        <h2 class="h2">Vorbaurollladen, farblich passend zum Rahmen.</h2>
        <p class="lead">Hier kam der Rollladen erst nach dem Fenster dazu \u2013 als Vorbaukasten in demselben Rotton wie der Rahmen. Von au\u00dfen wirkt es wie aus einem Guss, ohne dass das Fenster noch einmal angefasst werden musste.</p>
      </div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap wrap-narrow prose" data-reveal>
    <h2 class="h2">Am besten gleich beim Fenstertausch mitmessen</h2>
    <p>Insektenschutz und Rollladen kosten deutlich weniger, wenn sie beim Fensteraufmaß mit erfasst werden. Der Aufsatzkasten lässt sich dann direkt in das neue Element integrieren, Führungsschienen werden vor dem Verputzen gesetzt und der Insektenschutzrahmen wird auf den neuen Falz gefertigt. Wer erst zwei Jahre später nachrüstet, zahlt Vorbaulösungen, zusätzliche Anfahrt und bohrt in einen Rahmen, der eigentlich dicht sein sollte.</p>
    <p>Sagen Sie uns beim Termin einfach, dass Sie beides überlegen – wir nehmen die Maße dann in einem Durchgang mit auf, unverbindlich.</p>
    <p><a class="link-arrow" href="fenster.html">Zu den Fenstern</a></p>
  </div>
</section>

{cta}
""".format(
      ph=page_head("Insektenschutz &amp; Rollläden", "Draußen bleibt draußen: Insekten, Hitze, Blicke.",
        "Maßgefertigte Fliegengitter und Insektenschutztüren, dazu Rollläden, Raffstore und textiler "
        "Sonnenschutz – aufgemessen vor Ort und sauber montiert.",
        [("index.html", "Start"), ("leistungen.html", "Leistungen"), (None, "Insektenschutz")],
        "Insektenschutz"),
      img2=img("nachher-neufenster", "Fenster mit neuem roten Vorbaurollladen von au\u00dfen", w=768, h=1024),
      img1=img("sonnenschutz-halle", "Großflächiger textiler Sonnenschutz an einer Gewerbehalle", w=1707, h=1280),
      ic_bug=ICON["bug"],
      cta=cta_final("Ein Termin, alle Maße.",
                    "Wir messen Fenster, Insektenschutz und Rollladen in einem Durchgang – und Sie bekommen "
                    "ein Angebot statt drei.", "Insektenschutz"),
    ) + footer()
