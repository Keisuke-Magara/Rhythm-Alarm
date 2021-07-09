try:
    import Tkinter as tk
except:
    import tkinter as tk
    

    
root = tk.Tk()
root.geometry("480x720")
root.title("The jubeat alarm!")
root.resizable(width=False, height=False)
root.configure(bg="black")
#rootメインウィンドウのグリッドを1x1にする
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
#画面ごとにFrameを作成
root.mainloop()