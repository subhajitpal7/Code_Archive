def actualsol(n,s):
    l=len(s)
    good,a,b=0,0,0
    for i in xrange(n*l):
        if s[i%l]=='a':
            a+=1
        elif s[i%l]=='b':
            b+=1
        if a>b:
            good+=1
    return good
def derivedsol(n,s):
    l=len(s)
    if n*l<pow(10,6):
        return actualsol(n,s)
    else:
        good,good2,good3=actualsol(500,s),actualsol(501,s),actualsol(502,s)
        diff1=good2-good
        diff2=good3-good2
        if diff1==0:
            return good
        elif diff2==0:
            return good2
        else:
            return good2+diff2*(n-501)
if __name__=="__main__":
    for _ in xrange(int(raw_input())):
        inp=raw_input().split()
        n=int(inp[1])
        s=inp[0]
        print(derivedsol(n,s))
