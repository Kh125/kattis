inp = int(input())

def revdectobin(n):
  if n == 0:
    return ''
  else:
    if 2 <= n:
      return f'{n%2}{revdectobin(int(n/2))}'
    else:
      return f'{n}'
bin_num = revdectobin(inp)
print(int(bin_num,2))


