obsah = [
    ["jmeno;prijmeni;email;projekt"],
    ["Matous;Holinka;m.holinka@firma.cz;hr"],
    ["Petr;Svetr;p.svetr@firma.cz;devops"]
]

for riadok in obsah:
    for polozka in riadok:
        print(polozka, end=", ")
    print(riadok)

for bunka in riadok[0].split(";"):
    print(bunka)