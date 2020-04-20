b=list(map(int,input().split()))
keyboard=list(map(int,input().split()))
mouse=list(map(int,input().split()))
li=[]
budget=b
budget_1=b
verify=-1
count=0
if b[1]==1 and b[2]==1:
    max1=b[0]-keyboard[0]-keyboard[0]
    if max1>0:
        print(max1)
    else:
        print(-1)
else:
    x=min(len(keyboard),len(mouse))
    y=max(len(keyboard),len(mouse))
    for i in range(x):
        for j in range(y):
            if int(keyboard[i])+int(mouse[j])<=int(b[0]):
                count=count+1
                verify=b[0]-keyboard[i]-mouse[i]
                li.append(i)
                li.append(j)
    max1=0
    #print(li)
    for j in range(count):
        m=int(li[(2*j)+1])
        l=int(li[(2*j)])
        #print("l",l,"m",m)
        e=int(keyboard[l])
        f=int(mouse[m])
        if e+f>max1:
             max1=e+f
             
    
    if max1<=0:
        print(-1)#impossible to buy
    else:
        print(max1)
