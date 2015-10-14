# Assignment 6 - Roger Teran

import urllib.request as ul #url.request lib for handling the url
from bs4 import BeautifulSoup #bs for parsing the page

term_list=list()
while True:
	term = input("Enter a search term or END to exit: ")
	if term == 'END' or term == 'end':
		break
	term_list.append(term)

term_list_string = "+".join(term_list)
# print(term_list_string)

url = "http://www.epicurious.com/tools/searchresults?search=" + term_list_string

url_response = ul.urlopen(url,timeout=5)
soup = BeautifulSoup(url_response)

article_soup = soup.find_all('a', class_="recipeLnk", limit=1)
first_recipe = soup.find('a', class_="recipeLnk")

print("____________________________________________________")
print("Name: " + first_recipe.text)

link = first_recipe.get('href')
link = 'http://www.epicurious.com' + link
# print(link)

url_response = ul.urlopen(link,timeout=5)
soup = BeautifulSoup(url_response)

description_soup = soup.find('div', itemprop="description")
print("____________________________________________________")
print("Description: " + description_soup.text)

ingredient_soup = soup.find_all('li', itemprop="ingredients")
print("____________________________________________________")
print("Ingredients: ")
for ingredients in ingredient_soup:
	print(ingredients.text)

preparation_soup = soup.find_all('li', class_="preparation-step")
print("____________________________________________________")
print("Preparation: ")
for step in preparation_soup:
	print(step.text)














