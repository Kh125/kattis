
text = input()
temp = 1
a = 0
b = 0
c = 0

a_v = 1
b_v = 0
c_v = 0
for i in text:
  if i == 'A':
    if a == 0:
      temp = b_v
      b_v = a_v
      a_v = temp
      a = 1
    else:
      temp = b_v
      b_v = a_v
      a_v = temp
      a = 0
  elif i == 'B':
    if b == 0:
      temp = b_v
      b_v = c_v
      c_v = temp
      b = 1
    else:
      temp = b_v
      b_v = c_v
      c_v = temp
      b = 0
  else:
    if c == 0:
      temp = a_v
      a_v = c_v
      c_v = temp
      c = 1
    else:
      temp = a_v
      a_v = c_v
      c_v = temp
      c = 0


if a_v == 1:
  print('1')
elif b_v == 1:
  print('2')
else:
  print('3')