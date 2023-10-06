import math

a = float(input("Masukkan koefisien a: "))
b = float(input("Masukkan koefisien b: "))
c = float(input("Masukkan koefisien c: "))

determinan = b**2 - 4*a*c

if determinan > 0:
    x1 = (-b + math.sqrt(determinan)) / (2*a)
    x2 = (-b - math.sqrt(determinan)) / (2*a)
    print(f"Akar-akar persamaan kuadrat adalah x1 = {x1} dan x2 = {x2}")
elif determinan == 0:
    x1 = x2 = -b / (2*a)
    print(f"Akar ganda persamaan kuadrat adalah x1 = x2 = {x1}")
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-determinan) / (2*a)
    print(f"Akar kompleks persamaan kuadrat adalah x1 = {realPart} + {imaginaryPart}i dan x2 = {realPart} - {imaginaryPart}i")

print(f"Determinan persamaan kuadrat adalah {determinan}")
