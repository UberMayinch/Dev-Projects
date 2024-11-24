import requests as r
from bs4 import BeautifulSoup
import re


page_url = "http://www.nytimes.com/" 

req = r.get(page_url)
# req.json()

print(req.text)

with open('data.txt', 'w') as file:
    file.write(req.text)

rgx = re.compile("^\<p\>*\<p>^")
# print(rgx)

with open('data.txt', 'w+') as file:
    for line in file:
        if(line.startswith("<p>")):
            print(line)
    #    print(rgx.match(line))