#"pocet" – počet všetkých čísel v zozname,
#"parne" – zoznam všetkých párnych čísel,
#"neparne" – zoznam všetkých nepárnych čísel,
#"je_vzostupne" – True/False podľa toho, či je zoznam vzostupný.

def analyzuj_zoznam(zoznam):
    pocet = len(zoznam)
    parne = [x for x in zoznam if x % 2 == 0]
    neparne = [x for x in zoznam if x % 2 != 0]
    vzostupne = je_vzostupne(zoznam)

    return {
        'pocet': pocet,
        'parne': parne,
        'neparne': neparne,
        'je_vzostupne': vzostupne
    }

def je_vzostupne(zoznam):
    for i in range(1, len(zoznam)):
        if zoznam[i] < zoznam[i - 1]:
            return False
    return True

print(analyzuj_zoznam([1, 2, 3, 6, 8, 10]))