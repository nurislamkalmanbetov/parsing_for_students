import requests
from bs4 import BeautifulSoup as BS

file = open('example.html', encoding='utf-8')

html = file.read()

soup = BS(html, 'html.parser')

main_div = soup.find('div', class_='container')
print(main_div)
