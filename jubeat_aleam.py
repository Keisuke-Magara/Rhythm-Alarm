# coding : utf-8, CRLF
# Test environment:
# Operating System : Windows10 Pro education 64bit
# Python : Python 3.9.5 64bit, Tkinter version8.6
##########################################################################################################
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sys
import time
#自作モジュールインポート
#from music import playsound
#import Score
#import Alarm
#import Panel
#//

#グローバル変数
#//

class Panel(ttk.Button):
    bright:bool = False
    imgName = "./buttonImageTest.png"

    def __init__ (master=None, text=None, image=None, name=None, padding=None):
        super.__init__(master, text, name, padding)



    def callfor(self): # ボタンが押されたときに実行される処理 (panelが押されたパネルを示す)
        def inner(): # 実際に呼び出されるのはこっち (この中に処理を記述)
            panel.configure(text="pushd.")
        return inner

    #def refresh(): #ボタンのプロパティを反映する関数


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
        img = Image.open(self.imgName)
        img = ImageTk.PhotoImage(img)
        #img = tk.PhotoImage(file="./Test.png")
        for i in range (9):
            width = 35 #px
            height = 56 #px
            #, padding=(width, height, width, height)
            self.panel.append(Panel(self, image=img, name="panel_"+str(i), padding=(width, height, width, height)))
            pushd = self.callfor(self.panel[i])
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




class GameStart:
    timing = [[0]*10]
    pre_sec = 2 # call collisionDetection() pre_sec second before touch time.

    def __init__ ():
        music.playsound()


def main():
    #rootメインウィンドウの設定
    root = tk.Tk()
    root.geometry("480x720")
    root.title("The jubeat alarm!")
    root.resizable(width=False, height=False)
    #rootメインウィンドウのグリッドを1x1にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    #画面ごとにFrameを作成
    #frame_alarm = ttk.Frame(root)
    frame_jubeat = JubeatFrame(root)
    #Frameを配置
    frame_jubeat.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
    #app = Application(master=root)
    #frame_jubeatを最前面にする
    frame_jubeat.tkraise()
    #game = GameStart
    root.mainloop()

if __name__ == "__main__":
    main()