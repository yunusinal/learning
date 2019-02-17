vize1 = int(input("1. Vize notunu gir:"))
vize2 = int(input("2. Vize notunu gir:"))
final_notu = int(input("Final notunu gir:"))

toplam_not = vize1 *(30/100) + vize2 * (30/100) + final_notu * (40/100)
print(toplam_not)

if toplam_not >= 90 :
    print("AA")
elif toplam_not >= 85 :
    print("AB")
elif toplam_not >= 80 :
    print("BB")
elif toplam_not >= 75 :
    print("BC")
elif toplam_not >= 70 :
    print("CC")
elif toplam_not >= 65 :
    print("DC")
elif toplam_not >= 60 :
    print("DD")
elif toplam_not >= 55 :
    print("FD")
else:
    print("FF")




