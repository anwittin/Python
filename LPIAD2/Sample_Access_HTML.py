import urllib2
from bs4 import BeautifulSoup

def extractMData(webpage):
    soup = BeautifulSoup(webpage, "html.parser")
    print soup.title

# Open Webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")
soup = BeautifulSoup(webpage, "html.parser")

# Show the HTML Code from the a webpage
# print soup.title
# print soup.body

# Get the contents of container div
divContainer = soup.find("div", {"id":"container"})
divBlock = divContainer.findAll("div", {"class":"block"})
divSep = divBlock[3].findAll("div", {"class":"separator"})
members = divSep[3].findAll("a")

# Loop through members
for member in members:
    #Strip <a> tags
    href = member.get("href")
    # Create url Open
    url = "http://inadaybooks.com/justiceleague/" +href
    # Open the url
    mPage = urllib2.urlopen(url)
    extractMData(mPage)
    # print member.get("title")
    # print member.get("href")


# print divContainer
