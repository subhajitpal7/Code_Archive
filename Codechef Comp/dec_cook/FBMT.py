for q in range(int(input())):
    first = ""
    second = ""
    a = 0
    b = 0
    for j in range(int(input())):
        temp = input()
        if(j==0):
            first = temp
            a += 1
        elif(temp == first):
            a += 1
        else:
            second = temp
            b += 1
    if a>b:
        print(first)
    elif a<b:
        print(second)
    else:
        print("Draw")
