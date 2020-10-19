tc = int(input())
for i in range(tc):
  output = ''
  f_text = input()
  s_text = input()

  for j in range(len(f_text)):
    if f_text[j] == s_text[j]:
      output += '.'
    else:
      output += '*'
  
  print(f_text)
  print(s_text)
  print(output,'\n')
