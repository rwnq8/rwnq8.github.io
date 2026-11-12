"""SITE-ENGAGEMENT-LOOP-1: rewrite the READ-MOST block of index.html from the fleet's per-path reader counts.
Reads https://fleet.qnfo.org/api/site-engagement (bot-filtered Web Analytics page loads of this site, 7 days).
Lists up to 3 non-root pages readers actually reach; with fewer than 2 such pages the block stays empty."""
import json, re, sys, urllib.request
URL = "https://fleet.qnfo.org/api/site-engagement"
SKIP = ("/", "/index.html")
def block(paths):
    rows = [p for p in paths if p.get("path") not in SKIP and p.get("views", 0) > 0][:3]
    if len(rows) < 2:
        return ""
    items = "".join('<li><a href="%s">%s</a></li>' % (p["path"], p["path"].strip("/") or "home") for p in rows)
    return '\n<h2>Most read this week</h2>\n<ul class="read-most">%s</ul>\n' % items
def render(html, paths):
    return re.sub(r"<!-- READ-MOST:START -->.*?<!-- READ-MOST:END -->",
                  lambda _: "<!-- READ-MOST:START -->" + block(paths) + "<!-- READ-MOST:END -->", html, flags=re.S)
if __name__ == "__main__":
    data = json.load(urllib.request.urlopen(URL, timeout=30))
    old = open("index.html", encoding="utf-8").read()
    new = render(old, data.get("paths", []))
    if new != old:
        open("index.html", "w", encoding="utf-8", newline="").write(new)
        print("index.html updated")
    else:
        print("no change")
