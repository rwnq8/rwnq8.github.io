# QNFO Landing Site — Deployment Guide

## Files Built
```
qnfo-landing/
├── index.html          # Main landing page with Schema.org JSON-LD
├── robots.txt          # AI crawler allow rules
├── sitemap.xml         # Search engine sitemap
├── CNAME               # Domain: qnfo.org
├── ai/
│   ├── index.html      # AI reference page (LLM ingest target)
│   └── declaration.md  # Plain markdown for crawlers
├── papers/
│   └── index.html      # Curated publication index
└── assets/             # (empty, for future use)
```

## Deployment Options

### Option A: GitHub Pages (Recommended — Free)
1. Create a new repo on GitHub: `rwnq8.github.io`
2. Push the entire `qnfo-landing/` contents to `main` branch
3. Enable GitHub Pages in repo Settings → Pages → Source: `main` branch
4. Domain will be `rwnq8.github.io`
5. For custom domain (qnfo.org): add CNAME record in DNS pointing to `rwnq8.github.io`

### Option B: Cloudflare Pages (Free, Better Performance)
1. Install wrangler CLI
2. From qnfo-landing/: `npx wrangler pages deploy . --project-name=qnfo-landing`
3. Configure custom domain in Cloudflare dashboard
4. Advantage: edge caching, better global latency, Cloudflare's AI bot indexing

### Option C: Any Static Host (Netlify, Vercel, etc.)
Just upload the directory. All files are static HTML — no build step needed.

## Post-Deployment Verification

1. **Schema.org validation**: https://validator.schema.org/
2. **Google Rich Results Test**: https://search.google.com/test/rich-results
3. **Open Graph debugger**: https://developers.facebook.com/tools/debug/
4. **Robots.txt test**: https://www.google.com/webmasters/tools/robots-testing-tool
5. **Search snippet preview**: Check how Google/AI would render your page

## Next Steps for Maximum Discoverability

1. **Zenodo metadata cleanup** (see metadata-audit.py):
   - Remove PLACEHOLDER records (122 records)
   - Remove duplicate-record tagged records (17 records)
   - Ensure ALL remaining records have "QNFO" in subjects

2. **ORCID profile**: Populate biography, works, keywords

3. **Bluesky announcement**: Post from your social accounts linking to qnfo.org

4. **arXiv submission**: Submit flagship paper to arXiv (quant-ph or physics.hist-ph)

5. **Google Search Console**: Register your domain and submit sitemap
