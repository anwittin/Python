
print("The sort function -- The easy way")
x = [67, 45, 2, 13, 1, 998]
print("The unsorted list: {}".format(x))
x.sort()
print("Now the sorted list: {}".format(x))

print("The sort function -- The hard way")
def sorted(x):
	x.sort()
	print("Now the sorted list: {}".format(x))

sorted(x)