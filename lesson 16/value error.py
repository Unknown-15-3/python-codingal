try:
    number = int(input("enter a number: "))
    print("the number entered is: ", number)
except ValueError as ve:
    print("exception is",ve)