def urun():
    urunler=[]
    while True:
        try:

            secim = input("Bir Ürün Giriniz : (Çıkmak İçin q) ")

            if secim == "q":

                 break
            else :

                urunler.append(secim)
            
            print(urunler)
            break 
            
                
        except ValueError:
            print("Geçersiz Giriş!!")


import random

sayi = random.randint(1,10)
   # cevap=int(input("Sayı Tahmin Et : "))
  #  cevap = str(cevap)
liste=[]

while True :
    cevap=int(input("Sayı Tahmin Et : "))
    #cevap = str(cevap)

    if cevap != sayi:
        liste.append(cevap)

        print(f"Hatalı Giriş!! {liste} sayılarını tahmin ettiniz!! ")

            

    elif cevap  == sayi:
        urun()
        break
    else :
        print("???")



