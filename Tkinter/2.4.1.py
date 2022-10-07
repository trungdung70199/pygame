import tkinter
root = tkinter.Tk()
root.title("ボタンでフレームを移動1")

root.geometry = 

canvas1 = tkinter.Canvas(root, width=320, height=300, bg="blue")
canvas2 = tkinter.Canvas(root, width=320, height=300, bg="yellow")

button1 = tkinter.Button(root, text="ボタン1", width=10, height=2)
button2 = tkinter.Button(root, text="ボタン2", width=10, height=2)

canvas1.grid(column=0, row=0)
canvas2.grid(column=1, row=0)
button1.grid(column=0, row=1)
button2.grid(column=1,roww=1)

root.mainloop()



