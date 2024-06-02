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

        label_0 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "サーバーのアドレス")
        label_0.grid(row = 0, column = 0, padx = 5, pady = 5)
        label_1 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "サーバーのポート")
        label_1.grid(row = 1, column = 0, padx = 5, pady = 5)
        label_2 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "クライアントの数")
        label_2.grid(row = 2, column = 0, padx = 5, pady = 5)

        entry_0 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_0.grid(row = 0, column = 1, padx = 5, pady = 5)
        entry_1 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_1.grid(row = 1, column = 1, padx = 5, pady = 5)
        entry_2 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_2.grid(row = 2, column = 1, padx = 5, pady = 5)

        button = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "生成する", command = lambda : Generator(entry_0.get(), entry_1.get(), entry_2.get()))
        button.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = "nsew")

class Generator():
    def __init__(self, entry_0, entry_1, entry_2):
        self.entry_0 = entry_0
        self.entry_1 = entry_1
        self.entry_2 = entry_2

        self.main()
        self.genkey()

    def main(self):
        print(self.entry_0)
        print(self.entry_1)
        print(self.entry_2)

    def genkey(self):
        sub.run("wg genkey > server.key", shell = True)
        sub.run("type server.key | wg pubkey > server.pub", shell = True)
        for i in range(int(self.entry_2)):
            sub.run(f"wg genkey > client{i + 2}.key", shell = True)
            sub.run(f"type client{i + 2}.key | wg pubkey > client{i + 2}.pub", shell = True)
            sub.run(f"wg genkey > client{i + 2}-preshared.key", shell = True)

    def genconf():
        pass

root = tk.Tk()
version = "v0.0.0"
app = Window(root)
root.mainloop()
