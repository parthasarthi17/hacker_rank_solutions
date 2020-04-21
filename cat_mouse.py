q=int(input())#Entering number of queries
li=[]
for i in range(q):
    x=list(map(int,input().split())) #Entering positions of cats and mouse x=catA y=Catb z=mouse
    li.append(x[0])
    li.append(x[1])
    li.append(x[2])
max1=0
for i in range(q):
    a=li[3*i]-li[3*i+2]
    b=li[3*i+1]-li[3*i+2]
    if a<0:
            a=a*(-1)
    if b<0:
            b=b*(-1)
    if a>b:
            print("Cat B")
    if a<b:
            print("Cat A")
    if (li[3*i]>li[3*i+2] and li[3*i+1]<li[3*i+2]) or (li[3*i]<li[3*i+2] and li[3*i+1]>li[3*i+2]):
       if li[3*i]-li[3*i+2]==li[3*i]-li[3*i+2] :
            print("Mouse C")
#print(li)