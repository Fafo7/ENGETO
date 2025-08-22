krstne_mena = ("Jan", None, "Petr", "Eva", "Marie", None, "Josef")
priezvisko = ("Novák", "Svoboda", None, "Novotný", "Dvořák", None, "Černý")

def odstran_none(udaje):
    """
    Odstraní None hodnoty z předaného seznamu.
    """
    return tuple(udaj for udaj in udaje if udaj is not None)

print(
    *odstran_none(krstne_mena),
    odstran_none(priezvisko), 
    sep='\n'
    )
  