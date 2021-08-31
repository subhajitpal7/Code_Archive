if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        loop=n//7
        sum1=0
        for i in range(1,loop+1):
            sum1+=7*i
        print(sum1)
