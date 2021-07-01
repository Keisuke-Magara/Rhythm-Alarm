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
        self.quit_button = tk.Button(master=self, bg="DarkMagenta", font=("MSゴシック", "12", "bold"), text="QUIT", command=lambda : exit(), width=5, height=2)
        self.quit_button.place(x=380, y=10)
        # Put message area.
        self.msg_area = tk.Label(master=self, bg="DarkCyan", font=("游ゴシック Light", "15", "normal"), height=2, width=30, justify="center", text="Messages are shown here.\nメッセージはここに表示されます。")
        self.msg_area.place(x=0, y=10)
        # Show played music name.
        self.music_name_area = tk.Label(master=self, bg="gainsboro", font=("游ゴシック", "15", "bold"), height=2, width=30, justify="center", text="Music Name : " + "music1.mp3" + "\n　---> Output : " + "music1.score")
        self.music_name_area.place(x=0, y=100)
        # Show play time.
        self.music_time = tk.Label(master=self, font=("Segoe UI Black", "30", "bold"), height=1, width=15, justify="center", text="0:30 / 1:00")
        self.music_time.place(x=120, y=180)
        # Put help button.
        self.help_button = tk.Button(master=self, bg="gold3", text="HELP!!", width=5, height=2)
        self.help_button.place(x=380, y=115)
        # Put control buttons.
        self.play_button = tk.Button(master=self, bg="green3", font=("MSゴシック", "15", "bold"), text="▶ Play", width=6, height=2)
        self.play_button.place(x=0, y=180)
        self.stop_button = tk.Button(master=self, bg="red3", font=("MSゴシック", "15", "bold"), text="■ STOP", width=6, height=2)
        self.stop_button.place(x=100, y=180)
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
    args = sys.argv
    try:
        sys.argv[1]
    except:
        print ("\nBad argument : 引数として音楽ファイルを指定してください。\n\tex) " + args[0] + " music.mp3")
        print (args[0] + " --help とすることで簡単なヘルプを見ることができます。\n")
        exit()
    
    if (args[1] == "-h" or args[1] == "-H" or args[1] == "--help"):
        print ("\n -- 使い方 --")
        print ("1. 譜面を作りたい音楽ファイルをこのソフトがあるフォルダに置いてください。")
        print ("2. コマンドプロンプトで、このソフトを音楽ファイルのファイル名を引数にとって起動してください。\n     ex) " + args[0] + " music.mp3")
        print ("3. Playボタンを押すと再生されるので実際にパネルをクリックして譜面を作ります。")
        print ("4. 曲の最後まで終わるとスコアがこのフォルダに保存されます。\n")
        exit()
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
    pygame.mixer.init()
    #音楽ファイル読み込み
    #pygame.mixer.music.load(args[1])
    
    root.mainloop()