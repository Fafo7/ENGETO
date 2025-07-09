cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

for cislo in cisla:
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("FizzBuzz")
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)