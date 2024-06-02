import subprocess as sub

# capture_output = True

# 変数
client_number = 2
port = 51820
address = "example.com"

# output "server.key", "server.pub"
sub.run("wg genkey > server.key", shell = True)
sub.run("type server.key | wg pubkey > server.pub", shell = True)

# output "client*.key", "client*.pub", "client*-preshared.key"
for i in range(client_number):
    sub.run(f"wg genkey > client{i + 2}.key", shell = True)
    sub.run(f"type client{i + 2}.key | wg pubkey > client{i + 2}.pub", shell = True)
    sub.run(f"wg genkey > client{i + 2}-preshared.key", shell = True)

# read keys
with open("server.key", "r", encoding = "utf-8") as f:
    server_key = f.read()

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

with open("wg0.conf", "w", encoding = "utf-8") as f:
    f.write(wg0)


# output "client*.conf"
