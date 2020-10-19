inp = input().split(' ')
inp = list(map(int,inp))
v_crd = [6,3,1,8,5,2]
t_crd = [3,2,1,6,3,0]
dict_ans = {8:'Province',5:'Duchy',2:'Estate',6:'Gold',3:'Silver',0:'Copper'}
tot =inp[0]*t_crd[0] +inp[1]*t_crd[1]+inp[2]*t_crd[2]
v_out = []
t_out = []
# print(tot)
# if()
for i in range(3,len(v_crd)):
  if v_crd[i] <= tot:
    v_out.append(v_crd[i])
  if t_crd[i] <= tot:
    t_out.append(t_crd[i])


if len(v_out) > 0 and len(t_out):
  print(dict_ans[max(v_out)],'or',dict_ans[max(t_out)])
elif len(v_out) == 0:
  print(dict_ans[max(t_out)])
else:
  print(dict_ans[max(v_out)])