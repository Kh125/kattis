inp = input().split(' ')
inp = list(map(int,inp))

ct = 0
while ct <=max(inp[0],inp[1]):
  if ct!=0:
    ct += 1
    print(ct)
  else:
    ct = min(inp[0],inp[1])+1
    print(ct)