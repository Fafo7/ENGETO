oddelovac = "=" * 50

film_1 = {
    "nazov": "Interstellar", 
    "rok": 2014, 
    "reziser": "Christopher Nolan", 
    "herci": ["Matthew McConaughey", "Anne Hathaway"]
}
film_2 = {
    "nazov": "The Dark Knight", 
    "rok": 2008, 
    "reziser": "Christopher Nolan", 
    "herci": ["Christian Bale", "Heath Ledger"]
}
film_3 = {
    "nazov": "Titanic", 
    "rok": 1997, 
    "reziser": "James Cameron", 
    "herci": ["Leonardo DiCaprio", "Kate Winslet"]
}
# Vytvoření slovníku s filmy
filmy = {
    film_1["nazov"]: film_1, 
    film_2["nazov"]: film_2, 
    film_3["nazov"]: film_3
}

filmy_vypis = filmy.values()
herci = set()
reziser = set()

print("Všichni herci ve filmech:".center(62))
print(oddelovac)

for film in filmy_vypis:
    print(f" | ".join(film['herci']).center(62))

print(oddelovac)

for film in filmy.values():
    herci.update(film["herci"])

print("Všichni herci:".center(62))
print(oddelovac)
print(herci)
print(oddelovac)

#Vypíše filmy s Leonardem DiCapriem
print("Filmy s Leonardom DiCapriom:".center(62))
print(oddelovac)
for film in filmy.values():
    if "Leonardo DiCaprio" in film["herci"]:
        print(f"{film['nazov']} ({film['rok']}) - {film['reziser']}".center(62))
print(oddelovac)

# Vypíše herce, kteří se objevují ve filmech režiséra Christophera Nolana
print("Filmy režiséra Christophera Nolana:".center(62))
print(oddelovac)
for film in filmy.values():
    if "Christopher Nolan" in film["reziser"]:
        herci_text = ", ".join(film["herci"])
        print(f"{film['nazov']}: {herci_text}".center(62))
print(oddelovac)

# Zápis hercov, ktorý hrali v Nolanových filmoch do setu
herci_nolan = set()
for film in filmy.values():
    if film["reziser"] == "Christopher Nolan":
        herci_nolan.update(film["herci"])
print("Herci v Nolanových filmech:".center(62))
print(oddelovac)
print(", ".join(sorted(herci_nolan)).center(62))
print(oddelovac)