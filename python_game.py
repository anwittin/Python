nice = 0
mean = 0

def main():
    start()

def start():
    print "Hellp and welcome to nice or mean!"
    name = raw_input("What's your name? : ")
    print "Hi and welcome, "+name+"!"
    print "In this game, you will be greeted by several different people, you can be nice or mean."
    print "At the end of the game, your fate will be determined by how you treated people."

    choice = raw_input("Do you want to play? y / n ")
    if choice == "y":
        print "Great, use 'm' for mean or 'n' for nice"
        begin()

    if choice == "n":
        print "Okay Bye!"

def begin():
    global nice
    global mean

    if nice > 2:
        print "Nice job - you win! yay "
        
        choice = raw_input("Do you want to play again? y / n ")

        if choice == "y":
            print "Okay lets go!"
            nice = 0
            mean = 0
            begin()
            
        if choice == "n":
            print "Say no more"
            exit()

    if mean > 2:
        print "Too bad - game over!"

        choice = raw_input("Do you want to play again y / n ")

        if choice == "y":
             print "Okay lets go!"
             mean = 0
             nice = 0
             begin()
         
        if choice == "n":
            print "See ya later"
            exit()
            
        elif choice != "y"+"n":
            print "Please enter y or n"

            if choice == "y":
                begin()
            if choice == "n":
                print "See ya later"
                exit()
            if choice != "y"+"n":
                choice = raw_input("Do you want to play? y / n ")
    pick = raw_input("Someone approaches to talk. will you be nice or mean? n / m ")

    if pick == "n":
            print "They simle, wave and walks away."
            nice = nice+1
            print "You currently have " +str(nice) + " nice."
            begin()
    if pick == "m":
        print "They frown and punch you."
        mean = mean+1
        print "you currently have " +str(mean) + " mean."
        begin()

start()
