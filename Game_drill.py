import time
import random
apples = 0
gold = 0

def start():
	print("Hello and welcome!")
	name = input("What's your name: ").title()
	print("Welcome, {}!".format(name))
	print("The object of this game is to collect apples.")
	print("After collecting the apples you sell them")
	choice = input("Do you want to play Y/N \n:>").upper()
	if choice == "Y":
		begin()
	if choice == "N":
		print("Okay Seeya!")
def begin():
	global apples
	global gold
	
	print("Let's get started!")
	pick = input("Do you want to pick an apple Y/N?\n:>").upper()
	if gold > 99:
		print("You won the game!")
		play = input("Do you want to play again? Y/N\n:>").upper()
		if play == "Y":
			begin()
		else:
			print("Congrats, Have a good day!")
	
	if pick == "Y":
		#time.sleep(.1)
		print("You pick an apple.")
		apples += 1  
		print("You currently have, {} apples".format(apples))
		begin()
	if pick == "N":
		sell = input("Do you want to sell your apples? Y/N\n:>").upper()
		if sell == "Y":
			print("You currently have, {} apples".format(apples))
			print("You've sold you apples.")
			randnum = random.randrange(25)
			gold = apples *randnum
			apples = 0
			print("The current market value of apples is {} gold.".format(randnum))
			print("You now have {} gold".format(gold))
	if gold >= 99:
		gold = 0
		print("You won the game!")
		play = input("Do you want to play again? Y/N\n:>").upper()
		if play == "Y":
			begin()
		if play == "N":
			print("Congrats, Have a good day!")
			
	elif gold <= 98:  
		play = input("Bummer not enough gold to win try again? Y/N\n:>").upper()
		if play == "Y":
			begin()
		if play == "N":
			print("Okay Seeya!")
			
start()