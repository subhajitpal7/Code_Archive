#python file to generate input output
#just run the file and enter desired number of test cases
#The input and output will be printed in the respective IN.TXT and OUT.TXT
import random
def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id
def edit_distance():
    n=random.randrange(1,17)
    s,t=random_id(n),random_id(n)
    inp.append(s)
    inp.append(t)
    len1,len2=len(s),len(t)
    D=[[0]*(len2+1) for i in range(len1+1)]
    for i in range(len1+1):
        D[i][0]=i
    for j in range(len2+1):
        D[0][j]=j
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if s[i-1]==t[j-1]:
                D[i][j]=D[i-1][j-1]
            else:
                D[i][j]=min(D[i][j-1],D[i-1][j],D[i-1][j-1])+1
    return D[i][j]
if __name__=="__main__":
    f=open('out.txt','w')
    f1=open('in.txt','w')
    inp=[]
    ans=[]
    n=int(input())
    print(n,file=f1)
    for _ in range(n):
        ans.append(edit_distance())
    print(*ans,sep="\n",file=f)
    print(*inp,sep="\n",file=f1)
    f1.close()
    f.close()