a = int(input())
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(a):
  inp =  input()
  inp = inp.lower()
  missing = ''
  for i in range(len(alphabet)):  
      if alphabet[i] not in inp:        
        missing += alphabet[i]
  
  if len(missing) == 0:
    print('pangram')
  else:
    print(f'missing {missing}')