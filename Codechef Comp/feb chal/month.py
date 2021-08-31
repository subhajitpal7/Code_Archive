def fun():
    n,m,x,k=map(int,input().split())
    s=input()
    if m==0 or x==0:
        print("no")
        return
    odd_workers=s.count('O')
    even_workers=s.count('E')
    if m==1:
        print("yes" if min(x,odd_workers)>=n else "no")
    elif m%2!=0:
        oddmc=m//2+1
        evenmc=m//2
        val=0
        while True:
            n-=min(x,odd_workers)
            odd_workers-=min(x,odd_workers)
            oddmc-=1
            if n<=0:
                val=1
                break
            elif oddmc<=0 or odd_workers<=0:
                break
        if val==1:
            print("yes")
            return
        else:
            val=0
            while True:
                n-=min(x,even_workers)
                even_workers-=min(x,even_workers)
                evenmc-=1
                if n<=0:
                    val=1
                    break
                elif evenmc<=0 or even_workers<=0:
                    break
            if val==1:
                print("yes")
            else:
                print("no")
    else:
        oddmc=m//2
        evenmc=m//2
        val=0
        while True:
            n-=min(x,odd_workers)
            odd_workers-=min(x,odd_workers)
            oddmc-=1
            if n<=0:
                val=1
                break
            elif oddmc<=0 or odd_workers<=0:
                break
        if val==1:
            print("yes")
            return
        else:
            val=0
            while True:
                n-=min(x,even_workers)
                even_workers-=min(x,even_workers)
                evenmc-=1
                if n<=0:
                    val=1
                    break
                elif evenmc<=0 or even_workers<=0:
                    break
            if val==1:
                print("yes")
            else:
                print("no")
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
