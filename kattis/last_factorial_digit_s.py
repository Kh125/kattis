tc = int(input())
fact = 1
for i  in range(tc):
  inp = int(input())
  for i in range(1,inp+1):
    fact *= i
    
  fact = str(fact)
  print(fact[len(fact)-1])
  fact = int(fact)
  fact = 1