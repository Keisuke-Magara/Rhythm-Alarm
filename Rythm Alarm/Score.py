#codig: utf-8

import time

class Score:

    bad = 1000 #判定範囲(±ms)
    good = 300 #(±ms)
    great = 150 #(±ms)
    perfect = 60 #(±ms)
    tile1 = []
    tile2 = []
    tile3 = []
    tile4 = []
    tile5 = []
    tile6 = []
    tile7 = []
    tile8 = []
    tile9 = []
 
    #コンストラクタ
    def __init__(self, music_list):
        self.score = 0
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][1] == '1':
                self.tile1.append(int(music_list[i][0]))
        #print('tile1:'+str(self.tile1))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][2] == '1':
                self.tile2.append(int(music_list[i][0]))
        #print('tile2:'+str(self.tile2))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][3] == '1':
                self.tile3.append(int(music_list[i][0]))
        #print('tile3:'+str(self.tile3))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][4] == '1':
                self.tile4.append(int(music_list[i][0]))
        #print('tile4:'+str(self.tile4))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][5] == '1':
                self.tile5.append(int(music_list[i][0]))
        #print('tile5:'+str(self.tile5))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][6] == '1':
                self.tile6.append(int(music_list[i][0]))
        #print('tile6:'+str(self.tile6))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][7] == '1':
                self.tile7.append(int(music_list[i][0]))
        #print('tile7:'+str(self.tile7))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][8] == '1':
                self.tile8.append(int(music_list[i][0]))
        #print('tile8:'+str(self.tile8))
        for i in range(1, int(music_list[0][0])+1):
            if music_list[i][9] == '1':
                self.tile9.append(int(music_list[i][0]))
        #print('tile9:'+str(self.tile9))
        
    #引数:タイルの番号i,経過時間elatime 指定したタイルの判定範囲に応じたスコアを返す
    def determineScore(self,i,elatime):
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
            self.tile = self.tile5
        elif i == 6:
            self.tile = self.tile6
        elif i == 7:
            self.tile = self.tile7
        elif i == 8:
            self.tile = self.tile8
        elif i == 9:
            self.tile = self.tile9

        #判定(perfect=100点, great=70点, good= 50点, bad=10点)
        if any(elatime-self.perfect < t < elatime+self.perfect for t in self.tile):
            self.score = 100 #perfect
        elif any(elatime-self.great < t < elatime+self.great for t in self.tile):
            self.score = 70 #great
        elif any(elatime-self.good < t < elatime+self.good for t in self.tile):
            self.score = 50 #good
        elif any(elatime-self.bad < t < elatime+self.bad for t in self.tile):
            self.score = 10 #bad
        else:
            self.score = 0 #miss
            
        return self.score