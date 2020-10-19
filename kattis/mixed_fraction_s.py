inp = input().split()
inp = list(map(int,inp))
a = 0
b = 0
while inp[0] != 0 and inp[1] != 0:
  a = int(inp[0]/inp[1])
  b = inp[0]%inp[1]
  print(f'{a} {b} / {inp[1]}')
  a = 0
  b = 0
  inp.clear()
  inp = input().split()
  inp = list(map(int,inp))

