nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0
dial_position = 50
for data in datas:
    nb = int(data[1:])
    if data[0] == 'L':
        dial_position -= nb
    else:
        dial_position += nb
    dial_position %= 100
    if dial_position == 0:
        total += 1
print(total)