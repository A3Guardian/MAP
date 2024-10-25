def ziua_saptamanii():
    zi = int(input("Introdu un numar de la 1 la 7: "))
    zile = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
    
    if 1 <= zi <= 7:
        print(f"Ziua saptamanii este: {zile[zi - 1]}")
    else:
        print("Numarul introdus nu este valid.")

ziua_saptamanii()
