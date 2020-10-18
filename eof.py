
# while True:
#     try:
#         s=input()
        
#     except EOFError:
#         break


from sys import stdin

for a,b in enumerate(stdin):
  c,d = b.split(' ')
  c = int(c)
  d = int(d)
  c = abs(c)
  d = abs(d)
  max = max(c,d)
  min = min(c,d)
  print(max-min,'')


