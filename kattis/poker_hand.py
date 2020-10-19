inp = input().split(' ')
max_ans = []
for i in range(len(inp)):
  inp[i] = inp[i][:-1]

for i in range(len(inp)):  
  max_ans.append(inp.count(inp[i]))

print(max(max_ans))