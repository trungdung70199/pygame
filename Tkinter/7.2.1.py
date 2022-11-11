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
root.mainloop()