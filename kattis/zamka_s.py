li = []
sum = 0
a = int(input())
b = int(input())
c = int(input())
for i in range(a,b+1):
  i = str(i)
  for j in i:
    sum += int(j)
  if sum == c:
    li.append(int(i))
  sum = 0
  
print(min(li))
print(max(li))    
