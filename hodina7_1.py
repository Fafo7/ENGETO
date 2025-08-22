ciselna_rada = [1, 2, 3, 4, "sest", 5, 6, 7, 8, 9]
ciselna_rada1 = (2, 4, 8, "a")
ciselna_rada2 = [1, 3, 5, 7, 9]

def secti_vsechna_cisla(sekvence):
    soucet_cisel = 0

    for cislo in sekvence:
        if isinstance(cislo, str) and not cislo.isnumeric():
            continue
        soucet_cisel += int(cislo)
    else:
        print(soucet_cisel)

secti_vsechna_cisla(ciselna_rada)
secti_vsechna_cisla(ciselna_rada1)
secti_vsechna_cisla(ciselna_rada2)