mk = 0
indx = 0
for i in range(5):
  inp = input().split(' ')
  inp = list(map(int,inp))
  if mk < inp[0]+inp[1]+inp[2]+inp[3]:
    mk = inp[0]+inp[1]+inp[2]+inp[3]
    indx = i

print(indx+1,mk)