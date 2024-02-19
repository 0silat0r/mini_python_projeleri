# Isı-Sıcaklık Deger Donusumleri

def CelciusToFahrenheit():
    derece = float(input("Lutfen celcius degerini girin: "))
    fhrnht = (derece * (18/10)) + 32
    print(f"Derece: {derece}\nFahrenheit: {fhrnht}")
def FahrenheitToCelcius():
    fhrnht = float(input("Lutfen fahrenheit degerini girin: "))
    derece = (fhrnht - 32)/(18/10)
    print(f"Derece: {derece}\nFahrenheit: {fhrnht}")
def CelciusToKelvin():
    derece = float(input("Lutfen celcius degerini girin: "))
    kelvin = derece + 273.15
    print(f"Derece: {derece}\nKelvin: {kelvin}")
def KelvinToCelcius():
    kelvin = float(input("Lutfen kelvin degerini girin: "))
    derece = kelvin - 273.15
    print(f"Derece: {derece}\nKelvin: {kelvin}")

print("Enerji Deger Donusumleri\nHos Geldiniz")
try:
    secim = int(input("0- Cikis\n1- Celcius'dan Fahrenheit'a\n2- Fahrenheit'tan Celcius'a\n3- Celcius'dan Kelvin'e\n4-Kelvin'den Celcius'a\nLutfen seciminizi yapin\n: "))
    if secim == 1:
        CelciusToFahrenheit()
    elif secim == 2:
        FahrenheitToCelcius()
    elif secim == 3:
        CelciusToKelvin()
    elif secim == 4:
        KelvinToCelcius()
    elif secim == 0:
        exit()
    else:
        print("Yanlislik yaptiniz. Lutfen tekrar deneyin.")
        exit()

except ValueError:
    print("Lutfen sayisal deger girmeye calisiniz.")
except KeyboardInterrupt:
    print("\nProgramdan cikis yaptiniz!")
