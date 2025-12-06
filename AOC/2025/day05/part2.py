import copy
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
        if maxi >= freshed[i][1] and mini <= freshed[i][0]:
            freshed[i][0] = mini
            freshed[i][1] = maxi
        if maxi >= freshed[i][0] and maxi <= freshed[i][1] and mini >= freshed[i][0] and mini <= freshed[i][1]:
            return
    freshed.append([mini, maxi])
    
for data in datas:
    if data == '':
        listed = False
        break
    if listed:
        borne = data.split('-')
        frehit(int(borne[0]), int(borne[1]))

fresh = []

while len(fresh) != len(freshed):
  fresh = copy.deepcopy(freshed)
  freshed = []
  for f in fresh:
      frehit(int(f[0]), int(f[1]))

for fr in freshed:
    total += fr[1] - fr[0] + 1

print(total)

