a = input()
t = 0
c = 0
g = 0
tot = 0
for i in range(len(a)):
  if a[i] == 'T':
    t += 1
  elif a[i] == 'C':
    c += 1
  else:
    g += 1
tot = (t*t) + (c*c) + (g*g)
while t >= 1 and g >= 1 and c >= 1:
  tot += 7
  t -= 1
  c -= 1
  g -= 1
print(tot)