# Written by Percy Joonwoo Jang, 1800094804

import math


year = int(input())

if year%4 == 0 and (not(year%100 == 0) or year%400 == 0):
    print("1")
else:
    print("0")
