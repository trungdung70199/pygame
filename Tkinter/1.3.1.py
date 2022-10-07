##1.3.1.py

import tkinter

root = tkinter.Tk()

root.title("Tkinterの練習")

root.geometry("640x480")

fontname = "Meiryo"

label = tkinter.Label(root,text="こんにちは！", bg="white",font=("System",48))

label.place(x=180,y=180)


button = tkinter.Button(root,text="ボタンを押してください", bg="white",font=("System",24))

button.place(x=150,y=280)

root.mainloop()
