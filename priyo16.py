M,N=map(int,input().split())
for p in range(M+1,N):
    if p>0:
        for i in range(2,p):
            if p%i==0:
                break
        else:
            print(p,end=" ")
