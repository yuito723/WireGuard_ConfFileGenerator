"""
WireGuard_ConfFileGenerator-v1.0.0
(C) 2024 yuito723(https://github.com/yuito723)
"""

import tkinter as tk
import subprocess as sub

class Window(): # ウィンドウ
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.iconbitmap("./icon.ico")
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
        label_2 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "DNSサーバーのアドレス")
        label_2.grid(row = 2, column = 0, padx = 5, pady = 5)
        label_3 = tk.Label(frame, font = ("Yu Gothic UI", 15, "bold"), text = "クライアントの数")
        label_3.grid(row = 3, column = 0, padx = 5, pady = 5)

        entry_0 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_0.grid(row = 0, column = 1, padx = 5, pady = 5)
        entry_1 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_1.grid(row = 1, column = 1, padx = 5, pady = 5)
        entry_2 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_2.grid(row = 2, column = 1, padx = 5, pady = 5)
        entry_3 = tk.Entry(frame, font = ("Yu Gothic UI", 15, "bold"))
        entry_3.grid(row = 3, column = 1, padx = 5, pady = 5)

        button_0 = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "設定ファイルを生成", command = lambda : Generator(entry_0.get(), entry_1.get(), entry_2.get(), entry_3.get()))
        button_0.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = "nsew")
        button_1 = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "アプリの終了", command = lambda : self.master.destroy())
        button_1.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = "nsew")
        button_2 = tk.Button(frame, font = ("Yu Gothic UI", 15, "bold"), text = "フォルダを削除", command = lambda : sub.run("rmdir /s /q %HOMEPATH%\Desktop\WireGuard_ConfFileGenerator", shell = True, capture_output = True))
        button_2.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = "nsew")

class Generator(): # 生成
    def __init__(self, entry_0, entry_1, entry_2, entry_3):
        self.entry_0 = str(entry_0) # サーバーのアドレス
        self.entry_1 = int(entry_1) # サーバーのポート
        self.entry_2 = str(entry_2) # DNSサーバーのアドレス
        self.entry_3 = int(entry_3) # クライアントの数

        self.genkey()
        self.output_conf()

    def genkey(self): # 鍵の生成
        sub.run("wg genkey > server.key", shell = True, capture_output = True)
        sub.run("type server.key | wg pubkey > server.pub", shell = True, capture_output = True)
        for i in range(self.entry_3):
            sub.run(f"wg genkey > client{i + 2}.key", shell = True, capture_output = True)
            sub.run(f"type client{i + 2}.key | wg pubkey > client{i + 2}.pub", shell = True, capture_output = True)
            sub.run(f"wg genkey > client{i + 2}_preshared.key", shell = True, capture_output = True)

    def output_conf(self): # 設定ファイルの生成
        with open("server.key", "r", encoding = "utf-8") as f:
            server_key = f.read().strip()
        with open("server.pub", "r", encoding = "utf-8") as f:
            server_pub = f.read().strip()
        for i in range(self.entry_3):
            with open(f"client{i + 2}.key", "r", encoding = "utf-8") as f:
                g = f.read().strip()
                exec(f"self.client{i + 2}_key = g")
            with open(f"client{i + 2}.pub", "r", encoding = "utf-8") as f:
                g = f.read().strip()
                exec(f"self.client{i + 2}_pub = g")
            with open(f"client{i + 2}_preshared.key", "r", encoding = "utf-8") as f:
                g = f.read().strip()
                exec(f"self.client{i + 2}_preshared_key = g")

        wg0 = f"""#server1
[Interface]
Address = 192.168.5.1/24
SaveConfig = true
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
ListenPort = {self.entry_1}
PrivateKey = {server_key}
"""

        for i in range(self.entry_3):
            exec(f"self.client_pub = self.client{i + 2}_pub")
            exec(f"self.client_preshared_key = self.client{i + 2}_preshared_key")
            wg0 += f"""
#client{i + 2}
[Peer]
PublicKey = {self.client_pub}
PresharedKey = {self.client_preshared_key}
AllowedIPs = 192.168.5.{i + 2}/32
"""

        with open("wg0.conf", "w", encoding = "utf-8") as f:
            f.write(wg0)

        for i in range(self.entry_3):
            exec(f"self.client_key = self.client{i + 2}_key")
            exec(f"self.client_preshared_key = self.client{i + 2}_preshared_key")
            client = f"""#client{i + 2}
[Interface]
Address = 192.168.5.{i + 2}/24
DNS = {self.entry_2}
PrivateKey = {self.client_key}

[Peer]
PublicKey = {server_pub}
PresharedKey = {self.client_preshared_key}
AllowedIPs = 0.0.0.0/0
Endpoint = {self.entry_0}:{self.entry_1}
PersistentKeepalive = 25
"""
            with open(f"client{i + 2}.conf", "w", encoding = "utf-8") as f:
                f.write(client)

        sub.run("mkdir %HOMEPATH%\Desktop\WireGuard_ConfFileGenerator\keys %HOMEPATH%\Desktop\WireGuard_ConfFileGenerator\generated", shell = True, capture_output = True)
        sub.run("del /s /q %HOMEPATH%\Desktop\WireGuard_ConfFileGenerator", shell = True, capture_output = True)
        sub.run("move *.key %HOMEPATH%\Desktop\WireGuard_ConfFileGenerator\keys", shell = True, capture_output = True)
        sub.run("move *.pub %HOMEPATH%\Desktop\WireGuard_ConfFileGenerator\keys", shell = True, capture_output = True)
        sub.run("move *.conf %HOMEPATH%\Desktop\WireGuard_ConfFileGenerator\generated", shell = True, capture_output = True)

root = tk.Tk()
version = "v1.0.0"
app = Window(root)
root.mainloop()
