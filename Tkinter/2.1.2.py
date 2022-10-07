import tkinter
root = tkinter.Tk()
root.title("frame")
root.geometry("640x480")
fontname = "Meiryo"
frame1 = tkinter.Frame(root,)
frame2 = tkinter.Frame(root,)

canvas1 = tkinter.Canvas(frame1, width=600, height=240, bg="blue")
canvas1.pack()

canvas2 = tkinter.Canvas(frame2, width=600, height=240, bg="yellow")
canvas2.pack()

frame1.pack()
frame2.pack()

root.mainloop()


