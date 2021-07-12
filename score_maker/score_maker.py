# coding : utf-8
# test environment : Windows10 Education ver.21H1 64bit, Python 3.9.6 64bit, Tkinter 8.9, pygame 2.0.1

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
    # 平行リピート処理
    root.after(repeat_interval, repeat_function)
    root.mainloop()