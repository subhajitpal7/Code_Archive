def get_all_substrings(s):
    length = len(s)
    return ''.join(sorted([s[i: j] for i in range(length) for j in range(i + 1, length + 1)]))
if __name__=="__main__":
    g=0
    s=input()
    S=get_all_substrings(s)
    for i in range(int(input())):
        p,m=map(int,input().split())
        k=((g*p)%m)+1
        print(S[k-1])
        g+=ord(S[k-1])
