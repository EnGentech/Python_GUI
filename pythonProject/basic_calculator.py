from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def btn_click(number):
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(number))


def btn_clear():
    e.delete(0, END)


def btn_add():
    fnum = e.get()
    global fstNum
    fstNum = int(fnum)
    e.delete(0, END)


def btn_equal():
    curNum = e.get()
    e.delete(0, END)
    e.insert(0, fstNum + int(curNum))

btn1 = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
btn2 = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
btn3 = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))
btn4 = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
btn5 = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
btn6 = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))
btn7 = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
btn8 = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
btn9 = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))
btn0 = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
btn_plus = Button(root, text="+", padx=39, pady=20, command=btn_add)
btn_clr = Button(root, text="Clear", padx=77, pady=20, command=btn_clear)
btn_eq = Button(root, text="=", padx=86, pady=20, command=btn_equal )


btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn0.grid(row=4, column=0)
btn_clr.grid(row=4, column=1, columnspan=2)
btn_plus.grid(row=5, column=0)
btn_eq.grid(row=5, column=1, columnspan=2)

root.mainloop()
