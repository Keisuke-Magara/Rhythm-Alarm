#coding: utf-8

import time

class Score:

    max_score = 100  #最大スコア
    passable = 1000 #判定範囲(±ms)
    good = 300
    great = 150
    perfect = 60
 
    #コンストラクタ
    def __init__(self, music_list):
        self.score = 0
        self.tile1 = [x[0] for x in music_list if x[1]==1]
        self.tile2 = [x[0] for x in music_list if x[2]==1]
        self.tile3 = [x[0] for x in music_list if x[3]==1]
        self.tile4 = [x[0] for x in music_list if x[4]==1]
        self.tile5 = [x[0] for x in music_list if x[5]==1]
        self.tile6 = [x[0] for x in music_list if x[6]==1]
        self.tile7 = [x[0] for x in music_list if x[7]==1]
        self.tile8 = [x[0] for x in music_list if x[8]==1]
        self.tile9 = [x[0] for x in music_list if x[9]==1]
        
    #時間計測
    def starting(self):
        self.start = time.perf_counter()
        while True:
            #elatime=経過時間(単位はms)
            self.elatime = (time.perf_counter() - self.start) * 1000
            time.sleep(0.01) #約0.01秒ごとに更新

         
    #引数:タイルの番号i 指定したタイルの判定範囲に応じたスコアを返す
    def determineScore(self,i):
        #タイルの指定
        if i == 1:
            self.tile = self.tile1
        elif i == 2:
            self.tile = self.tile2
        elif i == 3:
            self.tile = self.tile3
        elif i == 4:
            self.tile = self.tile4
        elif i == 5:
            self.tile = self.tile6
        elif i == 7:
            self.tile = self.tile7
        elif i == 8:
            self.tile = self.tile8
        elif i == 9:
            self.tile = self.tile9

        #判定(perfect=100点, great=70点, good= 50点, passable=10点)
        if any(self.elatime-self.perfect < t < self.elatime+self.perfect for t in self.tile):
            self.judge = 1
        elif any(self.elatime-self.great < t < self.elatime+self.great for t in self.tile):
            self.judge = 2
        elif any(self.elatime-self.good < t < self.elatime+self.good for t in self.tile):
            self.judge = 3
        elif any(self.elatime-self.passable < t < self.elatime+self.passable for t in self.tile):
            self.judge = 4
        else:
            self.judge = 0

        if self.judge = 1:
            self.score = 100
        elif self.judge = 2:
            self.score = 70
        elif self.judge = 3:
            self.score = 50
        elif self.judge = 4:
            self.score = 10
        else:
            self.score = 0

        return self.score