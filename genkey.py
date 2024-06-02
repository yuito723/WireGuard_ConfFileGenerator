import subprocess as sub
import time

sub.run("mkdir keys", shell = True, capture_output = True)

# number of client
client_number = 1000

# output "server.key", "server.pub"
# sub.run("wg genkey > server.key", shell = True, capture_output = True)
# sub.run("type server.key | wg pubkey > server.pub", shell = True, capture_output = True)

# # output "server.key", "server.pub"
sub.run("wg genkey > keys/server.key", shell = True, capture_output = True)
sub.run("type keys/server.key | wg pubkey > keys/server.pub", shell = True, capture_output = True)

# output "client*.key", "client*.pub"
# for i in range(client_number):
#     sub.run(f"wg genkey > ./keys/client{i + 2}.key", shell = True, capture_output = True, text = True)
#     sub.run(f"type ./keys/client{i + 2}.key | wg pubkey > ./keys/client{i + 2}.pub", shell = True, capture_output = True, text = True)




# server_key = sub.check_output("wg genkey").decode("utf8").strip()
# server_pub = sub.check_output(["wg pubkey", "8NS3x1uIeFTo2JDCTln6WNLsAn8tCKgFi61S4HUapmo="]).decode("utf8").strip()

# server_key = sub.run("wg", shell = True).decode("utf8").strip()

# server_key = sub.run("wg genkey", shell = True)

# server_key = sub.run("type sv.key | wg pubkey ", shell = True, capture_output = True, text = True)

# server_key = sub.run(["wg", "pubkey", "8NS3x1uIeFTo2JDCTln6WNLsAn8tCKgFi61S4HUapmo="], capture_output = True, text = True)


# print("#########################################################")
# print(f"stdout : {server_key.stdout.strip()}")
# print(f"stderr : {server_key.stderr.strip()}")
# print("#########################################################")
# time.sleep(3)


# a = sub.check_output("wg genkey | tee server.key")

# b = sub.check_output(f"wg pubkey {a}")

# print(server_key)

# print(server_pub)

# print(a)