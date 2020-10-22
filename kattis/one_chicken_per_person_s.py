inp = input().split(' ')
inp = list(map(int,inp))

if inp[0] < inp[1]:
  dif = inp[1]-inp[0]
  if dif == 1:
    print(f'Dr. Chaz will have {dif} piece of chicken left over!')
  else:
    print(f'Dr. Chaz will have {dif} pieces of chicken left over!')

else:
  dif = inp[0] - inp[1]
  if dif == 1:
    print(f'Dr. Chaz needs {dif} more piece of chicken!')
  else:
    print(f'Dr. Chaz needs {dif} more pieces of chicken!')