def sol():
    n=int(input())
    teams=sorted(map(str,input().split()))
    #print(teams)
    team_score=[]
    for i in range(n):
        s=input().split()
        team_score.append([int(s[1]),s[0]])
    team_score.sort(reverse=True)
    #print(team_score)
    #print(sorted([team_score[0][1],team_score[1][1]]))
    if sorted([team_score[0][1],team_score[1][1]])==teams:
        print("right")
    else:
        print("wrong")
if __name__=="__main__":
    for _ in range(int(input())):
        sol()
