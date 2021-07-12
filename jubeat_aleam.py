# coding : utf-8, CRLF
# Test environment:
# Operating System : Windows10 Pro education 64bit
# Python : Python 3.9.5 64bit, Tkinter version8.6
##########################################################################################################
import tkinter as tk
from tkinter import ttk
from tkinter.constants import NO
from pygame.constants import BUTTON_RIGHT
#自作モジュールインポート
#import Score
import Alarm

def main():
    #rootメインウィンドウの設定
    root = tk.Tk()
    root.geometry("480x720")
    root.title("Rhythm Alarm!")
    root.resizable(width=False, height=False)
    #root.configure(background='#000000')
    #rootメインウィンドウのグリッドを1x1にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    #画面ごとにFrameを作成
    #frame_jubeat = JubeatFrame.JubeatFrame(root)
    frame_alarm = Alarm.AlarmFrame(root) #引数はroot
    #Frameを配置
    frame_alarm.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
    #frame_jubeat.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
    #app = Application(master=root)
    #frame_alarmを最前面にする
    frame_alarm.tkraise()
    #frame_jubeatを最前面にする
    #frame_jubeat.tkraise()
    #game = GameStart
    #sound.play_music("楽しみキッズ.mp3")
    root.mainloop()


    
if __name__ == "__main__":
    main()