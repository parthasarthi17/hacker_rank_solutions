n=int(input()) #Entering size of array
a=list(map(int,input().split()))
li=[a[0]]
print(li)
for w in range(1,len(a)):
    d=a[0]-a[w]
    if d<0:
        d=d*-1
    if (d<=1):
        print(a[w])
        li.append(a[w])
print(li)