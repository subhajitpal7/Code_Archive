def GoodOrBad():
    a=set(map(str,input().split()))
    b=set(map(str,input().split()))
    c=a.union(b)
    if len(c)<=6:
        return "similar"
    return "dissimilar"
        
if __name__=="__main__":
    for _ in range(int(input())):
        print(GoodOrBad())
