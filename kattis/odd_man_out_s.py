tc = int(input())
for i in range(tc):
  inp = int(input())
  prs = input().split(' ')

  for j in range(len(prs)):
    if prs.count(prs[j]) == 1:
      print(f'Case #{i+1}: {prs[j]}')