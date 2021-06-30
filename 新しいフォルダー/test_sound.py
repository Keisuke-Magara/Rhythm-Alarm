import sound
import tkinter
def botton1_clicked(a):
    sound.play_music(music_name='kaerunopiano.mp3')
def botton2_clicked(a):
    sound.stop_music()
def botton3_clicked(a):
    sound.play_se(se_name='suzu.mp3')
#ウィンドウ
root = tkinter.Tk()
root.title('test_sound')
#音楽再生ボタン
img1 = tkinter.PhotoImage(file='play_icon.png').subsample(2,2)
button1 = tkinter.Button(text='再生', image=img1, compound='top')
button1.bind('<Button-1>',botton1_clicked)
button1.grid(column=0, row=0)
#効果音停止ボタン
img2 = tkinter.PhotoImage(file='stop_icon.png').subsample(2,2)
button2 = tkinter.Button(text='停止', image=img2, compound='top')
button2.bind('<Button-1>',botton2_clicked)
button2.grid(column=1, row=0)
#効果音再生ボタン
button3 = tkinter.Button(text='効果音', width=22, height=11)
button3.bind('<Button-1>',botton3_clicked)
button3.grid(column=0, row=1)



root.mainloop()
