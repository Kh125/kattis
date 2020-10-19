tc = int(input())
tot = 0
pv_hr = 0
while tc != -1:
  for i in range(1,tc+1):
    inp = input().split(' ')
    inp = list(map(int,inp))
    pv_hr = inp[1]-pv_hr
    tot += inp[0]*pv_hr
    pv_hr = inp[1]
  
  print(tot,'miles')
  tot = 0
  pv_hr = 0
  tc = int(input())
