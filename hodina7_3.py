def vytvor_cele_jmeno(jmeno, prijmeni):
    """
    Spoji jméno a příjmení do jednoho celého jména.
    
    """

    return ".".join([
        jmeno[0].lower(),
        prijmeni.lower()
    ])

print(vytvor_cele_jmeno("Jan", "Novák"))