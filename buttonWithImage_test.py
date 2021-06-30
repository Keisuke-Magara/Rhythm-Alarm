import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class ImgButton (tk.Button):
    img = Image.open("./buttonImageTest.png")
    img = ImageTk.PhotoImage(img)

    def __init__(self, master):
        self(master, image=img, command=self.callfor())

def callfor():
    def inner():
        print("Push Detected.")
    return inner

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("360x250")
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, padx=20, pady=10)
    button = ttk.Button(frame, image=img, command=callfor())
    button.pack()
    root.mainloop()
