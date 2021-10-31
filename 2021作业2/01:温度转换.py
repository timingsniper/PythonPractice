# Written by Percy Joonwoo Jang, 1800094804
import math

testVal = input()
numVal = float(testVal[0:len(testVal)-1])

if(testVal[len(testVal)-1]== 'F'):
    ans = (numVal-32)/1.8
    print('%.2fC' %ans)
elif(testVal[len(testVal)-1]== 'K'):
    ans = numVal + 273.15
    print('%.2fC' % ans)
