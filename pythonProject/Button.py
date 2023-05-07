from tkinter import *

root = Tk()


def count():
    lbl = Label(root, text="This is a test")
    lbl.pack()


button = Button(root, text="Click me", padx=50, pady=10, command=count, fg="blue", bg="pink")
button.pack()

root.mainloop()