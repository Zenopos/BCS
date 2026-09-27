# Benchmark Contract Services LLC

Official website for **Benchmark Contract Services LLC** — a Virginia building-services contractor providing managed janitorial, landscaping, pressure washing, waste hauling, and painting services to government and commercial clients through one accountable contracting partner.

**Live site:** https://benchmarkcontractservices.com
**eVA Vendor ID:** 525389

## Stack

- Static HTML/CSS/JS — no build step, deployable straight to Netlify
- Navy/slate institutional design system, photo-driven editorial layout
- Netlify Forms for contact submissions (including SOW/RFQ file upload)
- Fully SEO-optimized: per-page titles/descriptions/canonicals, Open Graph, JSON-LD structured data, sitemap, robots

## Structure

- `*.html` — site pages (index, services, government, commercial, partners, about, contact, privacy, terms)
- `css/styles.css` — design system
- `js/main.js` — nav, validation, form behavior
- `docs/Capability-Statement.pdf` — downloadable capability statement (+ `build_cap.py`, its generator)
- `_headers` — Netlify security headers (CSP, HSTS, etc.)
- `sitemap.xml`, `robots.txt` — SEO

## Deploy

Push to `main`; Netlify auto-builds and deploys (no build command needed). Forms are wired via Netlify Forms — enable them in the Netlify site settings dashboard.