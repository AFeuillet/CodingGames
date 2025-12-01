from os import system
from time import sleep
nfile = open('data_base.txt', 'r')
datas = nfile.read().split('\n')

total = 0
dial_position = 50


def print_sc(dial_position):
    system('clear')
    for i in range(99):
        if dial_position == i:
            print("\033[1mXX\033[0m", end ='')    
        else:
            print(f"{i:02d}", end ='')
    print('')
    sleep(0.001)

for data in datas:
    nbb = int(data[1:])
    for nb in range(nbb):
        print_sc(dial_position)
        if data[0] == 'L':
            dial_position -= 1
        else:
            dial_position += 1
        dial_position %= 100
        if dial_position == 0:
            total += 1
print(total)