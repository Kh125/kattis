
inp = input().split(' ')
ans = ''
for i in inp:
  if(inp.count(i) >1):
    ans = 'no'
    break
  else:
    ans = 'yes'

print(ans)