inp = input()
inp = list(inp)
stat = True
pointer = 0
ct = 1
char = ''

# for i in range(1,len(inp)):
#   # print(i)
#   if not stat:
#     if ct > 1:
#       print('Occurrence')
#       ct = 1
#     stat = True
#   else:
#     if inp[i] == inp[i-1]:
#       print(inp[i]+'=='+inp[i-1])
#       pointer = i-1
#       print('Occurrence')
#       print('Pointer',pointer)
#       ct += 1
#       print('Count',ct)
#       stat = True
#       print('Stat',stat)
#     else:
#       stat = False
      

for i in range(1,len(inp)):
  if inp[i] == inp[i-1]:
    pointer = i-1
    ct += 1
    print('Pointer',pointer)
    print('Count',ct)
    stat = True
    print('==',inp[i],inp[i-1])
    print('if =',i)
  else:
    if ct>1:
      print('cont')
      print(inp[i])
      print(i)
    else:
      
      print('else else' ,inp[i-1])
      print(i)
    
