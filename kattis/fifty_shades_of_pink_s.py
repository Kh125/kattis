tc = int(input())
ct = 0
for i in range(tc):
  inp = input()
  inp = inp.lower()
  if inp.find('rose') != -1 or inp.find('pink') != -1:
    ct += 1
if ct ==0:
  print('I must watch Star Wars with my daughter')
else:
  print(ct)
