import tkinter

id = None

root = tkinter.Tk()
root.title("ex02_03")
root.geometry("640x480")

frame1 = tkinter.Frame(
    root,
)

frame2 = tkinter.Frame(
    root,
)

canvas = tkinter.Canvas(frame2, bg="#fff", width=640, height=400)
canvas.pack()

rect = canvas.create_rectangle(10,10,50,50, fill="#f0f0f0")
canvas.create_oval(10,70,50,110, fill="#0fffff", tag="oval")

def move():
    global id
    canvas.move(rect, 10, 0)
    canvas.move("oval", 10, 10)
    id = canvas.after(100, move)

def stop():
    global id
    canvas.after_cancel(id)

def reset():
    global id
    canvas.after_cancel(id)
    canvas.delete("rect")
    canvas.delete("oval")
    canvas.create_rectangle(10,10,50,50, fill="#f0f0f0", tag="rect")
    canvas.create_oval(10,70,50,110, fill="#0fffff", tag="oval")

def rmove():
    global id
    canvas.move("rect", -10, 0)
    canvas.move("oval", -10, -10)
    id = canvas.after(100, rmove)
    
    
button = tkinter.Button(frame1, text="GO", command=move)
button.pack(side="left")
button = tkinter.Button(frame1, text="STOP", command=stop)
button.pack(side="left")
button = tkinter.Button(frame1, text="RESET", command=reset)
button.pack(side="left")
button = tkinter.Button(frame1, text="RMOVE", command=rmove)
button.pack(side="left")

frame1.pack()
frame2.pack()

root.mainloop()