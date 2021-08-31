def fun():
    string=input()
    n=len(string)
    ans=0
    match=list("chef")
    for i in range(n-3):
        for j in range(i,i+4):
            if string[j] not in match:
                break
            match.remove(string[j])
        else:
            ans+=1
        match=list("chef")
    if ans==0:
        print("normal")
    else:
        print("lovely",ans)
if __name__=="__main__":
    for _ in range(int(input())):
        fun()
