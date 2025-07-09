import re

def uziv_meno(meno):
    meno = meno.strip()  
    # Odstránenie špeciálnych znakov a medzier
    meno_ciste = re.sub(r'[^a-zA-Z0-9]', '', meno) 
    vsetko_ok = True

    # Kontrola podmienok    
    if len(meno_ciste) != 8:
        print("Meno musí mať presne 8 znakov po odstránení špeciálnych znakov.")
        vsetko_ok = False
    if meno_ciste and meno_ciste[0].isdigit():
        print("Meno nesmie začínať číselným znakom.")
        vsetko_ok = False
    if not any(char.isdigit() for char in meno_ciste):
        print("Meno musí obsahovať aspoň jedno číslo.")
        vsetko_ok = False
    if not any(char.isalpha() for char in meno_ciste):
        print("Meno musí obsahovať aspoň jedno písmeno.")
        vsetko_ok = False
    if vsetko_ok:
        print(f"Prihlásenie bolo úspešné. Uživatelské meno: {meno_ciste}")
        return meno_ciste
    else:
        print("Prihlásenie zlyhalo. Skúste to znova.")
        return None
    
def uziv_heslo(heslo):
    heslo = heslo.strip()
    vsetko_ok = True
    # Kontrola podmienok
    if len(heslo) < 10:
        print("Heslo musí mať viac ako 10 znakov.")
        vsetko_ok = False
    if not any(char.isupper() for char in heslo):
        print("Heslo musí obsahovať aspoň jedno veľké písmeno.")
        vsetko_ok = False
    if not any(char.islower() for char in heslo):
        print("Heslo musí obsahovať aspoň jedno malé písmeno.")
        vsetko_ok = False
    if not any(char.isdigit() for char in heslo):
        print("Heslo musí obsahovať aspoň jedno číslo.")
        vsetko_ok = False
    if any(char in "@#" for char in heslo):
        print("Heslo nesmie obsahovať znaky '@' alebo '#'.")
        vsetko_ok = False
    if vsetko_ok:
        print("Heslo je v poriadku.")
        return heslo
    else:
        print("Heslo nie je v poriadku. Skúste to znova.")
        return None

while True:    
    meno = input("Zadej jméno: ")
    heslo = input("Zadaj heslo: ")
    vysledok = uziv_meno(meno)
    vysledok = uziv_heslo(heslo)
    if vysledok is not None and heslo is not None:
        print("Prihlásenie bolo úspešné.")
        break
         