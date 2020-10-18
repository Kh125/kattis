new = ['@','8','(','|)','3','#','6','[-]','|','_|','|<','1','[]\/[]','[]\[]','0','|D','(,)','|Z','$','\'][\'','|_|','\/','\/\/','}{','`/','2']
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text = []
inp = input() 
inp = inp.lower()

text[:] = inp
for i in text:
  if 'a'<=i and 'z'>=i:
    alp.index(i)
    print(new[alp.index(i)],end ='')
  else:
    print(i,end='')