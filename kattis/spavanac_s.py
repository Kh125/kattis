
inp = input().split(' ')
inp = list(map(int,inp))
hr = 0
minu = 0

if inp[0] == 0:
  tot = 1440+inp[1] -45
else:
  tot = (inp[0]*60)+inp[1] - 45
# print(tot)
if tot >= 60:
  hr = int(tot/60)
  minu = tot%60

print(hr,minu)
