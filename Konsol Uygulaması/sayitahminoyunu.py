import random
def sayiTahminOyunu():
    print("Sayı tahmin oyununa hoş geldiniz.")
    tahmin= int(input("Lütfen bir sayi giriniz:"))
    print("tahmininiz", tahmin)
    rastGeleSayi= random.randint(1,10)
    print("rast gele sayı:", rastGeleSayi)
    if tahmin == rastGeleSayi:
        print("Bildiniz!")
    else:
        print("Üzgünüm, bilemediniz.")
#sayiTahminOyunu() 