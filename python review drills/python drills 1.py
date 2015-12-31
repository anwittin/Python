#1. Write a Python program to print the following string in a specific format (see the output).
# print "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are"

#2. Write a Python program to get the Python version you are using.
# import sys
# print "Python Version : %s" % (sys.version)

#3. Write a Python program to display the current date and time.
# import datetime
# time = datetime.datetime.now()
# print "Current Date and Time : % s" % (time.strftime("%Y-%m-%d %H:%M:%S"))

#4. Write a Python program which accept the radius of a circle from the user and compute the area.
# from math import pi
# number = float(raw_input("Enter the Radius: >>>  "))
# radius = pi*(number**2)
# print radius

#5. Write a Python program which accept the user's first and last name and print them in reverse order with a space between them.
# fName = str(raw_input("Enter Your First Name : "))
# lName = str(raw_input("Enter Your Last Name : "))
# print "Hello %s %s!" %(lName, fName)

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# uList = str(raw_input("Please enter a list of numbers : ")).split(",")
# listy = list(uList)
# tupley = tuple(uList)
# print "Heres your numbers in a list: {} and a tuple: {}".format(listy, tupley)

#7. Write a Python program to accept a filename from the user print the extension of that.
# extention = raw_input("Please enter the filename: ")
# split = extention.split(".")
# print "Here is the file extension : %s" % repr(split[-1])

#8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print "%s %s" %(color_list[0],color_list[-1])

#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#exam_date = (11, 12, 2014)
#print "Exam date is %i/%i/%i. " %(exam_date)

#10. Write a Python program that accept an integer (n) and computes the value of n+nn+nnn.
# uNumber = int(raw_input("Please enter a number : "))
# n1 = int("%s" % uNumber)
# n2 = int("%s%s" % (uNumber,uNumber))
# n3 = int("%s%s%s" % (uNumber,uNumber,uNumber))
# print n1+n2+n3

#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
#print(abs.__doc__)

#12. Write a Python program to print the calendar of a given month and year.
# import calendar
# year = int(raw_input("please enter a year: "))
# month = int(raw_input("Please enter a month: "))
# print calendar.month(year, month)

#13. Write a Python program to print the following here document.
# print("""
# a string that you "don't" have to escape
# This
# is a  ....... multi-line
# heredoc string --------> example
# """)

#14. Write a Python program to calculate number of days between two dates.
# from datetime import date
# f_date = date.today()
# l_date = date(2016, 8, 20)
# delta = l_date - f_date
# print "Days between today and my Birthday is %s" % (delta.days)

#15. Write a Python program to get the volume of a sphere with radius 6.
# import math 
# radius = 6.0
# volume = 4.0/3.0*math.pi* radius**3
# print 'The volume of the sphere with radius %i is: %f ' %(radius,volume)

#16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

# def difference(n):
    # if n <= 17:
        # return 17 - n
    # else:
        # return (n - 17) * 2 
# num = int(raw_input("Please enter a number:> "))
# print "You chose %i there is a difference between 17 that is : %i " % (num, difference(num))

#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
# def near_thousand(n):
      # return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print "test whether a number is within 100 of 1000 or 2000."
# print "1000", near_thousand(1000)
# print "900", near_thousand(900)
# print "800", near_thousand(800)
# print "2200", near_thousand(2200)

#18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum. 
# def sum_thrice(x, y, z):

     # sum = x + y + z  
     # if x == y == z:
      # sum = sum * 3
     # return sum
# print"calculate the sum of three given numbers, if the values are equal then return thrice of their sum."
# print"Numbers 1, 2, 3 : ", sum_thrice(1, 2, 3)
# print"Numbers 3, 3, 3 : ", sum_thrice(3, 3, 3)

#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
# def new_string(str):
  # if len(str) >= 2 and str[:2] == "Is":
    # return str
  # return "Is" + str
# print(new_string("Array"))
# print(new_string("IsEmpty"))

#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# def larger_string(str, n):
   # result = ""
   # for i in range(n):
      # result = result + str
   # return result

# print(larger_string('supercalifragilisticexpialidocious', 2))
# print(larger_string('.py', 3))

#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
# num = int(raw_input("Please enter a positive number: "))

# def isEvenOrOdd(num):
    # if num % 2 == 0:
        # print "your number is even"
    # else:
        # print "your number is odd"
# isEvenOrOdd(num)

#22. Write a Python program to count the number 4 in a given list.
# def list_count_4(nums):
  # count = 0  
  # for num in nums:
    # if num == 4:
      # count = count + 1
  # return count

# print"There are %i 4's in this list" %(list_count_4([1, 4, 6, 7, 4]))
# print"There are %i 4's in this list" %(list_count_4([1, 4, 6, 4, 7, 4]))

#23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given sting. Return the n copies of the whole string if the length is less than 2.
# def substring_copy(str, n):
  # flen = 2
  # if flen > len(str):
    # flen = len(str)
  # substr = str[:flen]
  # result = ""
  # for i in range(n):
    # result = result + substr
  # return result
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3));

#24. Write a Python program to test whether a passed letter is a vowel or not. 
#entry = str(raw_input("Please enter a letter: "))

# def vowelOrCons(entry):
    # vowel = 'aeiou'
    # if entry in vowel:
        # print "%s is a vowel" % entry
    # else: 
        # print "%s is not a vowel" % entry
# vowelOrCons(entry)

#25. Write a Python program to check whether a specified value is contained in a group of values.
#fNum = int(raw_input("Please enter a number between 1 - 50: "))
# pNum = int(raw_input("Please enter your favorite number: "))
#list = range(fNum)
# def containedIn(n, set):
    # if n in set:
        # print "The number %i was found in the set %r True" %(n,set)
    # else: 
        # print "The number %i was not found in the set %r False" %(n, set)
# containedIn(pNum, list)
# #containedIn(-1, [1,5,8,3])

#26. Write a Python program to create a histogram from a given list of integers.

# def histogram( items ):
    # for n in items:
        # output = ''
        # times = n
        # while( times > 0 ):
          # output += '*'
          # times = times - 1
        # print(output)
# histogram(list)

#27. Write a Python program to concatenate all elements in a list into a string and return it.
# def concatenate_list_data(list):
    # result= ''
    # for element in list:
        # result += str(element)
    # return result
# print(concatenate_list_data([1, 5, 12, 2]))

# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
# numbers = [    
    # 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    # 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    # 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    # 958,743, 527
    # ]
# for x in numbers:
    # if x == 237:
        # break
    # elif x % 2 == 0:
        # print(x)

#29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# print color_list_1.difference(color_list_2)

#30. Write a Python program that will accept the base and height of a triangle and compute the area.
# b = int(raw_input("Input the base : "))
# h = int(raw_input("Input the height : "))
# area = b*h/2
# print"area = ", area

#31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
# x = int(raw_input("Enter a number: "))
# y = int(raw_input("Enter a number: "))

# def gcd(x, y):
    # gcd = 1
    
    # if x % y == 0:
        # return y
    
    # for k in range(int(y / 2), 0, -1):
        # if x % k == 0 and y % k == 0:
            # gcd = k
            # break  
    # print "The greatest common denominator is %i" % gcd
# gcd(x, y)

#32. Write a Python program to get the least common multiple (LCM) of two positive integers.
# x = int(raw_input("Enter a number: "))
# y = int(raw_input("Enter a number: "))

# def lcm(x, y):
   # if x > y:
       # z = x
   # else:
       # z = y

   # while(True):
       # if((z % x == 0) and (z % y == 0)):
           # lcm = z
           # break
       # z += 1
   # print "The least Common multiple is %i" % lcm
# lcm(x, y)

#33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
# x = int(raw_input("Enter a number: "))
# y = int(raw_input("Enter a number: "))
# z = int(raw_input("Enter a number: "))

# def sum(x, y, z):
    # if x == y or y == z or x==z:
        # sum = 0
    # else:
        # sum = x + y + z
    # print "The sum of your three numbers is: %i, if you duplicated any number the result will be 0" % sum
# sum(x, y, z)

#34. Sum of two given integers. However if the sum is between 15 to 20 it will return 20.
# x = int(raw_input("Enter a number: "))
# y = int(raw_input("Enter a number: "))
# def sum(x, y):
    # sum = x + y
    # if sum in range(15, 20):
        # print "Your numbers are in the range of 15-20 the result is always %i" % 20
    # else:
        # print "Your number is out side the range of 15-20 the result is: %i" % sum
# sum(x,y)

#35. Return true if the two given integer values are equal or their sum or difference is 5.
# x = int(raw_input("Enter a number: "))
# y = int(raw_input("Enter a number: "))
# def number5(x, y):
    # if x == 5 or y == 5 or abs(x-y) == 5 or (x+y) == 5:
        # print "Your numbers are 5 or the difference or sum is 5: %s" % True
    # else:
        # print "Your numbers are 5 or the difference or sum is 5: %s" % False
# number5(x,y)

#36. Add two objects if both objects are integer type.
# x = raw_input("Enter a number: ")
# y = raw_input("Enter a number: ")
# try:
    # sum = int(x+y)
    # print "The sum of your numbers is: %i" % sum
# except:
    # print "You did not enter numbers."

#37. Display your details like name, age, address in three different lines.
# name = raw_input("Enter your name: ")
# age = int(raw_input("Enter your age: "))
# address = raw_input("Enter your address: ")
# print "Hello %s\nyour age is %i\nyour address is %s\n" %(name, age, address)

#38. Solve (x + y) * (x + y).
# x = raw_input("Enter a number: ")
# y = raw_input("Enter a number: ")
# try:
    # x = int(x)
    # y = int(y)
    # sum = (x+y)*(x+y)
    # print "The total of (%i+%i) * (%i+%i) is: %i" %(x,y,x,y,sum)
# except:
    # print "Please enter numbers"

#39. Compute the future value of a specified principal amount, rate of interest, and number of years.
# amt = float(raw_input("Please enter a dollar amount: "))
# int = 3.5
# years = 7
# future_value  = amt*((1+(0.01*int)) ** years)
# print "The future value of $%.2f is: $%.2f" % (round(amt,2), round(future_value,2))

#40. Compute the distance between the points (x1, y1) and (x2, y2).
# from math import sqrt

# x1 = int(raw_input("Enter x1: "))
# y1 = int(raw_input("Enter y1: "))
# x2 = int(raw_input("Enter x2: "))
# y2 = int(raw_input("Enter y2: "))
# d = sqrt(((x2-x1)**2) + (((y2-y1)**2)))
# print "The distance between those points is %.11f" % d

