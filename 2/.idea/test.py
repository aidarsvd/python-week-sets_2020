import requests
from bs4 import BeautifulSoup as BS
import random
url = 'https://povar.ru/'
source = requests.get(url)
main_text = source.text
soup = BS(main_text,'lxml')
links = soup.findAll('a', {'class': 'listRecipieTitle'})
r_food = (url+ random.choice(links).get("href"))
print(url+ random.choice(links).get("href"))
source_f = requests.get(r_food)
main_text_f = source_f.text
soup_f = BS(main_text_f,'lxml')
details = soup_f.find('ul', {'class':'detailed_ingredients'}).findAll('li', {'itemprop':'ingredients'})
print('Ингредиенты')
for a in details:
    s = a.get_text()
    print("".join(s.split()))
source_rec = requests.get(r_food)
main_text_rec = source_rec.text
soup_rec = BS(main_text_f,'lxml')
recipes = soup_rec.findAll('div', {'itemprop':'recipeInstructions"'})