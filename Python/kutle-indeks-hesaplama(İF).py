print("Beden Kütle Endeksi hesaplama...")
boy=float(input("Boyunuzu girin(Örneğin: 1.74 cm)"))
kilo=int(input("Kilonuzu girin"))

kutle_indeks = kilo / ( boy *boy )
print(kutle_indeks)

if kutle_indeks <18.5 :
    print("Zayıfsınız")
elif kutle_indeks ==18.5 or kutle_indeks< 25  :
    print("Normal")
elif kutle_indeks == 25 or kutle_indeks< 30  :
    print("Fazla Kilolu")

else:
    print("Obez")


