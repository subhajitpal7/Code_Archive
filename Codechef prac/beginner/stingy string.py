def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def sol():
    charcount,k=map(int,input().split())
    intcount,sum1=0,0
    s=input()
    for a in s:
        if (ord(a)-96)/k>2:
            intcount+=1
            charcount-=1
            sum1+=(ord(a)-96)
    if sum1%k==0:
        print(sum1//k+charcount-intcount,1)
    else:
        div=gcd(sum1+k*(charcount-intcount),k)
        print(sum1+k*(charcount-intcount)//div,k//div)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
