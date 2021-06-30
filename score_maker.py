# coding : utf-8
# test environment : Windows10 Pro Education ver.21H1 64bit, Python 3.9.5 64bit, Tkinter 8.9, pygame 2.0.1

import tkinter as tk
from tkinter import ttk
import sys
import pygame

global score

class Panel (ttk.Button):
    def __init__ (self, master, text=None, padding=None):
        super().__init__(master)
        self.configure(command=self.callfor)
        if (text != None):
            self.configure(text=text)
        if (padding != None):
            self.configure(padding=padding)
        
    
    def callfor(self):
        print("pushd.")

class jubeat (ttk.Frame):
    panel = []
    quit_button = None

    def __init__ (self, master):
        super().__init__(master)
        self.create_widgets()
    
    def create_widgets(self):
        # Put control buttons.
        self.quit_button = tk.Button(master=self, text="QUIT", command=lambda : exit(), width=5, height=2)
        self.quit_button.place(x=390, y=0.1)
        # Put message area.
        # Show play time.
        # Put control buttons.
        # Put 9 panels.
        for i in range(10):
            width = 35 # Tkinter size
            height = 56 # Tkinter size
            self.panel.append(Panel(master=self, text=i, padding=(width, height, width, height)))
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

if __name__ == "__main__":
    #rootメインウィンドウの設定
    root = tk.Tk()
    root.geometry("480x720")
    root.title("Score maker for jubeat alarm ver.0.1")
    root.resizable(width=False, height=False)
    #rootメインウィンドウのグリッドを1x1にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    #Frameを作成
    frame = jubeat(root)
    #Frameを配置
    frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
    #frame_jubeatを最前面にする
    frame.tkraise()
    root.mainloop()