import random 
def tasKagitMakas():
    print("\33[35m Taş, Kağıt, Makas Oyununa hoş geldiniz.\33[0m]")
    secim=input("lütfen seçiminizi yapınız. T,K ya da M ")
    print("\033[31m seçiminiz:\033[0m", secim )
    bilgisayar_secimi= random.choice(["T","K","M"])
    print("\33[32m bilgisayar secimi\33[0m", bilgisayar_secimi)
    if secim == bilgisayar_secimi:
        print("Berabere!")
    elif (secim == "T" and bilgisayar_secimi == "M") or (secim == "K" and bilgisayar_secimi=="T") or (secim == "M" and bilgisayar_secimi== "K"):
        print("Kazandınız!")
    else:
        print("Kaybettiniz!")
#tasKagitMakas()
