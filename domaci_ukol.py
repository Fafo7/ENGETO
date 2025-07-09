sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62

film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}

film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}

film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

filmy = {
    film_1["jmeno"]: film_1,
    film_2["jmeno"]: film_2,
    film_3["jmeno"]: film_3
}

print("VÍTEJ V NAŠEM FILMOVÉM SLOVNÍKU!".center(62))
print(oddelovac)
print("dostupné filmy | detaily filmu | doporuč film".center(62))
print(oddelovac)

print("Dostupné filmy:".center(62))
print(oddelovac)
print(" | ".join(filmy.keys()).center(62))
print(oddelovac)

print("Detaily filmu:".center(62))
print(oddelovac)
for film in filmy.values():
    print(f"{film['jmeno']} | {film['rating']} | {film['rok']} | {film['reziser']} | {film['stopaz']} min".center(62))
    print(oddelovac)

reziseri = {film["reziser"] for film in filmy.values()}
print("Všichni režiséři:".center(62))
print(oddelovac)
print(" | ".join(reziseri).center(62))
print(oddelovac)

print(filmy["Shawshank Redemption"]["reziser"].center(62))
print(oddelovac)
print(filmy["The Godfather"]["reziser"].center(62))
print(oddelovac)
print(filmy["The Dark Knight"]["reziser"].center(62))
print(oddelovac)