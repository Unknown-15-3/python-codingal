import random

options = ["rock", "paper", "scissors"]

userchoice = input("enter your choice (rock, paper, scissors):")

computerchoice = random.choice(options)
print("your choice is:"  ,userchoice)
print("computer's choice is:" , computerchoice)

if userchoice == computerchoice:
    print("It is a.. TIE!")
elif (userchoice == "rock" and computerchoice == "scissors"):
    print("YOU ARE THE WINNER! rock always bears scissors")
elif (userchoice == "paper" and computerchoice == "rock"):
    print(" YOU ARE THE WINNER! paper always tend to cover rock in occasions")
elif (userchoice == "scissors" and computerchoice == "paper"):
    print("YOU ARE THE WINNER! scissors always cut paper")
else:
    print("YOU LOOSE!!!" + computerchoice + " many times beats " + userchoice + " but you can always try again! ") 