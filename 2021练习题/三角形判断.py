# Written by Percy Joonwoo Jang, 1800094804

import math

edges = input().split()
edgeOne = int(edges[0])
edgeTwo = int(edges[1])
edgeThree = int(edges[2])

if edgeOne+edgeTwo>edgeThree and edgeTwo+edgeThree>edgeOne and edgeOne+edgeThree>edgeTwo:
    print("yes")
else:
    print("no")
