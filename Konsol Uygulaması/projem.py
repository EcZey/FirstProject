import hesapmakinesi
import tahminoyunu
import taskagitmakas
import leapyearcalculator
import tipcalculator
import rollercoaster
import bmicalculator
import faktoriyelhesapla
def anaMenu():
    print("\33[1;32;40m")
    print("╔══════════════════════════╗")
    print("║\033[31m    Anamenu    \33[0m\33[1;32;40m           ║")
    print("║                          ║")
    print("║   1-) Hesap Makinesi     ║")
    print("║   2-) Sayi tahmini oyunu ║")
    print("║   3-) Tas,Kagit,Makas    ║")
    print("║   4_) Leap Year Calc.    ║")
    print("║   5-) Tip Calculator     ║")
    print("║   6_) Roller Coaster     ║")
    print("║   7-) Bmi Calculator     ║")
    print("║   8-) Faktoriyel Hesapla ║")
    print("║   Seçiminizi yapınız     ║")
    print("╚══════════════════════════╝")
    menu = input("seçiminizi yapınız: ")
    print("seçtiniz", menu)
    if menu == "1": hesapmakinesi.hesapMakinesi()
    elif menu == "2": tahminoyunu.sayiTahminOyunu()
    elif menu== "3": taskagitmakas.tasKagitMakas()
    elif menu== "4":leapyearcalculator.leapYearCalculator()
    elif menu== "5":tipcalculator.tipCalculator()
    elif menu== "6":rollercoaster.rollerCoaster()
    elif menu== "7":bmicalculator.bmiCalculator()
    elif menu == "8":faktoriyelhesapla.faktoriyelHesaplama()
anaMenu()