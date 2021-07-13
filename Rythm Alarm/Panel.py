from os import name, times
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sound
class Panel(ttk.Button):
    bright:bool = False
    defaultImg_name = "./assets/default.png"
    brightImg_name = "./assets/Box.gif" # 128*128px
    perfectImg_name = "./assets/perfect.png" # 128*128px
    greatImg_name = "./assets/great.png" # 128*128px
    goodImg_name = "./assets/good.png" # 128*128px
    badImg_name = "./assets/bad.png" # 128*128px
    fps = 28 # GIF画像は28fpsです。pyinstallerでexeファイル化するときは14fpsに設定(1/2倍速)に設定してください。

    def __init__ (self, master, score, time, text=None, imageName=None, name=None, padding=None, width=None):
        self.parent = master
        self.score = score
        self.timer = time
        self.style = ttk.Style()
        self.style.configure("GameStyle.TButton", background="blue")
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
        #self.default_img = Image.open(self.defaultImg_name)
        #self.default_img = ImageTk.PhotoImage(self.default_img)
        self.default_img = tk.PhotoImage(file=self.defaultImg_name)
        self.configure(image=self.default_img)
        self.bright_img = tk.PhotoImage(file=self.brightImg_name)
        self.perfect_img = tk.PhotoImage(file=self.perfectImg_name)
        self.great_img = tk.PhotoImage(file=self.greatImg_name)
        self.good_img = tk.PhotoImage(file=self.goodImg_name)
        self.bad_img = tk.PhotoImage(file=self.badImg_name)
        if (padding != None):
            self.configure(padding=padding)
        #self.bright()


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
                self.parent.miss += 1 #missの表示が切れたらミス数をインクリメント
                self.parent.combo = 0 #missしたのでコンボは0になる
        else:
            if self.moveable == True:
                self.root.after(int(1000/self.fps), self.next_frame)

    

    def callfor(self): # ボタンが押されたときに実行される処理 (panelが押されたパネルを示す)
        self.moveable = False
        sound.play_se('./assets/SE_panel.mp3') #(3)ボタンを押したときにSEを流す
        cur_score = self.score.determineScore(int(self.cget("text"))+1, int(self.timer.get_time()))
        self.show_well(cur_score)
        #self.root.after(int(1000/self.fps), self.show_well(cur_score))
        self.parent.total_score += cur_score
        #print(cur_score)
        if self.parent.total_score >= self.parent.goal_score:
            self.parent.parent.stop_game() #(4)終了処理を追加
            
    
    def show_well (self, score):
        self.parent.combo += 1 #ボタンが押されたらとりあえずコンボ数をインクリメント
        if (score == 100):
            self.configure(image=self.perfect_img)
            self.parent.perfect += 1 #perfect数をインクリメント
        elif (score == 70):
            self.configure(image=self.great_img)
            self.parent.great += 1 #great数をインクリメント
        elif (score == 50):
            self.configure(image=self.good_img)
            self.parent.good += 1 #good数をインクリメント
        elif (score == 10):
            self.configure(image=self.bad_img)
            self.parent.bad += 1 #bad数をインクリメント
            self.parent.combo = 0 #badだった場合はコンボ数を0にする
        if self.parent.combo > self.parent.max_combo: #最大コンボよりもコンボ数が多ければ最大コンボ数を更新
            self.parent.max_combo = self.parent.combo
        self.root.after(250, self.set_default)

    def set_default(self):
        self.configure(image=self.default_img)
        self.gif_index = 0

    #def refresh(): #ボタンのプロパティを反映する関数

    #def bright(self)
    #def debright()


if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack(fill = tk.BOTH, padx=20,pady=10)
    panel = Panel(root)
    panel.pack()
    #panel.bright()
    root.mainloop()