x=list(map(int,input().split())) #x1 v1 x2 v2
if (x[0]>x[2] and x[1]>x[3]) or (x[0]<x[2] and x[1]<x[3]) :
    print("NO")#They will never meet
else :
    i=1
    if x[1]==x[3] and x[0]!=x[1]:
        print("NO")
        break
    if x[0]>x[2]:
        while 1:
            if x[0]==x[2]:
                print("Yes")
                break
            x[0]=x[0]+i+x[1]
            x[2]=x[2]+i+x[3]
            i=i+1
            if x[0]<x[2]:
                print("NO")
                break
    i=1
    if x[0]<x[2]:
        while 1:
            if x[0]==x[2]:
                print("Yes")
                break
            x[0]=x[0]+i+x[1]
            x[2]=x[2]+i+x[3]
            i=i+1
            if x[0]>x[2]:
                print("NO")
                break
            
        
    
