def game():
    n,h=map(int,input().split())
    stacks=list(map(int,input().split()))[:n]
    queries=list(map(int,input().split()))
    index=0
    pickup=True
    dropdown=False
    for q in queries:
        if q==1 and index>0:
            index-=1
        elif q==2 and index<n-1:
            index+=1
        elif q==3 and stacks[index]>0 and pickup==True and dropdown==False:
            stacks[index]-=1
            pickup=False
            dropdown=True
        elif q==4 and stacks[index]<h and dropdown==True and pickup==False:
            stacks[index]+=1
            dropdown=False
            pickup=True
        elif q==0:
            break
        else:
            continue
        
    print(*stacks,sep=" ")
    
if __name__=="__main__":
    game()
