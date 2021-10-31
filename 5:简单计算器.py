# Written by Percy Joonwoo Jang, 1800094804
import math

s = input().split()
#print(s)
a = eval(s[0])
b = eval(s[1])
c = s[2]
if b == 0 and c == '/':
    print("Divided by zero!")
else:
    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '*':
        print(a*b)
    elif c == '/':
        print(int(a/b))
    else:
        print("Invalid operator!")
