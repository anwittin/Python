#Function to compute rates at normal time and overtime.
def computepay(h,r):
    otp = 0
    oth = 0
    reg = 0
           
    if h > 40:
       (h-40)+(r+(r/2))+(40*r)
            
    elif h < 40:
        return h*r
        

           

#Prompt user for hours and pay
hrs = float(raw_input("Enter Hours:"))
pay = float(raw_input("Enter Pay:"))

p = computepay(hrs,pay)
print "Pay",p
