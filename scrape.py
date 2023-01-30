import requests
from bs4 import BeautifulSoup

response = requests.get(
  url = 'https://en.wikipedia.org/wiki/Category:Musicians_from_Bristol'
)

soup = BeautifulSoup(response.content, 'html.parser')

main_content = soup.find(class_ = 'mw-category-columns')
artist_links = main_content.find_all('a')

result = []

for artist in artist_links:
  link = "https://en.wikipedia.org" + artist['href']
  name = artist['title']
  result.append([name, link])

print(result)