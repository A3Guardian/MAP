def suma_si_media():
    numere = input("Introdu numerele separate prin spatiu: ")
    lista_numere = list(map(float, numere.split()))
    suma = sum(lista_numere)
    media = suma / len(lista_numere) if lista_numere else 0
    print(f"Suma este: {suma}, Media este: {media}")

suma_si_media()
