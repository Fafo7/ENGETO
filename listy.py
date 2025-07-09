# vytvořím novou proměnnou s hodnotou list
muj_seznam_1 = ["c", "b", "a", "d", "e"] 

# přidám do listu "int" 1
muj_seznam_1.append("1") 

# vypíšem proměnnou
print(muj_seznam_1)

print(muj_seznam_1[0])  # vypíše první prvek
print(muj_seznam_1.count("a"))  # spočítá kolikrát se vyskytuje "a"

muj_seznam_1.sort()  # seřadí list
print(muj_seznam_1)  # vypíše seřazený list

muj_list = [1, 3, 4, 5] 
muj_list.insert(1, 2) # vloží 2 na index 1
muj_list.append(6)  # přidá 6 na konec listu
print(muj_list)