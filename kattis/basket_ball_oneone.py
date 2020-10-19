inp = input()
li = []
li[:] = inp
len_li = len(li)
# dict = {}
cc = 0
val_a = 0
val_b = 0
while cc <len_li:
  li[cc+1] = int(li[cc+1])
  cc+=2

for i in range(0,len_li,2):
  if(li[i]=='A'):
    val_a += li[i+1]
  else:
    val_b += li[i+1]
  

if val_a > val_b:
  print('A')
else:
  print('B')