import urllib
import xml.etree.ElementTree as ET


url = raw_input('Enter URL: ')

uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
counter = 0
for count in counts:
    counters = int(count.find('count').text)
    counter += counters
print counter
