import tkinter
# ウィンドウ作成
root = tkinter.Tk()
root.title("図形の表示")
root.geometry("640x480")
#キャンバス設定
canvas = tkinter.Canvas(root, bg="#fff", width=640, height=400)
canvas.pack()
# 矩形
canvas.create_rectangle(10,10,50,50, fill="#f0f0f0")
# 楕円
canvas.create_oval(10,70,50,110, fill="#0fffff")
# 線
canvas.create_line(10, 150, 100, 150, arrow=tkinter.LAST)
canvas.create_line(120,180,170, 130,220,180,width=3.0,fill='red')
# 文字
canvas.create_text(10, 200, text="あいうえお", anchor=tkinter.W, font=("",20))
# ビットマップ
canvas.create_bitmap(30,250,bitmap='hourglass')
root.mainloop()
