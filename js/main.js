/* Benchmark Contract Services — site behavior
   Nav toggle, scroll reveals, intent tabs, and accessible client-side
   validation for Netlify Forms. Forms use data-netlify="true" so Netlify's
   own injected script performs submission (including base64 file uploads).
   This file validates + honeypots only; it does NOT preventDefault on a
   valid submission, so native Netlify Forms handling runs. */
(function () {
  "use strict";

  /* Mobile nav */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* Subtle reveal */
  var reduceMotion = false;
  try { reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches; } catch (e) {}
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  /* Intent tabs (contact page) */
  document.querySelectorAll(".intent-tabs").forEach(function (tabs) {
    var buttons = Array.prototype.slice.call(tabs.querySelectorAll("button[role='tab']"));
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        buttons.forEach(function (b) { b.setAttribute("aria-selected", "false"); });
        btn.setAttribute("aria-selected", "true");
        document.querySelectorAll("[data-intent-panel]").forEach(function (p) {
          p.hidden = p.id !== btn.getAttribute("aria-controls");
        });
      });
    });
  });

  /* Forms: client-side validation + honeypot.
     Compatible with Netlify Forms: on a valid submission we do NOT
     preventDefault, so Netlify's injected <form data-netlify> JS takes over
     (AJAX POST to Netlify's forms handler, base64-encoding any file uploads). */
  function setInvalid(field, on) {
    var wrap = field.closest ? field.closest(".field") : null;
    if (wrap) wrap.classList.toggle("invalid", on);
    field.setAttribute("aria-invalid", on ? "true" : "false");
  }

  function validate(form) {
    var ok = true;
    Array.prototype.slice.call(form.querySelectorAll("[required]")).forEach(function (field) {
      if (field.type === "checkbox" || field.type === "radio") {
        var group = form.querySelectorAll('input[type="' + field.type + '"][name="' + field.name + '"]');
        var any = Array.prototype.slice.call(group).some(function (c) { return c.checked; });
        if (!any) ok = false;
        return;
      }
      var bad = !field.value.trim() ||
        (field.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value));
      setInvalid(field, bad);
      if (bad) ok = false;
    });
    return ok;
  }

  document.querySelectorAll("form[data-netlify]").forEach(function (form) {
    form.addEventListener("input", function (e) {
      if (e.target.closest && e.target.closest(".field")) setInvalid(e.target, false);
    });

    form.addEventListener("submit", function (ev) {
      var status = form.querySelector(".form-status");
      var hp = form.querySelector(".hp input");

      /* Honeypot: silently accept and drop bot submissions. */
      if (hp && hp.value) {
        if (status) { status.textContent = "Thank you. Your submission has been received."; status.className = "form-status ok"; }
        form.reset();
        ev.preventDefault();
        return;
      }
      if (!validate(form)) {
        if (status) { status.textContent = "Please complete the highlighted fields."; status.className = "form-status err"; }
        var firstBad = form.querySelector(".field.invalid input, .field.invalid select, .field.invalid textarea, .field.invalid .check-group input");
        if (firstBad) firstBad.focus();
        ev.preventDefault();
        return;
      }
      /* Valid — do not preventDefault. Netlify Forms JS handles submission
         (AJAX + attachment base64). The no-JS fallback POSTS to "/" and the
         hidden form-name field routes it to Netlify. */
    });
  });
})();