import urllib.request as ul #url.request lib for handling the url
from bs4 import BeautifulSoup #bs for parsing the page

url = "http://www.slate.com"

#Do stuff necessary to get the page text into a string
url_response=ul.urlopen(url,timeout=5)
soup = BeautifulSoup(url_response) #Soup stores the data in a structured way to make retrieval easy
#Soup also automatically decodes the page correctly (most of the time!)

print(soup.prettify()) #Prints page contents 

#Soup stores the page as a dictionary with tags for retrieval. 
#For example, the first div tag on the page is:
soup.div

#Or, to get the first link out of the page
soup.a

#To find all links on the page
soup.find_all('a')

links=soup.find_all('a')
print(len(links))

#Can we get all the links from finance.google.com using bs4?
#Try it here

goog_url='http://finance.google.com'
goog_response=ul.urlopen(goog_url,timeout=5)
goog_soup = BeautifulSoup(goog_response)

goog_links = goog_soup.find_all('a')
for link in goog_links:
    #print(link)
    if link and link.find('INDEXBVMF'):
        print(link)


# -----------------------------------

import selenium