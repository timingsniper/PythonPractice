# Written by Percy Joonwoo Jang, 1800094804

import math
import operator


a, b = input().split()
#print(a)
#print(b)

a = a[::-1]
b = b[::-1]
firstNum = int(a)
secNum = int(b)

if firstNum > secNum:
    print(firstNum)
else:
    print(secNum)
