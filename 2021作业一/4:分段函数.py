# Written by Percy Joonwoo Jang, 1800094804
import math

val = float(input())
if 0<=val<5:
    ans = -val+2.5
    print('%.3f' %ans)
elif 5<=val<10:
    ans = 2-1.5*(val-3)*(val-3)
    print('%.3f' % ans)
elif 10<=val<20:
   ans = val/2-1.5
   print('%.3f' % ans)
