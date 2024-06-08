import subprocess as sub

# 変数
client_number = 4
port = 51820
address = "example.com"
dns = "dns.example.com"

# output "server.key", "server.pub", "client*.key", "client*.pub", "client*-preshared.key"
sub.run("wg genkey > server.key", shell = True, capture_output = True)
sub.run("type server.key | wg pubkey > server.pub", shell = True, capture_output = True)
for i in range(client_number):
    sub.run(f"wg genkey > client{i + 2}.key", shell = True, capture_output = True)
    sub.run(f"type client{i + 2}.key | wg pubkey > client{i + 2}.pub", shell = True, capture_output = True)
    sub.run(f"wg genkey > client{i + 2}_preshared.key", shell = True, capture_output = True)

# read keys
with open("server.key", "r", encoding = "utf-8") as f:
    server_key = f.read().strip()

with open("server.pub", "r", encoding = "utf-8") as f:
    server_pub = f.read().strip()

for i in range(client_number):
    with open(f"client{i + 2}.key", "r", encoding = "utf-8") as f:
        g = f.read().strip()
        exec(f"client{i + 2}_key = g")
    with open(f"client{i + 2}.pub", "r", encoding = "utf-8") as f:
        g = f.read().strip()
        exec(f"client{i + 2}_pub = g")
    with open(f"client{i + 2}_preshared.key", "r", encoding = "utf-8") as f:
        g = f.read().strip()
        exec(f"client{i + 2}_preshared_key = g")

# output "wg0.conf"
wg0 = f"""#server1
[Interface]
Address = 192.168.5.1/24
SaveConfig = true
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
ListenPort = {port}
PrivateKey = {server_key}
"""

for i in range(client_number):
    exec(f"client_pub = client{i + 2}_pub")
    exec(f"client_preshared_key = client{i + 2}_preshared_key")
    wg0 += f"""
#client{i + 2}
[Peer]
PublicKey = {client_pub}
PresharedKey = {client_preshared_key}
AllowedIPs = 192.168.5.{i + 2}/32
"""

with open("wg0.conf", "w", encoding = "utf-8") as f:
    f.write(wg0)

# output "client*.conf"
for i in range(client_number):
    exec(f"client_key = client{i + 2}_key")
    exec(f"client_preshared_key = client{i + 2}_preshared_key")
    client = f"""#client{i + 2}
[Interface]
Address = 192.168.5.{i + 2}/24
DNS = {dns}
PrivateKey = {client_key}

[Peer]
PublicKey = {server_pub}
PresharedKey = {client_preshared_key}
AllowedIPs = 0.0.0.0/0
Endpoint = {address}:{port}
PersistentKeepalive = 25
"""
    with open(f"client{i + 2}.conf", "w", encoding = "utf-8") as f:
        f.write(client)

# finish
sub.run("del *.key *.pub", shell = True, capture_output = True)
print("done")
