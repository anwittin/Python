import json
import urllib

input = raw_input('Please Enter a URL: ')
uh = urllib.urlopen(input)
data = uh.read()
info = json.loads(data)


for item in info:
    print 'Count: ', item
