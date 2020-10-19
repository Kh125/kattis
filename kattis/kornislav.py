inp = input().split(' ')
inp = list(map(int,inp))
max_li = []
import itertools
set_li = set(itertools.permutations(inp))
for i in set_li:
  max_li.append(min(i[0],i[2])*min(i[1],i[3]))

print(max(max_li))