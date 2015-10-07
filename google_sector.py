#get data from finance.google.com
#print the contents of the page using beautifulsoup
url='http://finance.google.com'
import urllib.request as ul
from bs4 import BeautifulSoup
goog_req = ul.urlopen(url)
goog_soup = BeautifulSoup(goog_req)
print(goog_soup)

# From goog_soup, extract all the links

a_tags=goog_soup.find_all('a')
links=list()
for tag in a_tags:
    link=tag.get('href')
    links.append(link)
print(links)

#Figure out how to extract the information relating to sector performance from goog_soup
sector_perf=goog_soup.find('div',id='secperf')
sector_perf

# Now we can extract the sector performance and put it in a list of tuples. Each tuple contains:
#     The sector name
#     The sector movement
#     The url to the sector detail page

#First step, figure out how to get the entire table rows into a list
sector_table=sector_perf.find_all('tr')

#Row 0 contains headings. We can ignore that. Let's take a look at row 1
print(sector_table[1])
first_sector=sector_table[1]

#Find the url that will take us to the detail for row 1
link=first_sector.find('a').get('href')
link='http://www.google.com'+link
print(link)

#Find the sector name for row 1
sector_name=first_sector.find('a').get_text()
print(sector_name)

#Find the percent change for sector 1
sector_change=first_sector.find('span').get_text()	#strip away html tags and only get the inner text
print(sector_change)

#construct the tuple
sector_data=(sector_name,sector_change,link)
print(sector_data)

# Look for a pattern in the table that gives us the relevant sector details
# Remember, we're only interested in sector name, change, and the link to the detail page!

# Looks like the detail we're interested in is in rows 1, 4, 7, 10, etc.
# Generate a range object for these rows

row_identifier = range(1,len(sector_table),3)
print(list(row_identifier))

# Now let's iterate through the table pulling out the name, the change, and the link
# and putting this together in a list

sector_changes=list()
for index in row_identifier:
    sector_detail=sector_table[index]
    sector_name=sector_detail.find('a').get_text()
    sector_link=sector_detail.find('a').get('href')
    sector_link='http://www.google.com'+sector_link
    sector_change=sector_detail.find('span').get_text()    
    sector_changes.append((sector_name,sector_link,sector_change))
print(sector_changes)