import math
tc = int(input())
ct = 0
li = []
txt = ''
for i in range(tc):
  inp = input()
  row = int(math.sqrt(len(inp)))
  col = row
  if len(inp)%5 != 0:
    for ii in range(len(inp),len(inp)+(5-len(inp)%5)):
      inp += '#'
  
  for j in range(row):
    li.append([])
  for a in range(row):
    for b in range(ct,col+ct):
      li[a].append(inp[b])    
    ct += col
  for a in reversed(range(col)):
    for b in range(row):
      if li[b][a] != '#':
        txt += li[b][a]
  print(txt)

  row = 0
  col = 0
  li.clear()
  txt=''
  ct = 0