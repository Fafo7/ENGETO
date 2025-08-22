def analyza():
    text = input("Zadaj vetu: ")
    slova = text.split()
    unikatne = set(s.lower() for s in slova)
    pocet_slov = len(unikatne)
    print(f"vo vete {text} je {pocet_slov} unikátnych slov")
analyza()

def palindrom():
    retazec = input("Zadaj retazec: ")
    retazec = retazec.lower()
    retazec = "".join(znak for znak in retazec if znak.isalpha())
    return retazec == retazec[::-1]
print(palindrom())


