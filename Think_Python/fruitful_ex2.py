import math

def area(radius):
    temp = math.pi * radius**2
    return temp

def distance(x1, y1, x2, y2):
    dx = (x2 - x1)
    dy = (y2 - y1)
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    #print 'Result is: ', result
    return result

def circle_area(xc, yc, xp, yp):
    ca = area(distance(xc, yc, xp, yp))
    print 'The area of the circle is: ', ca
    return ca

circle_area(1,2,4,6)
