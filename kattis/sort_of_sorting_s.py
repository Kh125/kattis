tc = int(input())
inp = []
ans = ''
ans_li = []
while tc != 0:
  for i in range(tc):
    inp.append(input())  
  inp = sorted(inp, key=lambda x:x[:2])
  
  for i in range(len(inp)):
    if i != len(inp)-1:
      ans += inp[i]+'\n'
    else:
      ans += inp[i]
  ans_li.append(ans)
  inp.clear()
  ans = ''
  tc = int(input())

for i in range(len(ans_li)):
  if i != len(ans_li)-1:
    print(ans_li[i])
    print()
  else:
    print(ans_li[i])