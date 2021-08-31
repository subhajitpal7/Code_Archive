import math
def sol():
    i,d,t=map(int,input().split())
    deg=((math.acos(d/i)*180)/math.pi)
    #print(deg)
    finaldeg=(t*deg)
    #print(finaldeg)
    coor=i*math.cos(finaldeg*(math.pi/180))
    #print(coor)
    print(round(coor%mod))
if __name__=="__main__":
    mod=pow(10,9)+7
    for _ in range(int(input())):
        sol()
