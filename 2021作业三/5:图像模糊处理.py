# Written by Percy Joonwoo Jang, 1800094804
import math
import copy 

n, m = map(int, input(). split())
cross = []
fin = []
for i in range(n):
    line = list(map(int, input().split()))
    cross.append(line)

fin = copy.deepcopy(cross) #deepcopy has to be implemented, avoiding same pointer reference
#to use deepcopy, remember to add import copy at the header
for i in range(1,n-1):
     for j in range(1,m-1):
         tt = round((cross[i-1][j] + cross[i+1][j] + cross[i][j-1] + cross[i][j+1] + cross[i][j])/5) #using int() results in wrong answer
         fin[i][j] = tt


for i in range(n):
    for j in range(m):
        print(fin[i][j], end=" ")
    print()
