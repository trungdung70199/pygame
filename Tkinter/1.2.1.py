##1.2.1.py

import tkinter

root = tkinter.Tk()

root.title("Tkinterの練習")

root.geometry("640x480")

label = tkinter.Label(root,text="Hello World!", bg="white",font=("System",48))

label.place(x=180,y=180)

root.mainloop()
