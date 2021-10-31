# Written by Percy Joonwoo Jang, 1800094804
import math

a, b = map(int, input().split())
#print(a)
#sprint(b)
ans = 0

for counter in range(a,b+1):
    if(counter % 17 == 0):
        #print(counter)
        ans += counter

print(ans)
