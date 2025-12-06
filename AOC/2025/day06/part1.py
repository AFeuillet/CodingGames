import re
nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0
buck = {}

for data in datas:
    alln = re.findall(r'(\d+)', data)
    if alln:
        for i in range(len(alln)):
            if i not in buck:
                buck[i] = []
            buck[i].append(int(alln[i]))
    else:
        alln = re.findall(r'(\+|\*)', data)
        for i in range(len(alln)):
            if alln[i] == '+':
                total += sum(buck[i])
            elif alln[i] == '*':
                sub = 1
                for val in buck[i]:
                    sub *= val
                total += sub
print(total)