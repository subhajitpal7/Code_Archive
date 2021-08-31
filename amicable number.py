def sumPropDiv(n):
    dSum = 0
    for x in range(1, n//2 + 1):
        if n % x == 0:
            dSum += x
    return dSum
store=[]
storesum=[]
def amicSum(number):
    answer = 0
    for x in range(4, number):
        if sumPropDiv(x) > 4:
            if sumPropDiv(sumPropDiv(x)) == x and sumPropDiv(x) != x:
                store.append(x)
                print("store",store)
                answer += x
                storesum.append(answer)
                print("storesum",storesum)
    return answer
print(amicSum(100000))
print(store)
print(storesum)
