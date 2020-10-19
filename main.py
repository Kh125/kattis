test_case = int(input())
uni = []
team = []
for i in range(test_case):
  inp = input().split(' ')
  uni.append(inp[0])
  uni.append(inp[1])

for i in range(test_case):
  print(uni[i],'-->',team[i])