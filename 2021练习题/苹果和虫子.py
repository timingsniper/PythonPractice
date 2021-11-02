# Written by Percy Joonwoo Jang, 1800094804

import math

vals = input().split()
n = int(vals[0])
x = int(vals[1])
y = int(vals[2])

applesLeft = float(n - y/x) 
print(int(applesLeft)) #남은 사과 수의 정수값만 프린트. 예를들어 applesLeft가 7.75이면 7만 프린트
