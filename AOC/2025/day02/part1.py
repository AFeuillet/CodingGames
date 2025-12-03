nfile = open('data.txt', 'r')
datas = nfile.read().split(',')

total = 0

for data in datas:
    rang = data.split('-')
    for i in range(int(rang[0]), int(rang[1]) + 1, 1):
        stri = str(i)
        ln = len(stri)
        if ln % 2 == 0 and stri[:int(ln / 2)] == stri[int(ln / 2):]:
            total += i
print(total)