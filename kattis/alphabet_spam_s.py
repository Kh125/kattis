inp = input()
ud_score = 0
upper = 0
lower = 0
symb = 0
for i in inp:
  if i == '_':
    ud_score += 1
  elif i.isupper() == True:
    upper += 1
  elif i.islower() == True:
    lower += 1
  else:
    symb += 1
  
print(ud_score/len(inp))
print(lower/len(inp))
print(upper/len(inp))
print(symb/len(inp))