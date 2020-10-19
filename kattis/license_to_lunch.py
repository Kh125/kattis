tc = int(input())
inp = input().split(' ')
inp = list(map(int,inp))

min_v = min(inp)
indx = inp.index(min_v)
# if inp.count(min_v) > 1:
  # inp.index(min_v)

print(indx)