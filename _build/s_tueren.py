# -*- coding: utf-8 -*-
from chrome import *
from s_fenster import ld, page_head

def build():
    return head(
      "Haustüren &amp; Innentüren | FB Montagebetrieb Bayerbach",
      "Haust\u00fcren, Wohnungseingangs-, Zimmer- und Terrassent\u00fcren f\u00fcr Bayerbach und das Rottal. "
      "Beratung, Aufma\u00df und Montage vom Fachbetrieb \u2013 auch im Altbau.",
      "tueren.html",
      ld("tueren.html", "Türmontage und Türenverkauf",
         "Haustüren, Innentüren und Terrassentüren von der Beratung über das Aufmaß bis zur Montage.",
         "Türen")
    ) + header("tueren.html") + """

{ph}

<section class="pad">
  <div class="wrap">
    <div class="split">
      <div data-reveal>
        <p class="eyebrow">Haustüren</p>
        <h2 class="h2">Der erste Eindruck – und die wichtigste Schwachstelle.</h2>
        <p class="lead">Eine Haustür muss drei Dinge gleichzeitig können: gut aussehen, Wärme halten und Einbrecher aufhalten. Beim Aufmaß schauen wir uns zuerst an, wie tief Ihre Laibung ist und wie die Schwelle liegt – daran scheitern die meisten Tauschprojekte.</p>
        <ul class="checklist">
          <li><b>Mehrfachverriegelung</b> mit Bolzen oder Haken, dazu ein massives Schließblech im Rahmen.</li>
          <li><b>Gedämmtes Türblatt</b> mit Schaumkern statt Wabenpappe – sonst hilft das beste Fenster nichts.</li>
          <li><b>Barrierearme Schwelle</b>, wenn Sie langfristig planen: flach, aber trotzdem schlagregendicht.</li>
          <li><b>Zutritt ohne Schlüssel</b> auf Wunsch – Fingerscanner, Code oder Funk, sauber verkabelt.</li>
        </ul>
        <div class="actions"><a class="btn btn-dark" href="kontakt.html?leistung=Haustür">Haustür anfragen</a></div>
      </div>
      <div class="split-media" data-reveal data-delay="1">{img1}</div>
    </div>
  </div>
</section>

<section class="paper-2 pad">
  <div class="wrap">
    <p class="eyebrow" data-reveal>Alle Türarten</p>
    <h2 class="h2" data-reveal>Was wir einbauen.</h2>
    <div class="cards" style="margin-top:38px">
      <article class="card" data-reveal>
        <span class="card-icon">{ic_door}</span>
        <h3 class="h4">Haustüren</h3>
        <p>Kunststoff, Aluminium oder Holz. Mit Seitenteil, Oberlicht und passender Füllung – farblich abgestimmt auf Ihre Fenster.</p>
      </article>
      <article class="card" data-reveal data-delay="1">
        <h3 class="h4">Wohnungseingangstüren</h3>
        <p>Mit erhöhtem Schall- und Brandschutz, wo die Hausordnung oder der Bauplan es verlangt.</p>
      </article>
      <article class="card" data-reveal data-delay="2">
        <h3 class="h4">Zimmertüren</h3>
        <p>Vom weißen Standardblatt bis zur Echtholzfurnier- oder Glastür. Auch der reine Blatttausch in vorhandene Zargen.</p>
      </article>
      <article class="card" data-reveal>
        <h3 class="h4">Schiebetüren</h3>
        <p>Vor der Wand laufend oder in der Wand verschwindend. Der Platzgewinn, wenn ein Raum eng ist.</p>
      </article>
      <article class="card" data-reveal data-delay="1">
        <h3 class="h4">Terrassen- und Balkontüren</h3>
        <p>Dreh-Kipp, Hebe-Schiebe oder Parallel-Schiebe-Kipp. Große Elemente montieren wir zu zweit mit Saugern.</p>
      </article>
      <article class="card" data-reveal data-delay="2">
        <h3 class="h4">Nebeneingang und Keller</h3>
        <p>Robuste Türen für Garage, Heizraum und Keller – unempfindlich, dicht und abschließbar.</p>
      </article>
    </div>
  </div>
</section>

<section class="dark pad">
  <div class="wrap">
    <div class="split flip">
      <div data-reveal>
        <p class="eyebrow on-dark">Terrassentüren</p>
        <h2 class="h2">Große Elemente sind Millimeterarbeit.</h2>
        <p class="lead">Je größer die Glasfläche, desto weniger verzeiht die Montage. Ein Hebe-Schiebe-Element wiegt schnell über 200 Kilogramm – der Untergrund muss tragen, die Schwelle muss in der Waage liegen, sonst läuft die Tür nach einem Jahr schwer.</p>
        <ul class="checklist">
          <li>Wir prüfen vor der Bestellung, ob Sturz und Schwelle die Last aufnehmen.</li>
          <li>Wir setzen auf tragende Konsolen statt auf Keile und Schaum.</li>
          <li>Wir richten die Laufschiene aus und fahren das Element gemeinsam mit Ihnen ab.</li>
        </ul>
      </div>
      <div class="split-media" data-reveal data-delay="1">{img2}</div>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap wrap-narrow">
    <p class="eyebrow center" data-reveal>Gut zu wissen</p>
    <h2 class="h2 center" data-reveal>Fragen, die vor der Bestellung kommen sollten.</h2>
    <div class="faq" data-reveal>
      <details open><summary>Passt eine neue Tür in meine alte Zarge?</summary><div class="answer">Bei Zimmertüren oft ja – dann tauschen wir nur das Blatt und die Bänder, das spart Zeit und Geld. Bei Haustüren fast nie: Dort gibt die Zarge die Dämmung und die Verriegelung vor, deshalb tauschen wir das komplette Element.</div></details>
      <details><summary>Welche Sicherheitsstufe brauche ich wirklich?</summary><div class="answer">Für Haustüren im Einfamilienhaus ist RC2 der sinnvolle Standard: Mehrfachverriegelung, Sicherheitsglas, massives Schließblech und ein Zylinder mit Ziehschutz. Alles darunter hält einem Schraubendreher kaum stand, alles darüber lohnt meist erst bei besonderen Lagen.</div></details>
      <details><summary>Wie lange dauert der Einbau einer Haustür?</summary><div class="answer">Der Einbau selbst ist an einem Tag erledigt. Ihr Haus ist dabei nie über Nacht offen – wir bauen aus und wieder ein, bevor wir Feierabend machen.</div></details>
      <details><summary>Kann ich Tür und Fenster farblich abstimmen?</summary><div class="answer">Ja, und das empfehlen wir. Wir arbeiten mit denselben RAL-Tönen und Dekoren, damit Tür, Fenster und Rollladen an der Fassade zusammenpassen. Beim gemeinsamen Aufmaß legen wir das in einem Termin fest.</div></details>
    </div>
  </div>
</section>

{cta}
""".format(
      ph=page_head("Türen", "Türen, die satt schließen – Jahr für Jahr.",
        "Haustüren, Wohnungseingangstüren, Zimmertüren und Terrassentüren. Wir beraten zu Material, Sicherheit "
        "und Farbe, messen auf und montieren – auch dann, wenn die Laibung nicht rechtwinklig ist.",
        [("index.html", "Start"), (None, "Türen")], "Türen"),
      img1=img("haustuer-weiss", "Weiße zweiflügelige Haustür mit Seitenteil in einer Fassade", w=1024, h=768),
      img2=img("terrassentuer-festverglasung", "Große Terrassentür mit Festverglasung von innen gesehen", w=1707, h=1280),
      ic_door=ICON["door"],
      cta=cta_final("Welche Tür passt zu Ihrem Haus?",
                    "Wir bringen Muster mit, messen auf und sagen Ihnen, was der Tausch bei Ihnen wirklich bedeutet.",
                    "Türen"),
    ) + footer()
