#try:
        
import random
import tkinter

r = int(random.random()*10 % 3)
lhelo = [0, 0, 0]
hgold = [0, 0, 0]

hgold[0] = 1000
hgold[1] = 10000
hgold[2] = 100000

root = tkinter.Tk()
root.title("勇者求む")    
root.geometry("640x480")
root.option_add("*font", ("メイリオ"))

img1 = tkinter.PhotoImage(file='./img/6-1-1.png')
img2 = tkinter.PhotoImage(file='./img/6-1-2.png')
img3 = tkinter.PhotoImage(file='./img/6-1-3.png')

lhelo[0] = tkinter.PhotoImage(file='img/6-2-1.png')
lhelo[1] = tkinter.PhotoImage(file='img/6-2-2.png')
lhelo[2] = tkinter.PhotoImage(file='img/6-2-3.png')

canvas = tkinter.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
#canvas.create_image(320, 200, image=img1, tag="hero")
canvas.create_image(320, 200, image=lhelo[r], tag="hero")

serihu_text = tkinter.Label(text="勇者{}登場 「魔王を倒したらいくらくれる？」".format(r+1))
#serihu_text = tkinter.Label(text="勇者登場! 「魔王を倒したらいくらくれる？」")
serihu_text.place(x=140, y=10)
sys_text = tkinter.Label(text="報酬を設定", fg="red")
sys_text.place(x=180, y=380)

entry = tkinter.Entry(width=12)
entry.place(x=180, y=420)
gold_text = tkinter.Label(text="ゴールド")
gold_text.place(x=330, y=420)

def btn_click():
    gold = float(entry.get())
    if gold <=hgold[r]:
        canvas.delete("hero")
        canvas.create_image(320, 200, image=img3, tag="hero")
        serihu_text["text"] ="ごめん、勇者{}はその金額では魔王は倒せなかった!".format(r+1)
        sys_text["text"] = "報酬を受け取った"
    else:
        canvas.delete("hero")
        canvas.create_image(320, 200, image=img2, tag="hero")
        serihu_text["text"] = "勇者{}が魔王を倒したぞ！".format(r+1)
        sys_text["text"] = "報酬を受け取った"
    button["state"] = "disabled"
    entry["state"] = "disabled"
button = tkinter.Button(text="決定")
button.place(x=420, y=410)
button["command"] = btn_click

root.mainloop()
#except Exception as bug:
    #print(bug)
#input()
