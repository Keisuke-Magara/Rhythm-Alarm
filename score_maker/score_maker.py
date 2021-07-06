# coding : utf-8
# test environment : Windows10 Education ver.21H1 64bit, Python 3.9.5 64bit, Tkinter 8.9, pygame 2.0.1

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import sys
import pygame
import os
import Timer
import time
import jubeat


global root, frame, repeat_interval

repeat_interval = 250

def repeat_function():
    if (frame.refresh_music_time()):
        root.after(repeat_interval, repeat_function)

if __name__ == "__main__":
    #args = sys.argv
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
    #timer.reset()
    root = tk.Tk()
    root.geometry("480x720")
    root.title("Score maker for The jubeat alarm!")
    root.resizable(width=False, height=False)
    #rootメインウィンドウのグリッドを1x1にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    #Frameを作成
    frame = jubeat.jubeat(root)
    #Frameを配置
    frame.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
    #frame_jubeatを最前面にする
    frame.tkraise()
    increment = True
    pygame.mixer.init()
    #音楽ファイル読み込み
    #pygame.mixer.music.load(args[1])
    root.after(repeat_interval, repeat_function)
    root.mainloop()