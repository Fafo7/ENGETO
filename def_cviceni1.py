odstran_nuly = [0, 3, 0, 5, 0, 7]
def odstran_nul(zoznam: list) -> list:
    """
    # funkce, která odstraní zadané nuly z libovolného počtu argumentů
    """
    return [x for x in zoznam if x != 0]
print(odstran_nul(odstran_nuly))
print(help(odstran_nul))


najvacsie = [3, 7, 1, 9, 2]
def najvacsie_cislo(zoznam: list) -> int:
    return max(zoznam)
print(najvacsie_cislo(najvacsie))


najvacsie1 = [3, 7, 1, 9, 2]
def najvacsie_cislo1(zoznam: list) -> int:
    naj = zoznam[0]
    for cislo in zoznam:
        if cislo > naj:
            naj = cislo
    return naj
print(najvacsie_cislo1(najvacsie1))


cisla1 = [1, 3, 5]
cisla2 = [1, 4, 5, 9]
def obsahuje_parne(zoznam: list) -> bool:
    for x in zoznam:
        if x % 2 == 0:
            return True
    return False
print(obsahuje_parne(cisla1))
print(obsahuje_parne(cisla2))


cisla1 = [1, 3, 5]
cisla2 = [1, 4, 5, 9]
def obsahuje_parne(zoznam: list) -> bool:
    return any(x % 2 == 0 for x in zoznam)
print(obsahuje_parne(cisla1))
print(obsahuje_parne(cisla2))


def je_vzostupne(zoznam: list) -> bool:
    for i in range(1, len(zoznam)):
        if zoznam[i] <= zoznam[i - 1]:
            return False
    return True
print(je_vzostupne([1, 2, 3, 5]))
print(je_vzostupne([1, 2, 2, 3]))
print(je_vzostupne([9, 10, 11]))
print(je_vzostupne([3, 2, 1]))


def je_zostupne(zoznam: list) -> bool:
    for i in range(1, len(zoznam)):
        if zoznam[i] >= zoznam[i - 1]:
            return False
    return True
print(je_zostupne([5, 4, 3, 2, 1]))
print(je_zostupne([1, 2, 2, 3]))
print(je_zostupne([9, 10, 11]))
print(je_zostupne([3, 2, 1]))


def je_zostupne1(zoznam: list) -> bool:
    return all(zoznam[i] < zoznam[i - 1] for i in range(1, len(zoznam)))
print(je_zostupne1([1, 2, 3, 5]))
print(je_zostupne1([1, 2, 2, 3]))
print(je_zostupne1([11, 10, 9]))
print(je_zostupne1([3, 2, 1]))
