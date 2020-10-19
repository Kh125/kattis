inp = int(input())
no_of_candles = 0
ans = []
for i in range(inp):
  text = input().split(' ')
  text = list(map(int,text))

  for j in range(1,text[1]+1):
    no_of_candles += j
  no_of_candles  = no_of_candles+text[1]
  ans.append(no_of_candles)
  no_of_candles = 0  


for i,j in enumerate(ans):
  print(i+1,j)