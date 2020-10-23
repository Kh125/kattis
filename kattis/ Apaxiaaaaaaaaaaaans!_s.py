inp = input()+'*'
ans = ''
for i in range(len(inp)):
  if len(ans) != 0:
    if i != len(inp)-1:
      if inp[i] == inp[i+1]:
        if inp[i] != inp[i-1]:
          ans += inp[i]
      else:
        if inp[i] != inp[i-1]:
          ans += inp[i]
  else:
    ans += inp[i]  

print(ans)
