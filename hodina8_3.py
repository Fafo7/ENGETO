import string

zadany_text = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
tiger123@email.cz auctor massa molestie at. Nunc 
tristique fringilla congue. Donec ante diam cnn@info.com,
dapibus lacinia vulputate vitae, ullamcorper in justo.
vitae massa. Cras abc@gmail.com vel libero felis.
In augue elit, porttitor nec molestie quis, auctor
a quam. Quisque b2b@money.fr pretium dolor et tempor
luctus lacinia risus. Maecenas posuere leo sit amet
spam@info.cz. elit tincidunt maximus. Aliquam erat
volutpat. Donec eleifend felis at leo ullamcorper
fringilla est. Maecenas gravida turpis nec ultrices
aliquet.'''

def je_email(slovo: str) -> bool:
    """Zkontroluje, zda je slovo platná emailová adresa.
    Podmínky: musí obsahovat '@', nesmí být prázdné, musí
    obsahovat tečku po '@', nesmí obsahovat žádné mezery."""
    if "@" not in slovo:
        return False
    casti = slovo.split("@")
    if len(casti) != 2:
        return False
    local, domena = casti
    if not local or not domena:
        return False
    if "." not in domena:
        return False
    return True

def uloz_emailove_adresy(text, kontrola):
    """Zpracuje text a vrátí seznam unikátních emailových adres.
    Zachovává pořadí, v jakém se objevily."""
    emailove_adresy = set()
    vysledky = []
    for slovo in text.split():
        slovo = slovo.strip(string.punctuation)
        if kontrola(slovo) and slovo not in emailove_adresy:
            emailove_adresy.add(slovo)
            vysledky.append(slovo)  # zachovame poradie
    return vysledky

vysledky = uloz_emailove_adresy(zadany_text, je_email)
print(f"Načtené emaily: {', '.join(vysledky)}")
