x = 0
y = 1
vysledky = []
delka_rady = 15

i = 0

while i < delka_rady:
  vysledky.append(x)
  x, y = y, x + y
  i += 1

vysledky_str = ", ".join(map(str, vysledky))
print(f"Fibonacci: [<{vysledky_str}>]")
  

#print(f"Fibonacci: [<{', '.join(map(str, vysledky))}>]")