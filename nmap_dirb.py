# Hedefe yonelik kesif ve dizin taramasi yapan bir python programi

import subprocess
import os
import time

try:
    os.system("clear")

    url = input("Lutfen hedef URL'yi girin: ")
    server = url[8:24]

    print("Hedefe yonelik NMAP taramasi gerceklestiriliyor...")
    time.sleep(2)
    print("\n")

    subprocess.run(['nmap', '-f', '-O', f'{server}'])
    print("\n")

    print("Hedefe yonelik DIRB taramasi gerceklestiriliyor...")
    time.sleep(2)
    
    subprocess.run(['dirb',f'{url}'])
    print("\nTaramalar tamamlandi. Ciktilar yukaridaki gibidir.")

except KeyboardInterrupt:
    print("Programdan cikis yaptiniz!")
