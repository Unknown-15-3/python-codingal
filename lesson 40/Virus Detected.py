from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus Detected")
window.geometry("200x200")

def message():
    messagebox.showwarning("Alert!" , "\n An virus is detected in your systemt")

button = Button(window, text="scan for virus", command=message)
button.place(x = 40, y = 50)
button.pack()

window.mainloop()