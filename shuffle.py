def fun():
    M,X,Y = [int(x) for x in input().split()]
    vPosition = 1
    wPosition = 2
    for arrayLength in range(2,M-1,2):
 
        evenT_Length = arrayLength//2
        even_Length = arrayLength//2 + 1
        odd_Length = arrayLength//2 + 1
        positionGoing = even_Length*X//Y
 
        if vPosition < even_Length:
            new_vPosition = vPosition
            if new_vPosition > positionGoing:
                new_vPosition += 1
                new_vPosition = new_vPosition*2-1
        else:
            new_vPosition = vPosition - evenT_Length
            if new_vPosition > positionGoing:
                new_vPosition += 1
                new_vPosition = new_vPosition*2    
        vPosition = new_vPosition
        if wPosition < even_Length:
            new_wPosition = wPosition
            if new_wPosition > positionGoing:
                new_wPosition += 1
                new_wPosition = new_wPosition*2-1
        else:
            new_wPosition = wPosition - evenT_Length
            if new_wPosition > positionGoing:
                new_wPosition += 1
                new_wPosition = new_wPosition*2
        wPosition = new_wPosition
    print(wPosition,vPosition)
    return wPosition^vPosition
    
if __name__=="__main__":
    ans=[]
    for _ in range(int(input())):
        ans.append(fun())
    print(*ans,sep="\n")
