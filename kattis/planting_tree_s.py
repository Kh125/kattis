tc = int(input())
inp = input().split(' ')
inp = list(map(int,inp))
inp.sort(reverse=True)
# print(inp)
ans = []
for i in range(1,tc+1):
  a = inp[i-1]+i-1
  ans.append(a)

print(max(ans)+2)