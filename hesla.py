heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

heslo = input("Zadej heslo: ")

if heslo == "":
    print("Vynechal jsi pole s heslem!")
elif heslo[0].isdigit():
    print("Heslo nesmí začínat číselným znakem")
elif not any(char.isdigit() for char in heslo) or not any(char.isalpha() for char in heslo):
    print("Heslo musí obsahovat jak číselné znaky, tak písmena")
elif len(heslo) < 8:
    print("Heslo musí být alespoň 8 znaků dlouhé")
elif "@" in heslo:
    print("Heslo nesmí obsahovat '@'")
else:
    print("Heslo je v pořádku")
    