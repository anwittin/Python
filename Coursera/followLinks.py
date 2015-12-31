# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter the count: '))
pos = int(raw_input('Enter the position: '))


# Retrieve the specific links from a page


while count > 0:
   html = urllib.urlopen(url).read()
   soup = BeautifulSoup(html)
   tags = soup('a')[pos-1:pos]
   for tag in tags:
       href = tag.get('href', None)
       url = href
       tag = tag.get('href',None)
   print "Retrieving: %s" % tag
   count = count - 1

