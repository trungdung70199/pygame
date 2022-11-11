import tkinter
class FightManager:

    def __init__(self):
        self.dialog = tkinter.Frame(width=400, height=300)
        self.dialog.place(x=120, y=77)
        self.canvas = tkinter.Canvas(self.dialog, width=400, height=300, bg="black")
        self.canvas.place(x=0, y=0)
        # self.dialog.place_forget()

        self.fbutton = tkinter.Button(self.dialog, text="攻撃")
        self.fbutton.place(x=120, y=240)
        self.rbutton = tkinter.Button(self.dialog, text="守り")
        self.rbutton.place(x=240, y=240)

        self.images = [
        tkinter.PhotoImage(file="img8/chap8-monster1s.png"),
        tkinter.PhotoImage(file="img8/chap8-monster2s.png")
        ]
        self.canvas.create_image(100, 100, image=self.images[0])

        self.label = tkinter.Label(self.dialog, text="モンスター1が現れた!", fg="white", bg="black", justify="left")
        self.label.place(x=190, y=10)