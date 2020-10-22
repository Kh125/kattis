inp =  input().split(' ')
inp = list(map(int,inp))

if inp[0]+inp[1] == inp[2]:
  print(f'{inp[0]}+{inp[1]}={inp[2]}')
elif inp[0]-inp[1] == inp[2]:
  print(f'{inp[0]}-{inp[1]}={inp[2]}')
elif inp[0]*inp[1] == inp[2]:
  print(f'{inp[0]}*{inp[1]}={inp[2]}')
elif inp[0]/inp[1] == inp[2]:
  print(f'{inp[0]}/{inp[1]}={inp[2]}')
elif inp[0] == inp[1] + inp[2]:
  print(f'{inp[0]}={inp[1]}+{inp[2]}')
elif inp[0] == inp[1] - inp[2]:
  print(f'{inp[0]}={inp[1]}-{inp[2]}')
elif inp[0] == inp[1] * inp[2]:
  print(f'{inp[0]}={inp[1]}*{inp[2]}')
elif inp[0] == inp[1] / inp[2]:
  print(f'{inp[0]}={inp[1]}/{inp[2]}')