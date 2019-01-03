import urllib.request
import html
import re

doc = urllib.request.urlopen('https://newtimes.ru/articles/detail/139693/')
content = doc.read().decode('cp1251')

title = ''
get_title = re.search('<title>(.*?)</title>', content)
if get_title:
    title = get_title.group(1)

lead = ''
get_lead = re.search(r'"txtlead">(.*?)</div>', content)
if get_lead:
    lead = get_lead.group(1)

regexp = re.compile(r'<p>(.*?)</p>', re.DOTALL)
paragraphs = regexp.findall(content)
if paragraphs:
    paragraphs = ''.join(paragraphs)

regexp = re.compile(r'<img.*?<br>', re.DOTALL)
clean_paragraphs = regexp.sub('', paragraphs)

regexp = re.compile(r'.*?</div>', re.DOTALL)
clean_paragraphs = regexp.sub('', clean_paragraphs)

text = title + '\n' + lead + clean_paragraphs

text = html.unescape(text)

print(text)

#print(paragraphs)
#s = html.unescape(content)
#print(content)

