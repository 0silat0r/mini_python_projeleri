# Kullanicinin girmis oldugu hedef siniri kadar ag taramasi gerceklestiren mini bir python projesi.
# Dikkat: Bu yazilimin calisabilmesi icin Ubuntu yada Kali Linux araclarina sahip olmaniz gerekmektedir.

import subprocess
import time
import os

os.system("clear")

taranacak_hedefler=[]
hedef = int(input("Lutfen kac adet hedef tarayacaginizi belirtin: "))
print("\n")

print("Lutfen hedefin IP adresini veya HOST adresini girin.")
for i in range(0,hedef):
    ip = input("Hedef> ")
    taranacak_hedefler.append(ip)
print("\n")

for j in range(0,hedef):
    time.sleep(1)
    subprocess.run(['nmap',f'{taranacak_hedefler[j]}'])
print("\n")

print("Tarama tamamlandi.")
