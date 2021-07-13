import tkinter as tk
from tkinter import StringVar, ttk
import random
import datetime
import game_start
import sound

#セットした時間、音楽をsetting.txtから読み込み、リターンする
#settingsリストは[アラームセット時刻の時, アラームセット時刻の分, アラーム音, After関数用のID ]
def read_setting():
    with open('./setting.txt', 'r')as f:
        settings = f.read().split('\n')
        #print('settingファイル読み込み：'+str(settings))
    f.close()
    return settings
#セットした時間、音楽をsetting.txtに書き込み
def write_setting(settings):
    with open('./setting.txt', 'wt') as f:
        for num in range(4):
            f.write(settings[num]+'\n')
        #print('ファイル書き込み：'+str(settings))
    f.close()
def calc_time_delta(time_h, time_m): #入力時刻-現在時刻を計算して秒単位で返す
    now=datetime.datetime.now()
    #print('現在時刻：'+str(now))
    now = now.hour*3600 + now.minute*60 + now.second
    #print('現在時刻：'+str(now)+'秒')
    time = int(time_h)*3600 + int(time_m)*60
    #print('アラーム時刻：'+str(time)+'秒')
    if time-now >= 0:
        return time-now
    else:
        return time-now+86400

class AlarmFrame(ttk.Frame): # アラーム画面描画
    #コンストラクタ
    def __init__(self, master):
        master.configure(background='#000000')
        self.style = ttk.Style()
        self.style.theme_create('combostyle',settings={'TCombobox':{'configure':{'background':'#000000', 'selectbackground':'#000000', 'fieldbackground':'#000000', 'foreground':'#FFFFFF'}}})
        self.style.theme_use('combostyle')
        self.style.configure('GameStyle.TFrame', background='#000000')
        super().__init__(master, style='GameStyle.TFrame')
        settings = read_setting() 
        #アラームセット時刻のラベル
        label1 = ttk.Label(
            self,
            text = 'アラームセット時刻',
            foreground='#FFB340',
            background='#000000',
            font = ('游ゴシック', '32', 'bold', 'underline'),
        )
        label1.place(x=24, y=35)
        #現在のセット時刻のラベル
        now_setting = StringVar()
        now_setting.set('現在のセット時刻：'+settings[0]+':'+settings[1])
        label2 = ttk.Label(
            self,
            textvariable= now_setting,
            foreground='#A5A5AC',
            background='#000000',
            font = ('メイリオ', '18')
        )
        label2.place(x=78, y=230)
        #時間と分の間のコロンのラベル
        label3 = ttk.Label(
            self,
            text = '：',
            foreground='#FFFFFF',
            background='#000000',
            font = ('游ゴシック', '48', 'bold')
        )
        label3.place(x=187, y=140)
        #時間のコンボボックス
        hours = []
        for n in range(24):
            hours.append(str(n).zfill(2))
        h = StringVar()
        cb_hour=ttk.Combobox(self, textvariable=h, values=hours, width=2, height=13, font='MSゴシック 48 bold')
        cb_hour.set(settings[0])
        cb_hour.place(x=107,y=140)
        #分のコンボボックス
        minutes = []
        for n in range(60):
            minutes.append(str(n).zfill(2))
        m = StringVar()
        cb_minutes=ttk.Combobox(self, textvariable=m, values=minutes, width=2, height=15, font='MSゴシック 48 bold')
        cb_minutes.set(settings[1])
        cb_minutes.place(x=242,y=140)
        #セットのボタン
        def button1_clicked(a):#セットボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            settings[0] = h.get()
            settings[1] = m.get()
            settings[2] = mn.get()
            write_setting(settings)
            settings[3] = alarm(self, master)
            #曲選択がランダムだった場合にランダムな曲名をsettingsに格納
            #曲数が増えたらrandit(a,b)のbを曲数に変える
            if mn.get() == 'random':
                settings[2]=music_names[random.randint(1, int(self.num_of_music))]
            write_setting(settings)
            now_setting.set('現在のセット時刻：'+settings[0]+':'+settings[1])
        button1 = tk.Button(self, text='OK',bg='#FFB304', fg='#000000', width=5, font='游ゴシック 21 bold')
        button1.bind('<Button-1>',button1_clicked, self)
        button1.place(x=173, y=500)
        #アラーム音のラベル
        label4 = ttk.Label(
            self,
            text = 'アラーム音',
            foreground='#FFB340',
            background='#000000',
            font = ('游ゴシック', '32', 'bold', 'underline')
        )
        label4.place(x=110, y=300)
        #アラーム音のコンボボックス
        #music_names.txtを読み込み、楽曲リストmusic_namesを作成
        with open('./music_names.txt', 'r', encoding='utf-8')as f:
            music_names = f.read().split('\n')
            #print('楽曲ファイル読み込み：'+str(music_names))
        self.num_of_music = music_names[0]
        music_names[0] = 'random'
        f.close()

        mn = StringVar()
        cb_music=ttk.Combobox(self, textvariable=mn, values=music_names, width=15, height=5, font='MSゴシック 24 bold')
        cb_music.set(settings[2])
        cb_music.place(x=75,y=370)

        #アラームを実際に実行する関数(セットボタンを押したときに呼び出される)
        def alarm(frame_alarm, root):
            settings = read_setting()
            time_delta = calc_time_delta(settings[0], settings[1])
            #print('アラームまでの時間：'+str(time_delta)+'秒')
            frame_alarm.after_cancel(settings[3]) #前回設定したアラームのスケジュールを削除
            settings[3] = frame_alarm.after(time_delta*1000, game_start.game_start, root) #新しくアラームのスケジュールを設定
            write_setting(settings)
            return settings[3]
