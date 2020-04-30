p=int(input())
q=int(input())
li=[]
final=[]
if p>=1 :
    if p<=5:
        print("1",end=" ")
    if p<=9:
        print("9",end=" ")
    p+=9

for w in range(p,q):
    li.append(w)
print(li)
for i in range(len(li)):
    sqr=li[i]**2
    sqr1=str(sqr)
    a1=""
    a2=""
    b=len(sqr1)//2

    for w in range(b):
        a1 += sqr1[w]
    for w in range(b,len(sqr1)):
        a2+=sqr1[w]
    k=int(li[i])
    if int(a1)+int(a2)==k:
        final.append(li[i])
if len(final)==0:
    print("Invalid Range")
else :
    for w in final:
        print(w,end=" ")
