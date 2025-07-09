import time

for _ in range(5):
    print("Ahoj, světe!")
    time.sleep(1)  # Pauza na 1 sekundu


for seznam in jmena:
    for jmeno in seznam:
        print(jmeno)