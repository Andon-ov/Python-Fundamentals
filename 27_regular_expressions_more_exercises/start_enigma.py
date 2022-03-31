import sys
from io import StringIO

input1 = """<html>\n<head><title>Some title</title></head>\n<body>Here<p> is some </p>content <a href="www.somesite.com">\nclick</body>\n</html>"""

sys.stdin = StringIO(input1)

import re

title_regex = r'<title>([^<>]*)<\/title>'

info = input()

title = re.findall(title_regex, info)
title = ''.join(title)
print(f"Title: {title}")

body_regex = r'<body>.*</body>'

body = re.findall(body_regex, info)

body = ''.join(body)

content_regex = r">([^><]*)<"

content = re.findall(content_regex, body)

content = ''.join(content)
content = content.replace('\\n', '')

print(f'Content: {content}')