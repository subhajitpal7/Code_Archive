from collections import Counter as cnt
def sol():
    s=list(input())
    n=len(s)
    if n%2!=0 and cnt(s[:n//2])==cnt(s[n//2+1:]):
        print("YES")
    elif n%2==0 and cnt(s[:n//2])==cnt(s[n//2:]):
        print("YES")
    else:
        print("NO")
        
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
