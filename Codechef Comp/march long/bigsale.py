def sol():
    n=int(input())
    loss=0
    for i in range(n):
        price,quan,dis=map(int,input().split())
        upprice=price+(price*(dis/100))
        acprice=upprice-(upprice*(dis/100))
        loss+=quan*(price-acprice)
    print(loss)
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
