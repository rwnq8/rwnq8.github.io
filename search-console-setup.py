"""Search Console & Bing Webmaster Setup for Rowan Brad Quni-Gudzinas / QNFO domains.

This script documents exactly what needs to be done for Google Search Console
and Bing Webmaster Tools registration. DNS TXT records are managed via Cloudflare.
"""

SITEMAP_URLS = {
    "rwnq8.github.io": "https://rwnq8.github.io/sitemap.xml",
    "qnfo-landing.pages.dev": "https://qnfo-landing.pages.dev/sitemap.xml",
    "qnfo.org": "https://qnfo.org/sitemap.xml",
    "papers.qnfo.org": "https://papers.qnfo.org/sitemap.xml",
    "qwav.org": "https://qwav.org/sitemap.xml",
    "qwav.tech": "https://qwav.tech/sitemap.xml",
}

CLOUDFLARE_ZONES = [
    "qnfo.org",
    "qwav.org",
    "qwav.tech",
    "qwav.net",
    "qwav.uk",
    "qwave.tech",
    "qnfo.net",
    "qnfo.uk",
    "q-wave.tech",
    "ipatent.me",
    "q08.org",
    "empoweringchange.today",
]

print("""
============================================================
GOOGLE SEARCH CONSOLE & BING WEBMASTER TOOLS SETUP
============================================================

## STEP 1: Google Search Console — Add Properties

For each domain below, go to:
    https://search.google.com/search-console/welcome

Add a new property. For each, Google will give you a verification code.

### Domain Properties (strongly preferred — covers all subdomains):

""")

for zone in CLOUDFLARE_ZONES:
    print(f"   ✅ {zone}")

print("""
### URL-Prefix Properties (for specific subdomains):

""")

for domain in SITEMAP_URLS:
    print(f"   ✅ {domain}")

print("""
## STEP 2: Verification Methods (in order of ease)

### Method A: Cloudflare Integration (easiest if Cloudflare is DNS provider)
1. In Search Console, choose "Domain" property type
2. Enter: qnfo.org
3. Google will detect Cloudflare as your DNS provider
4. Click "Verify" — Cloudflare auto-adds the TXT record
5. Repeat for qwav.org, qwav.tech, qwav.net, qwav.uk

### Method B: DNS TXT Record (manual)
1. In Search Console, choose "Domain" property
2. Google gives you a TXT record like: google-site-verification=XXXXXXX
3. Add it via Cloudflare DNS API:
   curl -X POST "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records" \\
     -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \\
     -d '{"type":"TXT","name":"@","content":"google-site-verification=XXXXXXX","ttl":1}'
4. Wait 60 seconds, click "Verify"

### Method C: HTML Meta Tag (for rwnq8.github.io)
1. In Search Console, add as "URL-prefix": https://rwnq8.github.io
2. Choose "HTML tag" verification method
3. Add meta tag to index.html <head>:
   <meta name="google-site-verification" content="VERIFICATION_CODE" />
4. Push to rwnq8.github.io
5. Click "Verify"

## STEP 3: Submit Sitemaps

For each verified property, submit the sitemap:

""")

for domain, url in SITEMAP_URLS.items():
    print(f"   {domain}:")
    print(f"     Sitemap URL: {url}")
    print(f"     Console URL: https://search.google.com/search-console/sitemaps?resource_id=sc-domain:{domain}")

print("""
## STEP 4: Bing Webmaster Tools

1. Go to: https://www.bing.com/webmasters/home
2. Sign in with Microsoft account
3. "Add a site" for each domain
4. Bing can import from Google Search Console (easiest)
5. Or use the same DNS TXT verification method
6. Submit the same sitemap URLs

## STEP 5: robots.txt Verification

Verify each domain serves robots.txt correctly:

""")

for domain in SITEMAP_URLS:
    robots_url = f"https://{domain}/robots.txt"
    print(f"   https://{domain}/robots.txt")

print("""
============================================================
SUMMARY — Priority Order
============================================================

1. Register qnfo.org (Domain property) in Google Search Console
   → Covers ALL subdomains (papers, legal, graph-api, etc.)

2. Register qwav.org and qwav.tech (Domain properties)
   → Covers ALL qwav subdomains

3. Register rwnq8.github.io (URL-prefix property)
   → Your canonical landing page

4. Register qnfo-landing.pages.dev (URL-prefix property)
   → Cloudflare Pages deployment of landing page

5. Submit all sitemaps listed above

6. Repeat in Bing Webmaster Tools (can import from Google)

7. Wait 24-48 hours for initial indexing
   → Check "URL inspection" tool in Search Console
   → Request indexing for the landing page and /ai/ page
""")
