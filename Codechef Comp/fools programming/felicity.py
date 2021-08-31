if __name__=="__main__":
    t=int(input())
    for i in range(t):
        s=input()
        idx=0
        try:
            idx=s.index('*')
            print(s[:idx])
        except Exception as e:
            print(s)
            
    
