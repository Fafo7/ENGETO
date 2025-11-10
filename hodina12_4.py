def naformatuj_odkaz(rok):
    return f"https://cs.wikipedia.org/wiki/Wikipedie:%C4%8Cl%C3%A1nek_t%C3%BDdne/{rok}"


def projdi_vsechny_roky():
    for rok in range(2017, 2022):
        print(naformatuj_odkaz(rok))


if __name__ == "__main__":
    projdi_vsechny_roky()