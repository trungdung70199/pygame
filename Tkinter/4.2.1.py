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
root.mainloop()