t=int(input())
abc=[]
for i in range(t):
    li=list(map(int,input().split())) #n,nos,front
    abc.append(li)
#print(abc)
i=0
for w in range(len(abc)):
    while abc[i][1]>0:
        abc[i][1]=abc[i][1]-1
        if abc[i][1]==0:
            print(abc[i][2])
            continue
        #print("3",abc[i][1],abc[i][2])
        if abc[i][2]==abc[i][0]:
            abc[i][2]=1
            continue
        abc[i][2]=abc[i][2]+1
      
    i+=1

