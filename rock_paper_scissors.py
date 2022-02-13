# Author - Brennan Adams

import random

#creating number of user and cpu choices
options = ["rock", "paper", "scissors"]

userScore = 0
cpuScore = 0
rounds = 0

print("Welcome to rock, paper, scissors!\n")


while True:
    userChoice = input("Type rock, paper, or scissors or Q to quit : ").lower()

    #if user wants to quit
    if userChoice == "q":
        break

    #if user enters invalid choice, keep asking for an input
    if userChoice not in options:
        continue


    cpuChoice = random.choice(options)

    print("\n CPU choose " + cpuChoice + "\n")
    #if they throw same choice
    if cpuChoice == userChoice:
        print("Draw!\n")
        continue

    #if cpu wins, checks all cases
    if (cpuChoice == "rock" and userChoice == "scissors") or (cpuChoice == "scissors" and userChoice == "paper") or (cpuChoice == "paper" and userChoice == "rock"):
        print("CPU wins \n")
        cpuScore += 1
    #user wins
    else:
        print("User wins! \n")
        userScore += 1

    print("Game Score\nUser score: " + str(userScore) + "\nCPU score: " + str(cpuScore) + "\n")

    #check if we have a winner
    if userScore == 3:
        print("User wins game!\n")
        break
    elif cpuScore == 3:
        print("CPU wins game!\n")
        break

print("\nGame Over\n")

        
    

