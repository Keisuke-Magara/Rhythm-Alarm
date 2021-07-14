import tkinter as tk
from tkinter import StringVar, ttk
import random
import datetime
import game_start
import sound
from PIL import Image, ImageTk
from os import name, read, times
from tkinter.constants import FLAT, NO, Y
import Score
import Timer


#セットした時間、音楽をsetting.txtから読み込み、リターンする
#settingsリストは[アラームセット時刻の時, アラームセット時刻の分, アラーム音, After関数用のID ]
def read_setting():
    with open('./setting.txt', 'r', encoding='utf-8')as f:
        settings = f.read().split('\n')
        #print('settingファイル読み込み：'+str(settings))
    f.close()
    return settings
#セットした時間、音楽をsetting.txtに書き込み
def write_setting(settings):
    with open('./setting.txt', 'wt', encoding='utf-8') as f:
        for num in range(5):
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
        self.frame_delay_test = DelayTestFrame(self, master)
        self.frame_delay_test.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
        self.GameStart=game_start.game_start(self, master)

        master.configure(background='#000000')
        self.style = ttk.Style()
        self.style.theme_create('combostyle',settings={'TCombobox':{'configure':{'background':'#000000', 'selectbackground':'#000000', 'fieldbackground':'#000000', 'foreground':'#FFFFFF'}}})
        self.style.theme_use('combostyle')
        self.style.configure('GameStyle.TFrame', background='#000000')
        super().__init__(master, style='GameStyle.TFrame')
        settings = read_setting() 
        self.tkraise()
        
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
            settings[3] = alarm(self)
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

        def button2_clicked(a):#遅延調整ボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            self.frame_delay_test.tkraise()
            self.frame_delay_test.panel.fps=self.GameStart.frame_jubeat.panel[0].fps
        button2 = tk.Button(self, text='パネルの遅延調整',bg='#000000', fg='#FFB304', width=15, font='游ゴシック 18 bold underline', relief=FLAT)
        button2.bind('<Button-1>',button2_clicked, self)
        button2.place(x=103, y=570)

        #アラームを実際に実行する関数(セットボタンを押したときに呼び出される)
        def alarm(frame_alarm):
            settings = read_setting()
            time_delta = calc_time_delta(settings[0], settings[1])
            #print('アラームまでの時間：'+str(time_delta)+'秒')
            frame_alarm.after_cancel(settings[3]) #前回設定したアラームのスケジュールを削除
            settings[3] = frame_alarm.after(time_delta*1000, self.GameStart.start) #新しくアラームのスケジュールを設定
            write_setting(settings)
            return settings[3]
class DelayTestFrame (ttk.Frame): # ゲーム画面描画
    def __init__(self, parent, master):
        self.parent = parent
        self.style = ttk.Style()
        self.style.configure("GameStyle.TFrame", background="black")
        super().__init__(master, style="GameStyle.TFrame")
        self.delay_test_fumen = [['5','12000','0','0','0','0','0','0','0','0'],['2000','1','0','0','0','0','0','0','0','0'],['4000','1','0','0','0','0','0','0','0','0'],['6000','1','0','0','0','0','0','0','0','0'],['8000','1','0','0','0','0','0','0','0','0'],['10000','1','0','0','0','0','0','0','0','0']]
        self.score = Score.Score(self.delay_test_fumen)
        self.timer = Timer.MusicTimer()
        self.panel=DelayTestPanel(master=self, name=str(0), text=str(0))
        self.panel.place(x=153, y=300)
        self.after_id=[]
        self.num=0#テスト譜面ののノーツ番号
        self.delay_sum=0
        with open("./delay.txt", "r") as f:
            self.delay = int(f.readline())

        #遅延調整のラベル
        label1 = ttk.Label(
            self,
            text = 'パネルの遅延調整',
            foreground='#FFB340',
            background='#000000',
            font = ('游ゴシック', '32', 'bold', 'underline'),
        )
        label1.place(x=47, y=35)
        #遅延調整の説明のラベル
        label2 = ttk.Label(
            self,
            text = '測定ボタンを押し、下のパネルの四角が最も大\nきくなるタイミングでクリックしてください。\n5回クリックすると遅延が計算されます。',
            foreground='#FFFFFF',
            background='#000000',
            font = ('メイリオ', '16'),
        )
        label2.place(x=0, y=100)
        #現在の遅延 ：のラベル
        label2 = ttk.Label(
            self,
            text = '現在の遅延 ：',
            foreground='#FFFFFF',
            background='#000000',
            font = ('メイリオ', '21'),
        )
        label2.place(x=75, y=220)
        #遅延のエントリー
        self.delay_entry = StringVar()
        self.delay_entry.set(self.delay)
        entry1 = ttk.Entry(self, textvariable=self.delay_entry, width =5,font='メイリオ 21 bold')
        entry1.place(x=265, y=220)
        #パネルの速度のラベル
        self.settings=read_setting()
        label1 = ttk.Label(
            self,
            text = 'パネルの速度:'+str(self.settings[4]),
            foreground='#A5A5AC',
            background='#000000',
            font = ('メイリオ', '12'),
        )
        label1.place(x=156, y=440)
        #測定ボタン
        def button1_clicked(a):#測定ボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            self.timer.reset()
            self.timer.start()
            self.num=0
            self.delay=int(self.delay_entry.get())
            for id in self.after_id:
                self.after_cancel(id)
            for i in range(0,5):
                self.after_id.append(self.after(str((i+1)*2000-int(self.delay)), self.panel.bright))
            def stop():
                self.num=-1
            self.after_id.append(self.after(12000, stop))
        button1 = tk.Button(self, text='測定',bg='#FFB304', fg='#000000', width=5, font='游ゴシック 21 bold')
        button1.bind('<Button-1>',button1_clicked, self)
        button1.place(x=100, y=500)
        #完了ボタン
        def button2_clicked(a):#完了ボタンを押したときに実行される関数
            sound.play_se('./assets/SE_button.mp3')
            self.timer.reset()
            self.delay=int(self.delay_entry.get())
            with open("./delay.txt", "w") as f:
                int(f.write(str(self.delay)))
            for id in self.after_id:
                self.after_cancel(id)
                self.num=-1
            self.parent.tkraise()
            
        button2 = tk.Button(self, text='完了',bg='#FFB304', fg='#000000', width=5, font='游ゴシック 21 bold')
        button2.bind('<Button-1>',button2_clicked, self)
        button2.place(x=248, y=500)

    def calc_delay(self):
        if -1<self.num<5:
            self.delay_sum += self.timer.get_time() - (self.num+1)*2000
            if self.num==4:
                self.num=-1
                self.delay += int(self.delay_sum/5)
                self.delay_sum=0
                self.delay_entry.set(self.delay)
            else:
                self.num+=1
        else:
            self.num=-1
        
        


class DelayTestPanel(ttk.Button):
    bright:bool = False
    defaultImg_name = "./assets/default.png"
    brightImg_name = "./assets/Box.gif" # 128*128px
    perfectImg_name = "./assets/perfect.png" # 128*128px
    greatImg_name = "./assets/great.png" # 128*128px
    goodImg_name = "./assets/good.png" # 128*128px
    badImg_name = "./assets/bad.png" # 128*128px

    def __init__ (self, master, text=None, imageName=None, name=None, padding=None, width=None):
        self.fps=28#panelを参照して上書きされるため、書き換える必要はないです
        self.parent = master
        self.style = ttk.Style()
        self.style.configure("GameStyle.TButton", background="Black")
        super().__init__(master=master, name=name, width=width)
        self.defaultimg = None
        self.bright_img = None
        self.moveable = False
        self.root = master
        self.gif_index = 0
        self.configure(command=lambda:self.callfor())
        if (text != None):
            self.configure(text=text)
        if (imageName != None):
            self.defaultImg_name = imageName
        self.default_img = tk.PhotoImage(file=self.defaultImg_name)
        self.configure(image=self.default_img)
        self.bright_img = tk.PhotoImage(file=self.brightImg_name)
        self.perfect_img = tk.PhotoImage(file=self.perfectImg_name)
        self.great_img = tk.PhotoImage(file=self.greatImg_name)
        self.good_img = tk.PhotoImage(file=self.goodImg_name)
        self.bad_img = tk.PhotoImage(file=self.badImg_name)
        if (padding != None):
            self.configure(padding=padding)

    def bright(self):
        self.moveable = True
        self.next_frame()

    def next_frame(self):
        try: #(2)show_wellの表示が上書きされないようにself.moveable == trueの条件を加えた
            if self.moveable == True:
                self.configure(image=self.bright_img)
                self.bright_img.configure(format="gif -index {}".format(self.gif_index))
                self.gif_index += 1
        except tk.TclError:
            if self.moveable == True:
                self.set_default()
        else:
            if self.moveable == True:
                self.after(int(1000/self.fps), self.next_frame)

    def callfor(self): # ボタンが押されたときに実行される処理 (panelが押されたパネルを示す)
        self.moveable = False
        sound.play_se('./assets/SE_panel.mp3') #(3)ボタンを押したときにSEを流す
        cur_score = self.parent.score.determineScore(int(1), int(self.parent.timer.get_time()))
        self.show_well(cur_score)
        #self.root.after(int(1000/self.fps), self.show_well(cur_score))
        self.parent.calc_delay()
            
    
    def show_well (self, score):
        if (score == 100):
            self.configure(image=self.perfect_img)
        elif (score == 70):
            self.configure(image=self.great_img)
        elif (score == 50):
            self.configure(image=self.good_img)
        elif (score == 10):
            self.configure(image=self.bad_img)
        self.after(250, self.set_default)

    def set_default(self):
        self.configure(image=self.default_img)
        self.gif_index = 0

    #def refresh(): #ボタンのプロパティを反映する関数

    #def bright(self)
    #def debright()
