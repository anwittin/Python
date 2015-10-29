import time

print("First Drill")
print("Let's see how long you have lived in days, minutes and seconds.")

name = input("Name: ")
print("Please enter your age")
age = int(input("age: "))

days = age * 365
minutes = age * 525948
seconds = age * 31556926

print(name, "has been alive for", days,"days", minutes, "minutes", seconds,"seconds!")
time.sleep(1.5)
print("Second drill")

x = list(range(4))
print("First range:")
for i in x: print(i)

y = list(reversed(range(4)))
print("Second range:")
for i in y: print(i)
	
z = list(reversed(range(2, 10, 2)))
print("Third range:")
for i in z: print(i)