def sol():
    n=int(input())
    fingers=list(map(int,input().split()))
    gloves=list(map(int,input().split()))
    front=False
    back=False
    revgloves=gloves[::-1]
    if fingers==gloves:
        return "both"
    for i in range(n):
        if fingers[i]>gloves[i]:
            break
    else:
        front=True
    for i in range(n):
        if fingers[i]>revgloves[i]:
            break
    else:
        back=True
    if front and back:
        return "both"
    elif front and not back:
        return "front"
    elif not front and back:
        return "back"
    else:
        return "none"
if __name__=="__main__":
    for _ in range(int(input())):
        print(sol())
