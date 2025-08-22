data_1 = {
    "order": {
        "id": "1234", "type": "order.created", "chanel": "eshop cz"
    }
}
data_2 = {
    "order": {
        "id": "1234", "type": "order.created", "chanel": ""
    }
}
data_3 = {
    "order": {
        "id": "1234", "type": "order.created"
    }
}

def vrat_zemi_objednavky(objednavky: str) -> None:
    """funkce musi zpracovat promenne data_1 - data_3
    najit klič channel a rozdelit podle mezery
    pokud nenajde klič channel, ošettri vyjimku keyerror
    poukud funkce najde klič channel, ale bude prádzny, ošetrí indexerror"""
    try:
        channel = objednavky["order"]["chanel"]
        if not channel:
            raise IndexError("Channel is empty")
        zeme = channel.split(" ")
        print(f"Země objednávky: {', '.join(zeme)}")
    except KeyError:
        print("Chyba: Klič 'chanel' nebyl nalezen.")
    except IndexError as e:
        print(f"Chyba: {e}")
    
vrat_zemi_objednavky(data_1)
vrat_zemi_objednavky(data_2)
vrat_zemi_objednavky(data_3)

def vrat(data):
    try:
        return data["order"]["chanel"].split()(-1)
    except:
        print("Chyba: Klič 'chanel' nebyl nalezen nebo je prázdný.")
        return None
vrat(data_2)
