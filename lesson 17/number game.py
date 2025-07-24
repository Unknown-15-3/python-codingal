import random

playing = True

number = str(random.randint(10,20))

print("Hello! welcome!!")
print("lets play a cool game!")
print("I will generate number between 10 to 20 and you have to guess the correct number!")
print("the games when u guess the answer correct or we continue to play it")

while playing:
    guess = input("enter your guess: ")
    if number == guess:
        print( "IS CORRECT! you have guess the number right" )
        break
    else:
        print("oh dear! you have guessed it wrong, try again!")