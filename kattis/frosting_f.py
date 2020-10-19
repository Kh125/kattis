test_case = int(input())
row_1 = []
row_2 = []
col_0 = 0
col_1 = 0
col_2 = 0
a = input()
b = input()
row_1 = list(map(int,a.split(' ')))
row_2 = list(map(int,b.split(' ')))


for i in range (1,test_case+1):
  for j in range(1,test_case+1):
    if (i+j)%3 == 1:
      col_1 += row_1[i-1]*row_2[j-1]
    elif (i+j)%3 == 2:
      col_2 += row_1[i-1]*row_2[j-1]
    else:
      col_0 += row_1[i-1]*row_2[j-1]

print(col_0,col_1,col_2)