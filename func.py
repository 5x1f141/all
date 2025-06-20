liste=[]
while True:
    urun=input("Bir urun giriniz (Çıkmak icin 'q' ) : " )
    if urun == "q":
        break
    liste.append(urun)
    break

print("Ürünler : ",liste)

dosya=open("ornek.txt","w")
giris=input(f"Bir urun giriniz (Çıkmak icin 'q') ")
dosya.write(giris)
dosya.close()

dosya = open("ornek.txt","r" )
icerik= dosya.read()
print(icerik)
dosya.close()


