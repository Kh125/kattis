inp = input()
li = []
li[:] = inp
ct = 0
indx = 0
for i in range(1,len(li)):
  if ct > 0:
    if '<' == li[i]:
      ct+=1
      if i == len(li)-1:
        for j in range(ct*2):          
          inp = inp.replace(li[j+indx-ct],'!',1)          
            
    else:            

      for j in range(ct*2):        
        inp = inp.replace(li[j+indx-ct],'!',1)              
      indx = 0      
      ct = 0      
  else:
    if '<' == li[i]:
      ct+=1
      indx = i
      if i == len(li)-1:
        for j in range(ct*2):          
          inp = inp.replace(li[j+indx-ct],'!',1)          
      # else:                                

for i in inp:
  if i != '!':
    print(i,end='')


# inp = input()
# ans = inp
# ct = 0
# indx = 0
# for i in range(1,len(inp)):
#   if ct > 0:
#     if '<' == inp[i]:
#       ct+=1
#       if i == len(inp)-1:        
#         ans = ans[0:indx-ct:]+ans[indx+ct::]   
  

            
#     else:            
#       # index 3 ct 2      
#       ans = ans[0:indx-ct:]+ans[indx+ct::]              
#       ct = 0      
#   else:
#     if '<' == inp[i]:
#       ct+=1   
#       indx = i    
#       if i == len(inp)-1:      
#         print('reach',i)  
#         print(ct,indx)
#         ans = ans[0:indx-ct:]+ans[indx+ct::]   

# print(ans)