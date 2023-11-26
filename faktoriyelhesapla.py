# Faktoriyel hesaplamak için bir fonksiyon tanımla
def faktoriyelHesaplama():
  # Kullanıcıdan bir sayı al
  n = int(input("Bir sayı girin: "))

  # Faktoriyel hesaplamak için bir fonksiyon tanımla
  def faktoriyel(x):
    # 0 veya 1'in faktoriyeli 1'dir
    if x == 0 or x == 1:
      return 1
    # Diğer durumlarda, x'in faktoriyeli x*(x-1)*(x-2)*...*1'dir
    else:
      sonuc = 1
      for i in range(1, x+1):
        sonuc = sonuc * i
      return sonuc

  # 1'den n'e kadar olan sayıların faktoriyelini yazdır
  for i in range(1, n+1):
    print(i, "!", "=", faktoriyel(i))