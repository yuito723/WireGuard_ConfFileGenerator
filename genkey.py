import subprocess as sub

# capture_output = True

# number of client
client_number = 4

# output "server.key", "server.pub"
sub.run("wg genkey > server.key", shell = True)
sub.run("type server.key | wg pubkey > server.pub", shell = True)

# output "client*.key", "client*.pub", "client*-preshared.key"
for i in range(client_number):
    sub.run(f"wg genkey > client{i + 2}.key", shell = True)
    sub.run(f"type client{i + 2}.key | wg pubkey > client{i + 2}.pub", shell = True)
    sub.run(f"wg genkey > client{i + 2}-preshared.key", shell = True)
