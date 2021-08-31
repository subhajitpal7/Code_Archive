from random import randint
def mi():
    return map(int,input().split())
def ii():
    return int(input())
def update(time,lane):
    for j in range(lane,n):
        if direction[j]==1:
            position[j]+=(time*velo[j])
        else:
            position[j]-=(time*velo[j])
def sol():
    timecons=y/s
    time=0
    i=0
    while i<n:
        if direction[i]==1:
            if position[i]>0 and position[i]-length[i]<0:
                time+=(timecons+(abs(position[i]-length[i])/velo[i]))
                update(timecons+(abs(position[i]-length[i])/velo[i]),i)
                i+=1
            elif position[i]<=0 and (abs(position[i])/velo[i])<=timecons:
                time+=(timecons+(abs(position[i]-length[i])/velo[i]))
                update(timecons+(abs(position[i]-length[i])/velo[i]),i)
                i+=1
            else:
                time+=timecons
                update(timecons,i)
                i+=1
        else:
            if position[i]<0 and position[i]+length[i]>0:
                time+=(timecons+(abs(position[i]+length[i])/velo[i]))
                update(timecons+(abs(position[i]+length[i])/velo[i]),i)
                i+=1
            elif position[i]>=0 and abs(position[i])/velo[i]<=timecons:
                time+=(timecons+(abs(position[i]+length[i])/velo[i]))
                update(timecons+(abs(position[i]+length[i])/velo[i]),i)
                i+=1
            else:
                time+=timecons
                update(timecons,i)
                i+=1
    print(time)
if __name__=="__main__":
    for i in range(ii()):
        n,s,y=mi()
        velo=list(mi())
        direction=list(mi())
        position=list(mi())
        for i in range(n):
            if position[i]>0:
                position[i]-=pow(10,-6)
            else:
                position[i]+=pow(10,-6)
        length=list(mi())
        sol()
