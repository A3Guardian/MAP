def unghiuri_triunghi():
    a = int(input("Introdu primul unghi: "))
    b = int(input("Introdu al doilea unghi: "))
    c = int(input("Introdu al treilea unghi: "))
    if a + b + c == 180:
        print("Unghiurile pot forma un triunghi.")
    else:
        print("Unghiurile nu pot forma un triunghi.")

unghiuri_triunghi()
