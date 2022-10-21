import tkinter
import time

# グラフ用変数
start_x = 60
start_y = 60
width_px = 5
height_px = 32
distance_px = 4
# リスト
list = [70, 15, 66, 21, 19, 97, 33, 44, 30, 2]
# グラフ表示関数
def draw_graph(num):
    wl = list
    x = start_x
    y = start_y
    color = "blue"
    root.update()
    time.sleep(0.5)
    canvas.delete("graph")
    canvas.delete("txt")
    for i in list:
        j = int(i * width_px / height_px)
        d = int(i * width_px % height_px)
        for k in range(j):
            kk = k * height_px
            li = list.index(i)
            if li == num or li == num + 1:
                color = "red"
            else:
                color = "blue"
            canvas.create_oval(x + kk, y, x + kk + height_px,
            y + height_px, fill=color, outline=color,
            tag="graph")
            canvas.create_text(x+i*width_px+12, y+12, text=i, tag="txt")
        y = y + height_px + distance_px

root = tkinter.Tk()
root.title("棒グラフ仕上げ問題")
root.resizable(False, False)
root.geometry("640x480")
# キャンバス配置
canvas = tkinter.Canvas(root,width=640,height=480)
canvas.create_rectangle(40, 40, 600, 440, fill="gray78")
canvas.pack()
draw_graph(0)

# バブルソート
for k in range(len(list) - 1):
    for j in range(len(list) - 1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
    draw_graph(j)
root.mainloop()