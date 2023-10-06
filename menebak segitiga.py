
import math


a = float(input("Nilai pertama: "))
b = float(input("Nilai kedua: "))
c = float(input("Nilai ketiga: "))

if a+b>c and b+c>a and c+a>b:
    if a == b == c:
     segitiga="Sama Sisi"
    elif a == b or b == c or c == a:
     segitiga="Sama kaki"
    elif math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2):
     segitiga="Siku-siku"
    else:
     segitiga="Sembarang"
else:
    segitiga="Bukan Segitiga"

    
print(f"Segitiga yang dihasilkan merupakan segitiga {segitiga}")
