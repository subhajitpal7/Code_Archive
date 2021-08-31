def sol():
    arr=list(map(int,input().split()))
    ss=['Beginner','Junior Developer','Middle Developer','Senior Developer','Hacker','Jeff Dean']
    if 1 in arr:
        print(ss[arr.count(1)])
    else:
        print(ss[0])

if __name__=="__main__":
    for _ in range(int(input())):
        sol()
