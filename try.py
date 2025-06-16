def sayial(sira):
    while True:
        try:
            return float(input(f"{sira}. sayıyı gir :"))
        except ValueError:
            print("Geçersiz Sayı!!")
while True:
    print("\n--- Merhaba!! ---")
    print("\n1)Toplama")
    print("\n2)Çıkarma")
    print("\n3)Çarpma")
    print("\n4)Bölme")
    print("\n5)Çık")

    try:
        secim=int(input("\nLütfen bir seçim yap (1-5): "))
        if secim == 5:
            print("Byee!!!")
            break
        elif secim not in [1,2,3,4,5,]:
            print("Hatalı seçim!!")
            continue
        sayi1=sayial(1)
        sayi2=sayial(2)
        if secim==1:
            sonuc = sayi1 + sayi2
            islem = "+"
        elif secim == 2:
            sonuc=sayi1-sayi2
            islem="-"
        elif secim== 3:
            sonuc=sayi1*sayi2
            islem="*"
        elif secim == 4:
            if sayi2 == 0:
                print("Hata sayı 0'a bölünemez!!'")
                continue
            else :
                sonuc = sayi1/sayi2
                islem = "/"
        print(f"\nCevap : {sayi1} {islem} {sayi2} = {sonuc}")
        devam = input("Devam etmek istermisiniz ? (e/h))").lower()
        if devam != "e":
            print("Bye!!")
            break

    except ValueError:
        print("Hatalı giriş!!!")
