import csv

osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

with open("druhy_tabulkovy_soubor.csv", mode="w") as nove_csv:
    zahlavi = osoba_1.keys()
    zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)

    zapisovac.writeheader()
    zapisovac.writerow(osoba_1)
    zapisovac.writerow(osoba_2)