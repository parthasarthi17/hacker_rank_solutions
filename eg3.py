n=int(input())
li=list(map(int,input().split()))
dm=list(map(int,input().split()))
j=0
if len(li)==1 and dm[1]==1:
    print("1")
else:
    print(len(li)+1//2)
    a=[]
    for w in range (1,(len(li)+1)//2):
        #print(" sda",li[0]+li[w])
        #i=w
        
        sum1=0
        for i in range(dm[1]):
                sum1=sum1+li[i]
                #print("w",w)
                print("sum",sum1)
        if sum1==dm[0]:
                        a.append(sum1)
                        li.pop(w)
                        li.pop(0)
                        j=j+1
                        #print("removed",li)
                        print(a)
                        w=0
            
    print(j)
    print(a)
