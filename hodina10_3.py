zadany_slovnik = {
   'jmeno': 'Pepa',
   'prijmeni': 'Novak',
   'rok_narozeni': 1990,
   'email': 'pepa.novak@seznam.cz'
}

def obsahuje_udaje(klic, hodnota, slovnik):
    try:
        nalezena_hodnota = slovnik[klic]
        print(f"Klíč: {klic} nalezen.")
        
        if nalezena_hodnota == hodnota:
            vysledek = True
        else:
            vysledek = False
            print(f"Hodnota: {hodnota} nenalezena.")
            
    except KeyError:
        print(f"Klíč: {klic} nenalezen.")
        vysledek = False
        
    return vysledek

# Testovanie funkcie
vystup_1 = obsahuje_udaje(klic="jmeno", hodnota="Pepa", slovnik=zadany_slovnik)
vystup_2 = obsahuje_udaje(klic="jmeno", hodnota="Marek", slovnik=zadany_slovnik)
vystup_3 = obsahuje_udaje(klic="name", hodnota="John", slovnik=zadany_slovnik)

print(vystup_1, vystup_2, vystup_3, sep="\n")