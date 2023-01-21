import requests
from bs4 import BeautifulSoup

baseurl = 'https://seatgeek.com/'

headers = {
    'User-Agent': 'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'
}

r = requests.get('https://seatgeek.com/cities/toronto')
soup = BeautifulSoup(r.content, 'lxml')

i = 0

eventLinks = []
tabContent = soup.find_all('li', class_="presenters__ItemWrapper-sc-e3f40ed6-2 jNUXfT")
for item in tabContent:
    for link in item.find_all('a', href=True):
        eventLinks.append(baseurl + link['href'])

print(eventLinks)
