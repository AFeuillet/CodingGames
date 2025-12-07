nfile = open('data_base.txt', 'r')
datas = nfile.read().split('\n')

total = 0
plan = []
datas[0] = datas[0].replace('S', '|')

for a in datas:
  plan.append(list(a))

for i in range(len(plan)):
    for j in range(len(plan[i])):
       if i + 1 < len(plan) and plan[i][j] == '|':
           if plan[i + 1][j] == '.':
              plan[i + 1][j] = '|'
           elif plan[i + 1][j] == '^':
              total += 1
              if plan[i + 1][j + 1] == '.':
                plan[i + 1][j + 1] = '|'
              if plan[i + 1][j - 1] == '.':
                plan[i + 1][j - 1] = '|'
#for pl in plan:
#   print(pl)
print(total)