import copy
nfile = open('data.txt', 'r')
datas = nfile.read().split('\n')

total = 0
plan = []
for a in datas:
  plan.append(list(a))

leni = len(plan)
lenj = len(plan[0])
planb = copy.deepcopy(plan)

def checkpaper(i, j):
  st = 0
  if j + 1 < lenj:
    if plan[i][j + 1] == '@':
      st += 1
    if i + 1 < leni:
      if plan[i + 1][j + 1] == '@':
        st += 1
    if i - 1 >= 0:
      if plan[i - 1][j + 1] == '@':
        st += 1
  if j - 1 >= 0:
    if plan[i][j - 1] == '@':
      st += 1
    if i + 1 < leni:
      if plan[i + 1][j - 1] == '@':
        st += 1
    if i - 1 >= 0:
      if plan[i - 1][j - 1] == '@':
        st += 1
  if i - 1 >= 0:
    if plan[i - 1][j] == '@':
      st += 1
  if i + 1 < leni:
    if plan[i + 1][j] == '@':
      st += 1
  if st < 4:
    return True
  return False

tps = 0
while(True):
    for i in range(leni):
        for j in range(lenj):
            if plan[i][j] == '@' and checkpaper(i, j):
                plan[i][j] = '.'
                total += 1
    if total == tps:
      print(total)
      break
    tps = total
