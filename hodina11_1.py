import csv

hlavicka = ("Jmeno", "Prijmeni", "Vek")
osoba_1 = ("Jan", "Novak", 33)
osoba_2 = ("Petr", "Svoboda", 44)

csv_soubor = open("osoby.csv", mode="w", newline="", encoding="utf-8")
zapisovac = csv.writer(csv_soubor, delimiter=";")
zapisovac.writerow(hlavicka)
zapisovac.writerow(osoba_1)
zapisovac.writerow(osoba_2)
zapisovac.writerows((hlavicka, osoba_1, osoba_2))
csv_soubor.close()

print(type(csv_soubor))
print(csv_soubor)