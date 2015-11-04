import math

def hypotenuse(x1, y1):
	a2 = x1**2
	b2 = y1**2
	hsquared = math.sqrt(a2+b2)
	print 'the hypotenuse of your right triangle is: ', hsquared
	
	return hsquared
hypotenuse(9, 6)