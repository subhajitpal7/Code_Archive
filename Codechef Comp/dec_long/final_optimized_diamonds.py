def serie():
    for i in range(1,300001):
        b=str(i)
        if len(b)==1:
            series.append(int(b))
        else:
            while True:
                evencount=0
                oddcount=0
                for l in b:
                    if int(l)%2==0:
                        	evencount+=int(1)
                    else:
                        oddcount+=int(l)
                b=str(abs(evencount-oddcount))
                if len(b)==1:
                    series.append(int(b))
                    break
                else:
                    continue
def test():
    n=int(input())
    ans=series[n]*n
    for i in range(1,n):
        try:
            ans+=(series[n-i]+series[n+i])*(n-i)
        except:
            return 0
    return ans
if __name__=="__main__":
    ans=[]
    series=[]
    serie()
    for i in range(1,int(input())+1):
        print(test())
