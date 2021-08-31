def UniformStrings():
    s=input()
    l=len(s)
    dec=0
    for i in range(1,l+1):
        if (s[i-1]=='0' and s[i%l]=='1') or (s[i-1]=='1' and s[i%l]=='0'):
            dec+=1
        if dec>2:
            break
    else:
        return "uniform"
    return "non-uniform"
if __name__=="__main__":
    for _ in range(int(input())):
        print(UniformStrings())
