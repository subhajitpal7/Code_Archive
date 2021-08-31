def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
def twinpair(a):
    k=False
    i=3
    while(a>0):
        k=isPrime(i)==True and isPrime(i+2)==True
        if(k):
            a-=1
        i+=2
    s=str(i)
    return s
def fun():
    val=0
    n=int(input())
    phonenumber=[]
    for i in range(n):
        phonenumber.append(input())
    s=int(input())
    temp=""
    k=int(input())
    for i in range(len(str(s))):
        b=s%10
        s//=10
        c=str(twinpair(b+k))
        temp+=c
    temp=temp[::-1]
    for item in phonenumber:
        if temp in item:
            val=1
            print(item)
    if val==0:
        print("No Numbers Match") 
    
if __name__=="__main__":
    for i in range(int(input())):
        fun()
