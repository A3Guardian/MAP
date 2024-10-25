def sortare_lista():
    numere = input("Introdu numerele separate prin spatiu: ")
    lista_numere = list(map(int, numere.split()))

    # Algoritmul Bubble Sort
    for i in range(len(lista_numere)):
        for j in range(0, len(lista_numere) - i - 1):
            if lista_numere[j] > lista_numere[j + 1]:
                lista_numere[j], lista_numere[j + 1] = lista_numere[j + 1], lista_numere[j]

    print("Lista sortata este:", lista_numere)

sortare_lista()
