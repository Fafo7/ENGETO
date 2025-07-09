oddelovac = "=" * 30

for jazyk in enumerate(["Python", "Java", "C++"]):
    print(jazyk)
print(oddelovac)

for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
    print(pismeno)
print(oddelovac)

for pismeno in ("a", "b", "c", "d"):
    if pismeno in {"a", "b"}:
        continue
    print("Hodnota", pismeno, "je dulezita")
print(oddelovac)

for pismeno in ("a", "b", "c", "d"):
    print(pismeno.upper())
else:
    print("Vsechna pismena vypsana")