from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x400")
root.title("Demonination Calculator")
root.configure(bg = "light blue")

upload = Image.open("lesson 42/app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image = image,bg = "light blue" )
label.place(x =180, y = 20)

label1 = Label(root, text = "hey user! welcome to 'Denomination Calculator'", bg = "light green" )
label1.place (relx = 0.5, y = 10, anchor= CENTER)

def msg():
    msgbox = messagebox.showinfo("Aler!", "Do you wanna calculate the denomination count?")
    if msgbox == "ok":
        topwin()

button1 = Button(root, text = "click here to proceed", command = msg, bg = "brown")
button1.place(x = 250, y = 330)

def topwin():
    top = Toplevel()
    top.title("Denomination count")
    top.configure("light grey")
    top.geometry("400x300")

    label2 = Label(top, text = "Enter the amound", bg = "light grey")
    entry = Entry(top)
    lbl = label(top, text = "Denomination Count is:", bg = "light grey")

    l1 = Label(top, text = "2000", bg = "light grey")
    l2 = Label(top, text = "500", bg = "light grey")
    l3 = Label(top, text = "100", bg = "light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
     try:
        global amount

        amount = int(entry.get())
        note2000 = amount//2000
        amount %= 2000 
        note500 = amount//500
        amount %= 500
        note100 = amount//100
        amount %= 100 

        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)

        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
     except ValueError:
        messagebox.showerror("Invalid input", "please enter a valid amount")
    button2 = Button(top, text = "Calculate", command = calculate, bg = "light green")


    label.place(x=230, y= 50)
    entry.place(x=200, y = 80)
    lbl.place(x=140, y = 170)
    l1.place(x =180, y= 200)
    l2.place(x= 180, y = 230)
    l3.place(x = 180, y = 260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()