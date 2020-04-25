def bubble_sort(listt): 
    for i, num in enumerate(listt): 
        try: 
            if listt[i+1] < num: 
                listt[i] = listt[i+1] 
                listt[i+1] = num 
                bubble_sort(listt) 
        except IndexError :
            pass
    return listt 

n=int(input())#Enter no of elements
t=list(map(int,input().split()))
mean=0
for i in t:
    mean=mean+i
mean=mean/len(t)
print(mean)
#median
#arranging in ascending order
t=bubble_sort(t)
#print(t)
if len(t)%2 == 0:
    a=len(t)//2
    #print(t[a-1],t[a])
    median=(t[a-1]+t[a])/2
else:
    median=t[(len(t)//2)+1]
print(median)
#mode
li=[]
count=1
i=1
for w in t:
    while i<len(t)-1:
        if w ==t[i]:
            count=count+1
        i+=1
    li.append(count)
    count=0
b=li.index(max(li))
li.pop(b)
c=li.index(max(li))
#print(c)
if t[b]>t[c]:
    print(t[c])
else:
    print(t[b])
    
    
    
    
    
    
    
    
    
    
    
    