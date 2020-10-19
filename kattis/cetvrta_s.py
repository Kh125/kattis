inp1 = input().split(' ')
inp2 = input().split(' ')
inp3 = input().split(' ')
ans = []

if inp1[0] == inp2[0]:
  ans.append(inp1[1])
  ans.append(inp2[1])
  if inp3[1] == ans[0]:
    print(inp3[0],ans[1])
  else:
    print(inp3[0],ans[0])

elif inp1[0] == inp3[0]:
  ans.append(inp1[1])
  ans.append(inp3[1])
  if inp2[1] == ans[0]:
    print(inp2[0],ans[1])
  else:
    print(inp2[0],ans[0])

elif inp2[0] == inp3[0]:
  ans.append(inp2[1])
  ans.append(inp3[1])
  if inp1[1] == ans[0]:
    print(inp1[0],ans[1])
  else:
    print(inp1[0],ans[0])