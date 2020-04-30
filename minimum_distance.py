n=int(input()) #size of array
a=list(map(int,input().split()))
#print(a)
w=1
n=0
li=[]
for i in range(len(a)):
    find=a[i]
    while w<len(a):
        if a[w]==find:
            #print(a[w])
            if n==0:
                li.append(0)
                n+=1
            li.append(w)
            
        w+=1
    w=i+1
#print(li)
ori=[]
for w in range(len(li)-1):
    if a[li[w]]==a[li[w+1]]:
        ori.append(li[w])
        ori.append(li[w+1])
#print(ori)
if len(ori)==0:
    print(-1)
else:
    min1=ori[1]-ori[0]
    if min1==1:
        print(1)
    else:
        m=0
        for w in range(len(ori)//2):
            k=ori[m+1]-ori[m]
            
            if k<min1:
               min1=k
            m+=2
        print(min1)

