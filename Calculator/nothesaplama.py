# notHesaplama fonksiyonu tanımlanıyor
def notHesaplama():
  # öğrenci sayısı ve geçme notu kullanıcıdan alınıyor
  ogrenciSayisi = int(input("Öğrenci sayısını giriniz: "))
  gecmeNotu = int(input("Geçme notunu giriniz: "))
  # öğrencilerin notlarını tutacak bir liste oluşturuluyor
  notlar = []
  # her öğrenci için not alınıp listeye ekleniyor
  for i in range(ogrenciSayisi):
    notu = int(input(f"{i+1}. öğrencinin notunu giriniz: "))
    notlar.append(notu)
  # öğrencilerin durumları ekrana yazdırılıyor
  for i in range(ogrenciSayisi):
    if notlar[i] >= gecmeNotu:
      print(f"{i+1}. öğrenci {notlar[i]} ile geçti.")
    else:
      print(f"{i+1}. öğrenci {notlar[i]} ile kaldı.")

# notHesaplama fonksiyonu çağrılıyor
#notHesaplama()