# -*- coding: utf-8 -*-
from chrome import *
from s_fenster import page_head
import json


def kontakt():
    return head(
      "Kontakt &amp; kostenloses Aufmaß | FB Montagebetrieb Bayerbach",
      "Kontakt zu " + FIRMA + " in Bayerbach: Telefon " + TEL_TXT + ", " + MAIL +
      ". Kostenloses Aufmaß für Fenster, Türen und Böden.",
      "kontakt.html",
      '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "ContactPage",
        "name": "Kontakt", "url": SITE + "/kontakt.html",
        "mainEntity": {"@type": "LocalBusiness", "name": FIRMA, "telephone": "+49 177 5266889",
                       "email": MAIL,
                       "address": {"@type": "PostalAddress", "streetAddress": STRASSE, "postalCode": PLZ,
                                   "addressLocality": ORT, "addressCountry": "DE"}}},
        ensure_ascii=False)
    ) + header("kontakt.html") + """

{ph}

<section class="pad">
  <div class="wrap">
    <div class="contact-grid">
      <div data-reveal>
        <h2 class="h3">Anfrage senden</h2>
        <p class="muted" style="margin-top:8px">Je mehr Sie schreiben, desto genauer können wir antworten. Pflichtfelder sind mit * markiert.</p>

        <div class="note" id="form-prefill" hidden style="margin:20px 0">
          <b>Übernommen aus dem Rechner</b>
          Ihre Angaben stehen bereits im Formular. Ändern Sie sie gern noch.
        </div>

        <form id="anfrage-form" data-mail="{mail}" novalidate style="margin-top:22px">
          <div class="field">
            <label for="f-name">Name *</label>
            <input type="text" id="f-name" name="name" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="f-email">E-Mail *</label>
            <input type="email" id="f-email" name="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="f-tel">Telefon</label>
            <input type="tel" id="f-tel" name="telefon" autocomplete="tel">
            <p class="hint">Am schnellsten geht es, wenn wir kurz zurückrufen dürfen.</p>
          </div>
          <div class="field">
            <label for="f-ort">Ort und Postleitzahl</label>
            <input type="text" id="f-ort" name="ort" autocomplete="postal-code" placeholder="z. B. 94137 Bayerbach">
          </div>
          <div class="field">
            <label for="f-leistung">Worum geht es? *</label>
            <select id="f-leistung" name="leistung" required>
              <option value="Fenster">Fenster</option>
              <option value="Türen">Türen</option>
              <option value="Haustür">Haustür</option>
              <option value="Bodenbelag">Bodenbelag</option>
              <option value="Insektenschutz">Insektenschutz</option>
              <option value="Rollladen und Sonnenschutz">Rollladen und Sonnenschutz</option>
              <option value="Renovierung">Renovierung</option>
              <option value="Schallschutzfenster">Schallschutzfenster</option>
              <option value="Fenstertausch">Fenstertausch</option>
              <option value="Etwas anderes">Etwas anderes</option>
            </select>
          </div>
          <div class="field">
            <label for="f-zeit">Wann soll es passieren?</label>
            <select id="f-zeit" name="zeitraum">
              <option value="So bald wie möglich">So bald wie möglich</option>
              <option value="In den nächsten Monaten">In den nächsten Monaten</option>
              <option value="Ich plane erst">Ich plane erst</option>
            </select>
          </div>
          <div class="field">
            <label for="f-nachricht">Ihre Nachricht *</label>
            <textarea id="f-nachricht" name="nachricht" required placeholder="Wie viele Elemente? Alt- oder Neubau? Erdgeschoss oder Obergeschoss? Gibt es Besonderheiten?"></textarea>
          </div>
          <label class="consent">
            <input type="checkbox" name="einwilligung" required>
            <span>Ich bin damit einverstanden, dass meine Angaben zur Bearbeitung der Anfrage verwendet werden. Hinweise dazu stehen in der <a href="datenschutz.html">Datenschutzerklärung</a>. *</span>
          </label>
          <div class="actions">
            <button class="btn btn-amber" type="submit">Anfrage abschicken</button>
            <a class="btn btn-line" href="tel:{telh}">Lieber anrufen</a>
          </div>
          <p class="form-note">Das Formular öffnet Ihr E-Mail-Programm mit einer fertig ausgefüllten Nachricht an {mail}. Es wird nichts automatisch an uns übertragen und nichts auf dieser Seite gespeichert. Sie sehen die Nachricht, bevor Sie sie abschicken.</p>
          <p class="note" id="form-ok" hidden tabindex="-1" style="margin-top:18px"><b>Fast geschafft</b>Ihr E-Mail-Programm sollte sich jetzt geöffnet haben. Bitte die Nachricht dort noch abschicken. Wenn sich nichts öffnet, schreiben Sie uns direkt an <a href="mailto:{mail}">{mail}</a>.</p>
        </form>
      </div>

      <aside data-reveal data-delay="1">
        <h2 class="h3">Direkt erreichbar</h2>
        <ul class="info-list" style="margin-top:16px">
          <li>{ic_phone}<div><b>Telefon</b><a href="tel:{telh}">{telt}</a></div></li>
          <li>{ic_mail}<div><b>E-Mail</b><a href="mailto:{mail}">{mail}</a></div></li>
          <li>{ic_pin}<div><b>Adresse</b>{firma}<br>{strasse}<br>{plz} {ort}</div></li>
          <li>{ic_clock}<div><b>Erreichbarkeit</b>Mo–Do 07:00–17:00 Uhr<br>Fr 07:00–14:00 Uhr</div></li>
        </ul>

        <h3 class="h4" style="margin-top:34px">Öffnungszeiten</h3>
        <ul class="hours">
          <li><span>Montag bis Donnerstag</span><b>07:00–17:00</b></li>
          <li><span>Freitag</span><b>07:00–14:00</b></li>
          <li class="closed"><span>Samstag und Sonntag</span><b>geschlossen</b></li>
        </ul>

        <div class="note" style="margin-top:28px">
          <b>Sind wir auf der Baustelle?</b>
          Dann geht manchmal niemand ans Telefon. Sprechen Sie einfach auf die Mailbox oder schreiben Sie eine E-Mail – wir melden uns zurück.
        </div>

        <h3 class="h4" style="margin-top:34px">Einsatzgebiet</h3>
        <p class="muted" style="font-size:15.5px">Bayerbach, Bad Birnbach, Rotthalmünster, Bad Griesbach, Pfarrkirchen, Triftern, Tann, Simbach am Inn, Eggenfelden, Arnstorf, Massing und Passau. Auf Anfrage auch darüber hinaus.</p>
      </aside>
    </div>
  </div>
</section>

<section class="paper-2 pad-s">
  <div class="wrap wrap-narrow">
    <h2 class="h3 center">Was nach Ihrer Anfrage passiert</h2>
    <div class="steps" style="margin-top:36px">
      <span class="steps-line" aria-hidden="true"><b></b></span>
      <div class="step"><span class="step-n">1</span><h3 class="h4">Rückmeldung</h3><p>Wir melden uns und klären kurz, worum es geht.</p></div>
      <div class="step"><span class="step-n">2</span><h3 class="h4">Aufmaß</h3><p>Termin vor Ort, kostenlos und unverbindlich.</p></div>
      <div class="step"><span class="step-n">3</span><h3 class="h4">Angebot</h3><p>Festpreis, jede Position einzeln aufgeführt.</p></div>
      <div class="step"><span class="step-n">4</span><h3 class="h4">Termin</h3><p>Sie entscheiden, wir planen die Montage ein.</p></div>
    </div>
  </div>
</section>
""".format(
      ph=page_head("Kontakt", "Sagen Sie uns, was ansteht.",
        "Am schnellsten geht es per Telefon. Wenn Sie lieber schreiben: Das Formular unten stellt Ihre "
        "Anfrage fertig zusammen, Sie schicken sie mit einem Klick aus Ihrem E-Mail-Programm.",
        [("index.html", "Start"), (None, "Kontakt")]),
      mail=MAIL, telh=TEL_HREF, telt=TEL_TXT, firma=FIRMA, strasse=STRASSE, plz=PLZ, ort=ORT,
      ic_phone=ICON["phone"], ic_mail=ICON["mail"], ic_pin=ICON["pin"], ic_clock=ICON["clock"],
    ) + footer()


def impressum():
    return head(
      "Impressum | FB Montagebetrieb Bayerbach",
      "Impressum und Anbieterkennzeichnung von " + FIRMA + ", " + STRASSE + ", " + PLZ + " " + ORT + " im Landkreis Rottal-Inn.",
      "impressum.html", noindex=False
    ) + header("") + """

{ph}

<section class="pad">
  <div class="wrap wrap-narrow prose">
    <!-- Hinweis fuer die Betreiber: Die Angaben wurden von der bisherigen Website uebernommen.
         Bitte Schreibweise des Inhabernamens, Umsatzsteuer-Identifikationsnummer und die Angaben
         zur Handwerkskammer vor der Veroeffentlichung pruefen und gegebenenfalls korrigieren. -->
    <h2 class="h3">Angaben gemäß § 5 DDG</h2>
    <p>{firma}<br>Inhaber: Faton Bytyci<br>{strasse}<br>{plz} {ort}<br>Deutschland</p>

    <h2 class="h3">Kontakt</h2>
    <p>Telefon: <a href="tel:{telh}">{telt}</a><br>E-Mail: <a href="mailto:{mail}">{mail}</a></p>

    <h2 class="h3">Umsatzsteuer-Identifikationsnummer</h2>
    <p>Gemäß § 27 a Umsatzsteuergesetz: DE 549544543</p>

    <h2 class="h3">Wirtschafts-Identifikationsnummer</h2>
    <p>Gemäß § 139c Abgabenordnung: DE 540430-14050459</p>

    <h2 class="h3">Angaben zur Berufshaftpflichtversicherung</h2>
    <p>Berufsbezeichnung: Glaser (verliehen in der Bundesrepublik Deutschland).</p>

    <h2 class="h3">Zuständige Kammer</h2>
    <p>Handwerkskammer Niederbayern-Oberpfalz<br>Nikolastraße 10<br>94032 Passau<br>
    Internet: <a href="https://www.hwkno.de" rel="noopener">www.hwkno.de</a></p>

    <h2 class="h3">Verantwortlich für den Inhalt</h2>
    <p>{firma}, {strasse}, {plz} {ort}</p>

    <h2 class="h3">Verbraucherstreitbeilegung</h2>
    <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>

    <h2 class="h3">Haftung für Inhalte</h2>
    <p>Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Wir sind jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden entsprechender Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.</p>

    <h2 class="h3">Haftung für Links</h2>
    <p>Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft; rechtswidrige Inhalte waren nicht erkennbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.</p>

    <h2 class="h3">Urheberrecht und Bildnachweise</h2>
    <p>Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechts bedürfen der schriftlichen Zustimmung des jeweiligen Autors beziehungsweise Erstellers.</p>
    <p>Die auf dieser Website gezeigten Projektfotos stammen aus eigenen Aufträgen von {firma}. Die technischen Zeichnungen und Symbole wurden eigens für diese Website erstellt.</p>
  </div>
</section>
""".format(
      ph=page_head("Rechtliches", "Impressum",
        "Anbieterkennzeichnung nach § 5 Digitale-Dienste-Gesetz.",
        [("index.html", "Start"), (None, "Impressum")]),
      firma=FIRMA, strasse=STRASSE, plz=PLZ, ort=ORT, telh=TEL_HREF, telt=TEL_TXT, mail=MAIL,
    ) + footer()


def datenschutz():
    return head(
      "Datenschutz | FB Montagebetrieb Bayerbach",
      "Datenschutz auf der Website von " + FIRMA + ": keine Cookies, keine Analyse-Dienste, "
      "keine externen Schriftarten oder Karten.",
      "datenschutz.html"
    ) + header("") + """

{ph}

<section class="pad">
  <div class="wrap wrap-narrow prose">
    <!-- Hinweis fuer die Betreiber: Dieser Text beschreibt die Website in ihrem aktuellen Zustand
         (rein statisch, keine Cookies, keine Analyse, keine externen Ressourcen, Kontakt per mailto).
         Sobald Analyse-Werkzeuge, Karten, Schriftarten von Drittanbietern oder ein serverseitiges
         Formular ergaenzt werden, muss dieser Text angepasst werden. Vor Veroeffentlichung
         rechtlich pruefen lassen. -->
    <div class="note" style="margin-bottom:30px">
      <b>Kurz gefasst</b>
      Diese Website setzt keine Cookies, bindet keine Schriftarten oder Karten von Drittanbietern ein und nutzt keine Analyse- oder Werbedienste. Das Kontaktformular überträgt nichts an uns, sondern öffnet Ihr eigenes E-Mail-Programm.
    </div>

    <h2 class="h3">1. Verantwortlicher</h2>
    <p>{firma}<br>{strasse}<br>{plz} {ort}<br>Telefon: <a href="tel:{telh}">{telt}</a><br>E-Mail: <a href="mailto:{mail}">{mail}</a></p>

    <h2 class="h3">2. Aufruf der Website</h2>
    <p>Beim Aufruf dieser Website überträgt Ihr Browser technisch notwendige Daten an den Server des Hosting-Anbieters. Dazu gehören in der Regel die aufgerufene Adresse, Datum und Uhrzeit, die übertragene Datenmenge, der verwendete Browser und das Betriebssystem sowie die IP-Adresse. Diese Daten werden ausschließlich zur Auslieferung der Seite und zur Abwehr von Angriffen verarbeitet. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO; unser berechtigtes Interesse besteht am sicheren und stabilen Betrieb der Website. Die Serverprotokolle werden vom Hosting-Anbieter nach kurzer Zeit gelöscht.</p>

    <h2 class="h3">3. Cookies und Speicherung im Browser</h2>
    <p>Diese Website setzt keine Cookies und speichert keine Daten in Ihrem Browser. Es ist keine Einwilligung erforderlich, weil nichts gespeichert oder ausgelesen wird, was nicht für die Anzeige der Seite unbedingt nötig ist.</p>

    <h2 class="h3">4. Kontaktformular</h2>
    <p>Das Formular auf der Kontaktseite läuft vollständig in Ihrem Browser. Wenn Sie es absenden, wird daraus eine E-Mail zusammengestellt und Ihr E-Mail-Programm geöffnet. Erst wenn Sie dort auf Senden klicken, verlässt die Nachricht Ihr Gerät. Es werden keine Eingaben auf dieser Website oder beim Hosting-Anbieter gespeichert oder an Dritte übermittelt.</p>

    <h2 class="h3">5. Anfragen per E-Mail oder Telefon</h2>
    <p>Wenn Sie uns kontaktieren, verarbeiten wir Ihre Angaben zur Bearbeitung der Anfrage. Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, soweit die Anfrage auf einen Vertrag gerichtet ist, im Übrigen Art. 6 Abs. 1 lit. f DSGVO. Wir löschen die Daten, sobald sie nicht mehr erforderlich sind, und beachten dabei gesetzliche Aufbewahrungspflichten.</p>

    <h2 class="h3">6. Keine Dienste von Drittanbietern</h2>
    <p>Wir binden keine Analyse-Werkzeuge, keine Werbenetzwerke, keine Karten- oder Videodienste und keine Schriftarten von externen Servern ein. Alle Bilder, Schriften, Formatvorlagen und Skripte liegen auf dem Server dieser Website. Beim Besuch dieser Seiten wird daher keine Verbindung zu Servern Dritter aufgebaut.</p>

    <h2 class="h3">7. Hosting</h2>
    <p>Diese Website wird bei einem Dienstleister gehostet, der die Daten in unserem Auftrag verarbeitet. Mit diesem Anbieter besteht ein Vertrag zur Auftragsverarbeitung nach Art. 28 DSGVO. Den Namen des Anbieters nennen wir Ihnen auf Anfrage gern.</p>

    <h2 class="h3">8. Ihre Rechte</h2>
    <p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch (Art. 21). Eine erteilte Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen. Wenden Sie sich dazu an die oben genannten Kontaktdaten.</p>
    <p>Außerdem haben Sie das Recht, sich bei einer Aufsichtsbehörde zu beschweren. Zuständig ist das Bayerische Landesamt für Datenschutzaufsicht, Promenade 18, 91522 Ansbach.</p>

    <h2 class="h3">9. Änderungen</h2>
    <p>Wir passen diese Erklärung an, wenn sich die Website oder die Rechtslage ändert. Es gilt jeweils die hier veröffentlichte Fassung.</p>
  </div>
</section>
""".format(
      ph=page_head("Rechtliches", "Datenschutzerklärung",
        "Welche Daten beim Besuch dieser Website anfallen – und welche nicht.",
        [("index.html", "Start"), (None, "Datenschutz")]),
      firma=FIRMA, strasse=STRASSE, plz=PLZ, ort=ORT, telh=TEL_HREF, telt=TEL_TXT, mail=MAIL,
    ) + footer()
