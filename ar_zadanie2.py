cisla = [3, 7, 2, 9, 12, 5]
cislo_parne = []
cislo_neparne = []

for cislo in cisla:
    if cislo % 2 == 0:
        print(f"{cislo} je párne číslo")
        cislo_parne.append(cislo)
    else:
        print(f"{cislo} je nepárne číslo")
        cislo_neparne.append(cislo)
print(f"Parné čísla: {', '.join(map(str, cislo_parne))}")
print(f"Neparné čísla: {', '.join(map(str, cislo_neparne))}")
print(f"Počet párnych čísel: {len(cislo_parne)}")
print(f"Počet nepárnych čísel: {len(cislo_neparne)}")