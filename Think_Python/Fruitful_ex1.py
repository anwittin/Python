import math

def area(radius):
	temp = math.pi * radius**2
	return temp
	
#def absolute_value(x):
	#if x < 0:
	#	return -x
	#if x > 0:
	#	return x
	#if x == 0:
	#	return x
		
#def compare(x, y):
	#if x > y: 
	#	return 1
	#if x == y:
	#	return 0
	#if x < y:
	#	return -1
		
#print compare(3, 5)	

def distance(x1, y1, x2, y2):
		dx = (x2 - x1)
		dy = (y2 - y1)
		dsquared = dx**2 + dy**2
		print 'dsquared is: ', dsquared
		return 0.0
		
