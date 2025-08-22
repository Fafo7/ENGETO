index = 0

while index < 5:
   if index % 2 == 1:
       print("index:", index)
   index = index + 1

print("Smyčka skončila")

index = 0

while index <= 19:
   index = index + 1
   # pokud je aktuální hodnota proměnné sudá, 
   # pokračuj dále(přeskoč ji)
   if index % 2 == 0:
     continue
   print("index:", index)
