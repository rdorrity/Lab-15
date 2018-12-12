# Nathan Warren-Acord, Ryan Dorrity
# SCSI Logic
# CST 205 - Lab 15
# 12/6/2018
####################################

from random import randrange
from calendar import *
from datetime import *

##Problem 1

##Function prompts user for input and exits if they request.
##Otherwise, it returns the result of two dice rolls added together.
def roll():
	turn = input("Press 'enter' to perform roll >>>", )
	if "exit" in turn:
		print("Goodbye!")
		raise SystemExit
	dice = randrange(1,7)+randrange(1,7)
	print("Your roll was: {}".format(dice))
	return dice


##Prints the text for winning
def victory():
	print ("You win!")
	raise SystemExit

##Prints the text for losing
def defeat():
	print ("You lose!")
	raise SystemExit

## Main loop for craps that checks roll() against the rules for craps.
## 7,11 on first roll = win. 2,3,12 on first roll = lose.
## Else, number is the point and player rolls until
## they roll the 'point' number (win) or a 7 (lose).
def craps():
	print("Let's play some craps!")
	point = roll()
	if point in [7,11]:
		victory()
	elif point in [2,3,12]:
		defeat()
	else:
		print ("\nThe point is: {}\n".format(point))
		while True:
			dice = roll()
			if dice is point:
				victory()
			elif dice is 7:
				defeat()

##Problem 2

##Function prints out the birthday of Nathan and the number
##of days until his next one.
##The date that the Declaration of Independence was ratified is
##printed in a whole sentence.
def cal_dates():

	print("")
	print (month(1988,4))
	today = date.today()
	bday = date(today.year,4,5)
	if bday < today:
		bday = bday.replace(year=today.year+1)
	print ("There are {} days until my next birthday.".format(abs(bday-today).days))
	print("")
	d_of_i = date(1776,7,4)
	print("The Declaration of Independence was ratified on {}".format(d_of_i.strftime("%A %B %d, %Y.")))

##Main function. Allows for choosing which function to run.
def main():

	userInput = input("\nWhich function to run?\n1. Craps game\n2. Calendar and dates\nPick: ",)
	if userInput is "1":
		craps()
	elif userInput is "2":
		cal_dates()
	else:
		print ("\nOkay then.")
		raise SystemExit

main()