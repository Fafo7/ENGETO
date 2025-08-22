from statistics import mean
from random import choices
import statistics
import random

nahodne_cisla = choices(range(1, 1000), k=10)
#nahodne_cisla = [random.randint(1, 1000) for _ in range(10)]

prumer = mean(nahodne_cisla)
print(f"Čísla : {nahodne_cisla} Průměrná hodnota: {prumer:.2f}")


