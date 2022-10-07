import tkinter

root = tkinter.Tk()

root.title("Windows")

root.geometry("640x480")

fontname = "Meiryo"

def click_btn():
    button["text"]="こんにちは！"
    label["text"] = "こんばんは！"

button = tkinter.Button(root,text="ボタンを押してね！", font=(fontname,24), command=click_btn)

button.place(x=150,y=280)

label = tkinter.Label(root,text="Hello World!",bg="white",font=(fontname,48))

label.place(x=180,y=180)

root.mainloop()




