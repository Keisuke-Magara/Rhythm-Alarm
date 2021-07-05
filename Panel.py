import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sound
class Panel(ttk.Button):
    bright:bool = False
    imgName = "./buttonImageTest.png"

    def __init__ (self, master=None, text=None, image=None, name=None, padding=None):
        super().__init__(master)
        self.configure(command=self.callfor)
        if (text != None):
            self.configure(text=text)
        if (image != None):
            self.imgName = image
            img = Image.open(self.imgName)
            img = ImageTk.PhotoImage(img)
            self.configure(image=img)
        #if (name != None):
        #    self.configure(name=name)
        if (padding != None):
            self.configure(padding=padding)

    def callfor(self): # ボタンが押されたときに実行される処理 (panelが押されたパネルを示す)
        def inner(): # 実際に呼び出されるのはこっち (この中に処理を記述)
            self.configure(text="pushd.")
        return inner

    #def refresh(): #ボタンのプロパティを反映する関数