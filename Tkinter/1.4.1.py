import tkinter

root = tkinter.Tk()

root.title("キャンバス")

root.geometry("640x480")

canvas = tkinter.Canvas(root, width=640, height=480, bg="skyblue")
canvas.place(x = 0, y = 0)

#canvas pack()

gazou = tkinter.PhotoImage(file="./img/hebi.png")
canvas.create_image(320, 240, image=gazou)

root.mainloop()



