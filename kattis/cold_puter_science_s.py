inp = int(input())

text = input().split(' ')
text = list(map(int,text))
ct = 0
for i in range(len(text)):
  if text[i] < 0:
    ct += 1

print(ct)