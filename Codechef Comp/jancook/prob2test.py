def sol():
        k,a0,a1=map(int,input().split())
        #print(k,a0,a1)
        var=[2,6,14]
        ans=a0+a1
        s=str(a0)+str(a1)
        temp=a0+a1
        if k==2:
                print("YES" if temp%3==0 else "NO")
                return
        val=0
        for i in range(2,k):
            s+=str(ans%10)
            temp+=ans%10
            if ans%10==0:
                val=1
                break
            if s[-4:]=='2486':
                break
            ans+=(ans%10)
        if val==1:
            print("YES" if temp%3==0 else "NO")
        else:
            count=0
            idx=0
            if (k-i+1)>0:
                idx=((k-i+1)%4)
                count=((k-i+1)//4)
            act_ans=temp+(count*20)
            if idx>=1:
                act_ans+=var[idx-1]
            if act_ans%3==0:
                print("YES")
            else:
                print("NO")
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
