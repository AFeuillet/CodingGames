import re
nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0
buck = {}
oper = datas[-1]
lend = 0
pos = 0

for i in range(len(oper)):
    if oper[i] not in ['+', '*']:
        lend += 1
    else:
        buck[pos - 1] = [''] * lend
        pos += 1
        lend = 0
buck[pos - 1] = [''] * (lend + 1)

for data in datas[:-1]:
    ppl = 0
    for i in range(len(buck) - 1):
        pl = len(buck[i])
        for j in range(pl):
            if (j + ppl) < len(data):
                buck[i][j] += data[j + ppl]
        ppl += pl + 1

pos = 0
for i in range(len(oper)):
    if oper[i] == '+':
        for b in buck[pos]:
            total += int(b)
        pos += 1
    elif oper[i] == '*':
        sub = 1
        for b in buck[pos]:
            sub *= int(b)
        total += sub    
        pos += 1
print(total)