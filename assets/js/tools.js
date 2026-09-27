/* FB Handel und Montagebetrieb – Rechner und Konfigurator
   Alle Ergebnisse sind Richtwerte. Die Annahmen stehen jeweils unter dem Ergebnis. */
(function () {
  "use strict";

  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var nf = function (v, d) {
    return v.toLocaleString("de-DE", { minimumFractionDigits: d || 0, maximumFractionDigits: d || 0 });
  };
  var anfrage = function (leistung, nachricht) {
    return "kontakt.html?leistung=" + encodeURIComponent(leistung) +
           "&nachricht=" + encodeURIComponent(nachricht);
  };

  /* =======================================================================
     1) Schallschutz-Rechner
     Vereinfacht: Innenpegel = Aussenpegel minus bewertetes Schalldaemm-Mass
     plus ein pauschaler Zuschlag von 8 dB fuer das Verhaeltnis von Fensterflaeche
     zu Raumabsorption. Nach unten begrenzt auf 25 dB, das ungefaehre
     Grundgeraeusch eines ruhigen Wohnraums.
     ======================================================================= */
  var schall = $("#schall");
  if (schall) {
    var sAussen = $("#schall-aussen"), sAlt = $("#schall-alt"), sNeu = $("#schall-neu");
    var oInnen  = $("#schall-innen"), oAlt = $("#schall-alt-out"), oDiff = $("#schall-diff");
    var oMal    = $("#schall-mal"), oKlasse = $("#schall-klasse"), oBar = $("#schall-bar");
    var oCta    = $("#schall-cta"), waveOut = $$("#schall .sw-out"), waveIn = $$("#schall .sw-in");

    var RAUM = 8;    /* Zuschlag fuer Fensterflaeche und Raumabsorption */
    var GRUND = 25;  /* Grundgeraeusch eines ruhigen Wohnraums */

    var klasse = function (db) {
      if (db <= 26) return ["Sehr leise", "Sie hören den Raum, nicht die Straße"];
      if (db <= 30) return ["Leise", "etwa wie in einer Bibliothek"];
      if (db <= 35) return ["Ruhig", "ein leises Gespräch im Nebenraum"];
      if (db <= 42) return ["Hörbar", "Gesprächslautstärke im Raum"];
      return ["Störend", "Schlafen und Arbeiten fällt schwer"];
    };

    var rechne = function () {
      var aussen = parseFloat(sAussen.value);
      var rwAlt  = parseFloat(sAlt.value);
      var rwNeu  = parseFloat(sNeu.value);
      var innenAlt = Math.max(GRUND, aussen - rwAlt + RAUM);
      var innenNeu = Math.max(GRUND, aussen - rwNeu + RAUM);
      var diff = Math.max(0, innenAlt - innenNeu);
      var mal = Math.pow(2, diff / 10);
      var k = klasse(innenNeu);

      oInnen.textContent = nf(innenNeu);
      oAlt.textContent = nf(innenAlt);
      oDiff.textContent = nf(diff);
      oMal.textContent = mal >= 1.95 ? nf(mal, 1) : nf(mal, 1);
      oKlasse.innerHTML = "<b>" + k[0] + "</b> – " + k[1];
      oBar.style.width = Math.max(4, Math.min(100, (innenNeu - GRUND) / 40 * 100)) + "%";

      var f = Math.max(0.1, Math.min(1, (innenNeu - GRUND) / 35));
      waveOut.forEach(function (w) { w.setAttribute("stroke-width", "3"); w.style.opacity = "0.95"; });
      waveIn.forEach(function (w, i) {
        w.style.opacity = String(Math.max(0.12, f - i * 0.12));
        w.setAttribute("stroke-width", (1 + f * 2.4).toFixed(2));
      });

      var txtNeu = sNeu.options[sNeu.selectedIndex].textContent;
      var txtAus = sAussen.options[sAussen.selectedIndex].textContent;
      oCta.href = anfrage("Schallschutzfenster",
        "Ich habe den Schallschutz-Rechner genutzt.\n" +
        "Situation draußen: " + txtAus + "\n" +
        "Gewünschter Fensteraufbau: " + txtNeu + "\n" +
        "Rechnerisch bleiben ca. " + nf(innenNeu) + " dB im Raum – rund " + nf(diff) +
        " dB weniger als heute.\nBitte melden Sie sich für ein Aufmaß.");
    };
    [sAussen, sAlt, sNeu].forEach(function (el) { el.addEventListener("change", rechne); });
    rechne();
  }

  /* =======================================================================
     2) Fenster-Energierechner
     Transmissionswaerme: Q = U x A x Heizgradstunden. Wir rechnen mit
     84 kKh/a (Deutschland, 20 Grad innen, Heizgrenze 15 Grad) und einem
     Anlagennutzungsgrad von 0,9.
     ======================================================================= */
  var energie = $("#energie");
  if (energie) {
    var eA = $("#e-flaeche"), eAOut = $("#e-flaeche-out");
    var eAlt = $("#e-alt"), eNeu = $("#e-neu"), ePreis = $("#e-preis");
    var oKwh = $("#e-kwh"), oEuro = $("#e-euro"), oCo2 = $("#e-co2"), o10 = $("#e-10j"), eCta = $("#e-cta");
    var GRAD = 84, WIRKUNG = 0.9, CO2 = 0.201; /* kg CO2 je kWh Erdgas */

    var rechneE = function () {
      var A = parseFloat(eA.value);
      var uAlt = parseFloat(eAlt.value), uNeu = parseFloat(eNeu.value);
      var preis = Math.max(0.01, parseFloat(ePreis.value) || 0.11);
      var du = Math.max(0, uAlt - uNeu);
      var kwh = du * A * GRAD / WIRKUNG;
      var euro = kwh * preis;

      eAOut.textContent = nf(A) + " m²";
      oKwh.textContent = nf(Math.round(kwh / 5) * 5);
      oEuro.textContent = nf(Math.round(euro / 5) * 5);
      oCo2.textContent = nf(Math.round(kwh * CO2 / 5) * 5);
      o10.textContent = nf(Math.round(euro * 10 / 50) * 50);

      eCta.href = anfrage("Fenstertausch",
        "Ich habe den Energierechner genutzt.\n" +
        "Fensterfläche: ca. " + nf(A) + " m²\n" +
        "Heutiger Zustand: " + eAlt.options[eAlt.selectedIndex].textContent + "\n" +
        "Geplanter Aufbau: " + eNeu.options[eNeu.selectedIndex].textContent + "\n" +
        "Rechnerische Ersparnis: rund " + nf(Math.round(euro / 5) * 5) + " Euro im Jahr.\n" +
        "Bitte um ein Angebot mit Aufmaß vor Ort.");
    };
    [eA, eAlt, eNeu, ePreis].forEach(function (el) {
      el.addEventListener("input", rechneE); el.addEventListener("change", rechneE);
    });
    rechneE();
  }

  /* =======================================================================
     3) Projekt-Schnellcheck: drei Fragen bis zur fertigen Anfrage
     ======================================================================= */
  var konfig = $("#konfig");
  if (konfig) {
    var state = { vorhaben: "", umfang: "", zeit: "" };
    var out = $("#konfig-out"), cta = $("#konfig-cta"), zusammen = $("#konfig-summary");

    var texte = {
      "Fenster tauschen": "Wir bauen Ihre Fenster aus und die neuen fachgerecht wieder ein – inklusive Entsorgung der Altfenster.",
      "Haustür oder Innentüren": "Von der Haustür mit Sicherheitsbeschlag bis zur Zimmertür: Aufmaß, Lieferung, Montage.",
      "Bodenbelag verlegen": "Laminat, Parkett, Vinyl oder Designbelag – inklusive Untergrundprüfung und Sockelleisten.",
      "Insektenschutz oder Rollladen": "Maßgefertigte Gitter, Plissées und Rollladen – passgenau und ohne Bohren, wo es möglich ist."
    };

    var update = function () {
      $$("[data-konfig]", konfig).forEach(function (btn) {
        var k = btn.getAttribute("data-konfig"), v = btn.getAttribute("data-value");
        btn.setAttribute("aria-pressed", state[k] === v ? "true" : "false");
        btn.classList.toggle("on", state[k] === v);
      });
      var fertig = state.vorhaben && state.umfang && state.zeit;
      out.hidden = !fertig;
      if (!fertig) return;
      zusammen.innerHTML =
        "<b>" + state.vorhaben + "</b> · " + state.umfang + " · " + state.zeit +
        "<br><span class=\"muted\">" + (texte[state.vorhaben] || "") + "</span>";
      cta.href = anfrage(state.vorhaben,
        "Mein Vorhaben: " + state.vorhaben + "\n" +
        "Umfang: " + state.umfang + "\n" +
        "Zeitraum: " + state.zeit + "\n\n" +
        "Bitte melden Sie sich für einen Termin zum Aufmaß.");
    };

    $$("[data-konfig]", konfig).forEach(function (btn) {
      btn.addEventListener("click", function () {
        state[btn.getAttribute("data-konfig")] = btn.getAttribute("data-value");
        update();
      });
    });
    update();
  }
})();
