import math
tc = input().split(' ')
tc = list(map(int,tc))
p_h = math.sqrt(tc[1]*tc[1]+tc[2]*tc[2])
for i in range(tc[0]):
  inp = int(input())
  if inp <= p_h:
    print('DA')
  else:
    print('NE')
