import time

print(" ************** BURÇ ÖĞRENME PROGRAMINA HOŞGELDİN ********** ")
time.sleep(1)
a=input("Doğduğun ayı jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec şeklinde gir:")
b =int(input("Doğduğun günü gir pışto:"))
print("Burcun hesaplanıyor....")
time.sleep(3)
print("ZORT BURCUN HESAPLANAMADI")
time.sleep(2)
print("şaka şaka")
time.sleep(2)
dict={
    "month":{
        "jan": {"oglak": list(range(1,21)),"kova":list(range(21,32))},
        "feb": {"kova": list(range(1,20)),"balık":list(range(20,30))},
        "mar": {"balık": list(range(1,21)),"koç":list(range(21,32))},
        "apr": {"koç": list(range(1,21)),"boğa":list(range(21,32))},
        "may": {"boğa": list(range(1,22)),"ikizle":list(range(22,32))},
        "jun": {"ikizler": list(range(1,22)),"yengeç":list(range(22,32))},
        "jul": {"yengeç": list(range(1,23)),"aslan":list(range(23,32))},
        "aug": {"aslan": list(range(1,24)),"başak":list(range(24,32))},
        "sep": {"başak": list(range(1,24)),"terazi":list(range(24,32))},
        "oct": {"terazi": list(range(1,24)),"akrep":list(range(24,32))},
        "nov": {"akrep": list(range(1,23)),"yay":list(range(23,32))},
        "dec": {"yay": list(range(1,23)),"oglak":list(range(23,32))}
    }                   
   
    }
z = dict["month"][a]
list1= list(z.keys())
list2 = list(z.values())

if b in list2[0]:
    print("Burcun:",list1[0])
elif b in list2[1] :
    print("Burcun:",list1[1])
elif b not in list2:
    print("MK UZAYLIIIĞIIIsııI")

time.sleep(25)    



