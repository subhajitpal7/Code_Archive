import sys
def football(s):
    n=len(s)
    A=0
    B=0
    a=0
    b=0
    for i in range(1,len(s)+1):
        if i%2!=0:
            a+=1
        else:
            b+=1
        if s[i-1]=='1' and i%2!=0:
           A+=1
        elif s[i-1]=='1' and i%2==0:
            B+=1
        if i<=10:
            if(A-B>=1):
                shots_leftb=5-b
                if shots_leftb<A-B:
                    print("TEAM-A",i)
                    break
            elif(B-A>=1):
                shots_lefta=5-a
                if shots_lefta<B-A:
                    print("TEAM-B",i)
                    break     
        else:
            if i%2==0:
                if A>B:
                    print("TEAM-A",i)
                    break
                elif B>A:
                    print("TEAM-B",i)
                    break
    else:
        print("TIE")

if __name__=="__main__":
    ans=[]
    while True:
        try:
            b=input()
            football(b)
        except EOFError:
            break
