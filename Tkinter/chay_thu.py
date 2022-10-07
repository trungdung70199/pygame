import tkinter
### 定数
WIDTH = 640 # 画面横サイズ
HEIGHT = 480 # 画面縦サイズ
SIZE = 50 # 円サイズ
M_DOT = 10 # 移動ドット
W_TIME = 30 # 待ち時間
### 変数
x_pos = 0 # X座標
y_pos = 0 # Y座標
x_flg = 0 # 横限界フラグ
y_flg = 0 # 縦限界フラグ
# ウィンドウ作成
root = tkinter.Tk()
root.title("図形の移動4")
root.geometry("640x480")
#キャンバス設定
canvas = tkinter.Canvas(root, bg="#fff", width=WIDTH, height=HEIGHT)
canvas.pack()
#図形表示+図形に名前をつける
canvas.create_oval(x_pos, y_pos, x_pos+SIZE, y_pos+SIZE, fill="#0fffff", tag="oval")
#図形移動
def move():
### グローバル変数宣言
    global x_pos
    global y_pos
    global x_flg
    global y_flg
    ### 横座標設定
    if x_pos < 1:
        x_flg = 0
    elif x_pos > WIDTH - SIZE:
        x_flg = 1
        
    if x_flg == 0:
        x_pos += M_DOT
    else:
        x_pos -= M_DOT
    ### 縦座標設定
    if y_pos < 1:
        y_flg = 0
    elif y_pos > HEIGHT - SIZE:
        y_flg = 1
    if y_flg == 0:
        y_pos += M_DOT
    else:
        y_pos -= M_DOT
    ### 円表示
    canvas.coords("oval", x_pos, y_pos, x_pos+SIZE, y_pos+SIZE)
    #canvas.move("oval", 5, 5)
    canvas.after(W_TIME, move)
move()
root.mainloop()
