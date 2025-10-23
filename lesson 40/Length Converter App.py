from tkinter import *

def i_to_c():
    inches = ent_inch.get()
    try:
        inches = float(inches)
        cen = inches * 2.54
        la1["text"]= f"{round(cen,2)}centimeter"
    except ValueError:
        la1["text"] = "please enter a valid number"

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

frame = Frame(master= root)
ent_inch = Entry(master = frame, width = 10)
lb2= Label(master= frame, text= "inches")
ent_inch.grid(row = 0, column = 0, sticky = "e" )
lb2.grid (row=0, column= 1, sticky= "w")

btn = Button(master= root, text = "convert", command= i_to_c)
la1 = Label(master = root, text = "centimeter")

frame.grid (row = 0, column = 0, padx =10)
btn.grid(row = 0, column= 1, pady = 10)

la1.grid(row = 0, column=2, padx=10)

root.mainloop()