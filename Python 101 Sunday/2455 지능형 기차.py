# Written by Percy Joonwoo Jang, 1800094804


import math
import operator


endFlag = 0
currentNum = 0
most = 0

while endFlag == 0:
    deboard, board = map(int, input().split())
    if board == 0:
        endFlag = 1
    currentNum -= deboard 
    currentNum += board
    if currentNum > most:
        most = currentNum


print(most)
