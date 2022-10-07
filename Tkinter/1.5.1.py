import tkinter

root = tkinter.Tk()

root.title("キャンバス")

root.geometry("640x480")

canvas = tkinter.Canvas(root, width=640, height=480, bg="skyblue")

canvas.pack()

gazou = tkinter.PhotoImage(file="./img/hebi.png")
canvas.create_image(320, 240, image=gazou)

fontname = "System"
label = tkinter.Label(root,text="1からいくつまでの?, font=(fontname, 36), bg=skyblue")
label.place(x=240, y=100)

entry = tkinter.Entry(width=20, bd=2)
entry.place(x=280, y=95)

button = tkinter.Button(root, text="計算!", font=(fontname,24))
button.place(x=500, y=95)
root.mainloop()



