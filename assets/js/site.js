'use strict';
(() => {
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const number = (value, digits = 0) => new Intl.NumberFormat('de-DE', { maximumFractionDigits: digits, minimumFractionDigits: digits }).format(value);
  const arrow = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14m-5-5 5 5-5 5"/></svg>';
  // Content remains visible when JavaScript or IntersectionObserver is unavailable.
  if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.documentElement.classList.add('js');
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
    }), { threshold: 0.08 });
    $$('.reveal').forEach(el => observer.observe(el));
  }
  const menu = $('.main-nav');
  const toggle = $('.menu-toggle');
  const closeMenu = () => { menu?.classList.remove('is-open'); document.body.classList.remove('menu-open'); toggle?.setAttribute('aria-expanded', 'false'); toggle?.setAttribute('aria-label', 'Menü öffnen'); };
  toggle?.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open)); toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
    menu.classList.toggle('is-open', open); document.body.classList.toggle('menu-open', open);
  });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { if (toggle?.getAttribute('aria-expanded') === 'true') { closeMenu(); toggle.focus(); } } });
  document.addEventListener('click', e => { if (!e.target.closest('.site-header') && toggle?.getAttribute('aria-expanded') === 'true') closeMenu(); });
  $$('.main-nav a').forEach(a => a.addEventListener('click', closeMenu));
  matchMedia('(min-width: 901px)').addEventListener('change', e => { if (e.matches) closeMenu(); });

  $$('[data-planner]').forEach(planner => {
    let step = 0;
    let product = 'Fenster';
    const width = $('[data-width]', planner), height = $('[data-height]', planner), quantity = $('[data-quantity]', planner), context = $('[data-context]', planner);
    const next = $('[data-next]', planner), back = $('[data-back]', planner), inquiry = $('[data-inquiry]', planner), error = $('.planner-error', planner);
    const choices = $$('[data-product]', planner);
    choices.forEach(choice => choice.addEventListener('click', () => {
      product = choice.dataset.product;
      choices.forEach(c => c.setAttribute('aria-pressed', String(c === choice)));
      // Typical starting values; the user can freely change them.
      if (product === 'Türen') { width.value = '100'; height.value = '210'; }
      else { width.value = '120'; height.value = '140'; }
    }));
    const valid = () => {
      for (const field of [width, height, quantity]) {
        if (!field.checkValidity() || !Number.isFinite(field.valueAsNumber)) {
          error.textContent = 'Bitte geben Sie gültige Maße und eine ganze Stückzahl innerhalb der angegebenen Grenzen ein.';
          field.reportValidity(); field.focus(); return false;
        }
      }
      error.textContent = ''; return true;
    };
    const update = () => {
      $$('[data-step]', planner).forEach(el => el.hidden = Number(el.dataset.step) !== step);
      $$('[data-progress]', planner).forEach(el => {
        const active = Number(el.dataset.progress) <= step; el.classList.toggle('active', active);
        if (Number(el.dataset.progress) === step) el.setAttribute('aria-current', 'step'); else el.removeAttribute('aria-current');
      });
      back.hidden = step === 0; next.hidden = step === 2; inquiry.hidden = step !== 2;
      $('[data-step-label]', planner).textContent = `Schritt ${step + 1} von 3`;
      if (step === 2) {
        const w = width.valueAsNumber, h = height.valueAsNumber, q = quantity.valueAsNumber;
        const area = w * h * q / 10000;
        const data = { Leistung: product, Vorhaben: context.value, 'Gleiche Elemente': number(q), 'Ungefähres Maß je Element': `${number(w)} × ${number(h)} cm`, 'Rechnerische Gesamtfläche': `${number(area, 2)} m²` };
        const summary = $('[data-summary]', planner); summary.replaceChildren();
        Object.entries(data).forEach(([label, value]) => { const row = document.createElement('div'); const strong = document.createElement('strong'); strong.textContent = label + ': '; row.append(strong, document.createTextNode(value)); summary.append(row); });
        const hint = document.createElement('p'); hint.className = 'planner-sub'; hint.style.margin = '14px 0 0'; hint.textContent = 'Maße dienen der Erstberatung. Kein Angebot und keine Bestellmaße.'; summary.append(hint);
        const message = 'Mein Vorhaben mit 2bfensterwerk:\n\n' + Object.entries(data).map(([label,value]) => `${label}: ${value}`).join('\n') + '\n\nBitte beraten Sie mich zur passenden Ausführung und zum Aufmaß.';
        inquiry.href = 'kontakt.html?' + new URLSearchParams({ leistung: product, nachricht: message });
      }
    };
    next.addEventListener('click', () => { if (step === 1 && !valid()) return; step = Math.min(step + 1, 2); update(); const heading = $(`[data-step="${step}"] h3`, planner); heading.tabIndex = -1; heading.focus({ preventScroll: true }); });
    back.addEventListener('click', () => { step = Math.max(step - 1, 0); error.textContent = ''; update(); });
    update();
  });

  const energy = $('[data-energy]');
  if (energy) {
    const updateEnergy = () => {
      const values = {};
      $$('input', energy).forEach(input => {
        const value = input.valueAsNumber; values[input.name] = value;
        $(`[data-value="${input.id}"]`, energy).textContent = number(value, input.name.includes('U') ? 1 : 0) + ' ' + input.dataset.unit;
      });
      const delta = values.area * (values.oldU - values.newU) * values.degree / 1000;
      $('[data-energy-result]').textContent = number(Math.abs(delta));
      $('[data-energy-description]').textContent = delta > 0 ? 'Weniger rechnerischer Transmissionswärmeverlust über die betrachtete Fensterfläche.' : delta < 0 ? 'Mehr rechnerischer Transmissionswärmeverlust: Der neue U-Wert ist höher als der bisherige.' : 'Gleiche U-Werte: Im Modell ergibt sich keine Änderung des Transmissionswärmeverlusts.';
      const text = `Bitte beraten Sie mich zu neuen Fenstern.\n\nMeine Modellannahmen (keine Verbrauchsprognose):\nFensterfläche: ${number(values.area)} m²\nUw bisher: ${number(values.oldU, 1)} W/(m²K)\nUw neu: ${number(values.newU, 1)} W/(m²K)\nHeizgradstunden: ${number(values.degree)} Kh/a\nModellergebnis: ${number(Math.abs(delta))} kWh/Jahr ${delta > 0 ? 'weniger' : delta < 0 ? 'mehr' : 'Änderung'} Transmissionswärmeverlust.`;
      $('.energy-result a').href = 'kontakt.html?' + new URLSearchParams({ leistung: 'Fenster', nachricht: text });
    };
    energy.addEventListener('input', updateEnergy); energy.addEventListener('submit', e => e.preventDefault()); updateEnergy();
  }

  const contact = $('[data-contact]');
  if (contact) {
    const params = new URLSearchParams(location.search);
    const service = contact.elements.namedItem('service'), message = contact.elements.namedItem('message');
    const requested = params.get('leistung');
    if ([...service.options].some(option => option.value === requested)) service.value = requested;
    if (params.has('nachricht')) message.value = params.get('nachricht').slice(0, 2200);
    const status = $('.form-status', contact);
    const request = () => {
      const data = new FormData(contact);
      const subject = 'Projektanfrage · ' + String(data.get('service')).replace(/[\r\n]/g, ' ');
      const body = `Guten Tag 2bfensterwerk,\n\n${data.get('message')}\n\nMein Kontakt:\nName: ${data.get('name')}\nE-Mail: ${data.get('email')}\nTelefon: ${data.get('phone') || 'Nicht angegeben'}\nProjektort: ${data.get('location')}\nBereich: ${data.get('service')}\n\nIch bitte um Kontaktaufnahme zu meinem Vorhaben.\n\nFreundliche Grüße\n${data.get('name')}`;
      return { body, subject, mailto: 'mailto:info@2bfensterwerk.de?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body) };
    };
    contact.addEventListener('submit', e => {
      e.preventDefault(); if (!contact.reportValidity()) return;
      const draft = request(); status.hidden = false; status.replaceChildren();
      status.append(document.createTextNode('Die Anfrage ist für Ihr E-Mail-Programm vorbereitet. Bitte dort prüfen und selbst absenden. Falls sich kein Programm öffnet, können Sie die Anfrage kopieren oder '));
      const a = document.createElement('a'); a.href = draft.mailto; a.textContent = 'den E-Mail-Entwurf erneut öffnen'; status.append(a, document.createTextNode('. Es wurde noch keine Nachricht versendet.'));
      window.location.href = draft.mailto;
    });
    $('[data-copy]', contact).addEventListener('click', async () => {
      if (!contact.reportValidity()) return;
      const draft = request(); status.hidden = false;
      try { await navigator.clipboard.writeText(`An: info@2bfensterwerk.de\nBetreff: ${draft.subject}\n\n${draft.body}`); status.textContent = 'Ihre Anfrage wurde kopiert. Fügen Sie sie in eine E-Mail an info@2bfensterwerk.de ein und senden Sie diese selbst ab.'; }
      catch { status.replaceChildren(); const label = document.createElement('p'); label.textContent = 'Automatisches Kopieren ist hier nicht verfügbar. Markieren und kopieren Sie den folgenden Text:'; const area = document.createElement('textarea'); area.value = `An: info@2bfensterwerk.de\nBetreff: ${draft.subject}\n\n${draft.body}`; area.readOnly = true; area.style.width = '100%'; area.rows = 12; area.setAttribute('aria-label', 'Anfragetext zum Kopieren'); status.append(label, area); area.focus(); area.select(); }
    });
  }
  $$('[data-comparison]').forEach(el => $('input', el).addEventListener('input', e => el.style.setProperty('--split', e.target.value + '%')));
  const lightbox = $('.lightbox');
  let opener = null;
  $$('[data-lightbox]').forEach(button => button.addEventListener('click', () => {
    opener = button; const img = $('img', lightbox); img.src = button.dataset.lightbox; img.alt = button.dataset.caption;
    $('[data-lightbox-caption]', lightbox).textContent = button.dataset.caption; lightbox.showModal();
  }));
  $('.lightbox-close', lightbox)?.addEventListener('click', () => lightbox.close());
  lightbox?.addEventListener('click', e => { if (e.target === lightbox) { const r = lightbox.getBoundingClientRect(); if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) lightbox.close(); } });
  lightbox?.addEventListener('close', () => opener?.focus({ preventScroll: true }));
  // Preserve the original seven-layer SVG and its exploded-view animation.
  const anatomy = $('.anatomy');
  if (anatomy) {
    const reduced = matchMedia('(prefers-reduced-motion: reduce)');
    const svg = $('.anatomy-svg', anatomy);
    const art = $('.anatomy-art', anatomy);
    const toggle = $('[data-anatomy-toggle]', anatomy);
    const status = $('[data-anatomy-status]', anatomy);
    const items = $$('[data-anatomy-layer]', anatomy);
    const layers = $$('.anatomy-svg .layer', anatomy);
    const labels = $$('.anatomy-svg .layer-label', anatomy);
    const wraps = $$('.anatomy-svg .layer-wrap', anatomy);
    let selected = null;
    let seen = false;
    const highlight = index => {
      layers.forEach((layer, i) => layer.classList.toggle('mute', index !== null && i !== index));
      labels.forEach((label, i) => label.classList.toggle('dim', index !== null && i !== index));
    };
    const setOpen = open => {
      anatomy.classList.toggle('on', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? 'Wieder zusammensetzen' : 'Aufbau zeigen';
      status.textContent = open ? 'Aufgefächerter Aufbau' : 'Zusammengesetztes Fenster';
      if (!open) {
        selected = null; highlight(null);
        items.forEach(item => item.setAttribute('aria-pressed', 'false'));
      }
    };
    toggle.hidden = false;
    if (reduced.matches) { seen = true; setOpen(true); }
    else if ('IntersectionObserver' in window) setOpen(false);
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(entries => entries.forEach(entry => {
        anatomy.classList.toggle('in-view', entry.isIntersecting);
        if (entry.isIntersecting && !seen) { seen = true; setOpen(true); }
      }), { threshold: .2 });
      observer.observe(art);
    } else { anatomy.classList.add('in-view'); setOpen(true); }
    toggle.addEventListener('click', () => { seen = true; setOpen(!anatomy.classList.contains('on')); });
    items.forEach((item, i) => {
      item.addEventListener('mouseenter', () => { if (anatomy.classList.contains('on')) highlight(i); });
      item.addEventListener('mouseleave', () => highlight(selected));
      item.addEventListener('focus', () => { if (anatomy.classList.contains('on')) highlight(i); });
      item.addEventListener('blur', () => highlight(selected));
      item.addEventListener('click', () => {
        seen = true;
        if (!anatomy.classList.contains('on')) setOpen(true);
        selected = selected === i ? null : i;
        items.forEach((button, n) => button.setAttribute('aria-pressed', String(n === selected)));
        highlight(selected);
      });
    });
    const narrow = matchMedia('(max-width: 760px)');
    const setBox = () => svg.setAttribute('viewBox', narrow.matches ? '-6 10 612 590' : '0 0 900 600');
    setBox(); narrow.addEventListener('change', setBox);
    let raf = 0;
    const applyParallax = (x, y) => {
      wraps.forEach((wrap, i) => {
        const depth = (i - 3) * .34;
        wrap.style.transform = `translate(${(x * depth).toFixed(2)}px,${(y * depth).toFixed(2)}px)`;
      });
    };
    art.addEventListener('pointermove', e => {
      if (reduced.matches || e.pointerType !== 'mouse' || !anatomy.classList.contains('on')) return;
      const box = art.getBoundingClientRect();
      const x = ((e.clientX - box.left) / box.width - .5) * 22;
      const y = ((e.clientY - box.top) / box.height - .5) * 14;
      cancelAnimationFrame(raf); raf = requestAnimationFrame(() => applyParallax(x, y));
    });
    art.addEventListener('pointerleave', () => { cancelAnimationFrame(raf); applyParallax(0, 0); });
    reduced.addEventListener('change', () => { cancelAnimationFrame(raf); applyParallax(0, 0); if (reduced.matches) { seen = true; setOpen(true); } });
  }
  const comfort = $('[data-comfort]');
  if (comfort) {
    const reduced = matchMedia('(prefers-reduced-motion: reduce)');
    const buttons = $$('[data-comfort-mode]');
    const descriptions = {
      day: ['Tageslicht', 'Offen für Tageslicht. Der Blick nach draußen bleibt frei.', 'Rollladen geöffnet für Tageslicht'],
      privacy: ['Sichtschutz', 'Ein wenig Rückzug. Der Rollladen schirmt den oberen Fensterbereich ab.', 'Rollladen zur Hälfte abgesenkt für Sichtschutz'],
      night: ['Abendruhe', 'Zeit zum Abschalten. Der Rollladen schließt die Fensterfläche.', 'Rollladen vollständig geschlossen für Abendruhe']
    };
    let timers = [];
    const cancel = () => { timers.forEach(clearTimeout); timers = []; };
    const setMode = (mode, announce = true) => {
      comfort.dataset.mode = mode;
      $('[data-comfort-label]', comfort).textContent = descriptions[mode][0];
      comfort.setAttribute('aria-label', 'Interaktive Fensterillustration: ' + descriptions[mode][2]);
      buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.comfortMode === mode)));
      if (announce) $('[data-comfort-description]').textContent = descriptions[mode][1];
    };
    const play = () => {
      cancel();
      if (reduced.matches) { setMode('day'); return; }
      setMode('day');
      timers.push(setTimeout(() => setMode('privacy'), 300));
      timers.push(setTimeout(() => setMode('day'), 2400));
    };
    buttons.forEach(button => button.addEventListener('click', () => { cancel();setMode(button.dataset.comfortMode); }));
    $('[data-comfort-play]', comfort).addEventListener('click', play);
    if (!reduced.matches && 'IntersectionObserver' in window) {
      const observer = new IntersectionObserver(entries => {
        if (entries.some(entry => entry.isIntersecting)) { play(); observer.disconnect(); }
      }, {threshold:.45});
      observer.observe(comfort);
    }
    reduced.addEventListener('change', cancel);
  }
  // Draw the logo silhouette, then reveal the original metallic artwork.
  const logoMotionPreference = matchMedia('(prefers-reduced-motion: reduce)');
  const logoTimers = new Map();
  const playLogo = logo => {
    clearTimeout(logoTimers.get(logo));
    logo.classList.remove('is-drawing');
    if (logoMotionPreference.matches) { logo.dataset.logoState = 'complete';return; }
    // A layout read resets the animation for explicit replay without replacing the asset.
    void logo.getBoundingClientRect();
    logo.dataset.logoState = 'drawing';
    logo.classList.add('is-drawing');
    logoTimers.set(logo,setTimeout(() => { logo.classList.remove('is-drawing');logo.dataset.logoState='complete';logoTimers.delete(logo); },2850));
  };
  $$('[data-logo-motion]').forEach(logo => {
    if (logo.closest('.footer') && 'IntersectionObserver' in window && !logoMotionPreference.matches) {
      const observer = new IntersectionObserver(entries => {
        if (entries.some(entry=>entry.isIntersecting)) { playLogo(logo);observer.disconnect(); }
      },{threshold:.3});
      observer.observe(logo);
    } else playLogo(logo);
  });
  $$('[data-logo-replay]').forEach(button => {
    button.hidden=logoMotionPreference.matches;
    button.addEventListener('click',()=>playLogo($('[data-logo-motion]',button.closest('[data-logo-stage]'))));
  });
  logoMotionPreference.addEventListener('change',()=>{
    $$('[data-logo-motion]').forEach(logo=>{clearTimeout(logoTimers.get(logo));logo.classList.remove('is-drawing');logo.dataset.logoState='complete';});
    logoTimers.clear();
    $$('[data-logo-replay]').forEach(button=>button.hidden=logoMotionPreference.matches);
  });
})();
