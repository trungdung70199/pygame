import tkinter

root = tkinter.Tk()
root.title("サイコロを投げる")
root.resizable(False, False)
root.geometry("800x600")

canvas = tkinter.Canvas(root, bg='#fff',width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="./img/miko.png")
canvas.create_image(400, 300, image=gazou)

root.mainloop()

