import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def callfor():
    def inner():
        print("Push Detected.")
    return inner

root = tk.Tk()
root.geometry("360x250")
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, padx=20, pady=10)
img = Image.open("./buttonImageTest.png")
img = ImageTk.PhotoImage(img)
button = ttk.Button(frame, image=img, command=callfor())
button.pack()

root.mainloop()