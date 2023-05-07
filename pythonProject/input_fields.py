from tkinter import *

root = Tk()

def name():
    brand = ", this is EnGentech programming Lessons"
    lbl = Label(root, text="Hello " + e.get() + brand)
    lbl.pack()


e = Entry(root, width=50, bg="grey", fg="red", borderwidth=5)
e.pack()
e.insert(0, "Enter your Name:")

btn = Button(root, padx=50, text="Click me", command=name)
btn.pack()

root.mainloop()