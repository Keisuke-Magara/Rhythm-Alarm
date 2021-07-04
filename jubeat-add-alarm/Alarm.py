from os import write
import tkinter as tk
from tkinter import StringVar, ttk
import random
import datetime

from pygame import Color
#セットした時間、音楽をsetting.txtから読み込み、リターンする
#settingsリストは[アラームセット時刻の時, アラームセット時刻の分, アラーム音, After関数用のID ]
def read_setting():
    with open('setting.txt', 'r')as f:
        settings = f.read().split('\n')
        print('ファイル読み込み：'+str(settings))
    return settings
#セットした時間、音楽をsetting.txtに書き込み
def write_setting(settings):
    with open('setting.txt', 'wt') as f:
        for num in range(4):
            f.write(settings[num]+'\n')
        print('ファイル書き込み：'+str(settings))
def calc_time_delta(time_h, time_m): #入力時刻-現在時刻を計算して秒単位で返す
    now=datetime.datetime.now()
    print('現在時刻：'+str(now))
    now = now.hour*3600 + now.minute*60 + now.second
    print('現在時刻：'+str(now)+'秒')
    time = int(time_h)*3600 + int(time_m)*60
    print('アラーム時刻：'+str(time)+'秒')
    if time-now >= 0:
        return time-now
    else:
        return time-now+86400
class AlarmFrame(ttk.Frame): # アラーム画面描画
    #コンストラクタ
    def __init__(self, master, func, frame_jubeat):
        super().__init__(master)
        settings = read_setting() 
        #アラームセット時刻のラベル
        label1 = ttk.Label(
            self,
            text = 'アラームセット時刻',
            foreground='#FFB340',
            font = ('游ゴシック', '32', 'bold', 'underline'),
        )
        label1.place(x=24, y=35)
        #現在のセット時刻のラベル
        now_setting = StringVar()
        now_setting.set('現在のセット時刻：'+settings[0]+':'+settings[1])
        label2 = ttk.Label(
            self,
            textvariable= now_setting,
            foreground='#6B6B72',
            font = ('メイリオ', '18')
        )
        label2.place(x=78, y=200)
        #時間のコンボボックス
        hours = []
        for n in range(25):
            hours.append(str(n).zfill(2))
        h = StringVar()
        cb_hour=ttk.Combobox(self, textvariable=h, values=hours, width=2, height=13, font='MSゴシック 32 bold')
        cb_hour.set(settings[0])
        cb_hour.place(x=117,y=140)
        #時間と分の間のコロンのラベル
        label3 = ttk.Label(
            self,
            text = '：',
            font = ('游ゴシック', '32', 'bold')
        )
        label3.place(x=197, y=140)
        #分のコンボボックス
        minutes = []
        for n in range(61):
            minutes.append(str(n).zfill(2))
        m = StringVar()
        cb_minutes=ttk.Combobox(self, textvariable=m, values=minutes, width=2, height=15, font='MSゴシック 32 bold')
        cb_minutes.set(settings[1])
        cb_minutes.place(x=252,y=140)
        #セットのボタン
        def button1_clicked(a):#セットボタンを押したときに実行される関数
            settings[0] = h.get()
            settings[1] = m.get()
            settings[2] = mn.get()
            write_setting(settings)
            settings[3] = alarm(self, func, frame_jubeat)
            #曲選択がランダムだった場合にランダムな曲名をsettingsに格納
            #曲数が増えたらrandit(a,b)のbを曲数に変える
            if mn.get() == 'random':
                settings[2]=music_names[random.randint(1, 2)]
            write_setting(settings)
            now_setting.set('現在のセット時刻：'+settings[0]+':'+settings[1])
        button1 = tk.Button(self, text='OK',bg='#FFB304', fg='#FFFFFF', width=5, font='游ゴシック 21 bold')
        button1.bind('<Button-1>',button1_clicked, self)
        button1.place(x=173, y=500)
        #アラームのラベル
        label4 = ttk.Label(
            self,
            text = 'アラーム音',
            foreground='#FFB340',
            font = ('游ゴシック', '32', 'bold', 'underline')
        )
        label4.place(x=110, y=300)
        #アラームのコンボボックス
        music_names = ['random', '楽しみキッズ', 'かえるのピアノ']
        mn = StringVar()
        cb_music=ttk.Combobox(self, textvariable=mn, values=music_names, width=15, height=5, font='MSゴシック 24 bold')
        cb_music.set(settings[2])
        cb_music.place(x=75,y=370)

        #アラームを実際に実行する関数(セットボタンを押したときに呼び出される)
        def alarm(frame_alarm, func, frame_jubeat): #funcはメイン関数から定義, frame_jubeatはfuncの引数
            settings = read_setting()
            time_delta = calc_time_delta(settings[0], settings[1])
            print('アラームまでの時間：'+str(time_delta)+'秒')
            frame_alarm.after_cancel(settings[3]) #前回設定したアラームのスケジュールを削除
            settings[3] = frame_alarm.after(time_delta*1000, func, frame_jubeat) #新しくアラームのスケジュールを設定
            write_setting(settings)
            return settings[3]


