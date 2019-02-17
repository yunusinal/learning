print("""Hangi Şeklin Ne olduğunu merak ediyorsunuz? Şekliniz kaç kenarlı ?
1. 3
2. 4
""")
sekil= int(input("şekli seçin:"))

if sekil ==1 :
    a=int(input("1.kenarı girin:"))
    b=int(input("2.kenarı girin:"))
    c=int(input("3.kenarı girin:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if a==b and a==b and a==c :
            print("Eşkenar Üçgen")
        elif (a==b and a!=c) or (a==c and a!=b) or (b==c and c!=a) :
            print("İkizkenar Üçgen")
        else :
            print("Çeşitkenar Üçgen")

    else:
        print("Üçgen Olamaz")

elif sekil == 2:
    a=int(input("1.kenarı girin:"))
    b=int(input("2.kenarı girin:"))
    c=int(input("3.kenarı girin:"))
    d=int(input("4.kenarı girin:"))

    if a==b and a==c and a==d :
        print("Kare")
    elif (a==b and c==d and a!=c) or (a==c and b==d and a!= b) or (b==c and a==d and b!= a ) :
        print("Dikdörtgen")
    else:
        print(" Denişik bir dörtgen")

else:
    print("Lütfen geçerli bir şekil seçin..")













