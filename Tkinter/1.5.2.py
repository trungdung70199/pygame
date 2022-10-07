import tkinter

root = tkinter.Tk()

root.title("キャンバス")

root.geometry("640x480")

fontname = "Meiryo"

canvas = tkinter.Canvas(root, width=640, height=480, bg="skyblue")

canvas.pack()

gazou = tkinter.PhotoImage(file="./img/hebi.png")
canvas.create_image(320, 240, image=gazou)

fontname = "System"
label = tkinter.Label(root,text="1からいくつまでの和?", font=(fontname, 36), bg="skyblue")
label.place(x=240, y=30)

entry = tkinter.Entry(width=20, bd=2)
entry.place(x=280, y=95)

button = tkinter.Button(root, text="計算!", font=(fontname,24))
button.place(x=500, y=95)

ans = tkinter.Label(root,text="答えは??", font=(fontname,36), bg="skyblue")
ans.place(x=280, y=150)

def calc():
    val = entry.get()
    num = int(val)
    s = 0
    for i in range(1, num+1):
        s = s + i
    ans["text"] = "答えは" + str(s) + "です！"
button["command"] = calc

root.mainloop()



