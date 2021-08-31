def fun1(n):
    if n==0:
        return 2
    else:
        return fun1(n-1)+3*(n-1)
def fun2(n):
    return 2-6*n+(3*(n+1)*(n+2))//2-3
for i in range(20):
    print(fun1(i),fun2(i))
    
