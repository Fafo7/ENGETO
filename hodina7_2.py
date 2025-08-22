from random import choices


def vygeneruj_tuple(delka, max_hodnota):

    return tuple(choices(range(max_hodnota), k=delka))

print(vygeneruj_tuple(10, 4))  
print(vygeneruj_tuple(10, 100)) 
print(vygeneruj_tuple(15, 150)) 
