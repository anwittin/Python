largest = None
smallest = None
while True:
    
    num = raw_input("Enter a number: ")
    try:
        num = int(num)
    except:
        print "Invalid input"
    if num == "done" : break
    if smallest is None or num < smallest:
        smallest = num
        
    if largest is None or num > largest:
        largest = num
        
       
    print num
    

print "Maximum", largest
print "Minimum", smallest