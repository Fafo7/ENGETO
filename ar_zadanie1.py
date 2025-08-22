import random

ovocie = ['jablko', 'hruska', 'banan', 'pomeranc']
kosik = []

while len(kosik) < 3:
    vybrane = random.choice(ovocie)
    if vybrane not in kosik:
        kosik.append(vybrane)
print(f"V košíku jsou: {kosik}")

ovocie = ['jablko', 'hruska', 'banan', 'pomeranc']
kosik = random.sample(ovocie, 3)  # vyberie 3 rôzne ovocia

print(f"V košíku máš: {', '.join(kosik)}")



