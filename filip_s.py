area = input().split(' ')
# area = list(map(int,area))
a = int(area[0][2]+area[0][1]+area[0][0])
b = int(area[1][2]+area[1][1]+area[1][0])

if a > b:
  print(a)
else:
  print(b)