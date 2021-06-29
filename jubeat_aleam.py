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
#import Music
#import Score
#import Alarm
#import Panel
#//

#グローバル変数
#//

class Panel(ttk.Button):
    bright:bool = False
    img = 0

    #def refresh(): #ボタンのプロパティを反映する関数

#ウィンドウ描画
class JubeatFrame (ttk.Frame):
    panel = []
    img = Image.open("./buttonImageTest.png")
    img = ImageTk.PhotoImage(img)

    def __init__(self, master):
        super().__init__(master)
        #self.pack()
        #self.master.geometry("480x720")
        #self.master.title("The jubeat alarm!")
        self.create_widgets()

    def create_widgets (self):
        #display 9 panlels.
        #img = Image.open("./buttonImageTest.png")
        #img = ImageTk.PhotoImage(img)
        #img = tk.PhotoImage(file="./Test.png")
        for i in range (9):
            width = 35 #px
            height = 56 #px
            #padding=(width, height, width, height), 
            self.panel.append(Panel(master=self, image=self.img, command=self.callfor(), name="Panel_"+str(i)))
        y = 255
        self.panel[0].place(x=0, y=0.1 + y)
        self.panel[1].place(x=145, y=0.1 + y)
        self.panel[2].place(x=290, y=0.1 + y)
        self.panel[3].place(x=0, y=137 + y)
        self.panel[4].place(x=145, y=137 + y)
        self.panel[5].place(x=290, y=137 + y)
        self.panel[6].place(x=0, y=274 + y)
        self.panel[7].place(x=145, y=274 + y)
        self.panel[8].place(x=290, y=274 + y)
    
    def callfor(self):
        def inner (): # 実際に呼び出されるのはこっち
            print ("Push Detected.\n")
        return inner

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
    root.mainloop()

if __name__ == "__main__":
    main()