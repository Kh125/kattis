f = input().split(' ')
f = list(map(int,f))
set_li = []
ct = 0
while ct < f[1]:
  ct += 1
  inp = input().split()
  if inp[0] == '?':
    if inp[1]==inp[2]:
      print('yes')
    else:
      if inp[1] in set_li and inp[2] in set_li:
        print('yes')
      else:
        print('no')
  else:
    if inp[1] not in set_li:
      set_li.append(inp[1])
    if inp[2] not in set_li:
      set_li.append(inp[2])
