with open(r'C:\Users\LENOVO\qnfo-landing\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the robots meta tag and add google-site-verification after it
old = '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">'
new = old + '\n<meta name="google-site-verification" content="REPLACE_WITH_YOUR_VERIFICATION_CODE" />'
if old in content:
    content = content.replace(old, new, 1)
    with open(r'C:\Users\LENOVO\qnfo-landing\index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Meta tag added successfully')
else:
    print('Could not find robots meta tag')
