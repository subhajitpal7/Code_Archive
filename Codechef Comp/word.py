def sol():
    s=input()
    n=len(s)
    count=0
    word=list('chef')
    for i in range(n-4):
        for j in range(i,i+4):
            if s[i] not in word:
                break
        else:
            count+=1
    if count==0:
        print("normal")
    else:
        print("lovely",count)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
