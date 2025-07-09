cisla = range(1, 16)

print(" | ".join(
    "FizzBuzz" if cislo % 3 == 0 and cislo % 5 == 0 else
    "Fizz" if cislo % 3 == 0 else
    "Buzz" if cislo % 5 == 0 else
    str(cislo)
    for cislo in cisla
))