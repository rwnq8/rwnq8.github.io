import json, subprocess
result = subprocess.run(['gh', 'api', 'repos/rwnq8/rwnq8.github.io/pages'], capture_output=True, text=True)
d = json.loads(result.stdout)
print(f"URL: {d['html_url']}")
print(f"Status: {d['status']}")
print(f"CNAME: {d.get('cname','none')}")
