inp = input()
assign = 'PER'
days = 0
for i in range(len(inp)):
  if inp[i] != assign[i%3]:
    days += 1
print(days)