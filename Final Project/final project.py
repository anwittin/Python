from sys import exit
import time

def kitchen():
	print "This is the kitchen, there is food to cook and a small door at the back too."
	print "You're hungry. what do you do?"
	print "cook | enter door"
	
	choice = raw_input("> ").upper()
		
	if choice == 'cook':
		print "Nice, hopefully you know what you're doing!\n"
		print "Smells good, I hope you enjoy it"
		print "Here come the zombies!"
		dead("You shouldn't have started cooking...")
	else:
		print "Smart choice zombies like the smell of food."
		print "This door leads to a safe room."
		safe_room()
		
def front_room():
	print "You're in the living room, there is a body here."
	time.sleep(.75)
	print "The body looks worse for wear. It may be a zombie."
	time.sleep(.75)
	print "The body starts moving and is blocking the next room."
	time.sleep(.75)
	print "What are you going to do? Punch | Stab | Run"
	zombie_moved = False
	
	while True:
		choice = raw_input("> ").lower()
		
		if choice == "punch":
			dead("The zombie is fast and grabs you and eats your face.")
		elif choice == "stab": 
			print "The zombie takes the stabbing and keeps coming at you."
			print "What do you do now? Punch | Stab | Run"
		elif choice == "run":
			print "That was close!"
			safe_room()
		else:
			print "I got no idea what that means."
			
def bedroom_room():
	print "You are in a bedroom."
	time.sleep(.75)
	print "There is a bed, some clean clothes here and a closet."
	time.sleep(.75)
	print "What do you want to do? Sleep | Change | Closet | Cry "
	
	choice = raw_input("> ").lower()
	
	if "cry" in choice: 
		dead("Bummer, your tears brought the zombies.")
	elif "closet" in choice:
		safe_room()
	elif "change" in choice:
		tomorrow("A clean set of clothes helps win the smell battle.")
	elif "Sleep" in choice:
		dead("You gotta find a safer place to sleep!")
	else:
		print "Type Sleep | Change | Closet | Cry "
def safe_room():
	print "You found the safe room, with food, water and weapons."
	time.sleep(.75)
	print "Good job it looks like you may survive until tomorrow"
	time.sleep(.75)
	print "What do you want to do? Sleep | Eat | Equip weapons | Go Outside"
	while True:
		choice = raw_input("> ").lower()
		
		if choice == "sleep":
			tomorrow("Sleep until things get better")
		elif choice == "eat": 
			print "Nom Nom Nom"
			tomorrow("Full belly to fight again tomorrow")			
		elif choice == "equip weapons":
			print "You're a fighter!"
			tomorrow("Mount up")
		elif choice == "go outside":
			print "That was a bad idea :-/"
			dead("The zombies eat your brains.")
		else:
			print "I got no idea what that means."

def dead(why):
	print why,"Good job! You're a zombie now."
	print "Play again? Y / N"
	choice = raw_input("> ").upper()
	
	if choice == 'Y':
		start()
	else:	
		print "Thanks for playing"
		exit()
	
def tomorrow(why):
	print why, "\nWinner Winner not a zombie dinner!"
	print "Play again? Y / N"
	choice = raw_input("> ").upper()
	if choice == 'Y':
		start()
	else:	
		print "Thanks for playing"
		exit()
	
def start():
	print "You have just escaped from the zombies that are outside."
	print "There is a door to the north, east and west."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	if choice == "west":
		front_room()
	elif choice == "east":
		bedroom_room()
	elif choice == "north":
		kitchen()
	else:
		dead("You stumble around the room until you starve.")
			

start()
			