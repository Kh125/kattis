import itertools
p = input()
inp = []
max = []
# print('length',len(max))
inp[:] = p
p = int(p)
inp = list(map(int,inp))
inp = list(itertools.permutations(inp))

for i in range(len(inp)):
  inp[i] = ''.join(str(x) for x in inp[i])
  inp[i] = int(inp[i])
  # print(inp[i])
  # print(type(inp[i]))

for i in range(len(inp)):
  if inp[i] > p:
    max.append(inp[i])

if len(max) == 0:
  print('0')
else:
  print(min(max))