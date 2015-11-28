hrs = raw_input("Enter Hours:")
h = float(hrs)

pay = raw_input("Enter Pay:")
p = float(pay)

if hrs > 40:
	print (h - 40) * (p + (p/2)) + 40*p
elif hrs < 40:
    print h*p