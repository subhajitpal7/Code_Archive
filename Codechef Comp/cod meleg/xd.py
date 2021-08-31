def sol():
    n=int(input())
    temp=int(pow(n,.5))
    if pow(temp,2)==n:
        string="X"*temp+"D"*temp
        print(string.strip())
        return
    else:
        string=list("X"*temp+"D"*temp)
        l=n-pow(temp,2)
        temp2=temp
        while l>temp2:
             string.append("D")
             temp2+=1
             l-=temp
        string.insert(-l,"X")
        print(''.join(string))
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
