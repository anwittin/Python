# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter Website: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

spans = soup('span')
sum = 0
for span in spans:
    spn = int(span.renderContents())
    sum = spn + sum
   
    
print sum