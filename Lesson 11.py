import json

# JSON - java script

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}
vystup_s_jsonem = json.dumps(chuckuv_slovnik)
print(vystup_s_jsonem)

# bez knihovny nemůžeš pracovat s JSON objekty
import json
chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}
# funkci 'open' nachystáš objekt v Pythonu
json_soubor = open("prvni_json_soubor.json", mode="w")
# metoda 'dump' uloží objektu do souboru
json.dump(chuckuv_slovnik, json_soubor)
# ... nezapomeň objekt ukončit
json_soubor.close()