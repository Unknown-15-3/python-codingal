import random
class FruitQuiz:

    def __init__(self):
        self.fruits = {'apple': 'red',
                       'banana' : 'yellow',
                       'watermelon': 'green',
                       'grape': 'purple',
                       'orange': 'orange'}
    
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("what is the colour of {}?" .format(fruit))
            user_answer = input()
            if(user_answer.lower() == color):
                print("ue answer is correct!!")
            else:
                print("answer wrong!!")
            option = int(input("enter 0, if you want to try again or otherwise enter 1:-"))
            
            if(option):
                break

print("welcome to the FRUIT QUIZ! Lets check your knowledge about the fruits and their colours!!")
fq = FruitQuiz()
fq.quiz()