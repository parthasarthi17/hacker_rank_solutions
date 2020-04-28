n=int(input()) #total no of clouds
c=list(map(int,input().split()))
jump=0
i=0
for i in range(n):
    if c[i]==1:
        i-=1
    else :
        jump+=1    
print(jump-1)