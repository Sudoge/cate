
from lxml import etree

with open('index.html', 'r') as f:
    content = f.read()

html = etree.HTML(content)

print(html)