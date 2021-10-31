# Written by Percy Joonwoo Jang, 1800094804
import math

stuNum = int(input())
counter = 0
totalSum = 0
#average = 0

while counter<stuNum:
    stuAge = int(input())
    totalSum+=stuAge
    counter+=1


average = float(totalSum/stuNum)
print('%.2f' %average)
