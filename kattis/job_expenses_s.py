tc = int(input())
if tc <= 20000:
  x = list(map(int, input().split()))
  neg = 0
  for i in range(tc):
    if x[i] == 0:
      break
    elif x[i] < 0:
      neg += abs(x[i])

  if neg == 0:
    print(neg)
  else:
    print(neg)
