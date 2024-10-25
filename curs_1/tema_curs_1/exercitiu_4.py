def este_prim(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def verifica_numar_prim():
    numar = int(input("Introdu un numar: "))
    if este_prim(numar):
        print(f"{numar} este un numar prim.")
    else:
        print(f"{numar} nu este un numar prim.")

verifica_numar_prim()
