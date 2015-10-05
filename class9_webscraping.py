import urllib.request as ur
url = "http://giving.columbia.edu/contacts"
url_req = ur.Request(url)		#creating a rquest object that is in JSON
url_response = ur.urlopen(url_req)
url_data = url_response.read()
url_data = url_data.decode('utf-8')
# print(url_data)

mail_addr_start = url_data.find("mailto:")
mail_addr_end = url_data[mail_addr_start + 7:].find('"')
print(url_data[mail_addr_start + 7:mail_addr_start + 7 + mail_addr_end])

#-------------------------

def getListFromString(data_string,search_string,terminator):
    listToBeReturned = list() #An empty list that will contain the return value
    whereWeAre = 0 #WhereWeAre keeps track of the segment of data_string that has been processed
    while True: #We'll keep searching until we can't find search_string in data_string
        searchStringLoc = data_string[whereWeAre:].find(search_string)        
        if searchStringLoc == -1: #If we can find search_string, end the loop. We're done
            break
        #Since we've found searchString, the stuff we're looking for starts just after it
        data_start = whereWeAre + searchStringLoc + len(search_string)
        data_end = data_string[data_start:].find(terminator) + data_start
        item = data_string[data_start:data_end]
        listToBeReturned.append(item)
        whereWeAre = data_end + len(terminator)
        if whereWeAre > len(data_string):
            break
    return listToBeReturned

import urllib.request as ur
url = "http://giving.columbia.edu/contacts"
url_req = ur.Request(url)
url_response = ur.urlopen(url_req)
url_data = url_response.read()
url_data = url_data.decode('utf-8')
email_list = getListFromString(url_data,'mailto:','"')
print(email_list)

#-------------------------

url = 'http://www.epicurious.com/tools/searchresults?search=vegan+chili'
url_req = ur.Request(url)
url_response = ur.urlopen(url_req)
url_data = url_response.read()
url_data = url_data.decode('utf-8')
links_list = getListFromString(url_data,'<a href="/recipes/food/views/','"')
import pprint as pp
pp.pprint(links_list)

#-------------------------BEAUTIFUL SOUP LIBRARY - Does all the shit above!

import urllib.request as ul #url.request lib for handling the url
from bs4 import BeautifulSoup #bs for parsing the page

url = "http://rogteran.co"

#Do stuff necessary to get the page text into a string
url_response = ul.urlopen(url,timeout=5)
soup = BeautifulSoup(url_response) #Soup stores the data in a structured way to make retrieval easy
#Soup also automatically decodes the page correctly (most of the time!)

print(soup.prettify()) #Prints page contents 

#Or, to get the first link out of the page
soup.a

#To find all links on the page
links = soup.find_all('a')
links










