def dosyaya_yaz(name):
    while True:
        giris = input(f"{name}, Dosyaya Yazmak İstediğiniz Şeyi girin (çıkmak için 'q') : ")
        if giris !="q":
            with open(f"{name}_veri.txt", "a") as dosya:
                dosya.write(f"{giris}\n")
        elif giris == "q":
            break
        else:
            print("Geçersiz Giriş !!")

def oku(name):
    try:

        with open(f"{name}_veri.txt","r") as dosya:
            icerik = dosya.read()
        print(icerik)
    except FileNotFoundError:
        print(f"{name} için dosya bulunamadı.")

admins = ["enes","doa"]

while True:
    name= input("Kullanıcı Adı : ")
    if name not in admins:
        print("ERROR : Yetkisiz Kullanıcı!!")
    else:
        print(f"Hoşgeldin, {name}!")
        dosyaya_yaz(name)
        soru=input(f"{name}, içeriği okumak istermisiniz ? (e/h) ")
        if soru == "e":
            oku(name)
        elif soru == "h":
            break
        else:
            print("geçersiz giriş!!")


