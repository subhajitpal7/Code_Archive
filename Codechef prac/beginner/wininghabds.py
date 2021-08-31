#!/bin/python3

import sys
from random import randint as rd 
from itertools import combinations
from functools import reduce
    
def winningHands(m, x, l):
    ans=0
    for i in range(1, len(l) + 1):
        for lst in list(combinations(l, i)):
            if reduce(lambda c, d: c*d%m, lst)%m==x:
                ans+=1
    # Complete this function
    return ans
if __name__ == "__main__":
    for i in range(100):
        #n, m, x = input().strip().split(' ')
        #n, m, x = [int(n), int(m), int(x)]
        n,m=rd(1,21),rd(1,10**6)
        x=rd(0,m)
        print(n,m,x)
        #a = list(map(int, input().strip().split(' ')))[:n]
        a = [rd(1000000,10000000) for i in range(n)]
        print(a)
        result = winningHands(m, x, a)
        print(result)
