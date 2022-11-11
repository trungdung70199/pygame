import tkinter
import random
class FightManager:

    def __init__(self):
        self.dialog = tkinter.Frame(width=400, height=300)
        self.dialog.place(x=120, y=77)
        self.canvas = tkinter.Canvas(self.dialog, width=400, height=300, bg="black")
        self.canvas.place(x=0, y=0)
        # self.dialog.place_forget()

        self.fbutton = tkinter.Button(self.dialog, text="攻撃")
        self.fbutton.place(x=120, y=240)
        self.fbutton["command"] = self.fight_win
        self.rbutton = tkinter.Button(self.dialog, text="守り")
        self.rbutton.place(x=240, y=240)
        self.rbutton["command"] = self.fight_loose

        self.images = [
        tkinter.PhotoImage(file="img8/chap8-monster1s.png"),
        tkinter.PhotoImage(file="img8/chap8-monster2s.png")
        ]
        self.canvas.create_image(100, 100, image=self.images[0])

        self.label = tkinter.Label(self.dialog, text="モンスター1が現れた!", fg="white", bg="black", justify="left")
        self.label.place(x=190, y=10)

    def fight_start(self):
        self.dialog.place(x=120, y=77)
    
    def fight_win(self):
        self.dialog.place_forget()

    def fight_loose(self):
        # self.dialog.place_forget()
        canvas = tkinter.Canvas(self.dialog, width=400, height=300, bg="red")
        canvas.place(x=0, y=0)
        canvas.create_text(170, 60,
        fill="white", font=("メイリオ", 16),
        text="勇者は負けてしまった。\n最初からやり直してくれたまえ。")

class FightManager:

    def fight_start(self):
        self.dialog.place(x=120, y=77)
        self.monster = Mon1()
        self.canvas.create_image(100, 100, image=self.monster.img)
        self.label["text"] = self.monster.name + "が現れた"

class Character:

    def __init__(self):
        self.name = "ななし"
        self.hp = 0
        self.atk = 0

    def get_atk(self):
        return random.randint(1, self.atk)

    def culc_hp(self, atk):
        dmg = atk

        if dmg < 1:
            return self.hp
        self.hp = self.hp - dmg
        if self.hp < 1:
            self.hp = 0
        return self.hp

class Hero(Character):
    def __init__(self):
        self.name = "勇者"
        self.hp = 30
        self.atk = 15
class Mon1(Character):
    def __init__(self):
        self.name = "デビル"
        self.hp = 30
        self.atk = 15
        self.dfs = 10
        self.img = tkinter.PhotoImage(file="img8/chap8-monster1s.png")
                