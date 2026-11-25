function ddInit() {
  var VIEWS = ['home', 'assessment', 'families', 'gps', 'clinicians', 'privacy'];
  var pendingScroll = null;

  function show(name) {
    if (VIEWS.indexOf(name) === -1) name = 'home';
    VIEWS.forEach(function (v) {
      var el = document.getElementById('view-' + v);
      if (el) el.hidden = (v !== name);
    });
    document.querySelectorAll('[data-nav]').forEach(function (a) {
      if (a.getAttribute('data-nav') === name) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
    var titles = window.DD_TITLES || {};
    document.title = name === 'home'
      ? 'Dementia Diagnostics'
      : (titles[name] || 'Dementia Diagnostics') + ' · Dementia Diagnostics';

    if (pendingScroll) {
      var target = document.getElementById(pendingScroll);
      pendingScroll = null;
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        return;
      }
    }
    window.scrollTo({ top: 0, behavior: 'auto' });
  }

  function route() {
    show((location.hash || '#home').replace(/^#/, ''));
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!a) return;
    var want = a.getAttribute('href').replace(/^#/, '') || 'home';
    var scrollTo = a.getAttribute('data-scroll');
    if (scrollTo) pendingScroll = scrollTo;
    if (('#' + want) === location.hash || (want === 'home' && !location.hash)) {
      e.preventDefault();
      show(want);
    }
  });

  window.addEventListener('hashchange', route);
  route();

  var form = document.getElementById('enquiry-form');
  var sent = document.getElementById('sent');
  if (form && sent) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      form.hidden = true;
      sent.hidden = false;
      sent.setAttribute('tabindex', '-1');
      sent.focus();
      sent.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }
}
