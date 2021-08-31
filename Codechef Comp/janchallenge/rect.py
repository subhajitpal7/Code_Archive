for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(set(a))
    if len(b)==2:
        for t in b:
            if a.count(t)>2:
                print("NO")
                break
        else:
            print("YES")
    elif len(b)==1:
        if a.count(b[0])==4:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
