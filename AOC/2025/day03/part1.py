nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0

for data in datas:
    max1 = max(data[:len(data) - 1])
    maxid = data[:len(data) - 1].index(max1)
    max2 = max(data[maxid + 1:])
    total += int(str(max1 + max2))

print(total)