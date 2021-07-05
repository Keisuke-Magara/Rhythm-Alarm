import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import Panel
class JubeatFrame (ttk.Frame): # ゲーム画面描画
    panel = []
    #img = Image.open("./buttonImageTest.png")
    #img = ImageTk.PhotoImage(file="./buttonImageTest.png")

    def __init__(self, master):
        super().__init__(master)
        #self.pack()
        #self.master.geometry("480x720")
        #self.master.title("The jubeat alarm!")
        self.create_widgets()

    def create_widgets (self):
        #display 9 panlels.
        
        #img = tk.PhotoImage(file="./Test.png")
        for i in range (9):
            width = 35 #px
            height = 56 #px
            #padding=(width, height, width, height)
            self.panel.append(Panel.Panel(self, text=i, name="panel_"+str(i), padding=(width, height, width, height)))
            #pushd = self.callfor(self.panel[i])
            #self.panel[i].config(command=pushd)
        blank = 255
        self.panel[0].place(x=0, y=0.1 + blank)
        self.panel[1].place(x=145, y=0.1 + blank)
        self.panel[2].place(x=290, y=0.1 + blank)
        self.panel[3].place(x=0, y=137 + blank)
        self.panel[4].place(x=145, y=137 + blank)
        self.panel[5].place(x=290, y=137 + blank)
        self.panel[6].place(x=0, y=274 + blank)
        self.panel[7].place(x=145, y=274 + blank)
        self.panel[8].place(x=290, y=274 + blank)