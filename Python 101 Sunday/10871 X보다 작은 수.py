# Written by Percy Joonwoo Jang, 1800094804

import math


n, x = map(int, input().split())
numbers = input().split()
answer = []

for i in numbers:
    if int(i)<x:
        answer.append(i)


print(*answer, sep = ' ')
