# Vytvoř proměnné vyska, vaha a jmeno,k těmto proměnným 
# zadej hodnoty v těchto jednotkách:vyska v metrech,vaha v kilogramech,jmeno, 
# zadej svoje jméno.dále vytvoř proměnnou bmi, kam uložíš výpočet jako: 
# váha / výška^2 (tedy umocni hodnotu výšky na druhou),nakonec hodnotu vypiš ve formátu: 
# Jméno:  - BMI: .

vyska = float(input("Zadej svou výšku v metrech: "))
vaha = float(input("Zadej svou váhu v kilogramech: "))
jmeno = input("Zadej své jméno: ")
kategorie = None
bmi = vaha / (vyska ** 2)
print(f"{jmeno}: - BMI: {bmi:.2f}.")
# Vysvětlivka: {:.2f} formátování pro dvě desetinná místa
# Pokud bys chtěl více desetinných míst, můžeš změnit číslo
if bmi < 18.5:
  kategorie = "Podváha"
elif bmi >= 18.5 and bmi <= 24.9:
  kategorie = "Zdravá výživa"
elif bmi >= 25 and bmi <= 29.9:
  kategorie = "Mírná nadváha"
elif bmi >= 30 and bmi <= 39.9:
  kategorie = "Obezita"
else:
  kategorie = "Těžká obezita"

print (f"Jméno: {jmeno}, kategorie: {kategorie}")
