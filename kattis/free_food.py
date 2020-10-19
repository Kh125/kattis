tc = int(input())
min_day = []
for i in range(tc):
  inp = input().split(' ')
  inp = list(map(int,inp))
  rg = inp[1]-inp[0]+1
  for j in range(inp[0],inp[0]+rg):
    if j not in min_day:
      min_day.append(j)
  rg = 0

print(len(min_day))


