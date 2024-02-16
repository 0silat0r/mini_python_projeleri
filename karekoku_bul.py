# Girdi olarak verilen bir sayinin karekokunu bulan Python programi
# Hata yakalama metotlari

import math
while True:
    try:
        sayi=int(input("Lutfen bir sayi girin: "))
        sayinin_karekoku = math.sqrt(sayi)
        print(f"Sayinin Karekoku: {sayinin_karekoku}")
    
        if sayi == 0:
            break
    
    # Programi kullanan kisi yanlislikla sayi yerine harf girmeye calisirsa, program asagidaki uyariyi
    # yapacak ve calismaya devam edecek.
    except ValueError:
        print("Lutfen sayi girmeye calisin")
        continue
    
    # Programi kullanan kisi CTRL + C kombinasyonu ile
    # programdan cikmaya calisirsa asagidaki yaziyla 
    # karsilasacak ve sonsuz donguden cikis yaparak
    # program kapatilacak.
    except KeyboardInterrupt:
        print("\nProgramdan cikis yaptiniz!")
        break
    
