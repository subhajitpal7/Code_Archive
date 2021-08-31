def fun():
    count=0
    n=int(input())
    while n>1:
        n//=2
        count+=1
    print(count)
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
