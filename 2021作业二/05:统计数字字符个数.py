# Written by Percy Joonwoo Jang, 1800094804
import math

string = input()
numCount = 0

for i in string:
    if i in '0123456789':
        numCount += 1

print(numCount)
