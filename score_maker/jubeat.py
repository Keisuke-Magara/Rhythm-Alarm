import tkinter as tk
from tkinter import ttk
import Panel
import os
import sys
import pygame
import Timer
import time
from mutagen.mp3 import MP3
import shutil

class jubeat (ttk.Frame):
    def __init__ (self, master):
        super().__init__(master)
        pygame.mixer.init()
        self.msg = tk.StringVar()
        self.msg.set("こんにちは！\"OpenFile\"ボタンから\n音楽ファイルを選択してください。")
        self.music_name = tk.StringVar()
        self.music_name.set("Music Name : " + "______.mp3" + "\n　---> Output : " + "______.score")
        self.music_time = "--:--"
        self.playing_time = "--:--"
        self.Musicfilepath = None
        self.outputfile = None
        self.newMusicName = None
        self.overwrite = False
        self.panel = []
        self.timer = Timer.MusicTimer()
        self.time_info = tk.StringVar()
        self.music_status = -1 # -1:unload, 0:haven't started yet, 1:playing, 2:pausing
        self.music_score = []
        self.create_widgets()
        self.refresh_music_time()
    
    def refresh_music_time(self):
        if (self.music_status == 1 and pygame.mixer.music.get_busy() == 0):
            self.stop_music()
            self.save_file()
            return False
        else:
            sec = self.timer.get_time() / 1000
            min = int(sec/60)
            sec = int(sec - 60*min)
            self.playing_time = str(min) + ":" + str(sec).zfill(2)
            self.time_info.set(self.playing_time + " / " + self.music_time)
            return True
    
    def create_widgets(self):
        # Put control buttons.
        self.help_button = tk.Button(master=self, bg="gold3", font=("MSゴシック", "12", "bold"), text="HELP!!", command=lambda : self.showHELP(), width=5, height=2)
        self.help_button.place(x=380, y=10)
        # Put message area.
        self.msg_area = tk.Label(master=self, bg="DarkCyan", font=("游ゴシック Light", "15", "normal"), height=2, width=30, justify="center", textvariable=self.msg)
        self.msg_area.place(x=0, y=10)
        # Show played music name.
        self.music_name_area = tk.Label(master=self, bg="gainsboro", font=("游ゴシック", "15", "bold"), height=2, width=30, justify="center", textvariable=self.music_name)
        self.music_name_area.place(x=0, y=100)
        # Show play time.
        self.music_time_area = tk.Label(master=self, font=("Segoe UI Black", "30", "bold"), height=1, width=15, justify="center", textvariable=self.time_info)
        self.music_time_area.place(x=120, y=180)
        # Put help button.
        self.load_button = tk.Button(master=self, bg="#b0b0b0", font=("游ゴシック", "12", "bold"), text="Open\nFile", command=lambda: self.load_music(), width=5, height=2)
        self.load_button.place(x=380, y=100)
        # Put control buttons.
        self.play_button = tk.Button(master=self, bg="green3", font=("MSゴシック", "15", "bold"), text="▶ Play", command=lambda: self.play_music(), width=6, height=2)
        self.play_button.place(x=0, y=180)
        self.stop_button = tk.Button(master=self, bg="red3", font=("MSゴシック", "15", "bold"), text="■ STOP", command=lambda: self.stop_music(), width=6, height=2)
        self.stop_button.place(x=100, y=180)
        # Put 9 panels.
        for i in range(10):
            width = 35 # Tkinter size
            height = 56 # Tkinter size
            self.panel.append(Panel.Panel(master=self, text=i, padding=(width, height, width, height), referto=self))
        offset = 255
        self.panel[0].place(x=0, y=0.1 + offset)
        self.panel[1].place(x=145, y=0.1 + offset)
        self.panel[2].place(x=290, y=0.1 + offset)
        self.panel[3].place(x=0, y=137 + offset)
        self.panel[4].place(x=145, y=137 + offset)
        self.panel[5].place(x=290, y=137 + offset)
        self.panel[6].place(x=0, y=274 + offset)
        self.panel[7].place(x=145, y=274 + offset)
        self.panel[8].place(x=290, y=274 + offset)

    def showHELP (self):
        tk.messagebox.showinfo("使い方", "1. 譜面を作りたい音楽ファイルを\"OpenFile\"から読み込んで下さい。\n2. Playボタンを押すと再生されるので実際にパネルをクリックして譜面を作ります。\n＊再生と一時停止しかできないので、譜面を打ち間違えた場合は最初からやり直してください。\n3.曲が全て終了すると、このソフトがあるフォルダに保存されます。")

    def load_music (self):
        try:
            self.Musicfilepath = tk.filedialog.askopenfilename(filetypes=[("音楽ファイル", "*.mp3")], initialdir=os.path.abspath(os.path.dirname(__file__)))
            pygame.mixer.music.load(self.Musicfilepath)
            temp = self.Musicfilepath.split("/")
            name = temp[len(temp)-1].split(".")
            self.music_name.set("Music Name : " + name[0] + "." + name[1] + "\n　---> Output : " + name[0] + ".score")
            self.outputfile = str(name[0]) + ".score"
            self.newMusicName = str(name[0])
            if (os.path.isfile("./assets/" + self.outputfile)):
                response = tk.messagebox.askokcancel("上書き警告", "今から作成しようとしている譜面ファイル " + self.outputfile + " は既に存在するようです。\n譜面ファイルを上書きして続けますか？")
                if (response==False):
                    sys.exit()
                else:
                    self.overwrite = True
            self.music_status = 0
            self.msg.set("ファイルの読み込み完了\n\"▶Play\"ボタンをクリックで再生開始")
            audio = MP3(self.Musicfilepath)
            min = int(audio.info.length / 60)
            sec = int(audio.info.length - 60*min)
            self.music_time = str(min) + ":" + str(sec).zfill(2)
            self.timer.reset()
            self.refresh_music_time()
        except pygame.error:
            pass

    def play_music (self):
        try:
            time.sleep(1)
            if (self.music_status == 0 or self.music_status == 2 or self.music_status == 1):
                if (self.music_status == 0):
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.unpause()
                self.timer.start()
                self.music_status = 1
                self.msg.set("<<再生中>>\nパネルをクリックして譜面を作成")
            else:
                self.msg.set("音楽の再生に失敗しました。\nファイルを確認してください。")

        except pygame.error:
                self.msg.set("音楽の再生に失敗しました。\nファイルを確認してください。")

    def stop_music(self):
        if self.music_status == 1:
            pygame.mixer.music.pause()
            self.timer.stop()
            self.music_status = 2
            self.msg.set("<<再生一時停止中>>\n\"▶Play\"ボタンをクリックして再開")

    def save_file (self):
        try:
            os.mkdir("assets/")
        except FileExistsError:
            pass
        with open("./assets/" + self.outputfile, "w") as f:
            f.write(str(len(self.music_score)) + " " + str(int(self.timer.get_time()+1000)) + " 0 0 0 0 0 0 0 0\n")
            for i in range (len(self.music_score)):
                for j in range(10):
                    f.write(str(self.music_score[i][j]) + " ")
                f.write("\n")
        if (os.path.exists(self.newMusicName + ".mp3") == False):
            try:
                shutil.copyfile(self.Musicfilepath, "./assets/" + self.newMusicName + ".mp3")
            except:
                tk.messagebox.showerror("楽曲ファイルコピー失敗", "楽曲ファイルをassetsフォルダに移動することに失敗しました。\n手動での移動をお願いします。")
        if (self.overwrite):
            try:
                data = None
                with open("./music_names.txt", "r", encoding="utf-8") as f:
                    data = f.readlines() # ファイル内容を読み込み
                newnum = int(data[0].replace("\n", " "))+1 # 曲数+1
                data.append("\n" + self.newMusicName) # 曲リストに新しい曲を追加
                del data[0] # 曲数の部分を削除
                with open("./music_names.txt", "w", encoding="utf-8") as f:
                    f.write(str(newnum) + "\n") # 更新した曲数を書き込み
                    for i in range(len(data)):
                        f.write(data[i]) # 更新した曲名リストを書き込み
                res = tk.messagebox.showinfo("保存完了！", "曲が書き込まれました。\n場所: " + os.getcwd() + "\\assets\\" + self.outputfile)
                if (res == 'ok'):
                    sys.exit()
            except FileNotFoundError:
                res = tk.messagebox.showwarning("保存完了 - 警告", "曲が書き込まれました。\n場所: " + os.getcwd() + "\\assets\\" + self.outputfile + "\n\nerror: 新しいアラームをデータベースに登録できませんでした。\n音楽ファイル, scoreファイルをRhythm_alarm.pyがあるディレクトリのassetsフォルダ内に移動し、music_names.txtを編集してください。")
                if (res == 'ok'):
                    sys.exit()
        else:
            res = tk.messagebox.showwarning("保存完了 - 警告", "曲が書き込まれました。\n場所: " + os.getcwd() + "\\assets\\" + self.outputfile + "\n\nerror: 新しいアラームをデータベースに登録できませんでした。\n音楽ファイル, scoreファイルをRhythm_alarm.pyがあるディレクトリのassetsフォルダ内に移動し、music_names.txtを編集してください。")
            if (res == 'ok'):
                sys.exit()