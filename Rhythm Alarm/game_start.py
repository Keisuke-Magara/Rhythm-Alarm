import Timer
import JubeatFrame
import Alarm
import sound
import Score
import numpy
from tkinter import messagebox
import ResultFrame
import Alarm
import math
class game_start():
    #クラス変数
    frame_jubeat = None #JubeatFrameのインスタンス
    after_id_list = [] #実行予定のアフター関数のIDを記録
    fumen_list = [] #譜面の2次元配列
    settings = [] #設定ファイルの配列

    #game_startのコンストラクタ
    def __init__(self, parent, root):
        self.root = root
        self.delay = 571
        self.settings = Alarm.read_setting()
        self.fumen_list = self.read_fumen('./assets/'+self.settings[2]+'.score')
        #print('譜面行数:'+self.fumen_list[0][0])
        fumen_for_score = numpy.delete(self.fumen_list, 0, 0) #譜面ファイルの1行目を削除
        #print('譜面:\n'+str(fumen_for_score))
        #****************************************************************
        #もし河西さんのScore.pyで正しい点数が取得できない場合は
        #少し書き換えたScore.pyをAnother_Scoreに入れたのでそれと交換した後
        #1行下のScoreの引数をself.fumen_listに変更する
        #****************************************************************
        self.score=Score.Score(self.fumen_list)
        self.timer = Timer.MusicTimer()
        self.frame_jubeat = JubeatFrame.JubeatFrame(master=root, score=self.score, parent=self, time=self.timer)
        self.frame_jubeat.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
        #self.frame_jubeat.after(15000, self.stop_game) #stop関数のテスト
        #self.frame_jubeat.after(15000, print, 'stop関数のテストのため、15秒後に自動で停止しています。game_startの39, 40行目を削除してください')
        
    #譜面読み込みをする関数, 引数はファイル名、戻り値は譜面の2次元配列
    def read_fumen(self, file):
        import sys
        data = []
        try:
            f = open(file, 'r', encoding='utf-8')
        except Exception:
            #print("open error. not found file:", str(file))
            sys.exit(1)
        for line in f:
            line = line.strip() #前後空白削除
            line = line.replace('\n','') #末尾の\nの削除
            line = line.split(" ") #分割
            data.append(line)
        f.close()
        return data
    #譜面読み込み時のafter関数で実行される関数,
    #光らせるパネル番号を譜面から読み取って指定のパネルを光らせる    
    def panel_bright(self, notenum):
        for i in range(1,10):
            if self.fumen_list[notenum][i] ==  '1':
                self.frame_jubeat.panel[i-1].bright()
                #print(str(notenum)+':'+self.fumen_list[notenum][0]+':'+str(i))
    
    def start(self):
        with open("./delay.txt", "r") as f:
            self.delay = int(f.readline())
        self.settings = Alarm.read_setting()
        self.fumen_list = self.read_fumen('./assets/'+self.settings[2]+'.score')
        self.score=Score.Score(self.fumen_list)
        self.frame_jubeat.music_name.set("アラーム音: " + self.settings[2])
        self.frame_jubeat.tkraise()
        self.repeat_game()
    #ゲームの繰り返し部分を実行する関数
    def repeat_game(self):
        #print('repeat')
        self.timer.reset()
        self.timer.start()
        sound.play_music('./assets/'+self.settings[2]+'.mp3')
        for i in range(1,int(self.fumen_list[0][0])+1):
            #print(self.fumen_list[i][0])
            self.after_id_list.append(self.frame_jubeat.after(str(int(self.fumen_list[i][0])-self.delay), self.panel_bright, i))
        self.after_id_list.append(self.frame_jubeat.after(self.fumen_list[0][1], self.repeat_game))
    #ゲームを停止する関数
    def stop_game(self):
        #print('stop')
        sound.stop_music()
        for after_id in self.after_id_list:
            self.frame_jubeat.after_cancel(after_id)
        for i in range(0,9):
            self.frame_jubeat.panel[i].moveable = False
            self.frame_jubeat.panel[i].set_default()
            self.frame_jubeat.combo = self.frame_jubeat.max_combo
        #クリアタイムを計算
        clear_m = str(math.floor((86400-Alarm.calc_time_delta(self.settings[0], self.settings[1])) / 60))
        clear_s = str((86400-Alarm.calc_time_delta(self.settings[0], self.settings[1])) % 60).zfill(2)
        clear_time = 'クリアタイム: ' + str(clear_m +'分' + clear_s + '秒')
        #メッセージボックスの表示
        if messagebox.showinfo('Rhythm Alarm!', 'CLEAR!!') == 'ok':
            #メッセージボックスのOKが押されたら画面を切り替える
            self.frame_result = ResultFrame.ResultFrame(self, self.root, clear_time)
            self.frame_result.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
            self.frame_result.tkraise()
            #def destroy_child(frame):
                #children = frame.winfo_children()
                #for child in children:
                    #child.destroy()
            #destroy_child(self.frame_jubeat)
            #self.frame_jubeat.destroy()
            #self.frame_alarm = Alarm.AlarmFrame(self.root)
            #self.frame_alarm.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)
            #self.frame_alarm.tkraise()