import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.toronto.ca/'

headers = {
    'User-Agent': 'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'
}

r = requests.get('https://www.toronto.ca/explore-enjoy/festivals-events/festivals-events-calendar/')
soup = BeautifulSoup(r.content, 'lxml')

eventsList = soup.find_all('div', class_="row")

print(eventsList)
