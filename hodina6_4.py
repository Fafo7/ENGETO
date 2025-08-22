import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = list()
pocitac_volby = list()

while len(hrac_volby) < 3 or len(pocitac_volby) < 3:
  if len(hrac_volby) < 3:
    hrac_volby.append(random.choice(moznosti))
  if len(pocitac_volby) < 3:
    pocitac_volby.append(random.choice(moznosti))

for hrac, pocitac in zip(hrac_volby, pocitac_volby):
    print(f"Tvoja volba: {hrac}, Počítačova volba: {pocitac}")
    if hrac == pocitac:
      vysledek = "Remíza"
    elif (hrac == 'kamen' and pocitac == 'nuzky') or \
         (hrac == 'nuzky' and pocitac == 'papir') or \
         (hrac == 'papir' and pocitac == 'kamen'):
        vysledek = "Vyhrál jsi!"
    else:
        vysledek = "Vyhráva počítač!"

print(f"Výsledek: {vysledek}")