inp = input().split(' ')
inp = list(map(int,inp))
import datetime

dt = datetime.date(2009,inp[1],inp[0])
print(dt.strftime('%A'))