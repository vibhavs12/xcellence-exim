/* ==========================================================================
   Xcellence Exim — site behaviour
   Vanilla JS, no dependencies. Safe to load with `defer`.
   ========================================================================== */
(function () {
  'use strict';

  var doc = document;
  var $  = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };

  /* ----------------------------------------------------------------------
     1. Sticky header shadow
     ---------------------------------------------------------------------- */
  var header = $('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ----------------------------------------------------------------------
     2. Desktop dropdown — keyboard + touch support
        (hover is handled in CSS; this adds click/Enter/Escape)
     ---------------------------------------------------------------------- */
  $$('.has-dropdown').forEach(function (item) {
    var trigger = $('.nav__link', item);
    var menu    = $('.dropdown', item);
    if (!trigger || !menu) return;

    var close = function () {
      menu.classList.remove('is-open');
      trigger.setAttribute('aria-expanded', 'false');
    };
    var open = function () {
      $$('.dropdown.is-open').forEach(function (m) {
        if (m !== menu) {
          m.classList.remove('is-open');
          var t = m.parentNode && $('.nav__link', m.parentNode);
          if (t) t.setAttribute('aria-expanded', 'false');
        }
      });
      menu.classList.add('is-open');
      trigger.setAttribute('aria-expanded', 'true');
    };

    trigger.addEventListener('click', function (e) {
      e.preventDefault();
      if (menu.classList.contains('is-open')) { close(); } else { open(); }
    });

    item.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { close(); trigger.focus(); }
    });

    doc.addEventListener('click', function (e) {
      if (!item.contains(e.target)) close();
    });
  });

  /* ----------------------------------------------------------------------
     3. Mobile drawer
     ---------------------------------------------------------------------- */
  var drawer  = $('.drawer');
  var toggle  = $('.nav__toggle');
  var lastFocus = null;

  function focusables(root) {
    return $$('a[href], button:not([disabled]), select, input, textarea, [tabindex]:not([tabindex="-1"])', root)
      .filter(function (el) { return el.offsetParent !== null; });
  }

  function openDrawer() {
    if (!drawer) return;
    lastFocus = doc.activeElement;
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    if (toggle) toggle.setAttribute('aria-expanded', 'true');
    doc.documentElement.style.overflow = 'hidden';
    doc.body.style.overflow = 'hidden';
    var f = focusables($('.drawer__panel', drawer));
    if (f.length) setTimeout(function () { f[0].focus(); }, 60);
  }

  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    doc.documentElement.style.overflow = '';
    doc.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  if (toggle && drawer) {
    toggle.addEventListener('click', function () {
      if (drawer.classList.contains('is-open')) { closeDrawer(); } else { openDrawer(); }
    });
    $$('[data-drawer-close]', drawer).forEach(function (el) {
      el.addEventListener('click', closeDrawer);
    });
    // Close when navigating to an in-page anchor
    $$('.drawer__nav a', drawer).forEach(function (a) {
      a.addEventListener('click', function () {
        if (a.getAttribute('href').charAt(0) === '#') closeDrawer();
      });
    });
    doc.addEventListener('keydown', function (e) {
      if (!drawer.classList.contains('is-open')) return;
      if (e.key === 'Escape') { closeDrawer(); return; }
      if (e.key === 'Tab') {
        var f = focusables($('.drawer__panel', drawer));
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && doc.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });
    // Auto-close if the viewport grows back to desktop
    var mq = window.matchMedia('(min-width: 1161px)');
    var mqHandler = function (ev) { if (ev.matches) closeDrawer(); };
    if (mq.addEventListener) { mq.addEventListener('change', mqHandler); }
    else if (mq.addListener) { mq.addListener(mqHandler); }
  }

  /* Drawer accordions */
  $$('.drawer__acc').forEach(function (btn) {
    var sub = doc.getElementById(btn.getAttribute('aria-controls'));
    if (!sub) return;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      sub.classList.toggle('is-open', !open);
    });
  });

  /* ----------------------------------------------------------------------
     4. Language switcher
        GTranslate ships a plain <select> of 100+ names. We hide it and drive
        it from a custom picker: flag + endonym, key markets first, searchable.
        There is still only ONE GTranslate select on the page — the picker is
        moved between header and drawer rather than duplicated, so translation
        state survives a resize.
     ---------------------------------------------------------------------- */
  var RTL = window.XE_RTL_LANGUAGES || ['ar', 'he', 'iw', 'fa', 'ur', 'ps', 'sd', 'yi', 'ku', 'dv', 'ckb'];
  var LANGS = window.XE_LANGUAGES || {};
  var PRIORITY = window.XE_PRIORITY_LANGUAGES || ['en'];

  function currentLang() {
    var m = doc.cookie.match(/(?:^|;\s*)googtrans=([^;]+)/);
    if (m) {
      var parts = decodeURIComponent(m[1]).split('/');
      var l = parts[parts.length - 1];
      if (l) return l.toLowerCase();
    }
    var h = window.location.hash.match(/googtrans\(([^)]+)\)/);
    if (h) {
      var hp = h[1].split('|');
      return (hp[hp.length - 1] || 'en').toLowerCase();
    }
    return 'en';
  }

  // NOTE: this writes dir/lang/class onto <html>, and we also *observe*
  // <html> for changes. Every write must therefore be idempotent — only
  // touch an attribute when its value actually differs — otherwise the
  // observer re-triggers on our own mutation and spins forever.
  function applyDirection() {
    var lang = currentLang() || 'en';
    var base = lang.split('-')[0];
    var isRtl = RTL.indexOf(lang) > -1 || RTL.indexOf(base) > -1;
    var dir = isRtl ? 'rtl' : 'ltr';
    var html = doc.documentElement;

    if (html.getAttribute('dir') !== dir) html.setAttribute('dir', dir);
    if (html.getAttribute('lang') !== lang) html.setAttribute('lang', lang);
    if (html.classList.contains('is-rtl') !== isRtl) html.classList.toggle('is-rtl', isRtl);
  }

  applyDirection();

  // Google Translate mutates the cookie and <html class> asynchronously.
  var lastSeen = currentLang();
  setInterval(function () {
    var now = currentLang();
    if (now !== lastSeen) { lastSeen = now; applyDirection(); }
  }, 600);

  if (typeof MutationObserver === 'function') {
    var dirScheduled = false;
    new MutationObserver(function () {
      if (dirScheduled) return;          // coalesce bursts into one pass
      dirScheduled = true;
      setTimeout(function () { dirScheduled = false; applyDirection(); }, 0);
    }).observe(doc.documentElement, {
      attributes: true, attributeFilter: ['class', 'lang']
    });
  }

  var picker     = $('.langpick');
  var langHome   = $('[data-lang-desktop]');
  var langMobile = $('[data-lang-mobile]');

  function flagUrl(cc, big) {
    return 'https://flagcdn.com/' + (big ? 'w40' : 'w20') + '/' + cc + '.png';
  }

  function meta(code) {
    var m = LANGS[code] || LANGS[code.split('-')[0]];
    return m || null;
  }

  /* Renders <img> flag, or a lettered chip when the language has no
     meaningful single flag (Esperanto, Latin…) or the image fails. */
  function flagNode(code, label, big) {
    var m = meta(code);
    if (m && m[2]) {
      var img = doc.createElement('img');
      img.className = 'langpick__flag';
      img.src = flagUrl(m[2], big);
      img.srcset = flagUrl(m[2], big) + ' 1x, ' + 'https://flagcdn.com/' + (big ? 'w80' : 'w40') + '/' + m[2] + '.png 2x';
      img.alt = '';
      img.width = big ? 26 : 20;
      img.loading = 'lazy';
      img.onerror = function () {
        var chip = flagChip(label);
        if (img.parentNode) img.parentNode.replaceChild(chip, img);
      };
      return img;
    }
    return flagChip(label);
  }

  function flagChip(label) {
    var span = doc.createElement('span');
    span.className = 'langpick__flag langpick__flag--chip';
    span.setAttribute('aria-hidden', 'true');
    span.textContent = (label || '?').slice(0, 2).toUpperCase();
    return span;
  }

  if (picker) {
    var pickBtn   = $('.langpick__btn', picker);
    var pickPanel = $('.langpick__panel', picker);
    var pickLabel = $('.langpick__current', picker);
    var pickFlag  = $('.langpick__btn .langpick__flag', picker);
    var search    = $('.langpick__search input', picker);
    var priBox    = $('[data-lang-priority]', picker);
    var listBox   = $('[data-lang-list]', picker);
    var emptyMsg  = $('[data-lang-empty]', picker);
    var gtSelect  = null;
    var options   = [];   // { code, value, en, native, node }

    /* -- build from GTranslate's own <select>, so the list always matches
          exactly what the translation service supports ------------------- */
    function buildFrom(sel) {
      gtSelect = sel;
      options = [];
      priBox.innerHTML = '';
      listBox.innerHTML = '';

      var byCode = {};
      Array.prototype.forEach.call(sel.options, function (o) {
        if (!o.value) return;                       // "Select Language" placeholder
        var code = o.value.split('|').pop();
        if (!code || byCode[code]) return;
        var m = meta(code);
        byCode[code] = {
          code: code,
          value: o.value,
          en: (m && m[0]) || o.text,
          native: (m && m[1]) || o.text
        };
      });

      // Register every language exactly once, so search can reach all of them
      // (an earlier version only tracked the priority set, which meant the
      // search box silently ignored the other ~100 languages).
      options = Object.keys(byCode).map(function (k) { return byCode[k]; });

      // Key export markets first, as flag tiles
      PRIORITY.forEach(function (code) {
        var item = byCode[code];
        if (item) priBox.appendChild(tile(item));
      });

      // Then the complete list, alphabetically by English name
      options.slice()
        .sort(function (a, b) { return a.en.localeCompare(b.en); })
        .forEach(function (item) { listBox.appendChild(row(item)); });

      syncCurrent();
    }

    function choose(item) {
      if (!gtSelect) return;
      gtSelect.value = item.value;

      /* Three ways in, most reliable first.

         1. doGTranslate() is GTranslate's own public entry point and the only
            one guaranteed to actually perform the translation.
         2. A real change event, for builds that bind with addEventListener.
         3. An inline onchange handler, for older builds.

         Dispatching the event alone is NOT enough on every GTranslate build —
         that is what stopped the picker from translating. */
      var done = false;
      if (typeof window.doGTranslate === 'function') {
        try { window.doGTranslate(item.value); done = true; } catch (e) { /* fall through */ }
      }
      if (!done) {
        gtSelect.dispatchEvent(new Event('change', { bubbles: true }));
        if (typeof gtSelect.onchange === 'function') gtSelect.onchange.call(gtSelect);
      }

      closePicker();
      setTimeout(applyDirection, 400);
      setTimeout(applyDirection, 1400);
      setTimeout(fitHeader, 600);
      setTimeout(fitHeader, 1600);
    }

    function tile(item) {
      var b = doc.createElement('button');
      b.type = 'button';
      b.className = 'langpick__tile';
      b.setAttribute('data-code', item.code);
      b.setAttribute('data-search', (item.en + ' ' + item.native + ' ' + item.code).toLowerCase());
      b.appendChild(flagNode(item.code, item.en, true));
      var s = doc.createElement('span');
      s.textContent = item.native;
      b.appendChild(s);
      b.addEventListener('click', function () { choose(item); });
      item.tile = b;
      return b;
    }

    function row(item) {
      var li = doc.createElement('li');
      var b = doc.createElement('button');
      b.type = 'button';
      b.className = 'langpick__row';
      b.setAttribute('data-code', item.code);
      b.setAttribute('data-search', (item.en + ' ' + item.native + ' ' + item.code).toLowerCase());
      b.appendChild(flagNode(item.code, item.en, false));
      var n = doc.createElement('span');
      n.className = 'langpick__native';
      n.textContent = item.native;
      b.appendChild(n);
      if (item.native !== item.en) {
        var e = doc.createElement('span');
        e.className = 'langpick__en';
        e.textContent = item.en;
        b.appendChild(e);
      }
      b.addEventListener('click', function () { choose(item); });
      li.appendChild(b);
      item.row = li;
      return li;
    }

    function syncCurrent() {
      var code = currentLang();
      var item = null;
      for (var i = 0; i < options.length; i++) {
        if (options[i].code.toLowerCase() === code) { item = options[i]; break; }
      }
      if (!item) {
        var m = meta(code);
        item = { code: code, en: (m && m[0]) || code.toUpperCase(), native: (m && m[1]) || code.toUpperCase() };
      }
      if (pickLabel) pickLabel.textContent = item.native;
      if (pickFlag && pickFlag.parentNode) {
        pickFlag.parentNode.replaceChild(flagNode(item.code, item.en, false), pickFlag);
        pickFlag = $('.langpick__btn .langpick__flag', picker);
      }
      options.forEach(function (o) {
        var on = o.code.toLowerCase() === code;
        if (o.tile) o.tile.setAttribute('aria-current', on ? 'true' : 'false');
        if (o.row) {
          var rb = o.row.firstChild;
          if (rb) rb.setAttribute('aria-current', on ? 'true' : 'false');
        }
      });
    }

    function filter(q) {
      q = (q || '').trim().toLowerCase();
      var shown = 0;
      options.forEach(function (o) {
        var hit = !q || (o.en + ' ' + o.native + ' ' + o.code).toLowerCase().indexOf(q) > -1;
        if (o.row) o.row.hidden = !hit;
        if (o.tile) o.tile.hidden = !hit;
        if (hit) shown++;
      });
      var heads = $$('.langpick__heading', picker);
      // hide the "key markets" heading when nothing in that group matches
      var priShown = $$('.langpick__tile:not([hidden])', picker).length;
      if (heads[0]) heads[0].hidden = !priShown;
      if (priBox) priBox.hidden = !priShown;
      if (heads[1]) heads[1].hidden = !$$('.langpick__list > li:not([hidden])', picker).length;
      if (emptyMsg) emptyMsg.hidden = shown > 0;
    }

    function openPicker() {
      picker.classList.add('is-open');
      pickBtn.setAttribute('aria-expanded', 'true');
      pickPanel.hidden = false;
      if (search) { search.value = ''; filter(''); setTimeout(function () { search.focus(); }, 40); }
    }
    function closePicker() {
      picker.classList.remove('is-open');
      pickBtn.setAttribute('aria-expanded', 'false');
      pickPanel.hidden = true;
    }

    pickBtn.addEventListener('click', function () {
      if (picker.classList.contains('is-open')) closePicker(); else openPicker();
    });
    if (search) search.addEventListener('input', function () { filter(search.value); });

    doc.addEventListener('click', function (e) {
      if (picker.classList.contains('is-open') && !picker.contains(e.target)) closePicker();
    });
    picker.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closePicker(); pickBtn.focus(); }
    });

    /* -- wait for GTranslate, then take over ------------------------------ */
    var langTries = 0;
    var langTimer = setInterval(function () {
      langTries++;
      var sel = doc.querySelector('.gtranslate_wrapper select');
      if (sel) {
        clearInterval(langTimer);
        buildFrom(sel);
        picker.classList.add('is-ready');
        sel.addEventListener('change', function () {
          setTimeout(syncCurrent, 200);
          setTimeout(applyDirection, 400);
        });
      } else if (langTries > 80) {
        clearInterval(langTimer);
        // Translation service blocked or offline — keep the site usable.
        picker.classList.add('is-unavailable');
        pickBtn.disabled = true;
        var fb = $('[data-lang-fallback]');
        if (fb) fb.hidden = false;
      }
    }, 250);

    // keep the button label in step with cookie-driven changes
    setInterval(syncCurrent, 1200);
  }

  /* Move the picker between header and drawer — one instance, never cloned. */
  function placeLang() {
    if (!picker || !langHome || !langMobile) return;
    var compact = header && header.classList.contains('is-compact');
    var target = (compact || window.matchMedia('(max-width: 1160px)').matches) ? langMobile : langHome;
    if (picker.parentNode !== target) target.appendChild(picker);
  }

  /* ----------------------------------------------------------------------
     4b. Header overflow guard
         Translated menu labels can be 2–3x longer than the English ones
         (Armenian, German, Vietnamese…). Rather than guess a breakpoint,
         measure what the row actually needs and collapse to the hamburger
         the moment it stops fitting — in any language, at any zoom level.
     ---------------------------------------------------------------------- */
  var navRow  = $('.nav');
  var navMenu = $('.nav__menu');
  var navBrand = $('.brand');
  var navActs = $('.nav__actions');

  function fitHeader() {
    if (!header || !navRow || !navMenu || !navBrand || !navActs) return;
    if (window.matchMedia('(max-width: 1160px)').matches) {
      // below the breakpoint CSS already handles it; don't fight it
      header.classList.remove('is-compact');
      placeLang();
      return;
    }

    // Measure in the expanded state. Reading layout right after removing the
    // class is synchronous, so the browser never paints the intermediate step.
    header.classList.remove('is-compact');

    var gap = parseFloat(window.getComputedStyle(navRow).columnGap) || 16;
    var needed = navBrand.offsetWidth + navMenu.scrollWidth + navActs.scrollWidth + (gap * 2);
    var available = navRow.clientWidth
      - parseFloat(window.getComputedStyle(navRow).paddingLeft || 0)
      - parseFloat(window.getComputedStyle(navRow).paddingRight || 0);

    // If the header hasn't been laid out yet (hidden tab, print preview,
    // pre-paint) every measurement reads 0 — don't collapse on that.
    if (available > 0 && needed > 0 && needed > available - 4) {
      header.classList.add('is-compact');
    }
    placeLang();
  }

  fitHeader();
  window.addEventListener('resize', debounce(fitHeader, 120));
  if (doc.fonts && doc.fonts.ready && typeof doc.fonts.ready.then === 'function') {
    doc.fonts.ready.then(fitHeader);
  }
  window.addEventListener('load', fitHeader);

  // Google Translate swaps the nav text in asynchronously — re-measure when it does.
  if (navMenu && typeof MutationObserver === 'function') {
    var fitScheduled = false;
    new MutationObserver(function () {
      if (fitScheduled) return;
      fitScheduled = true;
      setTimeout(function () { fitScheduled = false; fitHeader(); }, 120);
    }).observe(navMenu, { childList: true, subtree: true, characterData: true });
  }

  /* ----------------------------------------------------------------------
     5. Certificate lightbox
     ---------------------------------------------------------------------- */
  var lb = $('.lightbox');
  if (lb) {
    var lbImg = $('img', lb);
    var lbPrev = null;
    var openLb = function (src, alt) {
      lbImg.src = src;
      lbImg.alt = alt || '';
      lb.classList.add('is-open');
      lb.setAttribute('aria-hidden', 'false');
      doc.body.style.overflow = 'hidden';
      var c = $('.lightbox__close', lb); if (c) c.focus();
    };
    var closeLb = function () {
      lb.classList.remove('is-open');
      lb.setAttribute('aria-hidden', 'true');
      doc.body.style.overflow = '';
      lbImg.src = '';
      if (lbPrev && lbPrev.focus) lbPrev.focus();
    };
    $$('[data-lightbox]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        lbPrev = el;
        var img = $('img', el);
        openLb(el.getAttribute('data-lightbox') || el.href, img ? img.alt : '');
      });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    var lbClose = $('.lightbox__close', lb);
    if (lbClose) lbClose.addEventListener('click', closeLb);
    doc.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lb.classList.contains('is-open')) closeLb();
    });
  }

  /* ----------------------------------------------------------------------
     6. Enquiry form

     Submits from the page (the visitor never leaves the site) and delivers a
     formatted email to the sales desk, with the director in CC.

     Transport is FormSubmit — a free form-to-email relay, no account and no
     server needed. It is configured entirely through the data- attributes on
     the <form> in contact.html:

       data-to        sales@xcellenceexim.com     primary recipient
       data-cc        ashwani@xcellenceexim.com   copied on every enquiry
       data-endpoint  (optional) override for Formspree/Web3Forms/Netlify

     ONE-TIME ACTIVATION: the very first submission sends a confirmation link
     to data-to. Someone has to open that email and click the link once —
     after that every enquiry is delivered automatically. Until it is clicked,
     submissions are held rather than delivered.

     If the relay is ever unreachable, the form falls back to opening the
     visitor's mail client with the same content, so an enquiry is never lost.
     ---------------------------------------------------------------------- */
  var form = $('#rfq-form');
  if (form) {
    var status = $('#form-status');
    var TO_EMAIL = form.getAttribute('data-to') || 'sales@xcellenceexim.com';
    var CC_EMAIL = form.getAttribute('data-cc') || '';
    var WA_NUMBER = (form.getAttribute('data-whatsapp') || '917985916897').replace(/\D/g, '');
    var ENDPOINT = form.getAttribute('data-endpoint') ||
                   ('https://formsubmit.co/ajax/' + TO_EMAIL);

    var setError = function (field, msg) {
      var wrap = field.closest('.field');
      if (!wrap) return;
      wrap.classList.add('is-invalid');
      var err = $('.err', wrap);
      if (err) err.textContent = msg;
      field.setAttribute('aria-invalid', 'true');
    };
    var clearError = function (field) {
      var wrap = field.closest('.field');
      if (!wrap) return;
      wrap.classList.remove('is-invalid');
      field.removeAttribute('aria-invalid');
    };

    $$('input, select, textarea', form).forEach(function (f) {
      f.addEventListener('input', function () { clearError(f); });
      f.addEventListener('change', function () { clearError(f); });
    });

    var validate = function () {
      var ok = true, firstBad = null;
      $$('[required]', form).forEach(function (f) {
        clearError(f);
        var v = (f.value || '').trim();
        if (!v) {
          setError(f, 'This field is required.');
          ok = false; firstBad = firstBad || f;
        } else if (f.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) {
          setError(f, 'Please enter a valid email address.');
          ok = false; firstBad = firstBad || f;
        }
      });
      if (firstBad) firstBad.focus();
      return ok;
    };

    function val(n) {
      var el = form.elements[n];
      return el ? String(el.value || '').trim() : '';
    }

    /* The email body. FormSubmit renders each key as a labelled row, so the
       keys are written the way we want them to read in the inbox. */
    function answers() {
      var o = {};
      o['Full name']            = val('name');
      o['Company']              = val('company') || '—';
      o['Email']                = val('email');
      o['Phone / WhatsApp']     = val('phone') || '—';
      o['Destination country']  = val('country');
      o['Destination port']     = val('port') || '—';
      o['Product']              = val('product');
      o['Quantity required']    = val('quantity') || '—';
      o['Preferred Incoterm']   = val('incoterm') || 'No preference';
      o['Packing preference']   = val('packing') || '—';
      o['Message']              = val('message');
      return o;
    }

    function subjectLine() {
      var bits = ['Export enquiry'];
      if (val('product')) bits.push(val('product'));
      if (val('country')) bits.push(val('country'));
      if (val('name')) bits.push(val('name'));
      return bits.join(' — ');
    }

    function asText() {
      var o = answers(), lines = [];
      Object.keys(o).forEach(function (k) {
        if (o[k] && o[k] !== '—') lines.push(k + ': ' + o[k]);
      });
      return lines.join('\n');
    }

    var show = function (kind, msg) {
      if (!status) return;
      status.className = 'form-status ' + (kind === 'ok' ? 'is-ok' : 'is-err');
      status.textContent = msg;
      if (typeof status.scrollIntoView === 'function') {
        try { status.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); }
        catch (e) { status.scrollIntoView(false); }
      }
    };

    var busy = function (on) {
      var btn = $('button[type="submit"]', form);
      if (!btn) return;
      if (on) {
        btn.disabled = true;
        if (!btn.dataset.label) btn.dataset.label = btn.textContent;
        btn.textContent = 'Sending…';
      } else {
        btn.disabled = false;
        if (btn.dataset.label) btn.textContent = btn.dataset.label;
      }
    };

    function mailtoFallback() {
      var url = 'mailto:' + TO_EMAIL +
        (CC_EMAIL ? '?cc=' + encodeURIComponent(CC_EMAIL) + '&' : '?') +
        'subject=' + encodeURIComponent(subjectLine()) +
        '&body=' + encodeURIComponent(asText());
      window.location.href = url;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Honeypot: pretend success, send nothing.
      if ((form.elements['company_website'] || {}).value) {
        show('ok', 'Thank you — your enquiry has been received.');
        return;
      }
      if (!validate()) {
        show('err', 'Please correct the highlighted fields and try again.');
        return;
      }

      var payload = answers();
      payload._subject  = subjectLine();
      payload._template = 'table';
      payload._captcha  = 'false';        // required for AJAX submissions
      payload._replyto  = val('email');   // hitting Reply answers the buyer
      if (CC_EMAIL) payload._cc = CC_EMAIL;

      busy(true);
      fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(payload)
      }).then(function (r) {
        return r.json().catch(function () { return { success: r.ok }; });
      }).then(function (data) {
        var ok = data && (data.success === true || data.success === 'true');
        if (!ok) throw new Error(( data && data.message) || 'relay error');
        form.reset();
        show('ok', 'Thank you — your enquiry is on its way to our export desk. ' +
                   'We reply within one business day, usually sooner.');
      }).catch(function () {
        show('err', 'We could not send that automatically. Your email app is opening ' +
                    'with the enquiry ready — or use the WhatsApp button instead.');
        setTimeout(mailtoFallback, 900);
      }).then(function () {
        busy(false);
      });
    });

    var waBtn = $('#rfq-whatsapp');
    if (waBtn) {
      waBtn.addEventListener('click', function () {
        if (!validate()) { show('err', 'Please complete the highlighted fields first.'); return; }
        var text = 'Export enquiry — Xcellence Exim\n\n' + asText();
        window.open('https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(text), '_blank', 'noopener');
      });
    }
  }

  /* ----------------------------------------------------------------------
     7. Reveal on scroll
     ---------------------------------------------------------------------- */
  var reveals = $$('.reveal');
  if (reveals.length) {
    if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add('is-in'); });
    }
  }

  /* ----------------------------------------------------------------------
     8. Current year
     ---------------------------------------------------------------------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ----------------------------------------------------------------------
     Helpers
     ---------------------------------------------------------------------- */
  function debounce(fn, wait) {
    var t;
    return function () {
      var args = arguments, ctx = this;
      clearTimeout(t);
      t = setTimeout(function () { fn.apply(ctx, args); }, wait);
    };
  }
})();
