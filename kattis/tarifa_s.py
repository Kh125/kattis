mb = int(input())
tc = int(input())
avg = 0
rm = 0
for i in range(tc):
  usage = int(input())
  avg += mb
  avg = avg - usage

print(avg+mb)