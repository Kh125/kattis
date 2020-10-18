cs = ''
tot_min = 0
prob = []
r_ct = 0
while cs != '-1':
  cs = input() 
  if cs == '-1':
    break
  min_l,no_p,chk = cs.split(' ')
  min_l = int(min_l)

  if(chk == 'wrong'):
    prob.append(no_p)
  else:
    r_ct += 1
    if(no_p in prob):
      tot_min += (prob.count(no_p)*20) + min_l
    else:
      tot_min += min_l


print(r_ct,tot_min)