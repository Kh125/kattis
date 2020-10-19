inp = int(input())
f_itr = 3
if inp == 1:
  print(f_itr*f_itr)
else:
  while inp > 1:
    f_itr = (f_itr*2) - 1
    inp -=  1
  print(f_itr*f_itr)