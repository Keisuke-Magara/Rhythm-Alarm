import tkinter as tk
from tkinter import ttk
from tkinter.constants import Y
from PIL import Image, ImageTk
import Panel
import datetime

class JubeatFrame (ttk.Frame): # ゲーム画面描画
    def __init__(self, master, score, parent, time):
        #self.configure(bg="black")
        self.goal_score = 150 # この点数に達するまで永遠にループ
        self.total_score = 0
        self.root = master
        self.parent = parent
        self.score_class = score # Scoreクラスのインスタンスの参照
        self.timer = time # MusicTimerクラスのインスタンスの参照
        self.panel = []
        self.style = ttk.Style()
        self.style.theme_use("alt")
        self.style.configure("GameStyle.TFrame", background="black")
        super().__init__(master, style="GameStyle.TFrame")
        self.msg = tk.StringVar()
        self.msg.set("こいつを止めるには、\nクリアするしかない。")
        self.clock = tk.StringVar()
        self.music_name = tk.StringVar()
        self.music_name.set("アラーム音: 夜に駆ける")
        self.score = tk.StringVar()
        self.create_widgets()
        self.root.after(1, self.repeat_processes)

    def create_widgets (self):
        # create clock area.
        self.clock_area = tk.Label(self, bg="brown", width=15, height = 1, font=("MSゴシック", 25, "bold"), textvariable=self.clock)
        self.clock_area.place(x=70, y=0)
        # create message area.
        self.message_area = tk.Label(self, bg="gold", width=26, height = 2, font=("MSゴシック", 20, "bold"), textvariable=self.msg)
        self.message_area.place(x=0, y=50)
        # create music name area.
        self.music_name_area = tk.Label(self, bg="black", fg="white", width=24, height=1, font=("MSゴシック", 25, "normal"), textvariable=self.music_name)
        self.music_name_area.place(x=0, y=130)
        # create Score area.
        self.score_area = tk.Label(self, bg="green", width=10, height = 1, font=("MSゴシック", 40, "bold"), textvariable=self.score)
        self.score_area.place(x=120, y=180)
        # create 9 panlels.
        for i in range (9):
            width = 10 # "0" size.
            height = 56 #px
            self.panel.append(Panel.Panel(master=self, score=self.score_class, time=self.timer, name=str(i), text=str(i)))
        xoffset = 5
        yoffset = 255
        self.panel[0].place(x=0+xoffset, y=0+yoffset)
        self.panel[1].place(x=145+xoffset, y=0+yoffset)
        self.panel[2].place(x=290+xoffset, y=0+yoffset)
        self.panel[3].place(x=0+xoffset, y=140+yoffset)
        self.panel[4].place(x=145+xoffset, y=140+yoffset)
        self.panel[5].place(x=290+xoffset, y=140+yoffset)
        self.panel[6].place(x=0+xoffset, y=278+yoffset)
        self.panel[7].place(x=145+xoffset, y=278+yoffset)
        self.panel[8].place(x=290+xoffset, y=278+yoffset)
    
    def repeat_processes(self):
        now = datetime.datetime.now()
        self.clock.set(now.strftime('%H:%M:%S'))
        self.score.set(str(self.total_score) + " / " + str(self.goal_score))
        self.root.after(100, self.repeat_processes)