inp_statue = int(input())

printer = 1
day = 0
printed_statue = 0

while printed_statue < inp_statue:
  if (printer < inp_statue - printed_statue):
    day += 1
    printer += printer

  else:
    day += 1
    printed_statue += printer


print(day)