index = 1

while index <= 6:
   print("index:", index)
   # --break-- přeskočí zbytek smyčky a i klauzuli else
   if index == 4:
       print("Mám hodnotu 4")
       break
   index = index + 1

else:
   print("index:", index, "--> hodnoty jsou si rovny, ukončuji smyčku..")

# interpret pokračuje až ZDE
print("Pokračuji..")