# 迷路データの表示
import tkinter
from tkinter import messagebox
mx = 1
my = 5
yuka = 0
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

def paint(mx, my):
    global yuka, maze
    canvas.create_rectangle(80*mx, 80*my, 80*mx + 79, 80*my + 79 ,fill="pink")
    yuka = yuka + 1
    if yuka == 29:
        canvas.update()
        messagebox.showinfo("goal", "clear")
    else:
        maze[my][mx] = 1

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

canvas.create_image(80*mx + 40, 80*my + 40, image=img1, tag="img")

def left(event):
    global mx, my
    mx -= 1
    if maze[my][mx] == 0 :
        x = -80
        y = 0
        paint(mx+1, my)
        canvas.move("img", x, y)
    else:
        mx += 1
def right(event):
    global mx, my
    mx += 1
    if maze[my][mx] == 0 :
        x = 80
        y = 0
        paint(mx-1, my)
        canvas.move("img", x, y)
    else:
        mx -= 1
def up(event):
    global mx, my
    my -= 1
    if maze[my][mx] == 0 :
        x = 0
        y = -80
        paint(mx, my+1)
        canvas.move("img", x, y)
    else:
        my += 1
def down(event):
    global mx, my
    my += 1
    if maze[my][mx] == 0 :
        x = 0
        y = 80
        paint(mx, my-1)
        canvas.move("img", x, y)
    else:
        my -= 1
    return
    
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
root.mainloop()