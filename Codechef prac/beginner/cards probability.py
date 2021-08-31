def sol():
    n=int(input())
    seen=1
    ans=1
    while True:
        if seen/n>0.5:
            break
        else:
            ans+=1
        seen+=1
    print(ans)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
