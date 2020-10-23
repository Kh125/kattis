tc = input().split(' ')
tc = list(map(int,tc))
ct = 0
tot = 0
inp = input().split(' ')
inp = list(map(int,inp))

for i in range(len(inp)):
  tot += inp[i]
  if(tc[1]-tot >= 0):
    ct += 1
  
print(ct)