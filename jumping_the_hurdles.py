n,k=input().split() # n for no_of_hurdles and k for max hieght Dan can jump naturally
li=list(map(int,input().split()))
max1=0
for w in li:
    if w>max1:
        max1=w
a=max1-int(k)
if a<0:
    print(0)
else:
    print(a)