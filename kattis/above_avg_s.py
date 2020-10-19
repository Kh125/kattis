tc = int(input())
pc = []
out = []
while tc > 0:
  stu = input()
  count = 0
  tot = 0
  pc = list(map(int,stu.split(' ')))
  i = 1
  j = 1
  vr = pc[0]
  while i <=vr:
    tot += pc[i]
    i += 1
  while j<=vr:
    if pc[0]*pc[j]>tot:
      count += 1
    j+=1

  out.append(format(round((count/pc[0])*100,3),'.3f'))
  count = 0
  tot = 0
  tc -= 1

for i in out:
  print(f'{i}%')

