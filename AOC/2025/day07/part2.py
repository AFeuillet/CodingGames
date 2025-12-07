import copy
nfile = open('data.txt', 'r')
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
#print(total)

ll = len(plan)
planb = copy.deepcopy(plan)
for j in range(len(plan[-1])):
    if plan[-1][j] == '|':
       planb[-1][j] = 1

for i in range(ll):
    for j in range(len(planb[i])):
        if plan[ll - i - 2][j] == '|':
            planb[ll - i - 2][j] = planb[ll - i - 1][j]
            if j > 0 and plan[ll - i - 2][j - 1] == '^':
                if planb[ll - i - 2][j - 1] == '^':
                    planb[ll - i - 2][j - 1] = planb[ll - i - 1][j]
                else: 
                   planb[ll - i - 2][j - 1] += planb[ll - i - 1][j]
            if j < len(planb[i]) - 1 and plan[ll - i - 2][j + 1] == '^':
                if planb[ll - i - 2][j + 1] == '^':
                    planb[ll - i - 2][j + 1] = planb[ll - i - 1][j]
                else: 
                   planb[ll - i - 2][j + 1] += planb[ll - i - 1][j]
print(planb[0])