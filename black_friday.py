inp = int(input())
li = input().split(' ')
li = list(map(int,li))
# print(inp,li)
# li.sort()
indx = 0
max_v = 0
for i in range(len(li)):
  if li.count(li[i]) == 1:
    if max_v < li[i]:
      max_v = li[i]
      indx = i

if max_v == 0:
  print('none')
else:
  print(indx+1)




# inp = input().split(' ')
# inp = list(map(int,inp))
# part = []
# for i in range(inp[1]):
#   part.append(input())

# ct = 0
# # for i in range(1,len(part)):
# #   if ct == inp[0]:
# #     print('break ct',ct)
# #     print('inp[0]',inp[0])
# #     break
# #   else:
# #     if part[ct] != part[i]:
# #       print('i',i)
# #       print('ct',ct)
# #       ct += 1
# #       print('after ct',ct)
# it = 1
# ocr = 0
# while ct != inp[0]:
#   if it == len(part)-1:
#     if part[it] != part[ct]:
#       ocr += 1
#       it  += 

# print(ct+1)