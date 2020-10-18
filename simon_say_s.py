inp = int(input())

for i in range(inp):
  text = input()
  if text.find('Simon says') != -1:
    ans = text.replace('Simon says ','')
    print(ans)