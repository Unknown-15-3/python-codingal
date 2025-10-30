from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Top a Window")

def toplevel():
    top = Toplevel()
    top.geometry("100x100")
    top.title("top level")
    l2 = Label(top, text = "This is a top level window")
    l2.pack()
    top.mainloop()
l = Label(root, text = "this root window")
btn = Button(root, text = "click here to open another window", command=toplevel)

l.pack()
btn.pack()
root.mainloop()