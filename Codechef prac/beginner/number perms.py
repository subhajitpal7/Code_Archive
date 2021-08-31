from itertools import permutations as perm
def sol():
    n=int(input())
    arr=input().split()
    ans=0
    for p in perm(arr):
        ans+=int(''.join(p))
    print(ans)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
