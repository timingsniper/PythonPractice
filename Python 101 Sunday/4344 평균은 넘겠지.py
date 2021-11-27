# Written by Percy Joonwoo Jang, 1800094804

import math
import operator


c = int(input())

for i in range(c):
    data = input().split()
    n = int(data[0])
    average = 0

    for j in range(1, n+1):
        average += int(data[j])
    average /= n
    #print(average)
    goodStudents = 0
    for j in range(1, n+1):
        if int(int(data[j])>average):
            goodStudents += 1

    #print(goodStudents)
    answer = round(goodStudents/n*100, 3)
    print("%.3f%%" %answer)
