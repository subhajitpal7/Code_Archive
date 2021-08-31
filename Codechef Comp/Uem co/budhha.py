def substr(a, S):
    i = 0 #on a
    j = 0 #on S
    while i < len(a) and j < len(S):
        if a[i]==S[j]:
            i+=1
            j+=1
        else:
            j+=1
    if i == len(a):
        return True
    return False

q = int(input())

for _q in range(q):
    a = input().rstrip('\n')
    b = input().rstrip('\n')
    a_cap = a.upper()
    a_onlycap = [c for c in a if ord('Z')>=ord(c)>=ord('A')]
    
    if substr(b, a_cap) and substr(a_onlycap, b):
        print("YES")
    else:
        print("NO")
