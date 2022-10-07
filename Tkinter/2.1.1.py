import tkinter

root = tkinter.Tk()

root.title("フレームの練習")
root.geometry("640x480")

frame1 = tkinter.Frame(root,)
frame2 = tkinter.Frame(root,)

canvas = tkinter.Canvas(frame1, width=600, heigth=240, bg="skyblue")
canvas.pack()

label = tkinter.label(frame1, text="!こんにちは！",font=('HGS創英角ﾎﾟｯﾌﾟ体', 40), bg="skyblue")
label.place(x=150, y=90)

canvas = tkinter.Cavas(frame2, width=600, heigth=240, bg="yellow")
canvas.pack()

label = tkinter.label(frame2, text="こんばんは！", font=('HGS創英角ﾎﾟｯﾌﾟ体',48), bg="skyblue")
label.place(x=150, y=90)

frame1.pack()
frame2.pack()

root.mainloop()
