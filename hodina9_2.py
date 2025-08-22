def precti_logy(cesta):
    with open(cesta) as f:
        return f.readlines()
    
def vyber_pouze_typ(sekvence):
    return tuple(msg.split()[0] for msg in sekvence)


cesta = "logy.txt"
print(vyber_pouze_typ(precti_logy(cesta)))
zaznamy = precti_logy(cesta)
print(vyber_pouze_typ(zaznamy))
    