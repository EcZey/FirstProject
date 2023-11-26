def adamAsmacaOyunu():
    import random
    kelimeler = ["elma", "armut", "muz", "karpuz", "kavun", "çilek", "kiraz", "üzüm", "ananas", "portakal"]
    kelime = random.choice(kelimeler)
    harfler = []
    can = 6
    while can > 0 and not set(kelime).issubset(set(harfler)):
        print(f"Kalan can: {can}")
        print(f"Tahmin edilen harfler: {harfler}")
        print(f"Kelime: {''.join([h if h in harfler else '_' for h in kelime])}")
        harf = input("Bir harf tahmin edin: ").lower()
        if harf in harfler:
            print("Bu harfi zaten tahmin ettiniz.")
        elif harf in kelime:
            print("Doğru tahmin!")
            harfler.append(harf)
        else:
            print("Yanlış tahmin!")
            can -= 1
            harfler.append(harf)
    if can == 0:
        print(f"Kaybettiniz! Doğru kelime: {kelime}")
    else:
        print(f"Tebrikler! Doğru kelimeyi buldunuz: {kelime}")