def maxim_vector():
    numere = input("Introdu numerele separate prin spatiu: ")
    lista_numere = list(map(int, numere.split()))
    maxim = max(lista_numere) if lista_numere else None
    print(f"Maximul din lista este: {maxim}")

maxim_vector()
