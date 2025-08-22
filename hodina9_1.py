# zápis správy do TXT súboru
def zapis_spravu_do_suboru(cesta, sprava):
    ovladac = open(cesta, "w", encoding="utf-8")
    pocet = ovladac.write(sprava + "\n")
    ovladac.close()
    return pocet
zapis_spravu_do_suboru(
    sprava="Ahoj, toto je testovacia správa.",
    cesta="testovacia_sprava.txt"
)