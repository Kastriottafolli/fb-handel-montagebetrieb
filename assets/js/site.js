/* FB Handel und Montagebetrieb – Oberflaeche
   Kein Framework, keine externen Abhaengigkeiten. */
(function () {
  "use strict";

  var $  = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Navigation ---------- */
  var burger = $(".burger");
  if (burger) {
    burger.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$(".nav a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
        burger.setAttribute("aria-expanded", "false");
      });
    });
    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("nav-open")) {
        document.body.classList.remove("nav-open");
        burger.setAttribute("aria-expanded", "false");
        burger.focus();
      }
    });
  }

  var head = $(".head");
  if (head) {
    var onScroll = function () { head.classList.toggle("scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Einblenden beim Scrollen ---------- */
  var revealables = $$("[data-reveal]");
  if (revealables.length) {
    if (!("IntersectionObserver" in window) || reduced) {
      revealables.forEach(function (el) { el.classList.add("in"); });
    } else {
      var ro = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) { e.target.classList.add("in"); ro.unobserve(e.target); }
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
      revealables.forEach(function (el) { ro.observe(el); });
    }
  }

  /* ---------- Zahlen zaehlen hoch ---------- */
  $$("[data-count]").forEach(function (el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduced || !("IntersectionObserver" in window)) {
      el.textContent = end.toLocaleString("de-DE") + suffix; return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        var t0 = null, dur = 1500;
        var tick = function (t) {
          if (t0 === null) t0 = t;
          var p = Math.min(1, (t - t0) / dur);
          var v = end * (1 - Math.pow(1 - p, 3));
          el.textContent = Math.round(v).toLocaleString("de-DE") + suffix;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.4 });
    io.observe(el);
  });

  /* ---------- Logo-Animation im Hero ---------- */
  var mark = $(".brand-anim");
  if (mark) {
    var mpaths = $$(".lg-frame path", mark);
    mpaths.forEach(function (path) {
      var len = 1400;
      try { if (path.getTotalLength) len = Math.ceil(path.getTotalLength()); } catch (e) {}
      path.style.setProperty("--len", len);
    });
    if (reduced) {
      mark.classList.add("static");
    } else {
      /* erst starten, wenn das Layout steht, sonst springt die Strichlaenge */
      requestAnimationFrame(function () {
        requestAnimationFrame(function () { mark.classList.add("go"); });
      });
    }
  }

  /* ---------- Anatomie eines Fensters ---------- */
  var ana = $(".anatomy");
  if (ana) {
    var items  = $$(".layer-list li", ana);
    var labels = $$(".anatomy-svg .layer-label", ana);
    var layers = $$(".anatomy-svg .layer", ana);
    var wraps  = $$(".anatomy-svg .layer-wrap", ana);
    var timers = [];

    var clearTimers = function () { timers.forEach(clearTimeout); timers = []; };

    var play = function () {
      clearTimers();
      ana.classList.add("on");
      items.forEach(function (li) { li.classList.remove("on"); });
      items.forEach(function (li, i) {
        timers.push(setTimeout(function () { li.classList.add("on"); }, 260 + i * 170));
      });
    };
    var reset = function () {
      clearTimers();
      ana.classList.remove("on");
      items.forEach(function (li) { li.classList.remove("on"); });
    };

    if (reduced) {
      ana.classList.add("on");
      items.forEach(function (li) { li.classList.add("on"); });
    } else if ("IntersectionObserver" in window) {
      var seen = false;
      var ioA = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting && !seen) { seen = true; play(); }
        });
      }, { threshold: 0.35 });
      ioA.observe(ana);
    } else {
      play();
    }

    var toggleBtn = $("[data-anatomy-toggle]", ana);
    if (toggleBtn) {
      toggleBtn.addEventListener("click", function () {
        if (ana.classList.contains("on")) {
          reset();
          toggleBtn.textContent = toggleBtn.getAttribute("data-label-play");
        } else {
          play();
          toggleBtn.textContent = toggleBtn.getAttribute("data-label-reset");
        }
      });
    }

    /* Schicht hervorheben */
    var highlight = function (idx) {
      layers.forEach(function (g, i) { g.classList.toggle("mute", idx !== null && i !== idx); });
      labels.forEach(function (g, i) { g.classList.toggle("dim", idx !== null && i !== idx); });
      items.forEach(function (li, i) { li.classList.toggle("hl", idx !== null && i === idx); });
    };
    items.forEach(function (li, i) {
      ["mouseenter", "focusin"].forEach(function (ev) {
        li.addEventListener(ev, function () { if (ana.classList.contains("on")) highlight(i); });
      });
      ["mouseleave", "focusout"].forEach(function (ev) {
        li.addEventListener(ev, function () { highlight(null); });
      });
      li.setAttribute("tabindex", "0");
    });

    /* Schmale Bildschirme: Beschriftungen entfallen, die Zeichnung bekommt den Platz */
    var svg = $(".anatomy-svg", ana);
    if (svg) {
      var schmal = window.matchMedia("(max-width: 760px)");
      var setBox = function () {
        svg.setAttribute("viewBox", schmal.matches ? "-6 10 612 590" : "0 0 900 600");
      };
      setBox();
      if (schmal.addEventListener) schmal.addEventListener("change", setBox);
      else if (schmal.addListener) schmal.addListener(setBox);
    }

    /* Leichte Parallaxe: das Bild folgt dem Zeiger */
    if (!reduced && wraps.length && window.matchMedia("(pointer: fine)").matches) {
      var art = $(".anatomy-art", ana), raf = null, tx = 0, ty = 0;
      art.addEventListener("mousemove", function (e) {
        var r = art.getBoundingClientRect();
        tx = ((e.clientX - r.left) / r.width - 0.5) * 22;
        ty = ((e.clientY - r.top) / r.height - 0.5) * 14;
        if (!raf) raf = requestAnimationFrame(apply);
      });
      art.addEventListener("mouseleave", function () { tx = 0; ty = 0; if (!raf) raf = requestAnimationFrame(apply); });
      var apply = function () {
        raf = null;
        wraps.forEach(function (w, i) {
          var d = (i - 3) * 0.34;
          w.style.transform = "translate(" + (tx * d).toFixed(2) + "px," + (ty * d).toFixed(2) + "px)";
          w.style.transition = "transform .5s cubic-bezier(.16,1,.3,1)";
        });
      };
    }
  }

  /* ---------- Ablauf-Linie ---------- */
  var steps = $(".steps");
  if (steps) {
    var line = $(".steps-line b", steps), stepEls = $$(".step", steps);
    if (reduced) {
      if (line) line.style.width = "100%";
      stepEls.forEach(function (s) { s.classList.add("on"); });
    } else if ("IntersectionObserver" in window) {
      var ioS = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          ioS.unobserve(e.target);
          if (line) line.style.width = "100%";
          stepEls.forEach(function (s, i) { setTimeout(function () { s.classList.add("on"); }, i * 220); });
        });
      }, { threshold: 0.3 });
      ioS.observe(steps);
    }
  }

  /* ---------- Vorher / Nachher ---------- */
  $$(".ba").forEach(function (ba) {
    var range = $(".ba-range", ba);
    if (!range) return;
    var set = function () { ba.style.setProperty("--pos", range.value + "%"); };
    range.addEventListener("input", set);
    set();
  });

  /* ---------- Grossansicht ---------- */
  var lb = $(".lightbox");
  if (lb) {
    var lbImg = $("img", lb), lbCap = $("p", lb), lastFocus = null;
    var open = function (src, cap) {
      lastFocus = document.activeElement;
      lbImg.src = src; lbImg.alt = cap || "";
      lbCap.textContent = cap || "";
      lb.classList.add("on");
      document.body.style.overflow = "hidden";
      $(".lightbox-close", lb).focus();
    };
    var close = function () {
      lb.classList.remove("on"); lbImg.removeAttribute("src");
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    };
    $$(".shot").forEach(function (fig) {
      var img = $("img", fig), cap = $("figcaption", fig);
      fig.setAttribute("tabindex", "0");
      fig.setAttribute("role", "button");
      var big = fig.getAttribute("data-full") || (img && img.src);
      var go = function () { open(big, cap ? cap.textContent.trim() : (img ? img.alt : "")); };
      fig.addEventListener("click", go);
      fig.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); go(); }
      });
    });
    $(".lightbox-close", lb).addEventListener("click", close);
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    window.addEventListener("keydown", function (e) { if (e.key === "Escape" && lb.classList.contains("on")) close(); });
  }

  /* ---------- Kontaktformular: Anfrage per E-Mail ---------- */
  var form = $("#anfrage-form");
  if (form) {
    /* Vorbelegung aus der Adresszeile: ?leistung=…&nachricht=… */
    var params = new URLSearchParams(location.search);
    var pre = function (name, value) {
      var el = form.elements[name];
      if (!el || !value) return;
      if (el.tagName === "SELECT") {
        var hit = Array.prototype.some.call(el.options, function (o) {
          if (o.value === value || o.textContent === value) { el.value = o.value; return true; }
          return false;
        });
        if (!hit) el.value = el.options[0].value;
      } else { el.value = value; }
    };
    pre("leistung", params.get("leistung"));
    pre("nachricht", params.get("nachricht"));
    if (params.get("leistung") || params.get("nachricht")) {
      var hinweis = $("#form-prefill");
      if (hinweis) hinweis.hidden = false;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var v = function (k) { return (d.get(k) || "").toString().trim(); };
      var betreff = "Anfrage " + (v("leistung") || "Website") + " – " + (v("name") || "ohne Namen");
      var zeilen = [
        "Name: " + v("name"),
        "E-Mail: " + v("email"),
        "Telefon: " + v("telefon"),
        "Ort / PLZ: " + v("ort"),
        "Leistung: " + v("leistung"),
        "Gewuenschter Zeitraum: " + v("zeitraum"),
        "",
        "Nachricht:",
        v("nachricht"),
        "",
        "— gesendet ueber fb-handel-montagebetrieb.de"
      ];
      var mail = form.getAttribute("data-mail");
      location.href = "mailto:" + mail + "?subject=" + encodeURIComponent(betreff) +
                      "&body=" + encodeURIComponent(zeilen.join("\n"));
      var ok = $("#form-ok");
      if (ok) { ok.hidden = false; ok.focus(); }
    });
  }

  /* ---------- Jahr in der Fusszeile ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
