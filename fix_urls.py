import os
root = os.path.expanduser(r'~\qnfo-landing')
files = ['index.html','ai/index.html','papers/index.html','robots.txt','sitemap.xml']
for f in files:
    fp = os.path.join(root, f)
    if os.path.exists(fp):
        with open(fp,'r',encoding='utf-8') as fh:
            c = fh.read()
        c = c.replace('rowan.quni-gudzinas.org','rwnq8.github.io')
        with open(fp,'w',encoding='utf-8') as fh:
            fh.write(c)
        print(f'updated: {f}')
