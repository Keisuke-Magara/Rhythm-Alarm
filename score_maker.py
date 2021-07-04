# coding : utf-8
# test environment : Windows10 Pro Education ver.21H1 64bit, Python 3.9.5 64bit, Tkinter 8.9, pygame 2.0.1

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sys
import pygame
import os
import Timer
import time

global score, timer, frame, music_loaded
music_loaded = -1

def openFile(ftype=[("音楽ファイル", "*.mp3")]):
    filepath = filedialog.askopenfilename(filetypes=ftype, initialdir=os.path.abspath(os.path.dirname(__file__)))
    return filepath


class Panel (ttk.Button):
    def __init__ (self, master, text=None, padding=None):
        super().__init__(master)
        self.configure(command=self.callfor)
        if (text != None):
            self.configure(text=text)
        if (padding != None):
            self.configure(padding=padding)
        
    
    def callfor(self):
        n = (self.cget("text")) # ボタンナンバー取得
        place = []
        for i in range(9):
            if (i==n):
                place.append(1)
            else:
                place.append(0)
        place.insert(0, timer.get_time())
        print(place)
        score.append(place)

class jubeat (ttk.Frame):
    panel = []
    msg = None
    music_name = None
    music_time = None
    outputfile = ""

    def __init__ (self, master):
        super().__init__(master)
        self.msg = tk.StringVar()
        self.msg.set("こんにちは！\"OpenFile\"ボタンから\n音楽ファイルを選択してください。")
        self.music_name = tk.StringVar()
        self.music_name.set("Music Name : " + "______.mp3" + "\n　---> Output : " + "______.score")
        self.create_widgets()
    
    def create_widgets(self):
        # Put control buttons.
        self.help_button = tk.Button(master=self, bg="gold3", font=("MSゴシック", "12", "bold"), text="HELP!!", command=lambda : self.showHELP(), width=5, height=2)
        self.help_button.place(x=380, y=10)
        # Put message area.
        self.msg_area = tk.Label(master=self, bg="DarkCyan", font=("游ゴシック Light", "15", "normal"), height=2, width=30, justify="center", textvariable=self.msg)
        self.msg_area.place(x=0, y=10)
        # Show played music name.
        self.music_name_area = tk.Label(master=self, bg="gainsboro", font=("游ゴシック", "15", "bold"), height=2, width=30, justify="center", textvariable=self.music_name)
        self.music_name_area.place(x=0, y=100)
        # Show play time.
        self.music_time_area = tk.Label(master=self, font=("Segoe UI Black", "30", "bold"), height=1, width=15, justify="center", text="0:30 / 1:00")
        self.music_time_area.place(x=120, y=180)
        # Put help button.
        self.load_button = tk.Button(master=self, bg="#b0b0b0", font=("游ゴシック", "12", "bold"), text="Open\nFile", command=lambda: self.load_music(), width=5, height=2)
        self.load_button.place(x=380, y=100)
        # Put control buttons.
        self.play_button = tk.Button(master=self, bg="green3", font=("MSゴシック", "15", "bold"), text="▶ Play", command=lambda: play_music(), width=6, height=2)
        self.play_button.place(x=0, y=180)
        self.stop_button = tk.Button(master=self, bg="red3", font=("MSゴシック", "15", "bold"), text="■ STOP", command=lambda: stop_music(), width=6, height=2)
        self.stop_button.place(x=100, y=180)
        # Put 9 panels.
        for i in range(10):
            width = 35 # Tkinter size
            height = 56 # Tkinter size
            self.panel.append(Panel(master=self, text=i, padding=(width, height, width, height)))
        offset = 255
        self.panel[0].place(x=0, y=0.1 + offset)
        self.panel[1].place(x=145, y=0.1 + offset)
        self.panel[2].place(x=290, y=0.1 + offset)
        self.panel[3].place(x=0, y=137 + offset)
        self.panel[4].place(x=145, y=137 + offset)
        self.panel[5].place(x=290, y=137 + offset)
        self.panel[6].place(x=0, y=274 + offset)
        self.panel[7].place(x=145, y=274 + offset)
        self.panel[8].place(x=290, y=274 + offset)

    def load_music (self):
        filepath = openFile()
        #filepath = filedialog.askopenfilename(filetypes=ftype, initialdir=os.path.abspath(os.path.dirname(__file__)))
        pygame.mixer.music.load(filepath)
        temp = filepath.split("/")
        name = temp[len(temp)-1].split(".")
        self.music_name.set("Music Name : " + name[0] + "." + name[1] + "\n　---> Output : " + name[0] + ".score")
        self.outputfile = str(name[0]) + ".score"
        music_loaded = 0
        print(music_loaded)
        self.msg.set("ファイルの読み込み完了\n\"▶Play\"ボタンをクリックで再生開始")

    def showHELP (self):
        messagebox.showinfo("使い方", "1. 譜面を作りたい音楽ファイルを\"OpenFile\"から読み込んで下さい。\n2. Playボタンを押すと再生されるので実際にパネルをクリックして譜面を作ります。\n＊再生と一時停止しかできないので、譜面を打ち間違えた場合は最初からやり直してください。\n3.曲が全て終了すると、このソフトがあるフォルダに保存されます。")

def play_music ():
    try:
        time.sleep(1)
        print(music_loaded)
        if (music_loaded == 0):
            pygame.mixer.music.play()
            print("pause")
            pygame.mixer.music.unpause()
        timer.start()
        frame.msg.set("<<再生中>>\nパネルをクリックして譜面を作成")

    except pygame.error:
            frame.msg.set("音楽の再生に失敗しました。\nファイルを確認してください。")

def stop_music():
    pygame.mixer.music.pause()
    timer.stop()
    frame.msg.set("<<再生一時停止中>>\n\"▶Play\"ボタンをクリックして再開")

if __name__ == "__main__":
    args = sys.argv
    #try:
    #    sys.argv[1]
    #except:
    #    print ("\nBad argument : 引数として音楽ファイルを指定してください。\n\tex) " + args[0] + " music.mp3")
    #    print (args[0] + " --help とすることで簡単なヘルプを見ることができます。\n")
    #    exit()
    
    #if (args[1] == "-h" or args[1] == "-H" or args[1] == "--help"):
    #    print ("\n -- 使い方 --")
    #    print ("1. 譜面を作りたい音楽ファイルをこのソフトがあるフォルダに置いてください。")
    #    print ("2. コマンドプロンプトで、このソフトを音楽ファイルのファイル名を引数にとって起動してください。\n     ex) " + args[0] + " music.mp3")
    #    print ("3. Playボタンを押すと再生されるので実際にパネルをクリックして譜面を作ります。")
    #    print ("4. 曲の最後まで終わるとスコアがこのフォルダに保存されます。\n")
    #    exit()
    #rootメインウィンドウの設定
    score = []
    timer = Timer.MusicTimer()
    #timer.reset()
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
    increment = True
    pygame.mixer.init()
    #音楽ファイル読み込み
    #pygame.mixer.music.load(args[1])
    
    root.mainloop()