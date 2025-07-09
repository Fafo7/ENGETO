set_a = {"zena", "ruze", "kost"}
set_a.add("pisen")
set_a.update(("Matous", "Lucie"))
print(set_a)
print(sorted(set_a))
set_a.discard("kost")
print(set_a)


jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}

if jmeno in uzivatel and heslo == uzivatel[jmeno]:
  zprava = "Ahoj Marek, vítej v aplikaci! Pokračuj..."
else:
  zprava = "Uživatelské jméno nebo heslo nejsou v pořádku!"

print(f"Výstup: {zprava}")

