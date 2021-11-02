# Written by Percy Joonwoo Jang, 1800094804

import math

vals = input().split()
h = int(vals[0])
r = int(vals[1])
volume = int(r*r*h*3.14159)
ans = 20000/volume
print(int(ans+1))
