nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0
listed =True
freshed = []

def frehit(mini, maxi):
    for i in range(len(freshed)):
        if maxi >= freshed[i][0] and maxi <= freshed[i][1] and mini <= freshed[i][0]:
            freshed[i][0] = mini
        if mini >= freshed[i][0] and mini <= freshed[i][1] and maxi >= freshed[i][1]:
            freshed[i][1] = maxi
        if maxi >= freshed[i][0] and maxi <= freshed[i][1] and mini >= freshed[i][0] and mini <= freshed[i][1]:
            return
    freshed.append([mini, maxi])
        
def isfresh(ingred):
    for fr in freshed:
        if ingred >= fr[0] and ingred <= fr[1]:
            return True
    return False

for data in datas:
    if data == '':
        listed = False
        continue
    if listed:
        borne = data.split('-')
        frehit(int(borne[0]), int(borne[1]))
    else:
        ingred = int(data)
        if isfresh(ingred):
            total += 1

print(total)