def caesar_sifrele(metin, kaydirma):
    sifreli_metin = ""
    for harf in metin:
        if harf.isalpha():

            ilk_harf = 'a' if harf.islower() else 'A'

            yeni_harf = chr((ord(harf) - ord(ilk_harf) + kaydirma) % 26 + ord(ilk_harf))
            sifreli_metin += yeni_harf
        else:
            sifreli_metin += harf
    return sifreli_metin

metin = input("Şifrelenecek metni girin: ")
kaydirma = int(input("Kaydırma miktarı: "))
print("Şifrelenmiş Metin:", caesar_sifrele(metin, kaydirma))
