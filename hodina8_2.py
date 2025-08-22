def spoj_slova(*args, spojovac: str = " - ") -> str:
    return spojovac.join(str(arg) for arg in args if arg is not None)
if __name__ == '__main__':
    print(spoj_slova("Ahoj", "světe", None, "Python"))  # Ahoj - světe - Python
    print(spoj_slova())  # None
    print(spoj_slova("Jablko", "Banán", spojovac=" | "))  # Jablko | Banán

def vypocitej_vyskyt_dat(text):
    """
    Vrátí slovník, který obsahuje zaevidovaný výskyt hodnot
    v parametru "text".
    """
    vyskyt = dict()

    for slovo in text:
        vyskyt[slovo] = vyskyt.setdefault(slovo, 0) + 1

    return vyskyt


print(vypocitej_vyskyt_dat(("a", "b", "a", "c", "d", "b", "a")))