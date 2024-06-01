"""
WireGuard_ConfFileGenerator
(C) 2024 yuito723(https://github.com/yuito723)
"""

import tkinter as tk
import tkinter.ttk as ttk
import subprocess as sub

class Main(): # メイン画面
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x500")
        self.master.resizable(False, False)
        self.master.iconbitmap("./system/yuito723_circle.ico")
        self.master.title(f"WireGuard_ConfFileGenerator-{version}")
        self.master.configure(background = "white")
        self.master.focus_force()

        style = ttk.Style() # スタイル設定
        style.theme_use("clam")
        style.configure("TFrame", background = "white")
        style.configure("TNotebook", background = "white")
        style.configure("TNotebook.Tab", width = 300, font = ("Yu Gothic UI", 35, "bold"), anchor = "center", background = "whitesmoke")
        style.configure("TLabel", font = ("Yu Gothic UI", 15), anchor = "center", background = "white")
        style.configure("bold.TLabel", font = ("Yu Gothic UI", 25, "bold"), anchor = "center", background = "white")
        style.configure("logo.TLabel", background = "white")
        style.configure("TButton", font = ("Yu Gothic UI", 25, "bold"), background = "whitesmoke")
        style.configure("TSeparator", background = "white")
        style.map("TNotebook.Tab", background = [("selected", "white")])
        style.map("TButton", background = [("active", "whitesmoke"), ("disabled", "lightgray")])

        self.main()

    def main(self):
        pass

root = tk.Tk()
version = "v0.0.0"
app = Main(root)
root.mainloop()
