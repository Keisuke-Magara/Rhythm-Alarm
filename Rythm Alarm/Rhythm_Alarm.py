# coding : utf-8, CRLF
# Test environment:
#  Operating System : Windows10 Pro education version 21H1 64bit
#  Python : Python 3.9.6 64bit, Tkinter version8.6, pygame 2.0.1 (SDL 2.0.14)
#  Used external library : tkinter, Pillow, numpy, pygame, mugen
##########################################################################################################
# >>Pythonファイルを実行する場合
#   Panel.py 14行目 fpsの値を 14 に設定してください。
#   delayを 636ms に設定してください。
# >>Pyinstallerを使ってexeファイル化して実行する場合
#   Panel.py 14行目 fpsの値を 28 に設定してください。
#   delayを 571ms に設定してください。
# 詳しくは README.md ファイル や GitHub (https://github.com/Keisuke-Magara/The-Rhythm-Alarm) をご確認ください。
##########################################################################################################
import tkinter as tk
from tkinter import ttk
from tkinter.constants import NO
from pygame.constants import BUTTON_RIGHT
import Alarm

def main():
    #rootメインウィンドウの設定
    root = tk.Tk()
    root.geometry("480x720")
    root.title("Rhythm Alarm!")
    root.resizable(width=False, height=False)
    #rootメインウィンドウのグリッドを1x1にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    #画面ごとにFrameを作成
    frame_alarm = Alarm.AlarmFrame(root) #引数はroot
    #Frameを配置
    frame_alarm.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
    #frame_alarmを最前面にする
    frame_alarm.tkraise()
    root.mainloop()


    
if __name__ == "__main__":
    main()