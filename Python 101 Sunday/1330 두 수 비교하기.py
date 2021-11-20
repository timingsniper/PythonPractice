# Written by Percy Joonwoo Jang, 1800094804

import math


a, b = map(int, input().split())

if a>b:
    print(">")
elif a<b:
    print("<")
elif a == b:
    print("==")
