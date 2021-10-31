# Written by Percy Joonwoo Jang, 1800094804
import math

val = int(input())
hund = int(val/100)
fifty = int((val%100)/50)
twenty = int((val%100-fifty*50)/20)
ten = int((val%100-fifty*50-twenty*20)/10)
five = int((val%10)/5)
one = int(val%10-5*five)

print(hund)
print(fifty)
print(twenty)
print(ten)
print(five)
print(one)
