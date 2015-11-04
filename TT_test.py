def add_list(num):
	x = 0
	for items in num:
		x += items
	print(x)
	return x
add_list([1, 2, 3])

def summarize(num):
	x=0
	for items in num:
		x += items
	print("The sum of {} is {}.".format(num, x))
	
summarize([1, 2, 3])
	