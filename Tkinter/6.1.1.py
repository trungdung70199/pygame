import tkinter

# ウィンドウ作成
root = tkinter.Tk()
root.title("勇者求む!")
root.geometry("640x480")
#fontname = "Meiryo"
#fontname=tkinter.font.Font(family="Meiryo",underline=True,slant="italic",size=18)
root.option_add("*font", ("メイリオ", 14))

# 画像読み込み
img1 = tkinter.PhotoImage(file = './img/6-1-1.png')
# キャンバス作成
canvas = tkinter.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(320, 200, image=img1, tag="hero")

# ラベル配置
serihu_text = tkinter.Label(text= "勇者登場!「魔王を倒したらいくらくれる?」")
serihu_text.place(x=140, y=10)
sys_text = tkinter.Label(text="報酬を設定", fg="red")
sys_text.place(x=180, y=380)

# 入力ボックス配置
entry= tkinter.Entry(width=12)
entry.place(x=180, y=420)
gold_text = tkinter.Label(text="ゴールド")
gold_text.place(x=330, y=420)

# ボタン配置
button = tkinter.Button(text="決定")
button.place(x=420, y=410)
root.mainloop()
