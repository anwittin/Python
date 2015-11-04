import math

def circle_area(xc, yx, xp, yp):
	radius = distance(xc, yc, xp, yp)
	result = area(radius)
	print result
	return result
	
circle_area(2, 3, 5, 6)
