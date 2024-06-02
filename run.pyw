"""
WireGuard_ConfFileGenerator-v0.0.0
(C) 2024 yuito723(https://github.com/yuito723)
"""

import tkinter as tk
import subprocess as sub

class Window(): # ウィンドウ
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.iconbitmap("./system/yuito723_circle.ico")
        self.master.title(f"WireGuard_ConfFileGenerator-{version}")
        self.master.focus_force()

        self.main()

    def main(self):
        frame = tk.Frame(self.master, padx = "5", pady = "5")
        frame.pack()

        label = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "サーバーのアドレス")
        label.grid(row = 0, column = 0, padx = 5, pady = 5)
        label = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "サーバーのポート")
        label.grid(row = 1, column = 0, padx = 5, pady = 5)
        label = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "クライアントの数")
        label.grid(row = 2, column = 0, padx = 5, pady = 5)

        entry = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry.grid(row = 0, column = 1, padx = 5, pady = 5)
        entry = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry.grid(row = 1, column = 1, padx = 5, pady = 5)
        entry = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry.grid(row = 2, column = 1, padx = 5, pady = 5)

        button = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "生成する", command = "")
        button.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = "nsew")




# class Window(): # ウィンドウ
#     def __init__(self, master):
#         self.master = master
#         # self.master.geometry("500x300")
#         self.master.resizable(False, False)
#         self.master.iconbitmap("./system/yuito723_circle.ico")
#         self.master.title(f"WireGuard_ConfFileGenerator-{version}")
#         self.master.configure(background = "white")
#         self.master.focus_force()

#         style = ttk.Style() # スタイル設定
#         style.theme_use("vista")
#         style.configure("TFrame", background = "white")
#         style.configure("TLabel", font = ("Yu Gothic UI", 15, "bold"), anchor = "center", background = "white")
#         style.configure("TEntry", background = "white")
#         style.configure("TButton", font = ("Yu Gothic UI", 15, "bold"), background = "white")


class Generator():
    def __init__(self):
        pass

root = tk.Tk()
version = "v0.0.0"
app = Window(root)
root.mainloop()
