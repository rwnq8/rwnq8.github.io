import urllib.request, json

def check(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req) as r:
            return f'HTTP {r.status}'
    except Exception as e:
        return f'ERROR: {str(e)[:100]}'

urls = [
    'https://rwnq8.github.io',
    'https://qnfo-landing.pages.dev',
    'https://rwnq8.github.io/ai/',
    'https://rwnq8.github.io/robots.txt',
    'https://rwnq8.github.io/sitemap.xml',
]
for u in urls:
    print(f'{u}: {check(u)}')
