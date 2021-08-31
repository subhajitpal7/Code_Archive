def sol():
    n=int(input())
    clist1=[]
    clist=[]
    for i in range(n):
        s=input()
        clist1.append(s[0])
        clist.append(s[-1])
    l=sorted(clist1)
    k=sorted(clist)
    dec=True
    for i in range(n):
        if l[i] not in k and dec:
            dec=False
        elif l[i] not in k and not dec:
            break
        else:
            continue
    else:
        print("The door will be opened")
        return
    print("The door cannot be opened")
        
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
