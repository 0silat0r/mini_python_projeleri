# Netdiscover bir ag kesif aracidir. Modeme bagli olan aglari taramaya baslar. Ve bu aglara bagli olan cihazlari kesfeder.
# Netdiscover; Kali Linux isletim sisteminde bulunur. Fakat eger Ubuntu gibi isletim sistemlerinde calistiracaksaniz, araci kurmaniz onerilir.
# Araci kurmadan yazilimi calistirirsaniz, program hata verecek ve islem durdurulacaktir.

import subprocess
import os
import time

os.system("clear")
host = ["192.168.1.0/24","192.168.2.0/24","192.168.3.0/24"]

print("Ag kesfi baslatiliyor...")
time.sleep(2)

for i in host:
    subprocess.run(['sudo', 'netdiscover', '-r', f'{i}'])
    # Finished yazisini gorur gormez CTRL + C kombinasyonunu kullanmaniz onerilir.
    # Aksi takdirde program islemine devam etmeyecektir.
print("\nTarama tamamlandi. Sonuclar listede gorundugu gibidir.")
