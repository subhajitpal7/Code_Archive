n = int(input())
def query():
    count = 0
    if L == []:
        return 0
    for item in L:
        #print (item)
        if len(item) % 2 == 0 and len(item) > 0:
            count += 1
    return count
L = []
while True:
    b = input()
    if b == '-1':
        break
    b = b.split()
    if b[0] == 'Q':
        print (query())
        continue
    b = list(map(int, b[1:]))
    if b[0] in range(0,n+1) and b[1] in range(0,n+1):
        if L == []:
            temp = {b[0],b[1]}
            L.append(temp)
        else:
            for i in range(len(L)):
                if b[0] in L[i]:
                    if b[1] not in L[i]:
                        for j in range(len(L)):
                            if b[1] in L[j]:
                                L[i] = L[i].union(L[j])
                                L[j] = {}
                                break
                        else:
                           L[i].add(b[1])
                    break
                if b[1] in L[i]:
                    if b[0] not in L[i]:
                        for j in range(len(L)):
                            if b[0] in L[j]:
                                L[i] = L[i].union(L[j])
                                L[j] = {}
                                break
                        else:
                            L[i].add(b[0])
                    break
            else:
                temp = {b[0],b[1]}
                L.append(temp)
                
                    
    
