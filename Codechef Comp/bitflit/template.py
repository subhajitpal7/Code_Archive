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
    m.sort(cmp=mycmp, reverse=True)
    print(m)
if __name__=="__main__":
    for i in range(int(input())):
        fun()
