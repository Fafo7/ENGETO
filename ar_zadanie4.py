vstupni_text = "Ahoj všem, tady Engeto"
def zdvojnasob_znaky(vstupni_text):
  zdvojene = (znak * 2 for znak in vstupni_text)
  return "".join(zdvojene) 

vysledek = zdvojnasob_znaky(vstupni_text)
print(f"Zdvojené znaky: {vysledek}")