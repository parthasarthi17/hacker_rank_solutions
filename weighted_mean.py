n=int(input()) #Entering no of inputs
x=list(map(int,input().split()))
w=list(map(int,input().split()))
sumx=0
sumw=0
i=0
for a in x:
    sumx=sumx+a*w[i]
    sumw=sumw+w[i]
    i+=1
res=sumx/sumw
print("{:.1f}".format(res))