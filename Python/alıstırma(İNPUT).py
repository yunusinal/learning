"""Problem 1
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
"""

a = int(input("birinci sayı:"))
b = int(input("ikinci sayı:"))
c = int(input("üçüncü sayı:"))

print("Yazdığınız sayıların çarpımı: {}" .format(a*b*c))


# --Problem 2--
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

print("VUCÜT KİTLE ENDEKSİNİ HESAPLA")
a= float(input("Boyunuzu 'metre . cm'  cinsinden giriniz (örneğin 1.74 cm):"))
b= int(input("Kilonuzu Tam sayı cinsinden giriniz (örneğin 75 kg):"))

print("Vucüt kitle endeksiniz:",b/(a**2))





