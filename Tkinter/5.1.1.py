import tkinter
from turtle import distance

start_x = 60
start_y = 60
width_px = 5
height_px = 32
distance_px = 4

list = [70, 15, 66, 21, 19, 97, 33, 44, 30, 2]

def draw_graph():
    wl = list[0]
    x = start_x
    y = start_y
    color = "blue"
    canvas.create_rectangle(x, y, x + wl * width_px,
        y + height_px, fill=color, outline=color,
        tag="graph")
    canvas.create_text(x+wl*width_px+12, y+12, text=wl)

root = tkinter.Tk()
root.title("棒グラフ1")
root.resizable(False, False)
root.geometry("640x480")

canvas = tkinter.Canvas(root,width=640,height=480)
canvas.create_rectangle(40, 40, 600, 440, fill="gray78")
canvas.pack()
draw_graph()
root.mainloop()
