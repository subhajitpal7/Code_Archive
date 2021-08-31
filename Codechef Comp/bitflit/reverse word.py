from functools import cmp_to_key as cmp
def mycmp(a, b):
    a, b = str(a), str(b)
    ab, ba = a + b, b + a
    if ab == ba:
        return 0
    if ab < ba:
        return -1
    return 1
def fun():
    n=int(input())
    m=list(map(int,input().split()))
    m=sorted(m,key=cmp(mycmp), reverse=True)
    print(''.join(map(str,m)))
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
