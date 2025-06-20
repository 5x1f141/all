def dosyaya_yaz():
    while True:
        giris=input("Dosyaya Yazmak istediğiniz şeyi girin (çıkmak için 'q' ) : ")
        if giris != "q":
            with open("veri.txt","a") as dosya:
                dosya.write(f"{giris},\n")
        elif giris == "q":
            break
        else:
            print("Geçersiz Giriş!!")
def oku():
    with open("veri.txt","r") as dosya :
        icerik=dosya.read()
    print(icerik)

while True:
    admin = "enes"

    name=input("Enter your username : ")

    if name != admin:
        print("Yetkisiz Kullanıcı !!")
    elif name == admin:

        print("Hoşgeldiniz!!")
        dosyaya_yaz()
        soru= input("İçeriği Okumak İstermisiniz ? (e/h)\n").lower()
        if soru == "e":
            oku()
        else:
            break
    else:
        print("Geçersiz Giriş!!")
    
        

