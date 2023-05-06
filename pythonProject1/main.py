from tkinter import *
from tkinter.ttk import Style


window = Tk()
style = Style()
window.geometry("500x500")
window.title("Sorting Algorithm")


def printt():
    print("To be continued...")


def exit1():
    exit()


label1 = Label(window, text="Binary VS Linear search", highlightbackground="#053351",
               highlightthickness=2, width=24, font=("arial", 16, "bold"))
label1.place(x=90, y=53)

label2 = Label(window, text="email:", width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=130)

label3 = Label(window, text="Linear search took:", width=20, font=("arial", 10, "bold"))
label3.place(x=80, y=190)

label4 = Label(window, text="Binary search took:", width=20, font=("arial", 10, "bold"))
label4.place(x=80, y=250)

btn1 = Button(window, text="Submit", width=12, bg="brown", fg='white', command=printt)
btn1.place(x=150, y=380)

btn2 = Button(window, text="Exit", width=12, bg="brown", fg='white', command=exit1)
btn2.place(x=280, y=380)

window.mainloop()
