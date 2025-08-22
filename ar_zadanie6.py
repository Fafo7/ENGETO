# Napíš funkciu analyzuj_zoznam(zoznam), ktorá pre zadaný zoznam čísel:
# Spočíta, koľko čísel je párnych.
# Spočíta, koľko čísel je nepárnych.
# Zistí, či je zoznam vzostupný/zostupný/neusporiadaný.
# Vypíše min, max a priemer
def analyzuj_zoznam(zoznam):
    parne = [x for x in zoznam if x % 2 == 0]
    neparne = [x for x in zoznam if x % 2 != 0]
    vzostupne = zoznam_vzostupny(zoznam)
    zostupne = zoznam_zostupny(zoznam)
    najvacsie = max(zoznam)
    najmensie = min(zoznam)
    priemer = round(sum(zoznam) / len(zoznam), 2)
    print(f"Párnych čísel: {len(parne)}")
    print(f"Nepárnych čísel: {len(neparne)}")
    if vzostupne:
        print("Zoznam je: vzostupný")
    elif zostupne:
        print("Zoznam je: zostupný")
    else:
        print("Zoznam je: neusporiadaný")
    print(f"Najväčšie číslo je: {najvacsie} ")
    print(f"Najmenšie číslo je: {najmensie}")
    print(f"Priemer je: {priemer}")

def zoznam_vzostupny(zoznam):
    for x in range(1, len(zoznam)):
        if zoznam[x] <= zoznam[x - 1]:
            return False
    return True

def zoznam_zostupny(zoznam):
    for i in range(1, len(zoznam)):
        if zoznam[i] >= zoznam[i - 1]:
            return False
    return True

print(analyzuj_zoznam([1, 2, 3, 8, 12, 13, 55]))