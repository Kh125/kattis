test_case = int(input())
uni = []
team = []
for i in range(test_case):
  inp = input().split(' ')
  if inp[0] not in uni:
    uni.append(inp[0])
    team.append(inp)

for i in range(12):
  print(team[i][0],' ',team[i][1])  