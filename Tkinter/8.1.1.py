import tkinter

root = tkinter.Tk()
root.title("ダンジョン&パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])

canvas = tkinter.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray")
root.mainloop()