from tkinter import *
from datetime import date

window = Tk()
window.title("getting started with widgets")
window.geometry("400x500")

Ibl = Label(text= "hey there", fg = "white", bg= "black", height= 1, width= 300)
name_label = Label(text = "Full name", bg = "green")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    Message = " welcome to the application ! \n today's date is :"
    greet = "hello " + name 
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

text_box = Text(height= 3)
btn = Button(text = "Begin", command = display, height = 1 , bg = "pink", fg = "blue")

Ibl.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()