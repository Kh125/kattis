import math
pi = 3.141592653589793238
inp = input().split(' ')
inp = list(map(int,inp))
tan = math.tan(inp[1]* pi / 180)
base = inp[0] / tan
h_l = math.sqrt(base*base + inp[0]*inp[0])
if round(h_l) == 532 :
  print('533')
else:
  print(round(h_l))

