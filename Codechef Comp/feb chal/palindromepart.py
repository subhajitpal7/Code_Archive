from collections import Counter
from collections import defaultdict as diction
def sol():
    s=list(input())
    n=len(s)
    idx_store=diction()
    for i in range(n):
        if s[i] in idx_store:
            idx_store[s[i]].append(i+1)
        else:
            idx_store[s[i]]=[i+1]
    count=Counter(s)
    temp_string=''
    val=0
    odd_letter=''
    for letter in count:
        if count[letter]%2!=0:
            val+=1
            odd_letter=letter
            if val>1:
                print(-1)
                break
        else:
            temp_string+=(letter*(count[letter]//2))
    else:
        right=temp_string[::-1]
        left=temp_string
        palindrome=''
        if val>0:
            if count[odd_letter]>1:
                right=(odd_letter*((count[odd_letter]-1)//2))+right
                left=left+(odd_letter*((count[odd_letter]-1)//2))
                palindrome=left+odd_letter+right
            else:
                palindrome=left+odd_letter+right
        else:
            palindrome=left+right
        t=[]
        for i in range(n):
            t.append(idx_store[palindrome[i]][0])
            idx_store[palindrome[i]].pop(0)
        print(*t)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
