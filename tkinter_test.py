import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry ("400x300")

#グローバル変数一覧
buttonText = "test"
img = Image.open("Test.png")
img = ImageTk.PhotoImage(img)
buttonImage = tk.PhotoImage(file=img)

#関数一覧
def collisionDetection (event):
    global buttonText
    buttonText = "Clicked!"
    print (buttonText)


Button = tk.Button (text=buttonText,  width=50)
Button.bind("<Button-1>", collisionDetection)
Button.pack()

root.mainloop()
