
tc = int(input())
uni = []
team = []
for i in range(tc):
  a,b = input().split(' ')
  uni.append(a)
  team.append(b)

for i in range(tc):
  print(uni[i],'*',team[i])