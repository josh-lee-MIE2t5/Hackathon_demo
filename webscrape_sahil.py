import requests
from bs4 import BeautifulSoup

baseurl = 'https://seatgeek.com/'

headers = {
    'User-Agent': 'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'
}

r = requests.get('https://seatgeek.com/cities/toronto')
soup = BeautifulSoup(r.content, 'lxml')

eventLinks = []
tabContent = soup.find_all('div', class_="small-card-mobile")
for item in tabContent:
    for link in item.find_all('a', href=True):
        eventLinks.append(baseurl + link['href'])

print(eventLinks)



# "title": "event 2",
#    "description": "death",
#    "location": "my hall",
#    "_type": "competition",
#    "startDate": "2023-01-21",
#    "endDate": "2023-01-25",
#    "registrationReq": false,
#    "frequency": "yearly"''' + toParse,
