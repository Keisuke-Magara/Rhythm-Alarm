#coding: utf-8

import time

class Score:
    
    max_score = 100
    score = None

    #コンストラクタ
    def __init__(self, i, ):
        self.score = 0

        
    #スコアの変化（呼び出されてから1秒後に最高点に達し、2秒後に0に戻って終了
    def determineScore(self):
        start = time.perf_counter()
        while True:
            Time = time.perf_counter() - start
            self.score = 2
            print(self.score)
            if (Time >= 2):
                self.score = 0
                break
        
    #スコアの呼び出し
    def getScore(self):
        return self.score