def sol():
    s=input()
    temp=''
    for a in s:
        if a in letters:
            temp+=letters[25-(ord(a)-97)]
        elif a in letters1:
            temp+=letters1[25-(ord(a)-65)]
        else:
            temp+=a
    print(temp)
if __name__=="__main__":
    letters=list('abcdefghijklmnopqrstuvwxyz')
    letters1=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for _ in range(int(input())):
        sol()
