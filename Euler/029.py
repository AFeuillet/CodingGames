combis = set()
for a in range(2, 101):
    for b in range(2, 101):
        combis.add(a ** b)
print(len(combis))