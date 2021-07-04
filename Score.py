#coding: utf-8

import time

class Score:

    max_score = 100

    #コンストラクタ
    def __init__(self):
        score = 0
         
    #スコアの変化（呼び出されてから1秒後に最高点に達し、2秒後に0に戻って終了
    def determineScore(self):
        start = time.perf_counter()
        while True:
            time = time.perf_counter() - start
            score = -max_score*(time-1)**2 + max_score
            if (time >= 2):
                score = 0
                break
        
    #スコアの呼び出し
    def getScore(self):
        return score