import math

polomery = (1, 2, 3, 4, 5)

# plocha kruhu
for polomer in polomery:
    plocha = math.pi * polomer **2
    print(f"Polomer: {polomer}, Plocha: {plocha:.2f}")

# import math
# polomery = (1, 2, 3, 4, 5)  
# plochy = list() 
# for polomer in polomery:
#     plochy.append(round(math.pi * pow(polomer, 2), 2))
# print(plochy)