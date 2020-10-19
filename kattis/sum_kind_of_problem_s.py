tc = int(input())

for a in range(tc):
  inp = input().split(' ')
  inp = list(map(int,inp))
  od = 0
  ev = 0
  i = 1
  k = 1
  s1 = 0
  s2 = 0
  s3 = 0
  for j in range(1,inp[1]+1):
      s1+=j

  while od != inp[1] or ev != inp[1]:
    
    if i%2 != 0:
      s2 += i
      od += 1
    
    elif i%2 == 0:
      s3 += i
      ev += 1
    i += 1
  
  print(f'{a+1} {s1} {s2} {s3}')
 