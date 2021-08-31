#!/bin/python3

import sys

def addperm(x,l):
    return [ l[0:i] + [x] + l[i:]  for i in range(len(l)+1) ]

def perm(l):
    if len(l) == 0:
        return [[]]
    return [x for y in perm(l[1:]) for x in addperm(l[0],y) ]
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        self.visit=1
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
                root.visit+=1
            else:
                root.visit+=1
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
                root.visit+=1
            else:
                root.visit+=1
                insert(root.left, node)
def expectedAmount(item):
    ansyoo=0
    r=Node(item[0])
    for i in range(1,len(item)):
        insert(r,Node(item[i]))
    current = r 
    s = []
    done = 0
    while(not done):
        if current is not None:
            s.append(current)
            current = current.left 
        else:
            if(len(s) >0 ):
                current = s.pop()
                if current.visit<=1:
                    ansyoo+=current.val
                current = current.right 
 
            else:
                done = 1
    return ansyoo

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        ans=0
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        arr=perm(a)
        for item in arr:
            ans+=expectedAmount(item)
        g=len(arr)
        divider=gcd(ans,g)
        if divider==g:
            print(ans)
        else:
            ans//=divider
            g//=divider
            print(str(ans)+"/"+str(g))
            
        
