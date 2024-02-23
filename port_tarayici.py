# Python Programlama Dili ile Port Tarayici yazilimini Olusturmak

import socket
import os

os.system("clear")
print("Port Scanner")
print("Programing by cpu-astatine")
ip=input("Lutfen IP Adresini girin: ")

for i in range(20, 444):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, i))
        print(f"{i} Numarali Port Acik")
    except Exception as e:
        pass
    finally:
        s.close()
