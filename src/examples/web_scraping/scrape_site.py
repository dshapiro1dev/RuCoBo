# this example program will scrape a web site

# requests:  allows python to communicate with websites - lets grab the library
import requests

# beautiful soup: allows us to parse (decode) the contents we get
from bs4 import BeautifulSoup

# lets grab a wikipedia page on Yak
page = requests.get('https://en.wikipedia.org/wiki/Domestic_yak')
#page = requests.get('https://en.wikipedia.org/wiki/Yak_(disambiguation)')
contents = page.content

# next we pass it to our beautiful soup parser (yes its called beautiful soup)
soup = BeautifulSoup(contents, 'html.parser')

# page title
print(soup.title.string)

#for link in soup.find_all('a'):
#    print(link.get('href'))

# lets print out all the links that exist on the page
print("--------------------\n\n Going to print all the links now\n~~~~~~~~~~")
links = soup.find_all('link')
for xx in links:
    print(xx)

# lets print out all the text on the page
# the page is littered with \n - too many blank lines
alltext = soup.get_text()
print(alltext)

# now a bit of string fixing magic: lets import 're' which allows us to use regular expressions
import re
newfix = re.sub('\n+','\n',alltext)  # lets remove many \n chains - replace with single \n
print(newfix)

# lets find any mentions of odour on the page
smells = soup.find_all('odour')
print(smells)

# finally - print the entire page - its surprisingly complicated to make sense of
print(soup.prettify())

# how to use beautiful soup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/