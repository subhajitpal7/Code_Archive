#!/bin/python3

import sys
from collections import defaultdict as dic
from random import randint as rd
def winningLotteryTicket(tickets):
    temp=list(tickets.keys())
    #l=[set(a) for a in temp]
    #print(l)
    #print(temp)
    n=len(temp)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if set(temp[i]).union(set(temp[j]))==win:
                #print(sorted(set(temp[i]).union(set(temp[j]))))
                ans+=((tickets[temp[i]])*(tickets[temp[j]]))
                #print(tickets[temp[i]],"*",tickets[temp[j]])
    if '0123456789' in temp and tickets['0123456789']%2!=0:
       ans+=(tickets['0123456789'])*(tickets['0123456789']//2)
    else:
        ans+=(tickets['0123456789']-1)*(tickets['0123456789']//2)
    return ans
    # Complete this function
def winningLotteryTicket1(tickets):
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if tickets[i].union(tickets[j])==win:
                ans+=1
    return ans
if __name__ == "__main__":
    n = int(input().strip())
    tickets = dic()
    tickets1=[]
    tickets_i = 0
    r1=pow(10,18)+7
    r2=pow(10,32)+7
    win=set('0123456789')
    for tickets_i in range(n):
        #y=set(input().strip())
        y=set(str(rd(r1,r2)))
        tickets_t = "".join(sorted(y))
        tickets1.append(y)
        if tickets_t in tickets.keys():
            tickets[tickets_t]+=1
        else:
            tickets[tickets_t]=1
    result = winningLotteryTicket(tickets)
    result1 = winningLotteryTicket1(tickets1)
    print(tickets)
    print("my result",result)
    print("Actual result",result1)
    #print(tickets)
