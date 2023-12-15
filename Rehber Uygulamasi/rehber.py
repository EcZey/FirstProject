def menu():
    print("\33[1;34;40m ")
    print("╔═════════════════════════════════════╗")
    print("║\33[36m    REHBER UYGULAMASI               \33[0m\33[1;34;40m ║")
    print("║═════════════════════════════════════║")
    print("║\33[36m   1-)  Rehbere Ekle              \33[0m\33[1;34;40m   ║")
    print("║\33[36m   2-)  Numaraları Listele          \33[0m\33[1;34;40m ║")
    print("║\33[36m   3-)  Numaraları Düzelt          \33[0m\33[1;34;40m  ║")
    print("║\33[36m   4-)  Numaraları Sil         \33[0m\33[1;34;40m      ║")
    print("║\33[36m   5-)  Okuma             \33[0m\33[1;34;40m           ║")
    print("║\33[36m   Seçiminizi Giriniz          \33[0m\33[1;34;40m      ║")
    print("╚═════════════════════════════════════╝")
    secim=input("Lütfen seçiminizi giriniz: ")
    if secim == "1":
        try:
            rehbereEkle()
        except:
            print("dosya bulunamadı")
    if secim== "2":
        listele()

    if secim=="5":
        oku()
    


def rehbereEkle():
    dosya=open("rehber.txt","a")
    ad=input("İsim giriniz: ")
    soyad=input("Soyisim giriniz: ")
    numara=input("Numara giriniz: ")
   
    if len(numara) == 10:
         ekle= ad + " " + soyad + " " + numara + "\n"
         ekleLower= ekle.lower()
         dosya.write(ekleLower)
         listele()
   
    else:
        print("Numara 10 haneli olmalıdır!")

    menu()
    dosya.close()

def listele():
    try:
        dosya=open("rehber.txt","r")
        print("\33[1;36;40m REHBER KAYIT LİSTESİ \33[0m\33[1;34;40m")
        print("═════════════════════════\n")
        isimler=dosya.readlines()
        isimler.sort()
        num=1
        for isim in isimler:
            print(num,isim)
            num+=1
            
        dosya.close()
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için enter tuşuna basınız.")






def oku():
    print("\nPozisyon Bilgisi")
    dosya=open("rehber.txt","r")
    parca= dosya.read(5)
    print("1.okunan:",parca)
    pozisyon=dosya.tell()
    print("şu anki pozisyon :", pozisyon)



menu()