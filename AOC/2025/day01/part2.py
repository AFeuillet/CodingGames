nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0
dial_position = 50
for data in datas:
    nbb = int(data[1:])
    for nb in range(nbb):
        if data[0] == 'L':
            dial_position -= 1
        else:
            dial_position += 1
        dial_position %= 100
        if dial_position == 0:
            total += 1
print(total)