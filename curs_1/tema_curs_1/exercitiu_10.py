import cmath

def ecuatie_gradul_2():
    a = float(input("Introdu coeficientul a: "))
    b = float(input("Introdu coeficientul b: "))
    c = float(input("Introdu coeficientul c: "))

    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print(f"Solutiile sunt: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Solutia este: x = {x}")
    else:
        print("Nu exista solutii reale.")

ecuatie_gradul_2()
