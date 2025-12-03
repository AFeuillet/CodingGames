nfile = open('data.txt', 'r')
datas = nfile.read().split(',')

total = 0
buck = set()

def issame(stri, sp, j):
    cur = stri[:sp]
    for k in range(j):
        if cur != stri[sp * k :sp * (k + 1)]:
            return False
    return True

for data in datas:
    rang = data.split('-')
    for i in range(int(rang[0]), int(rang[1]) + 1):
        stri = str(i)
        ln = len(stri)
        for j in range(2, ln + 1):
            if i not in buck and ln % j == 0 and issame(stri, int(ln / j), j):
                total += i
                buck.add(i)
print(total)