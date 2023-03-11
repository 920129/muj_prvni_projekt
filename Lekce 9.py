# print("Hello Wolrd")
# print(isinstance({"a","b","c"}),set)

def moje_funkce(x):
    y = print(x**2)

moje_funkce(100)


#*******************

#
# def spustím_skript():
#     jmeno = "Matous"
#     domena = "@matous.cz"
#
#     hlavni_fce(j=jmeno,d=domena)
# def hlavni_fce(j, d):
#     pritn(f"Zkombinujeme promenne_{j}{d}")
#
# spustím_skript()

##### Kalkulačka jako projekt xxxx
import os
def spocitat_zkladni_op() -> float:
    while True:
        Tlacitko = input("Tlacitko: ")
        if tlacitko. isnumeric() or tlacitko in ("+". "-"):
            zapis+= str(tlacitko)
        elif tlacitko in ("/","*"):
            zapis+= f"){Tlacitko}("
        elif tlacitko == "=":
            zapis +=")" if zapis [:-1] !=")"else ""
            print(zapis)
            print("vysledke"), eval(zapis))
            break
def spocitat_prum() -> float:
    rada_cisel = list()
    while (hodnota := input("dalsi cislo: ")) != "quit":
        if hodnota.isnumeric():
            rada_cisel.append(int(hodnota))
    os.system("clear")
    print("Prumer:", sum(rada_cisel)/len(rada_cisel))

    ...
def umocneni_exp() -> int:
    hodnota = int(input("Hodnota"))
    mocnina = int(input("Mocnina"))
    os.system("clear")
    print("Vysledek: ", hodnota, mocnina,
    )
# hodnota
#mocnina

def kalkulacka():
    procesy = ("zakladni_op","prum","pow","quit")
    while True:
        vyber = input("vyber operaci:")
        if vyber not in procesy:
            print("neexistuje")
            continue
        if vyber == "quit":
            break
        elif vyber == "pow":
            umocneni_exp()
        elif vyber == "prum":
            spocitat_prum()
        else vyber == "zakladni_op":
            spocitat_zakladni_op()

if name == "main_":
    kalkulacka()



