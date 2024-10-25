def verificare_numere():
    if 10>20:
        print("Este mai mare")
    else:
        print("NU este mai mare")
 
def tipuri_de_date():
    x=int(2)
    y="MAP"
    print(type(x))
    print(type(y))
 
def tuplu():
    masini=["Audi","BMW","Dacia"]
    x,y,z = masini
    print(x+" "+y+" "+z)
 
def interpolare():
    varasta = 14
    text = "Numele meu este Sorin si am {} de ani"
    print(text.format(varasta))
 
def instructiunea_while():
    i = 1
    while i<=5 :
        print("Bucla While", i)
        i+=1
 
def lista_elemente():
    elemente=[]
    n = int(input("Introdu numarul de elemente"))
    for i in range (0,n):
        print("Introdu elementeul pentru pozitia ",i)
        item=int(input())
        elemente.append(item)
    print("Lista este ", elemente)
 
lista_elemente()
#instructiunea_while()
# interpolare()
#tuplu()
#verificare_numere()
#tipuri_de_date()
 