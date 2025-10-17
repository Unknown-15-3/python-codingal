from tkinter import *

root = Tk()
root.title("Login App")
root.geometry("400x400")

frame = Frame( master= root, height= 200, width= 300, bg = "yellow")

Ibl1 = Label(frame, text = "Full Name:- ", bg = "orange", fg = "black", width= 12)
Ibl2 = Label(frame, text = "enter Email ID:- ", bg = "pink", fg = "black", width= 12)
Ibl3 = Label(frame, text = "enter password:- ", bg = "red", fg = "black", width= 12)

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show = "*")

def display():
    name = name_entry.get()
    greet = "hiya !!" + name
    Message = "\n congratulations, you have successfully made a new account"
    textbox.insert(END, greet + Message)

textbox = Text(bg = "light blue", fg = "black")

btn = Button(text = "create a new account", command=display)

frame.place(x = 20, y = 0)
Ibl1.place(x = 20, y = 20)
name_entry.place(x = 150, y = 20)
Ibl2.place(x = 20, y = 80)
email_entry.place(x = 150, y = 80)
Ibl3.place(x = 20, y = 140)
password_entry.place(x = 150, y = 140)

btn.place(x = 130, y = 210)
textbox.place(y = 250)

root.mainloop()