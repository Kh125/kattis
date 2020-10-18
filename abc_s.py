counter = 3
num_val = input()
alpha_val = input()
num_li = []
alpha_li = []
output = []

num_li = list(map(int, num_val.split(' ')))
alpha_li[:] = alpha_val

sort_num = sorted(num_li)
dict_num = {'A': sort_num[0], 'B': sort_num[1], 'C': sort_num[2]}

for i, j in enumerate(sort_num):
    output.append(dict_num[alpha_li[i]])

print('{} {} {}'.format(output[0], output[1], output[2]))
