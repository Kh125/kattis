a = []
b = []
c = []
d = []
e = []
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
c = list(map(int,input().split(' ')))
d = list(map(int,input().split(' ')))
dir = int(input())
e = [a,b,c,d]

for i in range(len(e)):
  for j in range(len(e)):
    print(e[i][j],end = ' - ')
    print(i,j,end='\n')
  print()


def chg_ct():
  for i in range(4):
    if e[i][3] == 0:
      print('0')
    else:
      print('aft brk')
# # if dir == 2:
# print('if up')
# for i in range(len(e)):
#   for j in range(len(e)-1,-1,-1):
#     print(e[j][i],end=' ')
#   print()

# # if dir == 3:
# print('if down')
# for i in range(len(e)):
#   for j in range(len(e)):
#     print(e[j][i],end=' ')
#   print()

# # if dir == 2:
# print('if right')
# for i in range(len(e)):
#   for j in range(len(e)):
#     print(e[i][j],end=' ')
#   print()

if dir == 0:
# print('if left')
  # for i in range(4):
    # for j in range(4-1,-1,-1):
  for i in range(4):
      if e[i][3] == 0:
        print('0')
      else:
        print('aft brk')
