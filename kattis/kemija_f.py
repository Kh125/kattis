inp = input()
ans = inp
for i in range(len(inp)):
  if inp[i] == 'a' or inp[i] == 'e' or inp[i] == 'i' or inp[i] == 'o' or inp[i] == 'u':
    if i != len(inp)-1:
      # print('i',i)
      if inp[i+1] == 'p':
        if i+1 != len(inp)-1:
          # print('i+1',i+1)
          if inp[i] == inp[i+2]:
            new_sub = inp[i]+inp[i+1]+inp[i+2]
            ans = inp.replace(new_sub,inp[i],1)


print(ans)