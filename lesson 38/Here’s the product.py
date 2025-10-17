from tkinter import *
from datetime import date

window = Tk()
window.title("getting started with widgets")
window.geometry("400x500")

Ibl1 = Label(text= "enter the 1st number:-", fg = "black", bg= "white", height= 1, width= 300)
first_entry = Entry()

Ibl2 = Label(text= "enter the 2nd number:-", fg = "cyan", bg= "black", height= 1, width= 300)
second_entry = Entry()

def display():
    firstnum = first_entry.get()
    secondnum = second_entry.get()
    product = int(firstnum) * int(secondnum)
    text_box.insert(END, product)

text_box = Text(height= 3)
btn = Button(text = "multiply", command = display, height = 1 , bg = "purple", fg = "white")

Ibl1.pack()
first_entry.pack()
Ibl2.pack()
second_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()