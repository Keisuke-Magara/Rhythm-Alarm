from tkinter import ttk
import Timer

class Panel (ttk.Button):
    def __init__ (self, master, referto, text=None, padding=None):
        super().__init__(master)
        self.configure(command= lambda: self.callfor(referto))
        if (text != None):
            self.configure(text=text)
        if (padding != None):
            self.configure(padding=padding)
        
    
    def callfor(self, referto):
        if (referto.music_status == 1):
            n = (self.cget("text")) # ボタンナンバー取得
            place = []
            for i in range(9):
                if (i==n):
                    place.append(1)
                else:
                    place.append(0)
            place.insert(0, int(referto.timer.get_time()))
            referto.music_score.append(place)