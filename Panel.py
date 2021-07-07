import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sound
class Panel(ttk.Button):
    bright:bool = False
    defaultImg_name = "./default.png"
    brightImg_name = "./Box.gif" # 128*128px

    def __init__ (self, master=None, text=None, imageName=None, name=None, padding=None, width=None):
        super().__init__(master=master, name=name, width=width)
        self.defaultimg = None
        self.bright_img = None
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
        if (padding != None):
            self.configure(padding=padding)
    
    def bright(self):
        try:
            self.configure(image=self.bright_img)
            self.bright_img.configure(format="gif -index {}".format(self.gif_index))
            self.gif_index += 1
            print("bright")
        except tk.TclError:
            self.gif_index = 0
            #self.set_default()
        else:
            root.after(143, self.bright)

    

    def callfor(self): # ボタンが押されたときに実行される処理 (panelが押されたパネルを示す)
        print("pushd")

    #def refresh(): #ボタンのプロパティを反映する関数

    #def bright(self)
    #def debright()


if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack(fill = tk.BOTH, padx=20,pady=10)
    panel = Panel(root)
    panel.pack()
    panel.bright()
    root.mainloop()