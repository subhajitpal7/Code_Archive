# cook your dish here
import math
test = int(input())
for _ in range(test):
    n = int(input())
    t =int(math.sqrt(n))
 
    temp= n- (t*t)
    ans=0
    while temp<700 and t>0:
        ans += temp
        t-=1
        temp = n-(t*t)
    ans = t*700+ ans
    print(ans)
