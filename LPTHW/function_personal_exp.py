def checkForMoney(money_earned, money_spent, savings_goal):
	print "You have earned $ %d this month." % money_earned
	print "You have $ %d as a savings goal." % savings_goal
	print "You spent $ %d this month" % money_spent
	savings = (money_earned - money_spent)	
	print "To reach your goal of $ %d we need to save extra money every month" % savings_goal
	print "You currently have $ %d that you can put in savings" % savings
	
		
print "Here is your monthly stats:"
checkForMoney(2000, 1500, 10000)

