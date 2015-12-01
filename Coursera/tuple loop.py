name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()

for line in fh:
	if not line.startswith("From ") : continue
	tmp = line.split()[5:6]
	w = ''.join(tmp).split(':')
	words = w[0:1]
	for word in words:
		w = counts[word] = counts.get(word, 0) +1
	for v,k in w [:10] :
		print sorted( [(k,v) for k,v in counts.items() ])

print sorts[1:-1]
# lst = list()
# for k,v in counts.items():
	# lst.append((v,k))
# lst.sort(reverse=True)
# for v,k in lst[:10] :
	# print sorted([(v, k) for k,v in counts.items()] )
