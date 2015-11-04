import math

def factorial(n):
	if not isinstance (n, int):
		print 'Factorial is only defined for integers.'
		return None
	elif n < 0:
		print 'Factorial is not defined for negitive numbers.'
		return None
	space = ' ' * (4 * n)
	print space, 'factorial', n
	if n == 0:
		print space, 'returning 1'
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		print space, 'retunring', result
		return result
	
	
	
	
		
factorial(5)