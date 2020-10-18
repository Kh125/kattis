inp = input().split(' ')
inp = list(map(int,inp))
nm = [1,1,2,2,2,8]

for i in range(len(nm)):
  print(nm[i]-inp[i],end=' ')