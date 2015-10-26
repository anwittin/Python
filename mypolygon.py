from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(turtle, length):
	for i in range(4):
		fd(turtle, length)
		lt(turtle)

#square(bob, 50)

def polygon(turtle, length, n):
	angle = 360 / n
	polyline(turtle, length, n, angle)
	
#polygon(bob, 25, 6)

def circle(turtle, r):
	arc(turtle, r, 360)

#circle(bob, 10)

def arc(turtle, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length /n
	step_angle = float(angle) /n
	polyline(turtle, length, step_angle)
	
	for i in range(n):
		fd(turtle, step_length)
		lt(turtle, step_angle)

def polyline(turtle, length, n, angle):
	
	for i in range(n):
		fd(turtle, length)
		lt(turtle, angle)
		
print bob
wait_for_user()