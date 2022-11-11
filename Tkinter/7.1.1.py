import tkinter
tmr = 0
id = None
fontname = 'Helvetica 40 bold'

def move():
    global tmr
    global id
    tmr = tmr + 1
    #label["text"] = str(tmr) + "秒"
    canvas.delete("txt")
    canvas.create_text(330, 30, text= str(tmr)+"秒",fill="black",font=fontname, tag="txt")
    id = canvas.after(1000, move)

def stop():
    global id
    canvas.after_cancel(id)
    
def reset():
    global tmr
    global id
    canvas.after_cancel(id)
    canvas.delete("txt")
    tmr = 0
    canvas.create_text(330, 30, text= "0秒",fill="black",font=fontname, tag="txt")

root = tkinter.Tk()
root.title("カウントアップ")
root.geometry("640x480")
root.option_add("*font", ("メイリオ", 14))

frame1 = tkinter.Frame(root,)
frame2 = tkinter.Frame(root,)

img1 = tkinter.PhotoImage(file = 'img/6-1-1.png')

canvas = tkinter.Canvas(frame2, bg="#fff", width=640, height=460)
canvas.pack()
canvas.create_image(330, 200, image=img1, tag="hero")
canvas.create_text(330, 30, text= "0秒",fill="black",font=fontname, tag="txt")

button = tkinter.Button(frame1, text="GO", command=move)
button.pack(side="left")
button2 = tkinter.Button(frame1, text="STOP", command=stop)
button2.pack(side="left")
button3 = tkinter.Button(frame1, text="RESET", command=reset)
button3.pack(side="left")

frame1.pack()
frame2.pack()

root.mainloop()