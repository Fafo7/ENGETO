jmeno_souboru = "novy_soubor.txt"
pozdrav = "Ahoj, toto je první zápis do textového souboru"
# otevření souboru
txt_soubor = open(jmeno_souboru, mode="w", encoding="utf-8")
# metoda pro zapisování
txt_soubor.write(pozdrav)
# řádné zavření souboru
print(txt_soubor.closed)
txt_soubor.close()
print(txt_soubor.closed)

txt_soubor = open("novy_soubor.txt", mode="r", encoding="utf-8")
obsah_txt = txt_soubor.read()
print(obsah_txt)
txt_soubor.close()

druhy_radek = "\nTed pridavas druhy radek"

txt_soubor = open("novy_soubor.txt", mode="r+")
obsah_txt = txt_soubor.read()
txt_soubor.write(druhy_radek)

txt_soubor.close()