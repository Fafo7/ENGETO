import csv
from typing import List, Dict

data = [
    {"name": "Alice", "age": 23, "score": 85},
    {"name": "Bob", "age": 30, "score": 90},
    {"name": "Charlie", "age": 25, "score": 88},
    {"name": "David", "age": 35, "score": 92}
]

def zpracuj_vsechny_uzivatele(zadane_hodnoty, nezadouci):
    vysledek = []
    for uzivatel in zadane_hodnoty:
        vysledek.append(filtruj_nezadouci_sloupce(uzivatel, nezadouci))
    return tuple(vysledek)

def filtruj_nezadouci_sloupce(zadany_slovnik, nezadouci):
    filtrovany = {}
    for klic, hodnota in zadany_slovnik.items():
        if klic not in nezadouci:
            filtrovany[klic] = hodnota
    return filtrovany

def zapis_jako_csv_soubor(data, cesta_k_souboru):
    with open(cesta_k_souboru, mode="w", newline="", encoding="utf-8") as csv_soubor:
        hlavicka = data[0].keys()
        zapisovac = csv.DictWriter(csv_soubor, fieldnames=hlavicka, delimiter=";")
        zapisovac.writeheader()
        zapisovac.writerows(data)

zpracuj_vsechny_uzivatele(data, ["age"])
print(zpracuj_vsechny_uzivatele(data, ["age"]))
