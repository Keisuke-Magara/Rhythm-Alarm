import tkinter as tk
from tkinter import StringVar, ttk
import Alarm
import datetime
import sys
import sound
class ResultFrame(ttk.Frame): # アラーム画面描画
    #コンストラクタ：引数はroot, clear_time
    def __init__(self, master, clear_time):
        self.style = ttk.Style()
        self.style.configure('GameStyle.TFrame', background='#000000')
        super().__init__(master, style='GameStyle.TFrame')
        #おはようございますのラベル
        label1 = ttk.Label(
            self,
            text = 'おはようございます',
            foreground = '#FFB340',
            background = '#000000',
            font = ('游ゴシック', '32', 'bold')
        )
        label1.place(x=24, y=60)

        #クリア時間のラベル
        label2 = ttk.Label(
            self,
            text = clear_time,
            foreground = '#FFFFFF',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        label2.place(x=83, y=140)

        #現在時刻のラベル
        now_time = StringVar()
        self.clock(now_time)
        label3 = ttk.Label(
            self,
            textvariable= now_time,
            foreground='#FFFFFF',
            background='#000000',
            font = ('メイリオ', '50', 'bold')
        )
        label3.place(x=56, y=250)

        #終了のボタン
        def button1_clicked(a):#セットボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            self.after(300, sys.exit)
        button1 = tk.Button(self, text='終了',bg='#FFB340', fg='#000000', width=5, font='游ゴシック 21 bold')
        button1.bind('<Button-1>',button1_clicked, self)
        button1.place(x=173, y=500)

    def clock(self,now_time):
        now = datetime.datetime.now()
        now_time.set('{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second))
        self.after(100, self.clock, now_time)