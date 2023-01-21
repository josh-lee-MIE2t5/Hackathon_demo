import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.destinationtoronto.com/'

headers = {
    'User-Agent': 'https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'
}

r = requests.get('https://www.destinationtoronto.com/events/?view=list&sort=date&bounds=false')
soup = BeautifulSoup(r.content, 'lxml')

i = 0

tabContent = soup.find_all('div', class_="root-panel panel-page")
print(tabContent)

# eventsList = soup.find_all('div', class_="row event-list-row", recursive= False)
# print(event)
# print(eventNew)
# for item in eventsList:
#      for display in item.find_all('div', id_="fecListDisplay"):
#         print(display)
