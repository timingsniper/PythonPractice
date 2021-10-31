# Written by Percy Joonwoo Jang, 1800094804
import math

n = int(input())
counter = 0
#total = 0
gold = 0
silver = 0
bronze = 0


while counter<n:
    a, b, c = map(int, input().split())
    gold += a
    silver += b
    bronze += c
    counter += 1


total = gold+silver+bronze
print('%d %d %d %d' %(gold,silver, bronze, total))
