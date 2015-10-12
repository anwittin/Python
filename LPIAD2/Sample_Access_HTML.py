import urllib2, progressbar, csv, os, time
from bs4 import BeautifulSoup
from progressbar import Bar, ProgressBar, Percentage

# The path to the script
currentPath = os.path.dirname(os.path.abspath("__file__"))

# make the spreadsheet
outputCsv = currentPath + '/members.csv'

# open the file
csvFile = open(outputCsv, "wb")

# Create writer object
writer = csv.writer(csvFile, delimiter=',')


def extractMData(webpage):
    soup = BeautifulSoup(webpage, "html.parser")

    # Find all the div blocks
    divBlock = soup.findAll("div", {"class": "block"})
    info = divBlock[3]
    # Extract info_left and info_right divs
    getLeft = info.findAll("div", {"class": "info_left"})
    getRight = info.findAll("div", {"class": "info_right"})
    getLeftArr = []
    getRightArr = []

    for i in range(0, len(getLeft)):
        textLeft = getLeft[i].get_text()
        textRight = getRight[i].get_text()
        getLeftArr.append(textLeft)
        getRightArr.append(textRight)
    return [getLeftArr, getRightArr]


# Open Webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

# Convert to BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

# Show the HTML Code from the a webpage
# print soup.title
# print soup.body

# Get the contents of container div
divContainer = soup.find("div", {"id": "container"})
divBlock = divContainer.findAll("div", {"class": "block"})
divSep = divBlock[3].findAll("div", {"class": "separator"})
members = divSep[3].findAll("a")

nMembers = len(members)
bar = ProgressBar(widgets=[Percentage(), Bar()], maxval=nMembers).start()
for i in range (nMembers):
	time.sleep(0.01)
	bar.update(i+1)
bar.finish()


count = 0

# Loop through members
for member in members:
    # Strip <a> tags
    href = member.get("href")
    # Create url Open
    url = "http://inadaybooks.com/justiceleague/" + href
    # Open the url
    mPage = urllib2.urlopen(url)


    data = extractMData(mPage)
    if count == 0:
        writer.writerow(data[0])

    writer.writerow(data[1])


    # Increment count
count += 1

    # Update progress bar
bar.update(count)
