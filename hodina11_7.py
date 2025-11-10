import csv
jmeno_souboru = 'muj_soubor.csv'
zadane_hodnoty = [
    [10, "a1", 1],
    [12, "a2", 3],
    [14, "a3", 5],
    [16, "a4", 7],
    [18, "a5", 9]
]
def zapis_csv(jmeno,hodnoty):
    with open(jmeno, mode="w", encoding="utf-8", newline="") as f:
        zapisovac = csv.writer(f)
        zapisovac.writerows(hodnoty)

def precti_csv(jmeno):
    with open(jmeno, mode="r", encoding="utf-8", newline="") as f:
        nacti_obsah = csv.reader(f, delimiter=";")
        vystup = tuple(nacti_obsah)
    return vystup


zapis_csv(jmeno_souboru, zadane_hodnoty)
vystup = precti_csv(jmeno_souboru)
print(f"Obsah: {vystup}")
  