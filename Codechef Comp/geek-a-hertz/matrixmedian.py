def matrixmedian():
    n=int(input())
    s=[]
    for i in range(n):
        b=sorted(list(map(int,input().split())))[:n]
        m=b[n//2]
        s.append(m)
    s.sort()
    print(s[n//2])
if __name__=="__main__":
    for _ in range(int(input())):
        matrixmedian()
