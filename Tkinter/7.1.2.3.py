import tkinter

root = tkinter.Tk()
root.title("図形のキー移動")
root.geometry("640x480")

img = tkinter.PhotoImage(file = 'img/kurikuri_s.png')

canvas = tkinter.Canvas(root, bg="#fff", width=640, height=480)
canvas.pack()

canvas.create_oval(10,70,50,110, fill="#0fffff", tag="img")

def left(event):
    x = -10
    y = 0
    canvas.move("img", x, y)

def right(event):
    x = 10
    y = 0
    canvas.move("img", x, y)

def up(event):
    x = 0
    y = -10
    canvas.move("img", x, y)

def down(event):
    x = 0
    y = 10
    canvas.move("img", x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()