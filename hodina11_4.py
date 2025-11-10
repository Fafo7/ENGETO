import csv

with open('druhy_tabulkovy_soubor.csv') as cteni_csv:
    cteni = csv.reader(cteni_csv)
    print(tuple(cteni))

with open('druhy_tabulkovy_soubor.csv') as cteni_csv:
    cteni = csv.DictReader(cteni_csv)
    print(tuple(cteni))