# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Matthew Powell
# Creation Date: 29 July 2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time #These two imports could share one line (import random, time). This works, but usually a second import implies that the second line is a custom import.

def displayIntro(): #Syntax error; triple commas is used for multiline comments; use ' or " in the print() function, or adding comments could be impossible.
	print('''You are in a land full of dragons. In front of you, 
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = '' # Syntax error; spacing methods must be consistent, and this is indented with 4 spaces, instead of a tab like everything else.
	while cave != '1' and cave != '2': 
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves # This is a spelling error. "caves" is different from "cave", defined above

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3) # Logic error; this is set for 3 seconds, not 2
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!' # Syntax error; print() is missing the parentheses

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y': #Syntax Error; there should be two = signs (playAgain ==)
	displayIntro()
	caveNumber = choosecave() #Logic error; it should be 'chooseCave()'
	checkCave(caveNumber)  # Line 47 and 48 use "caveNumber" instead of "chosenCave", as defined in the "checkCave()" function. It works, but it does not read well.
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no": #Logic error; if user enters 'n' instead of 'no', the program will quit, without displaying exit message. Add 'or playAgain == 'n''.
		print("Thanks for planing") #Spelling error; "Thanks for playing."

