import json
urunler = {
    "elma":10,
    "muz":12
}
for urun, fiyat in urunler.items():
    print(f"{urun}: {fiyat} ")


urunler2={
    "armut":19,
    "karpuz":90
}
with open ("urunler.json","w") as dosya:
    json.dump(urunler2,dosya)

with open ("urunler.json","r") as dosya2:
    veri = json.load(dosya2)
print(veri)
