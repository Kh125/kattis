inp = int(input())
name = []
ct = 1
f = ''
s = ''
while inp != 0:

  for i in range(inp):
    name.append(input())
  print(f'SET {ct}')
  for i in range(len(name)):
    if i%2 == 0:     
        f += name[i]+'\n'      
  
  for j in reversed(range(len(name))):
    if j%2 != 0:
      if j == 1:
        s += name[j]
      else:
        s += name[j]+'\n'
  print(f+s)

  name.clear()
  s = ''
  f = ''
  ct += 1
  inp = int(input())