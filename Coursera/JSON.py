import json
import urllib

input = urllib.urlopen('http://python-data.dr-chuck.net/comments_200791.json')
data = input.read()
try: info = json.loads(str(data))
except: info = None
count = 0
total = 0
for item in info['comments']:
    count = count+1
    total += item['count']
print 'Count: ', count
print 'Sum: ', total
