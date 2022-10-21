import tkinter
import time

start_x = 60
start_y = 60
width_px = 5
height_px = 32
distance_px = 4

list = [70, 15, 66, 21, 19, 97, 33, 44, 30, 2]
# print("0度目:{}".format(list))

root = tkinter.Tk()
root.title("バブルソート")
root.resizable(False, False)
root.geometry("640x480")

canvas = tkinter.Canvas(root,width=640,height=480)
canvas.create_rectangle(40, 40, 600, 440, fill="gray78")
canvas.pack()

def draw_graph():
    wl = list
    x = start_x
    y = start_y
    color = "blue"
    root.update()
    time.sleep(0.5)
    canvas.delete("graph")
    canvas.delete("txt")
    for i in list:
        canvas.create_rectangle(x, y, x + i * width_px,
        y + height_px, fill=color, outline=color,
        tag="graph")

        canvas.create_text(x+i*width_px+12, y+12, text=i, tag="txt")
        y = y + height_px + distance_px
draw_graph()

for k in range(len(list) - 1):
    # print("{}度目".format(k+1),end=":")
    for j in range(len(list) - 1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            # print(list)
        draw_graph()

root.mainloop()