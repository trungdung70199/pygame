import tkinter

# ウィンドウ作成
root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False, False)
root.geometry("800x600")
#キャンバス設定
canvas = tkinter.Canvas(root, bg="#fff", width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="./img/miko.png")
canvas.create_image(400, 300, image=gazou)

label = tkinter.Label(root, text="占い", font=("Times New Roman", 120), bg="white")
label.place(x=380, y=60)
#ボタン
button = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman", 36), fg="black")
button.place(x=380, y=400)

root.mainloop()
