inp = int(input())
tot = 0
for i in range(inp):
  num = input()
  b = int(num[:-1])
  p = int(num[len(num)-1])
  tot += (b**p)

print(tot)