#Počet slov v texte.
#Počet unikátnych slov (ignoruj veľkosť písmen).
#Najdlhšie slovo.
#Počet slov, ktoré začínajú na samohlásku (a, e, i, o, u).
#Text premenený na veľké písmená.
#Overenie, či text obsahuje čísla (áno/nie).
def analyzuj_text(text):
    slova = text.split()
    pocet_slov = len(slova)
    unikatne_slova = set(s.lower() for s in slova)
    pocet_unikatne = len(unikatne_slova)
    najdlhsie_slovo = max(slova, key=len)
    samohlasky = ("a", "e", "i", "o", "u")
    so_samohlaskou = sum(1 for s in slova if s[0].lower() in samohlasky)
    cisla = any(char.isdigit() for char in slova)
    print(f"Pocet slov: {pocet_slov}")
    print(f"Pocet unikatne: {pocet_unikatne}")
    print(f"Najvacsie: {najdlhsie_slovo}")
    print(f"So samohlaskou: {so_samohlaskou}")
    print(f"Cisla: {text.upper()}")
    print(f"Cisla: {"Ano" if cisla else "nie"}")

analyzuj_text("Python je super jazyk, ktorý má veľa možností 2025")