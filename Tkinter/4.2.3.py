import tkinter
# ウィンドウ作成
root = tkinter.Tk()
root.title("ネコ好き診断アプリ")
root.resizable(False, False)
root.geometry("800x600")
#キャンバス設定
canvas = tkinter.Canvas(root, bg="#fff", width=800, height=600)
canvas.pack()
#背景画像設定
gazou = tkinter.PhotoImage(file="./img/sumire.png")
canvas.create_image(400, 300, image=gazou)
#ボタン
button = tkinter.Button(text="診断する", font=("Times New Roman", 32), bg="lightgreen")
button.place(x=400, y=480)
#テキストボックス
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=360, y=30)

#リストの設定
bvar = [None]*7
cbtn = [None]*7
#7つの質問
ITEM = [
"高いところが好き",
"ボールを見ると転がしたくなる",
"びっくりすると髪の毛が逆立つ",
"ネズミの玩具が気になる",
"匂いに敏感",
"魚の骨をしゃぶりたくなる",
"夜、元気になる"
]
#表示ループ
for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160+40*i)

#チェックボタンを数える関数
def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "チェックの数は" + str(pts))
button["command"] = click_btn
root.mainloop()
