# import json
#
# # JSON - java script
#
# chuckuv_slovnik = {
#     "jmeno": "Chuck Norris",
#     "neuspech": None,
#     "kliky": "vsechny",
#     "konkurence": False,
#     "fanousek": "Łukasz"
# }
# vystup_s_jsonem = json.dumps(chuckuv_slovnik)
# print(vystup_s_jsonem)
#
# # bez knihovny nemůžeš pracovat s JSON objekty
# import json
# chuckuv_slovnik = {
#     "jmeno": "Chuck Norris",
#     "neuspech": None,
#     "konkurence": False,
#     "fanousek": "Łukasz"
# }
# # funkci 'open' nachystáš objekt v Pythonu
# json_soubor = open("prvni_json_soubor.json", mode="w")
# # metoda 'dump' uloží objektu do souboru
# json.dump(chuckuv_slovnik, json_soubor)
# # ... nezapomeň objekt ukončit
# json_soubor.close()

import os
import json


import csv


hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]


# ... nachystáš nový soubor pro zápis
nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")
# ... vytvoříš zapisovací objekt, který do souboru zapíše údaje
zapisovac = csv.writer(nove_csv, delimiter =',')
# ... nejprve zapíšeš záhlaví
zapisovac.writerow(hlavicka)
# ... potom první údaj
zapisovac.writerow(osoba_1)
# ... druhý údaj
zapisovac.writerow(hlavicka)
# ... nakonec objekt a soubor uzavřeš
nove_csv.close()

cteni = csv.reader("prvni_tabulkovy_soubor.csv",delimiter=",")
type(cteni)
for radek in cteni:
    print(radek)


nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")
zapisovac = csv.writer(nove_csv)
print(zapisovac, type(nove_csv), sep="\n")
nove_csv.close()

# Nezapomeň nahrát knihovnu, jinak soubor nevytvoříš
import csv
hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]
# ... nachystáš nový soubor pro zápis
nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")
# ... vytvoříš zapisovací objekt, který do souboru zapíše údaje
zapisovac = csv.writer(nove_csv)
# ... zapíšeš všechny hodnoty
zapisovac.writerows(
    (
        hlavicka,
        osoba_1,
        osoba_2
    )
)
# ... nakonec objekt a soubor uzavřeš
nove_csv.close()
print(nove_csv)



