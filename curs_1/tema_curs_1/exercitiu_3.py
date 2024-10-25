import math

def gcd_dua_numere():
    num1 = int(input("Introdu primul numar: "))
    num2 = int(input("Introdu al doilea numar: "))
    gcd = math.gcd(num1, num2)
    print(f"Cel mai mare divizor comun dintre {num1} si {num2} este: {gcd}")

gcd_dua_numere()
