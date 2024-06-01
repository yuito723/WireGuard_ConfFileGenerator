import subprocess as sub

import time

# server_key = sub.check_output("wg genkey").decode("utf8").strip()
# server_pub = sub.check_output(["wg pubkey", "8NS3x1uIeFTo2JDCTln6WNLsAn8tCKgFi61S4HUapmo="]).decode("utf8").strip()

# server_key = sub.run("wg", shell = True).decode("utf8").strip()

# server_key = sub.run("wg genkey", shell = True)

server_key = sub.run("type sv.key | wg pubkey ", shell = True, capture_output = True, text = True)

# server_key = sub.run(["wg", "pubkey", "8NS3x1uIeFTo2JDCTln6WNLsAn8tCKgFi61S4HUapmo="], capture_output = True, text = True)


print("#########################################################")
print(f"stdout : {server_key.stdout.strip()}")
print(f"stderr : {server_key.stderr.strip()}")
print("#########################################################")
time.sleep(3)


# a = sub.check_output("wg genkey | tee server.key")

# b = sub.check_output(f"wg pubkey {a}")

# print(server_key)

# print(server_pub)

# print(a)