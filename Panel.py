from os import name, times
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sound
class Panel(ttk.Button):
    bright:bool = False
    defaultImg_name = "./default.png"
    brightImg_name = "./Box.gif" # 128*128px
    perfectImg_name = "./perfect.png"
    greatImg_name = "./great.png"
    goodImg_name = "./good.png"
    badImg_name = "./bad.png"
    fps = 30

    def __init__ (self, master, score, time, text=None, imageName=None, name=None, padding=None, width=None):
        self.parent = master
        self.score = score
        self.timer = time
        self.style = ttk.Style()
        self.style.configure("GameStyle.TButton", background="black")
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
        self.bright()
    

    def bright(self):
        self.moveable = True
        self.next_frame()
    
    def next_frame(self):
        try:
            self.configure(image=self.bright_img)
            self.bright_img.configure(format="gif -index {}".format(self.gif_index))
            self.gif_index += 1
        except tk.TclError:
            self.set_default()
        else:
            if (self.moveable):
                self.root.after(int(1000/self.fps), self.next_frame)

    

    def callfor(self): # ボタンが押されたときに実行される処理 (panelが押されたパネルを示す)
        self.moveable = False
        cur_socre = self.score.determineScore(int(self.cget(name)), self.timer.get_time())
        self.root.after(int(1000/self.fps), self.show_well(cur_socre))
        self.parent.total_score += cur_socre
    
    def show_well (self, score):
        if (cur_score == 100):
            self.configure(image=self.perfect_img)
        elif (cur_score == 70):
            self.configure(image=self.great_img)
        elif (cur_socre == 50):
            self.configure(image=self.good_img)
        elif (cur_socre == 10):
            self.configure(image=self.bad_img)
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