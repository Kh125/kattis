inp = input().split(' ')
inp = list(map(int,inp))
val = 0
if inp[0] == 0 and inp[1] == 0:
  print('Not a moose')
else:
  val = max(inp)*2
  if inp[0] == inp[1]:
    print('Even',val)
  else:
    print('Odd',val)
  

