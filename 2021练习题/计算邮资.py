# Written by Percy Joonwoo Jang, 1800094804

import math

vals = input().split()
weight = int(vals[0])
#print(weight)
express = str(vals[1])
ans = int(0)

if weight<=1000:
    ans+=8
elif weight>1000:
    ans+=8
    ans+=int(int(int(weight-1000)/500)*4)
    if 1 <=int((weight-1000)%500) <= 499:
        ans+=4

if(express == 'y'):
    ans+=5

print(ans)
