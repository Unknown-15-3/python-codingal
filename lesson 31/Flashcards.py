class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+' ( ' +self.meaning+ ' ) '
    
flash = []
print("welcome to the FLASHCARD APPLICATION ladies and gentlemen!!")

while (True):
    word = input("Enter the nsme you would like to add in your flashcards:- ")
    meaning = input("enter the meaning of the word you place in your flashcards:- ")

    flash.append(flashcards(word,meaning))
    option = int(input("enter 0, if you want to add another card or otherwise enter 1:-"))

    if(option):
        break

print("\n your flashcards:-")
for i in flash:
    print(">", i)