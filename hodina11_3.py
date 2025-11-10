import sys
jmeno = "Petr"
prijmeni = "Svetr"
if not jmeno or not prijmeni:
 print("Chybí jméno nebo příjmení")
 # jednička představuje obecně jakoukoliv chybu
 sys.exit(1)
else:
 print("Program pokračuje..")

if sys.platform == "darwin":
 print("Jsem na Macu..")
elif sys.platform == "windows":
 print("Jsem na Windowsech..")
elif sys.platform == "linux":
 print("Jsem na Linuxu..")