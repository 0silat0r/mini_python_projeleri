# Resmi ve kurumsal firmalarda calisan Insan Kaynaklari Uzmanlari ile Muhasebe bolumunde calisan Muhasebe uzmanlarinin
# kullanmis olduklari veritabani yonetim sisteminden ufak bir gorunum.

# Python programlama dili kullanarak olusturacagimiz bu program, sadece personel kaydi konusunda islevini gorecektir.

import time
import os

class Personel():
    def __init__(self,ID,name,surname,balance,year):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.balance = balance 
        self.year = year

personel_siniri = int(input("Kac adet personelin kaydini gireceksiniz: "))
for i in range(0, personel_siniri):
    sira = int(input("Personelin liste numarasi: "))
    adi = input("Personelin Adi: ")
    soyadi = input("Personelin Soyadi: ")
    maas = int(input("Personelin Maas Bordrosu: "))
    yil = int(input("Personelin Ise Baslama Yili: "))
    per = Personel(sira,adi,soyadi,maas,yil)
    
    file = open("personel_kayit_dosyasi.txt","a")
    file.write(f"PERSONEL BILGILERI\nID: {per.ID}\nAdi: {per.name}\nSoyadi: {per.surname}\nMaasi: {per.balance}\nIse Baslama Yili: {per.year}\n\n")    
    file.close()
    
    print("Personel kaydi yapildi!")
    time.sleep(2)
    os.system("clear")

    
