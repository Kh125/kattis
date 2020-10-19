inp = []

for i in range(10):
  inp.append(int(input())%42)

set_ans = set(inp)
print(len(set_ans))