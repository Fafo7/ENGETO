uzivatel = {}
uzivatel["priezvisko"] = "Novák"
uzivatel["vek"] = 42
admin = uzivatel.copy()
admin["práva"] = ("cteni", "zapis", "mazani")
print(len(admin))
print(len(admin["práva"]))

s1 = {
    "ab", "cd", "ce", "ef", "ab", "cd", "ef", 
    "xy", "ef", "ac", "cd", "a", "b", "c", "d"
    }
s2 = {"ab", "xz", "a"}
print(set(s1).intersection(s2))
print(set(s1).union(s2))
print(set(s1).difference(s2))

while len(s1) > 5:
    s1.pop()
print(s1)

s1.discard("cd")

s2c = s2.copy()
s2c.add("h")
print(set(s1).symmetric_difference(s2c))
print(len(s1.symmetric_difference(s2c)))

print("jano", "lubo", "karol", sep="\n")