index = 0

while index <= 20:
    if len(str(index)) != 2:
        index = index + 1
    else:
        print(index)
        index = index + 1

else:
    print("-" * 23, "Podmínka -> False".center(23), "-" * 23, sep="\n")

print(">Pokračujem pod smyčkou<")


count = 0
total = 0
while count < 5 or total < 20:
    count += 1 
    total += count
    print(f"Count: {count}, Total: {total}")
print("Loop finished")

data = [0, 1, 2, 3, 5, "Matúš",  "Lukáš", "Tomáš"]
dvojnasobok = [cislo * 2 for cislo in data if isinstance(cislo, int)]
print(dvojnasobok)
