"""
	Python calculator

"""

from tkinter import *

root = Tk()
root.geometry("500x250+400+200")
root.iconbitmap('youtube.png')
root.title("Python GUI Calculator")

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)

text = ""
expr = StringVar()

Entry(root, background="gray", foreground="white", textvariable=expr).pack(fill=BOTH, ipady=5)


def addnum(num):
	global text
	text += num
	expr.set(text)

def calculate():
	global text
	result = str(eval(expr.get()))
	text = result
	expr.set(text)

def clear():
	global text
	text = ""
	expr.set(text)

Button(frame1, text="7", background="skyblue", command=lambda: addnum('7')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame1, text="8", background="skyblue", command=lambda: addnum('8')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame1, text="9", background="skyblue", command=lambda: addnum('9')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame1, text="+", background="#ff8", command=lambda: addnum('+')).pack(expand=1, fill=BOTH, side=LEFT)


Button(frame2, text="4", background="skyblue", command=lambda: addnum('4')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame2, text="5", background="skyblue", command=lambda: addnum('5')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame2, text="6", background="skyblue", command=lambda: addnum('6')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame2, text="-", background="#ff8", command=lambda: addnum('-')).pack(expand=1, fill=BOTH, side=LEFT)

Button(frame3, text="1", background="skyblue", command=lambda: addnum('1')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame3, text="2", background="skyblue", command=lambda: addnum('2')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame3, text="3", background="skyblue", command=lambda: addnum('3')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame3, text="*", background="#ff8", command=lambda: addnum('*')).pack(expand=1, fill=BOTH, side=LEFT)

Button(frame4, text="0", background="skyblue", command=lambda: addnum('0')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame4, text=".", background="#ff8", command=lambda: addnum('.')).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame4, text="C", background="coral", command=clear).pack(expand=1, fill=BOTH, side=LEFT)
Button(frame4, text="/", background="#ff8", command=lambda: addnum('/')).pack(expand=1, fill=BOTH, side=LEFT)

Button(frame5, text="=", background="lightgreen", command=calculate).pack(expand=1, fill=BOTH, side=LEFT)

frame1.pack(fill=BOTH, expand=1)
frame2.pack(fill=BOTH, expand=1)
frame3.pack(fill=BOTH, expand=1)
frame4.pack(fill=BOTH, expand=1)
frame5.pack(fill=BOTH, expand=1)
root.mainloop()