# 迷路データの表示
import tkinter

maze = [
[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,1,0,0,1],
[1,0,1,1,0,0,1,0,0,1],
[1,0,0,1,0,0,0,0,0,1],
[1,0,0,1,1,1,1,1,0,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]
]
root = tkinter.Tk()
root.title("迷路の表示")
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.pack()
for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill="gray")

img1 = tkinter.PhotoImage(file = 'img/kurikuri_s.png')

canvas.create_image(120, 440, image=img1, tag="img")

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