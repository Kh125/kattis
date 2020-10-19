test_case = int(input())
no_of_candies = 0
check_pos = []
print()
while test_case > 0:
  pm_mean = int(input())
  no_chdl = pm_mean
  while no_chdl > 0:
    no_of_candies += int(input())
    no_chdl -= 1

  if no_of_candies%pm_mean == 0:
    check_pos.append(no_of_candies)
  else:
    check_pos.append(no_of_candies)
  no_of_candies = 0
  test_case -= 1
  
  print()


for i in check_pos:
  print(i)




