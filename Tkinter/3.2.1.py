import tkinter
# ウィンドウ作成
root = tkinter.Tk()
root.title("図形の移動1")
root.geometry("640x480")
#キャンバス設定
canvas = tkinter.Canvas(root, bg="#fff", width=640, height=400)
canvas.pack()
#図形表示+図形に名前をつける
rect = canvas.create_rectangle(10,10,50,50, fill="#f0f0f0")
canvas.create_oval(10,70,50,110, fill="#0fffff", tag="oval")

root.mainloop()