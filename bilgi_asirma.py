# Python Programlama Dili ile Ağ Üzerinden Bilgi Toplama - TCP/IP
# cpu-astatine tarafindan kodlandi

import os
import socket
import subprocess
import time

def clear():
    os.system("clear")
clear()
print("Ağ Üzerinden Bilgi Toplama")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Lutfen hedef host'u girin: ")
port = int(input("Lutfen hedef port'u girin: "))
connection = s.connect((host, port))
print("Baglanti saglandi")
time.sleep(1)
print("\n")

while True:
    try:
        komut = input("Yardim icin '?' veya 'yardim' seklinde yazarak komutlar hakkinda daha fazla yardim alabilirsiniz.\nLutfen ogrenmek istediginiz bilgileri komut araciligi ile girin: ")
        if komut == "ip":
            ipaddress = socket.gethostbyname(host)
            print(f"Hedef sunucunun IP adresi: {ipaddress}")
            print("\n")
        elif komut == "nmap":
            print("Hedefe karsi NMAP taramasi baslatiliyor...")
            time.sleep(1)
            print(f"Host: {host}\nPort: {port}")
            subprocess.run(['nmap','-Pn',f'{host}'])
            print("\n")
        elif komut == "nikto":
            print("Hedefe karsi NIKTO taramasi baslatiliyor...")
            time.sleep(1)
            print(f"Host: {host}\nPort: {port}")
            subprocess.run(['nikto','-h',f'{host}'])
            print("\n")
        elif (komut == "yardim") or (komut == "?") or (komut == "help"):
            komutlar = ["ip","nmap","nikto"]
            print("Kullanabilecegin komutlar asagida listelenmistir.")
            print("###############################")
            for komut in komutlar:
                print(komut)
            print("###############################")
            print("\n")
        
    except KeyboardInterrupt:
        print("\nBaglanti kapatildi.")
        s.close()
        break
    except ValueError:
        print("Lutfen sayisal degerler girmeye calisin.")
        continue
