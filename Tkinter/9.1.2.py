import tkinter
from tkinter import messagebox

MAX_WIDTH = 10
MAX_HEIGHT = 7
map_data = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 2, 0, 5, 1, 3, 1],
[1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 0, 5, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 5, 1],
[1, 0, 5, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

hero_x = 1
hero_y = 0
dist = 62

def draw_map():
    for y in range(0, MAX_HEIGHT):
        for x in range(0, MAX_WIDTH):
            p = map_data[y][x]
            canvas.create_image(x*62+31, y*62+31, image=images[p])
    canvas.create_image(hero_x*62+31, hero_y*62+31,
    image=images[4], tag="hero")

def check_move(x, y):
    global hero_x, hero_y, flag_key
    p = map_data[y][x]
    if p == 1:
        return
    elif p == 3:
        flag_key = True
        map_data[y][x] = 0
        canvas.delete("all")
        draw_map()
    elif p == 2:
            if flag_key == True:
                messagebox.showinfo("ゲームクリア", "ゴール!")
            else:
                return

    dx = (x - hero_x)*dist
    dy = (y - hero_y)*dist
    hero_x = x
    hero_y = y
    canvas.move("hero", dx, dy)

def left():
    check_move(hero_x-1, hero_y)
def right():
    check_move(hero_x+1, hero_y)
def up():
    check_move(hero_x, hero_y-1)
def down():
    check_move(hero_x, hero_y+1)

def fightManager():
    dialog = tkinter.Frame(width=400, height=300)
    dialog.place(x=120, y=77)
    canvas = tkinter.Canvas(dialog, width=400, height=300, bg="black")
    canvas.place(x=0, y=0)
    #dialog.place_forget()

root = tkinter.Tk()
root.title("ダンジョン&パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

canvas = tkinter.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray")

button_up = tkinter.Button(text="↑")
button_up.place(x=720, y=150)
button_up["command"] = up
button_down = tkinter.Button(text="↓")
button_down.place(x=720, y=210)
button_down["command"] = down
button_left = tkinter.Button(text="←")
button_left.place(x=660, y=180)
button_left["command"] = left
button_right = tkinter.Button(text="→")
button_right.place(x=780, y=180)
button_right["command"] = right

images = [tkinter.PhotoImage(file="img8/chap6-mapfield.png"),
    tkinter.PhotoImage(file="img8/chap6-mapwall.png"),
    tkinter.PhotoImage(file="img8/chap6-mapgoal.png"),
    tkinter.PhotoImage(file="img8/chap6-mapkey.png"),
    tkinter.PhotoImage(file="img8/chap6-mapman.png"),
    tkinter.PhotoImage(file="img8/chap7-mapmonster.png")]

flag_key = False
draw_map()
fightManager()
root.mainloop()