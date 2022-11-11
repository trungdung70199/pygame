import tkinter
class FightManager:

    def __init__(self):
        self.dialog = tkinter.Frame(width=400, height=300)
        self.dialog.place(x=120, y=77)
        self.canvas = tkinter.Canvas(self.dialog, width=400, height=300, bg="black")
        self.canvas.place(x=0, y=0)
        # self.dialog.place_forget()