from random import randint
import os
# Zadanie: Hra Uhádni číslo
print("🎮 Hra: Uhádni číslo od 1 do 20!")
meno = input("Zadaj svoje meno: ")

pocitadlo_vysledkov = 0
body = 0
subor = "top_skore.txt"

while True:
    cisla = randint(1, 20)
    pokusy = 0
    max_pokusy = 5
    print("Máš 5 pokusov na uhádnutie čísla.")

    while pokusy < max_pokusy:
        hrac = input("Zadej číslo od 1 do 20: ")
        if hrac.isdigit():
            hrac = int(hrac)
            if 1 <= hrac <= 20:
                pokusy += 1
                if hrac == cisla:
                    print(f"✅ Gratulujem! Uhádol si číslo {cisla} na {pokusy}. pokus!")
                    pocitadlo_vysledkov += 1
                    # počítadlo bodov
                    pridane_body = 6 - pokusy
                    body += pridane_body
                    print(f"🏆 Získavaš {pridane_body} bodov!")
                    break
                elif hrac < cisla:
                    print("Zkus větší číslo.")
                else:
                    print("Zkus menší číslo.")
            else:
                print("❌ Číslo musí být v rozmezí 1 až 20.")
        else:
            print("❌ Zadej platné číslo.")
    else:
        print(f"❌ Prohrál jsi, správné číslo bylo {cisla}.")

# pokračovanie v hre
    znova = input("Chceš hrát znovu? (ano/ne): ").strip().lower()
    if znova != "ano":
        print("\n🎯 Herná štatistika:")
        print(f"✅ Výhry: {pocitadlo_vysledkov}")
        print(f"🏅 Celkové body: {body}")

         # ✅ Uloženie výsledku do súboru
        with open(subor, "a", encoding="utf-8") as f:
            f.write(f"{meno};{body}\n")

        # ✅ Načítanie a zoradenie TOP skóre
        if os.path.exists(subor):
            with open(subor, "r", encoding="utf-8") as f:
                skore_list = [line.strip().split(";") for line in f.readlines()]
                skore_list = [(m, int(b)) for m, b in skore_list]
                skore_list.sort(key=lambda x: x[1], reverse=True)  # zoradiť podľa bodov

            print("\n🏆 TOP 5 hráčov:")
            for i, (m, b) in enumerate(skore_list[:5], start=1):
                print(f"{i}. {m} - {b} bodov")
        print("Ďakujem za hru!")
        break
