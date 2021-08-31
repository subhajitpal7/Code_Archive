import random
t=int(input())
for i in range(t):
    n=random.randrange(100)
    print("i/p",n)
    if n<3:
        print(1)
    else:
        count=0
        while n>1:
            if n<3:
                count+=1
                break
            elif n%3==0:
                n=n//3
            elif (n+1)%3==0:
                n=n+1
            elif (n-1)%3==0:
                n=n-1
            count+=1
        print(count)
