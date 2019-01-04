import urllib.request
from bs4 import BeautifulSoup


doc = urllib.request.urlopen('https://newtimes.ru/articles/detail/139693/')
page = doc.read().decode('cp1251')

soup = BeautifulSoup(page, features="lxml")

date_and_author = soup.find_all("h4")[1].text.strip()
title = soup.find("title").text
lead = soup.find("div",{"class":"txtlead"}).text

content = soup.find_all("p")
body = ''
for i in content:
    i = i.text
    body += str(i)

article = date_and_author + '\n' + title + '\n' + lead + '\n' + body

print(article)