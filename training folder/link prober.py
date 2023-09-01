 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request("https://7learn.com/")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
