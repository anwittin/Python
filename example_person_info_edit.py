name = 'Tony Wittinger'
age = 38 
height = 71 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Very little'.lower()

def heightConvert(x):
	heightCM = height * 2.54
	return heightCM
def KgConvert(x):
	weightKg = weight / 2.2
	return weightKg
	
def stoneConverter(x):
	weightSt = weight / 14
	return weightSt


print "Let's talk about %s." % name
print "He's %d inches tall, which is %d centmeters" %(height, heightConvert(height))
print "He's %d pounds, %d kilograms or %d stone." %(weight, KgConvert(weight), stoneConverter(weight))
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try and get it exactly right

print "If I add %d, %d and %d I get %d." %(age, height, weight, age + height + weight)
