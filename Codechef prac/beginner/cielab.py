def sol():
    a,b=map(int,input().split())
    if (a-b)%10==9:
        print(a-b-1)
    else:
        print(a-b+1)
if __name__=="__main__":
    sol()

	
