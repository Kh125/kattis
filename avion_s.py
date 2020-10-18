li = []
for i in range(5):
  inp = input()
  if inp.find('FBI') != -1:
    li.append(i+1)

if(len(li)!=0):
  li.sort()
  for i in li:
    print(i,end=' ')
else:
  print('HE GOT AWAY!')