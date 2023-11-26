import hesapmakinesi
import tahminoyunu
import taskagitmakas
import leapyearcalculator
import tipcalculator
import rollercoaster
import bmicalculator
def anaMenu():
    print("\33[1;32;40m")
    print("╔══════════════════════════╗")
    print("║\033[31m    Anamenu    \33[0m\33[1;32;40m           ║")
    print("║                          ║")
    print("║   1-) Hesap Makinesi     ║")
    print("║   2-) Sayi tahmini oyunu ║")
    print("║   3-)                    ║")
    print("║   4_) Not Hesaplama      ║")
    print("║   5-)                    ║")
    print("║   6_)                    ║")
    print("║   7-)     çıkış (e)      ║")
    print("║                          ║")
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
anaMenu()