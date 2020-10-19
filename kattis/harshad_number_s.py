inp = input()
tot = 0
ans_li = []

while len(ans_li) == 0:
  n = int(inp)
  for i in inp:
    tot += int(i)
  if n%tot == 0:
      ans_li.append(n)
  n += 1
  inp = str(n)
  tot = 0 
print(min(ans_li))
