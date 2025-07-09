# Skuska pre Engeto kurz Python
jmeno = input("Zadej sve jmeno: ")
vek = int(input("Zadej svuj vek: "))

if vek >= 18:
 print(f"Bezva, {jmeno.upper()}, muzes s nami na pivo.")
else:
 print(f"Bohuzel, {jmeno.title()},jeste nemuzes pit.")