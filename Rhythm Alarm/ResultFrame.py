import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import FLAT
import datetime
import sys
import sound
class ResultFrame(ttk.Frame): # アラーム画面描画
    #コンストラクタ：引数はroot, clear_time
    def __init__(self, parent, master, clear_time):
        self.parent = parent
        self.clear_time = clear_time
        self.style = ttk.Style()
        self.style.configure('GameStyle.TFrame', background='#000000')
        super().__init__(master, style='GameStyle.TFrame')
        self.frame_score =ScoreFrame(master,self)
        self.frame_score.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
        self.tkraise()
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
        label2.place(x=93, y=140)

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
        def button1_clicked(a):#終了ボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            self.after(300, sys.exit)
        button1 = tk.Button(self, text='終了',bg='#FFB340', fg='#000000', width=5, font='游ゴシック 21 bold')
        button1.bind('<Button-1>',button1_clicked, self)
        button1.place(x=173, y=500)

        #スコアの詳細を表示のボタン
        def button2_clicked(a):#スコアの詳細を表示ボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            self.frame_score.tkraise()
            self.frame_score.label_place()
        button2 = tk.Button(self, text='スコアの詳細を開く',bg='#000000', fg='#FFB340', width=15, font='游ゴシック 18 bold underline', relief=FLAT)
        button2.bind('<Button-1>',button2_clicked, self)
        button2.place(x=103, y=570)

    def clock(self,now_time):
        now = datetime.datetime.now()
        now_time.set('{0:0>2d}:{1:0>2d}:{2:0>2d}'.format(now.hour, now.minute, now.second))
        self.after(100, self.clock, now_time)

class ScoreFrame(ttk.Frame): # アラーム画面描画
    #コンストラクタ：引数はroot, clear_time
    def __init__(self, master, parent):
        self.parent = parent
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
            text = parent.clear_time,
            foreground = '#FFFFFF',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        label2.place(x=93, y=140)
        #最大コンボ数のラベル
        self.label8 = ttk.Label(
            self,
            text = '最大コンボ数 ',
            foreground = '#FFFFFF',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        #self.label8.place(x=93, y=190)
        #perfectのラベル
        self.label3 = ttk.Label(
            self,
            text = 'PERFECT',
            foreground = '#df3179',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        #self.label3.place(x=93, y=240)
        #greatのラベル
        self.label4 = ttk.Label(
            self,
            text = 'GREAT',
            foreground = '#68c035',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        #self.label4.place(x=93, y=290)
        #goodのラベル
        self.label5 = ttk.Label(
            self,
            text = 'GOOD',
            foreground = '#697ee5',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        #self.label5.place(x=93, y=340)
        #badのラベル
        self.label6 = ttk.Label(
            self,
            text = 'BAD',
            foreground = '#7910be',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        #self.label6.place(x=93, y=390)
        #misaのラベル
        self.label7 = ttk.Label(
            self,
            text = 'MISS',
            foreground = '#79685b',
            background = '#000000',
            font = ('メイリオ', '18')
        )
        #self.label7.place(x=93, y=440)
        #最大コンボ数の数値
        combo = parent.parent.frame_jubeat.combo
        self.label9 = ttk.Label(
            self,
            text=combo,
            foreground='#FFFFFF',
            background='#000000',
            font=('メイリオ', '18'),
            anchor='e',
            width=5
        )
        #self.label9.place(x=264, y=190)
        #perfectの個数
        perfect = parent.parent.frame_jubeat.perfect
        self.label10 = ttk.Label(
            self,
            text=perfect,
            foreground='#df3179',
            background='#000000',
            font=('メイリオ', '18'),
            anchor='e',
            width=5
        )
        #self.label10.place(x=264, y=240)
        #greatの個数
        great = parent.parent.frame_jubeat.great
        self.label11 = ttk.Label(
            self,
            text=great,
            foreground='#68c035',
            background='#000000',
            font=('メイリオ', '18'),
            anchor='e',
            width=5
        )
        #self.label11.place(x=264, y=290)
        #goodの個数
        good = parent.parent.frame_jubeat.good
        self.label12 = ttk.Label(
            self,
            text=good,
            foreground='#697ee5',
            background='#000000',
            font=('メイリオ', '18'),
            anchor='e',
            width=5
        )
        #self.label12.place(x=264, y=340)
        #badの個数
        bad =parent.parent.frame_jubeat.bad
        self.label13 = ttk.Label(
            self,
            text=bad,
            foreground='#7910be',
            background='#000000',
            font=('メイリオ', '18'),
            anchor='e',
            width=5
        )
        #self.label13.place(x=264, y=390)
        #missの個数
        miss = parent.parent.frame_jubeat.miss
        self.label14 = ttk.Label(
            self,
            text=miss,
            foreground='#79685b',
            background='#000000',
            font=('メイリオ', '18'),
            anchor='e',
            width=5
        )
        #self.label14.place(x=264, y=440)

        #スコアの詳細を閉じるのボタン
        def button2_clicked(a):#スコアの詳細を閉じるボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            parent.tkraise()
        button2 = tk.Button(self, text='スコアの詳細を閉じる',bg='#000000', fg='#FFB340', width=15, font='游ゴシック 18 bold underline', relief=FLAT)
        button2.bind('<Button-1>',button2_clicked, self)
        button2.place(x=103, y=570)

    def label_place(self):
        def place(label, x, y):
            label.place(x=str(x), y=str(y))
        self.label8.place_forget()
        self.label3.place_forget()
        self.label4.place_forget()
        self.label5.place_forget()
        self.label6.place_forget()
        self.label7.place_forget()
        self.label9.place_forget()
        self.label10.place_forget()
        self.label11.place_forget()
        self.label12.place_forget()
        self.label13.place_forget()
        self.label14.place_forget()
        self.after(100, place, self.label8, 93, 190)
        self.after(200, place, self.label3, 93, 240)
        self.after(300, place, self.label4, 93, 290)
        self.after(400, place, self.label5, 93, 340)
        self.after(500, place, self.label6, 93, 390)
        self.after(600, place, self.label7, 93, 440)
        self.after(100, place, self.label9, 264, 190)
        self.after(200, place, self.label10, 264, 240)
        self.after(300, place, self.label11, 264, 290)
        self.after(400, place, self.label12, 264, 340)
        self.after(500, place, self.label13, 264, 390)
        self.after(600, place, self.label14, 264, 440)