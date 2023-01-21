import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=wig20'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

svg = soup.find('svg', {'class': 'chrt-svg'})

if svg:
    print(svg.prettify())
else:
    print('Nie znaleziono wykresu SVG')
