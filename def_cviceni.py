def je_prvocislo(n):
    """# funkce, která vrací T/F podle toho, zda je parametr prvočíslo"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    print(je_prvocislo(7))  # True


def je_cislo_palindrom(cislo):
    """
    # funkce, která vrací T/F podle toho, zda je zadané *číslo* **palindrom**
    # (čtené zezadu stejně jako zepředu)
    """
    cislo_str = str(cislo)
    return cislo_str == cislo_str[::-1]
if __name__ == '__main__':
    print(je_cislo_palindrom(121))  # True


def je_retazec_palindrom(retazec):
    """
    # funkce, která vrací T/F podle toho, zda je zadaný *řetězec* palindrom
    # (volitelné parametry mohou určovat, zda budeme ignorovat mezery či obecně
    # znaky mimo písmena a zda budeme ignorovat rozdíly ve velikosti písmen -
    # 'Rotor'? 'a Toyota'?)
    """
    retazec = retazec.lower()
    retazec = "".join(znak for znak in retazec if znak.isalpha())
    return retazec == retazec[::-1]
if __name__ == '__main__':
    print(je_retazec_palindrom("rotor"))

def faktorial_cyklem(n):
    """# funkce, která vrací faktoriál daného čísla (cyklem)"""
    vysledok = 1
    for i in range(1, n + 1):
        vysledok *= i
    return vysledok
if __name__ == '__main__':
    print(faktorial_cyklem(5))


def faktorial_rekurzi(n):
    """# funkce, která vrací faktoriál daného čísla (rekurzí, BEZ cyklů)"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial_rekurzi(n - 1)
if __name__ == '__main__':
    print(faktorial_rekurzi(10))


def obracene_cislo(n):
    """
    # funkce, která pro zadané číslo vrátí číslo **obrácené**
    # (471 => 174; 20069 => 96002; 1000 => 1). Bez použití řetězců!
    """
    vysledok = 0
    while n > 0:
        posledna_cifra = n % 10
        vysledok = vysledok * 10 + posledna_cifra
        n = n // 10
    return vysledok
if __name__ == '__main__':
    print(obracene_cislo(471))


def ciferny_sucet(n):
    """# funkce, která vrátí ciferný součet zadaného čísla (bez použití řetězců)"""
    vysledok = 0
    while n > 0:
        vysledok += n % 10
        n = n // 10
    return vysledok
if __name__ == '__main__':
    print(ciferny_sucet(71))

# funkce, která pro zadanou sekvenci vrátí druhý největší prvek
def druhy_prvek(sekvence):