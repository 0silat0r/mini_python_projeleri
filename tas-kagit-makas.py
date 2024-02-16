# Python ile yazilmis bir tas-kagit-makas oyunu

import random
import os

os.system("clear")

liste = ["Taş","Kagit","Makas"]
pc = random.choice(liste)
# Oyuncu butun harfleri kucuk veya buyuk bir sekilde artik yazabilir.
print("Taş - Kagit - Makas")
print("Programming by cpu-astatine")
player = input("Tas-Kagit-Makas: ").capitalize()

if (player == "Kagit") and (pc == "Makas"):
    print("Makas, kagidi keser. Bilgisayar kazandi.")
elif (player == "Makas") and (pc == "Taş"):
    print("Taş, makasi kirar. Bilgisayar kazandi.")
elif (player == "Taş") and (pc == "Kagit"):
    print("Kagit, taşi sarar. Bilgisayar kazandi.")
elif (player == "Makas") and (pc == "Kagit"):
    print("Makas, kagidi keser. Oyuncu kazandi.")
elif (player == "Taş") and (pc == "Makas"):
    print("Taş, makasi kirar. Oyuncu kazandi.")
elif (player == "Kagit") and (pc == "Taş"):
    print("Kagit, taşi sarar. Oyuncu kazandi.")
elif player == pc:
    print("Durum berabere.")
else:
    print("Liste disi giris yaptiniz. Lutfen tekrar deneyin.")
