nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0
res = 0

def getmax(str):
    mx, px = -1, -1
    for j in range(len(str)):
        if int(str[j]) > mx:
            mx, px = int(str[j]), j
    return (mx, px)

for data in datas:
    nbsize = 12
    pos = 0
    for i in range(nbsize - 1, -1, -1):
        gm = getmax(data[pos:len(data) - i])
        res = res * 10 + gm[0]
        pos = gm[1] + pos + 1
    total += res
    res = 0

print(total)