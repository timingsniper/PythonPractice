# Written by Percy Joonwoo Jang, 1800094804

import math

vals = input().split()
a = float(vals[0])
b= float(vals[1])
c = float(vals[2])

if b*b == 4*a*c:
    root = float((-b+math.sqrt(b*b-4*a*c))/(2*a))
    print('x1=x2=%.5f' %root)
elif b*b > 4*a*c:
    rootOne = float((-b+math.sqrt(b*b-4*a*c))/(2*a))
    rootTwo = float((-b-math.sqrt(b*b-4*a*c))/(2*a))
    if rootTwo>rootOne:
        temp = rootTwo
        rootTwo = rootOne
        rootOne = temp
    print('x1=%.5f;x2=%.5f' %(rootOne, rootTwo))
elif b*b < 4*a*c:
    rootReal = float(-b/(2*a))
    rootImaginary = float(math.sqrt(4*a*c-b*b)/(2*a))
    if rootReal == float(-0):
        rootReal = 0

    print('x1=%.5f+%.5fi;x2=%.5f-%.5fi' %(rootReal, rootImaginary, rootReal, rootImaginary))
