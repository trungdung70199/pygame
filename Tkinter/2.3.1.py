import tkinter
root = tkinter.Tk()
root.title("frame")
root.geometry = "Meiryo"

frame1 = tkinter.Frame(root,)
frame2 = tkinter.Frame(root,)

canvas1 = tkinter.Canvas(frame1, width=320, height=300, bg="blue")
canvas1.pack()

canvas2 = tkinter.Canvas(frame2, width=320, height=300, bg="yellow")
canvas2.pack()

button1 = tkinter.Button(frame1, text="ボタン1", width=10, height=2)
button1.pack()

button2 = tkinter.Button(frame2, text="ボタン2", width=10, height=2)
button2.pack()

frame1.grid(column=0, row=0)
frame2.grid(column=1, row=0)

root.mainloop()



