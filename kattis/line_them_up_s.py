tc = int(input())
org_li = []
at = 0
bt = 0
for i in range(tc):
  org_li.append(input())

a = sorted(org_li)
b = sorted(org_li,reverse=True)
for i in range(len(org_li)):
  if a[i] == org_li[i]:
    at += 1
  if b[i] == org_li[i]:
    bt += 1

if at == len(org_li):
  print('INCREASING')
elif bt == len(org_li):
  print('DECREASING')
else:
  print('NEITHER')