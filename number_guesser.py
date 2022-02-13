# - Author: Brennan Adams

from math import ceil
import random

#lower and upper bounds of random function
ceiling = 15
floor = 0

#asking for generating a random int and getting user input
randomNum = random.randint(floor, ceiling)

userInput = int(input("Guess a number between " + str(floor) + " and " + str(ceiling) + " : "))
numAttempts = 1

#check if user entered in range
while(userInput > ceiling or userInput < floor):
    print()
    userInput = int(input("Please enter a value between " + str(floor) + " and  " + str(ceiling)+ " : "))



#while loop to keep asking for input untill user guesses number
while(userInput != randomNum):

    #user guessed number
    if userInput == randomNum:
        print("You guessed the random number!")
    
    #input is lower than random number
    elif userInput < randomNum:
        print("Higer")
        numAttempts += 1
    #input is higher than random number
    else:
        print("Lower")
        numAttempts += 1
    
    userInput = int(input("Try entering a new number : "))
    


print("\n Game finished! \n You finished in " + str(numAttempts) + "\n")




